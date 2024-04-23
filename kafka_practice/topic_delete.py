from kafka.admin import KafkaAdminClient
from kafka.errors import UnknownTopicOrPartitionError

client_kafka = KafkaAdminClient(bootstrap_servers="localhost:9092")

topic_to_delete = "topico_particiones"
try:
    client_kafka.delete_topics(topics=[topic_to_delete])
    print(f"The topic {topic_to_delete} was successfully deleted")
except UnknownTopicOrPartitionError:
    print(f"Error when deleting the topic {topic_to_delete}")