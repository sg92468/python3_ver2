import zmq

host = '127.0.0.1'
port = 6789
ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)
sub.connect(f'tcp://{host}:{port}')
topics = ['maine coon', 'persian']
for topic in topics:
    sub.setsockopt(zmq.SUBSCRIBE, topic.encode('utf-8'))
while True:
    cat_bytes, hat_bytes = sub.recv_multipart() #機能しない。なぜ？
    cat = cat_bytes.decode('utf-8')
    hat = hat_bytes.decode('utf-8')
    print(f'Subscribe: {cat} wears a {hat}')
