from confluent_kafka import Consumer

consumer = Consumer({
    'bootstrap.servers': 'pkc-6ojv2.us-west4.gcp.confluent.cloud:9092',
    'group.id': 'hello',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': 'EPC3A4HH6T3I6DJL',
    'sasl.password': 'yyATfupdXzpyYxK9P1J1+TkwMTVqaoRkkRoI1yvj9Aqid8ir2h5BlCf9yicJWfqQ',
    'session.timeout.ms': 45000,
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['test'])

while True:
    message = consumer.poll()

    print(message.value().decode('utf-8'))
