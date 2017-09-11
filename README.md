uWSGI socket example
====================

Re https://stackoverflow.com/q/45834465/51685

Usage
-----

(1) Start uWSGI and point it to Python's built-in demo WSGI app.
```
uwsgi --wsgi wsgiref.simple_server:demo_app --master --http :8181 --socket :9090
```
(You can see what the app does by navigating to http://127.0.0.1:8181/.)

(2) Run uwsgi_socket_example.py:
```
python uwsgi_socket_example.py /hello
```

(3) The script should connect to uWSGI, make a minimal request and hex-dump the output:

```
485454502f312e3020323030204f4b0d0a436f6e74656e742d547970653a20746578742f706c6169 HTTP/1.0 200 OK..Content-Type: text/plai
6e3b20636861727365743d7574662d380d0a0d0a48656c6c6f20776f726c64210a0a504154485f49 n; charset=utf-8....Hello world!..PATH_I
4e464f203d20272f68656c6c6f270a75777367692e6e6f6465203d206227476165612e6775657374 NFO = '/hello'.uwsgi.node = b'Gaea.guest
2e746b752efcf0fcf0fcf0fcf0fcf0270a75777367692e76657273696f6e203d206227322e302e31 .foo.example.xx'.uwsgi.version = b'2.0.1
35270a777367692e6572726f7273203d203c5f696f2e54657874494f57726170706572206e616d65 5'.wsgi.errors = <_io.TextIOWrapper name
3d32206d6f64653d27772720656e636f64696e673d275554462d38273e0a777367692e66696c655f =2 mode='w' encoding='UTF-8'>.wsgi.file_
77726170706572203d203c6275696c742d696e2066756e6374696f6e2075777367695f73656e6466 wrapper = <built-in function uwsgi_sendf
696c653e0a777367692e696e707574203d203c75777367692e5f496e707574206f626a6563742061 ile>.wsgi.input = <uwsgi._Input object a
742030783130613536636133383e0a777367692e6d756c746970726f63657373203d2046616c7365 t 0x10a56ca38>.wsgi.multiprocess = False
0a777367692e6d756c7469746872656164203d2046616c73650a777367692e72756e5f6f6e636520 .wsgi.multithread = False.wsgi.run_once
3d2046616c73650a777367692e75726c5f736368656d65203d202768747470270a777367692e7665 = False.wsgi.url_scheme = 'http'.wsgi.ve
7273696f6e203d2028312c2030290a                                                   rsion = (1, 0).
```