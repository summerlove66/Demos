from xmlrpc.server import SimpleXMLRPCServer
import requests
import time
import random

ua_list=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'
         ,'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36',
         'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.277.400 QQBrowser/9.4.7658.400']



def getHanders():
    headers = { "User-Agent": "{}".format(random.choice(ua_list)),}

    return headers

class KeyValueServer:

    def __init__(self, address):

        self._serv = SimpleXMLRPCServer(address, allow_none=True)

        self._serv.register_function(getattr(self, 'download'))

        self .proxy =None
    def download(self ,url, headers=getHanders(), proxies=req_proxy, retry=3, data=None, method='GET', req=requests, verify=None,
             timeout=50):
        try:
            if method == 'POST':
                res = req.post(url, proxies=proxies, headers=headers, timeout=timeout, data=data, verify=verify)
            else:
                res = req.get(url, proxies=proxies, headers=headers, timeout=timeout, data=data, verify=verify)
                # print(res.headers)
            # res.encoding='utf8'
            html = res.text


        except Exception as e:
            html =None
            print('download error', e)
            if retry > 1:
                time.sleep(5)
                global req_proxy
                req_proxy = self.change_proxy()
                html =self.download(url, headers=headers, retry =retry-1)


        return html
    def change_proxy(self):
        '''return  new  proxy'''

        pass

    def serve_forever(self):
        self._serv.serve_forever()


# Example
if __name__ == '__main__':
    kvserv = KeyValueServer(('', 8000))
    kvserv.serve_forever()
