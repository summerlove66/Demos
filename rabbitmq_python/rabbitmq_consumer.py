import pika
import requests
import time
credentials = pika.PlainCredentials("hui","smile")
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost",5672,"/",credentials))
channel = connection.channel()
channel.queue_declare(queue="balance")

def callback(ch,method,properties,body):
    body = body.decode()
    line = "__" * 30
    time.sleep(3)
    if body.startswith("http"):
        r = requests.get(body)
        time.sleep(3)

        print("[x] Received : {}\n {} \n {}".format(body,r.headers,line))
    # elif  body.startswith("人"):
    #     raise  Exception("NOT KNOW ")
    else:
        print(" [x] Received: {} \n {}".format( body,line))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback,queue="balance",no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()