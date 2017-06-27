
#Server 端
from xmlrpc.server import SimpleXMLRPCServer
import socketserver
import requests
import sys
class Clawer:
    def get(self,user,url,params=None,headers =None):
        try:
            if user =='username':
                r = requests.get(url,params=params,headers=headers)
                return r.text
            else:
                return ''
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # ip = sys.argv[1]
    # port =sys.argv[2]
    class RPCThreading(socketserver.ThreadingMixIn,SimpleXMLRPCServer):
        pass
    clawer_obj =Clawer()
    server =RPCThreading(('localhost',8000))
    server.register_instance(clawer_obj)
    print('Listening')
    server.serve_forever()
	
#Client 端
	
from xmlrpc.client import ServerProxy

p =  ServerProxy("http://localhost:8000")
p.get("username","http://www.baidu.com")
pass


	
	
	
