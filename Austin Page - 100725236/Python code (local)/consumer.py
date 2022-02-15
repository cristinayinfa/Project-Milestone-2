import json
from kafka import KafkaConsumer

if __name__ == '__main__':

    consumer = KafkaConsumer(
        'austin',
        bootstrap_servers="localhost:9093"
    )

    for message in consumer:
        print(json.loads(message.value))