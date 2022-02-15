from confluent_kafka import Producer

producer = Producer({
    'bootstrap.servers': 'pkc-6ojv2.us-west4.gcp.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': 'EPC3A4HH6T3I6DJL',
    'sasl.password': 'yyATfupdXzpyYxK9P1J1+TkwMTVqaoRkkRoI1yvj9Aqid8ir2h5BlCf9yicJWfqQ'
})


def cb(err, message):
    if err is not None:
        print("error: ")
    else:
        print("delivered: ")


for i in range(10):
    producer.poll(0)

    producer.produce(
        'test',
        key=i.to_bytes(2, 'big'),
        value=b'for video',
        callback=cb
    )

producer.flush()
