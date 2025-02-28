from kafka import KafkaConsumer
import json
import os
# Kafka consumer setup
consumer = KafkaConsumer(
    'test1',  # Change to your topic name
    bootstrap_servers=['kafka-release.kafka.svc.cluster.local:9092'],
    security_protocol="SASL_PLAINTEXT",
    sasl_mechanism="SCRAM-SHA-512",
    sasl_plain_username="user1",
    sasl_plain_password="v2YYHRmR2a",
    auto_offset_reset='earliest',  # Options: 'earliest', 'latest', 'none'
    enable_auto_commit=True
)

output_file = "/app/messages.txt" 

# Ensure the directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

print("Consumer is running...")

with open(output_file, "a") as f:
    for message in consumer:
        data = json.loads(message.value.decode("utf-8"))
        print(f"Received: {data}")
        f.write(json.dumps(data) + "\n")

