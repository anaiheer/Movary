import socket
for h in ('backend', 'postgres', 'redis'):
    try:
        print(h, '->', socket.getaddrinfo(h, 80)[0][4])
    except Exception as e:
        print(h, '-> ERR', e)
