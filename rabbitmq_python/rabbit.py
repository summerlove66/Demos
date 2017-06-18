import pika

credentials = pika.PlainCredentials("hui","smile")


def sent_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", 5672, "/", credentials))
    channel = connection.channel()

    channel.queue_declare(queue="balance")
    channel.basic_publish(exchange="",routing_key ="balance",body =message)
    print("[x] sent ",message)
    connection.close()
