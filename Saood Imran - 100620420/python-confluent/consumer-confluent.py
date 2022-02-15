from kafka import KafkaConsumer
from json import loads

try:
    USERNAME="U7NXH3DZK2U2LHYA"
    PASSWORD='jr6uPdKQr9Bc/DLzGs2tZSRamdxENxVMmmz8AlbSUHxbAMjuAflRW2H82YqVOlsR'
    consumer = KafkaConsumer(bootstrap_servers="pkc-6ojv2.us-west4.gcp.confluent.cloud:9092", sasl_plain_username=USERNAME, sasl_plain_password=PASSWORD, sasl_mechanism="PLAIN", security_protocol="SASL_SSL", auto_offset_reset='earliest', group_id=None)
    consumer.subscribe("topicTest")
    for message in consumer:
        print(message.value.decode('utf-8'))
except:
    print("Consumer error.")