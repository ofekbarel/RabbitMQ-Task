import pika
def on_massage_recived(ch, method, properties, body):
    print(f"recived new massage: {body}")

connction_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connction_parameters)

channel = connection.channel()

channel.queue_declare(queue='ABC')


channel.basic_consume(queue='ABC', auto_ack=True, on_message_callback=on_massage_recived)

print("Starting")
channel.start_consuming()