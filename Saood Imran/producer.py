from kafka import KafkaProducer
from json import dumps
import time
from time import sleep
try:
    producer = KafkaProducer(bootstrap_servers=['localhost:9093'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
    data = {'message' : "How are you?"}
    for x in range(0,100):
        producer.send('topicTest', value=data)
        print("Sent message ", x)
        time.sleep(1)
    producer.flush
    producer.close
except:
    print("Producer error")
