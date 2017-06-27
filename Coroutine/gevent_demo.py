from gevent import monkey; monkey.patch_all()
import gevent
import requests
import  time

#   some demo -----------------------------
monkey.patch_socket()
def f():
    for i in range(1,5):
        time.sleep(0.3)
        gevent.sleep(0)  #有io时会自动切换到下一个线程
        print(i)

def g():
    for i in list('abcdef'):
        time.sleep(0.2)
        gevent.sleep(0)
        print(i)

glist =[gevent.spawn(f,),gevent.spawn(g,)]
gevent.joinall(glist)


#  IO 协程---------------------------------------

url_list = ['http://hz.ganji.com/ershoubijibendiannao/o{}/'.format(i) for i in range(1, 10)]

def readit(link):

    res = requests.get(link)
    print(res.url)
def coroutine():
    a =time.time()
    gevent.joinall([gevent.spawn(readit ,i)  for i in url_list ])
    print(time.time() -a )



