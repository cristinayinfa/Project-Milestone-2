from confluent_kafka import Producer

producer = Producer({
    'bootstrap.servers': 'pkc-v12gj.northamerica-northeast2.gcp.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': 'PCG4R4IOAUMPFA5Z',
    'sasl.password': 'NJOqszPaUyP/gJkLfVPPqEQ/RF8lfnHWtP2K/C4JTb+/HAnUJ0G2ko2a7c9vo1xq',
    'session.timeout.ms': 45000,
})
def status(err, message):
    if err is not None:
        print("Error")
    else:
        print("Sending messsage to-> {}  [{}]".format(message.topic(), message.partition()))

for i in range(10):
    producer.poll(0)

    producer.produce(
        'poems',
        key=i.to_bytes(2, 'big'),
        value=b'kafka-cloud',
        callback=status
    )

producer.flush()