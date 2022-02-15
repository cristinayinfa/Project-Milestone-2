import json
from kafka import KafkaConsumer

if __name__ == '__main__':
    # Kafka Consumer
    consumer = KafkaConsumer(
        'topic-testpy',
        bootstrap_servers='localhost:9094',
        auto_offset_reset='earliest'
    )
    print("Connected!")

    # Print messages
    for message in consumer:
        print(json.loads(message.value))
