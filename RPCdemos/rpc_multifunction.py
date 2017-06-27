from xmlrpc.server import SimpleXMLRPCServer


#server
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


server = SimpleXMLRPCServer(("localhost", 8000))
print ("Listening on port 8000...")
server.register_multicall_functions()
server.register_function(add, 'add1')
server.register_function(subtract, 'subtract1')
server.register_function(multiply, 'multiply1')
server.register_function(divide, 'divide1')
server.serve_forever()



#client
proxy =xmlrpc.client.ServerProxy("http://localhost:8000/")
multicall =xmlrpc.client.MultiCall(proxy)
# multicall.add1(7,3)
# multicall.subtract1(7,4)
# multicall.multiple1(8,5)
# multicall.divide1(9,2)
# result =multicall()
print(multicall.add1(7,3))