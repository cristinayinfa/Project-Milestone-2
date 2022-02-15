import json
from kafka import KafkaProducer


def serializer(message):
    return json.dumps(message).encode('utf-8')


producer = KafkaProducer(bootstrap_servers="localhost:9093",
                         value_serializer=serializer)

if __name__ == '__main__':
    while True:
        try:
            message = input("Message: ")
            topic = input("Topic: ")
            part = input("Partition: ")
            producer.send(str(topic), value=str(message), partition=int(part))
            print(" ---------- Message sent! ---------- ")
        except:
            print(" ---------- An error occurred ---------- ")
