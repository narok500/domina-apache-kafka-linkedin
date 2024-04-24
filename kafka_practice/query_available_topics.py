from kafka import KafkaAdminClient

client_kafka = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
)
topics_list = client_kafka.list_topics()

for topic in topics_list:
    print(topic)