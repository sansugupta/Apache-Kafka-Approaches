from kafka import KafkaProducer
import requests
import json
import time

# Kafka broker details
KAFKA_BROKER = "kafka-release.kafka.svc.cluster.local:9092"
TOPIC_NAME = "test1"

# Configure the producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    security_protocol="SASL_PLAINTEXT",
    sasl_mechanism="SCRAM-SHA-512",
    sasl_plain_username="user1",
    sasl_plain_password="v2YYHRmR2a",
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Function to fetch users and send to Kafka
def fetch_and_produce():
    for user_id in range(1, 101):  # Fetch first 10 users
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
        if response.status_code == 200:
            user_data = response.json()
            producer.send(TOPIC_NAME, user_data)
            print(f"Sent: {user_data}")
        time.sleep(2)  # Avoid API rate limits

fetch_and_produce()
producer.flush()
producer.close()

