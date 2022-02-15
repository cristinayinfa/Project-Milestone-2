from kafka import KafkaProducer
from json import dumps
import time
from time import sleep



try:
    USERNAME="U7NXH3DZK2U2LHYA"
    PASSWORD='jr6uPdKQr9Bc/DLzGs2tZSRamdxENxVMmmz8AlbSUHxbAMjuAflRW2H82YqVOlsR'
    producer = KafkaProducer(bootstrap_servers="pkc-6ojv2.us-west4.gcp.confluent.cloud:9092", sasl_plain_username=USERNAME, sasl_plain_password=PASSWORD, sasl_mechanism="PLAIN", security_protocol="SASL_SSL")
    for x in range(0,100):
        producer.send('topicTest', b'NewTest')
        print("Sent message ", x)
        time.sleep(1)
    producer.flush
    producer.close
except:
    print("Producer error")
