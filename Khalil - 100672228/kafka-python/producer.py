from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9093'])

producer.send('data', b'Hello World!')
producer.flush()