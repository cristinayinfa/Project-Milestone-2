from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9093"
)

topic_name = input("Topic: ")
partitions = input("Partitions: ")
rf = input("Replication Factor: ")

topic = NewTopic(name=str(topic_name), num_partitions=int(partitions), replication_factor=int(rf))
admin_client.create_topics(new_topics=[topic], validate_only=False)
