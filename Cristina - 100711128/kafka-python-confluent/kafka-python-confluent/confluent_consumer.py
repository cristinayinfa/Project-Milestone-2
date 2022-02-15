from confluent_kafka import Consumer

consumer = Consumer({
    'bootstrap.servers': 'pkc-v12gj.northamerica-northeast2.gcp.confluent.cloud:9092',
    'group.id': 'group1',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': 'PCG4R4IOAUMPFA5Z',
    'sasl.password': 'NJOqszPaUyP/gJkLfVPPqEQ/RF8lfnHWtP2K/C4JTb+/HAnUJ0G2ko2a7c9vo1xq',
    'session.timeout.ms': 45000,
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['poems'])

while True:
    message = consumer.poll(1.0)

    if message is None:
        continue
    if message.error():
        print("error")
        continue

    print(message.value().decode('utf-8'))
    