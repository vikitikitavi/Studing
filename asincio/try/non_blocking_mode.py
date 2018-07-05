import socket
import time

from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ


selector = DefaultSelector()
n_task = 0


def get(path):
    global n_task
    n_task += 1
    s = socket.socket()
    s.setblocking(False)

    try:
        s.connect(('0.0.0.0', 5000))
    except BlockingIOError:
        pass

    request = 'GET %s HTTP/1.0\r\n\r\n' % path

    def callback(): connected(s, request)

    selector.register(s.fileno(), EVENT_WRITE, data=callback)


def connected(s, request):
    selector.unregister(s.fileno())

    s.send(request.encode())

    chunks = []

    def callback(): readable(s, chunks)

    selector.register(s.fileno(), EVENT_READ, data=callback)


def readable(s, chunks):
    # s is reachable!
    global n_task

    selector.unregister(s.fileno())
    chunk = s.recv(1000)
    if chunk:
        chunks.append(chunk)

        def callback(): readable(s, chunks)
        selector.register(s.fileno(), EVENT_READ, data=callback)
    else:
        body = (b''.join(chunks)).decode()
        print(body.split('\n')[0])
        n_task -= 1
        return


start = time.time()
get('/foo')
get('/bar')

while n_task:
    events = selector.select()
    for event, mask in events:
        cb = event.data
        cb()
print('took %.1f sec ' % (time.time() - start))
