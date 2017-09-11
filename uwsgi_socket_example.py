import sys
import argparse
import socket
import struct
from binascii import hexlify

assert sys.version_info[0] == 3, 'Use Python 3.'


def force_bytes(value):
    if isinstance(value, bytes):
        return value
    return str(value).encode('utf-8')


def encode_uwsgi_vars(values):
    """
    Encode a list of key-value pairs into an uWSGI request header structure.
    """
    # See http://uwsgi-docs.readthedocs.io/en/latest/Protocol.html#the-uwsgi-vars
    buffer = []
    for key, value in values:
        key_enc = force_bytes(key)
        val_enc = force_bytes(value)
        buffer.append(struct.pack('<H', len(key_enc)))
        buffer.append(key_enc)
        buffer.append(struct.pack('<H', len(val_enc)))
        buffer.append(val_enc)
    return b''.join(buffer)


def send_uwsgi_request(socket, header_content):
    data = encode_uwsgi_vars(header_content)
    header = struct.pack(
        '<BHB',
        0,  # modifier1: 0 - WSGI (Python) request
        len(data),  # data size
        0,  # modifier2: 0 - always zero
    )
    socket.sendall(header)
    socket.sendall(data)


def dump_from_socket(socket, width=32):
    while True:
        chunk = socket.recv(width)
        if not chunk:
            break
        print('%-*s  %s' % (
            width * 2,
            hexlify(chunk).decode(),
            ''.join(b if b.isprintable() else '.' for b in chunk.decode('ascii', 'replace'))
        ))


def talk_to_uwsgi(host, port, path):
    s = socket.socket()
    s.connect((host, port))
    send_uwsgi_request(s, {
        'PATH_INFO': path,
    }.items())
    dump_from_socket(s)
    s.close()
		

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--host', default='localhost')
    ap.add_argument('--port', type=int, default=9090)
    ap.add_argument('path')
    args = ap.parse_args()
    talk_to_uwsgi(host=args.host, port=args.port, path=args.path)


if __name__ == '__main__':
    main()