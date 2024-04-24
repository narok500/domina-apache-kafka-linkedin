from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092"
)

list_fruits = ["apple", "pear", "grape"]

for fruit in list_fruits:
    producer.send("python_topic", bytes(fruit, "utf-8"))

producer.flush()  # espera a que se realicen todas las solicitudes
producer.close()  # cierra la conexión