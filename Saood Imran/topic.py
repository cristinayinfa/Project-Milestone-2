from kafka.admin import KafkaAdminClient, NewTopic

admin = KafkaAdminClient(
    bootstrap_servers=["localhost:9093","localhost:9094","localhost:9095"],
    client_id='test'
)

try:
    topic_list = []
    topic_list.append(NewTopic(name="topicTest", num_partitions=3,replication_factor=1))
    admin.create_topics(new_topics=topic_list, validate_only=False)
except:
    print("An error occured")
