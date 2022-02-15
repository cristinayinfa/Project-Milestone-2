from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'data',
    bootstrap_servers='localhost:9093'
)
for message in consumer:
    print(message)