import json
from kafka import KafkaProducer


# Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')


producer = KafkaProducer(
    bootstrap_servers=['localhost:9094'],
    value_serializer=serializer
)

if __name__ == '__main__':
    while True:
        mes = input("Enter message: ")
        producer.send('topic-testpy', mes)
