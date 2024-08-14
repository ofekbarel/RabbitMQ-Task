import pika 

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='ABC')

for i in range(10):
    massage = f"Massage {i + 1}"
    channel.basic_publish(exchange='', routing_key='ABC', body=massage)
    print(f"sent massage: {massage}")

connection.close