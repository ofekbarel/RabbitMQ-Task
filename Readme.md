# Queue Management with RabbitMQ and Python

## Overview

This project demonstrates how to manage message queues efficiently using **RabbitMQ** and Python. RabbitMQ, a widely-used message broker, will help organize queues, while Python scripts will be used to send and receive messages.

## Prerequisites

Ensure you have the following installed and set up:

- **RabbitMQ**: The message broker used for managing queues.
- **Python 3**: The programming language used for scripting.
- **pika**: The Python client library for RabbitMQ.

## Installation and Setup

### Installing RabbitMQ

1. **Download and Install RabbitMQ**:
   Follow the official RabbitMQ installation guide for your operating system: [RabbitMQ Installation Guide](https://www.rabbitmq.com/download.html).

2. **Start RabbitMQ**:
   Launch RabbitMQ using the following command:
   ```bash
   /opt/homebrew/sbin/rabbitmq-server
   ```

3. **Access the RabbitMQ Management Interface**:
   Open your browser and navigate to `http://localhost:15672`. Log in with the default credentials:
   - **Username**: guest
   - **Password**: guest

4. **Create a Queue**:
   In the RabbitMQ management interface, create a queue named `abc` for this project.

### Setting Up Python Environment

1. **Install the `pika` Library**:
   Use pip to install the `pika` library:
   ```bash
   pip install pika
   ```

2. **Publisher Script**:
   This script sends 10 messages to the RabbitMQ queue named `abc`.

   Save the following code as `publisher.py`:
   ```python
   import pika 

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='ABC')

for i in range(10):
    massage = f"Massage {i + 1}"
    channel.basic_publish(exchange='', routing_key='ABC', body=massage)
    print(f"Massages sent: {massage}")



connection.close
   ```

   Execute the script with:
   ```bash
   python3 publisher.py
   ```

3. **Consumer Script**:
   This script listens for messages from the RabbitMQ queue `abc` and prints them to the terminal.

   Save the following code as `consumer.py`:
   ```python
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
   ```

   Execute the script with:
   ```bash
   python3 consumer.py
   ```

## Summary

This project provides a comprehensive approach to managing message queues using RabbitMQ. The `publisher.py` script is designed to send messages to the queue, while the `consumer.py` script listens for and processes these messages. 

Feel free to adapt and extend this setup to suit your specific use cases. For further details or advanced configurations, consult the RabbitMQ documentation and `pika` library references.




##steps for Mac##



1. # update

 brew update 



2. # install rabbitmq server locally

 brew install rabbitmq



3. # start rabbitmq service

 /opt/homebrew/sbin/rabbitmq-server
 



4. # open rabbitme interface

browse : localhost:15672



5. # install pika library
pip3 install pika



6. # Run the code

python3 cunsumer.py
python3 producer.py
