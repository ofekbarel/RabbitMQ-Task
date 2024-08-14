##steps for Mac##



1. # update

 brew update 



2. # install rabbitmq server locally

 brew install rabbitmq



3. # start rabbitmq service

 /opt/homebrew/optrabbitmq/sbin/rabbitmq-server
 



4. # open rabbitme interface

browse : localhost:15672



5. # install pika library
pip3 install pika



6. # Run the code

python3 cunsumer.py
python3 producer.py
