from kafka import KafkaConsumer
from json import loads

try:
    consumer = KafkaConsumer(
    'topicTest',
     bootstrap_servers=['localhost:9093'],
     value_deserializer=lambda x: loads(x.decode('utf-8')))
     
    for message in consumer:
        print(message.value)
except:
    print("Consumer error.")