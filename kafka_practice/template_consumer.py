from kafka import KafkaConsumer

consumer = KafkaConsumer(
    bootstrap_servers="localhost:9092",
    group_id="python_consumer",
    auto_offset_reset="earliest",
)

consumer.subscribe(["python_topic"])

for message in consumer:
    print(message.partition)
    print(message.value.decode("utf-8"))

consumer.close()