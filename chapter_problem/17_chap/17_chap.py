# 17.5.1 DNS
import socket
print(socket.gethostbyname('www.crappytaxidermy.com'))
print(socket.gethostbyname_ex('www.crappytaxidermy.com'))
print(socket.getaddrinfo('www.crappytaxidermy.com', 80))
print(socket.getaddrinfo('www.crappytaxidermy.com', 80, socket.AF_INET, socket.SOCK_STREAM))

print(socket.getservbyname('http'))
print(socket.getservbyport(80))

# 17.7 データのシリアライズ
import datetime
import pickle

now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)
print(now1)
print(now2)

class Tiny:
    def __str__(self):
        return 'tiny'

obj1 = Tiny()
print(obj1)
pickled = pickle.dumps(obj1)
print(pickled)
obj2 = pickle.loads(pickled)
print(obj2)
print(str(obj2))