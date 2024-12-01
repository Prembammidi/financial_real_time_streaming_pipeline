import requests
from kafka import KafkaProducer
import json
import time
import sys

# Kafka configuration
KAFKA_TOPIC = 'alpha-vantage-topic'
KAFKA_BROKER = 'localhost:9092'

# Alpha Vantage API configuration
API_KEY = 'your_api_key_here'  # Use your own Alpha Vantage API key
STOCK_SYMBOL = 'IBM'  # Change to any stock symbol you want
API_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK_SYMBOL}&interval=5min&apikey={API_KEY}'

# Kafka Producer setup
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Function to fetch stock data from Alpha Vantage
def fetch_data():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data from Alpha Vantage. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Function to send data to Kafka
def send_to_kafka(data):
    try:
        producer.send(KAFKA_TOPIC, data)
        producer.flush()  # Ensure data is sent
        print("Data sent to Kafka:", data)
    except Exception as e:
        print(f"Error sending data to Kafka: {e}")

# Main loop to fetch and send data every 5 minutes
if __name__ == '__main__':
    try:
        while True:
            data = fetch_data()
            if data:
                send_to_kafka(data)
            time.sleep(300)  # Wait for 5 minutes before making the next API request
    except KeyboardInterrupt:
        print("Program interrupted, closing...")
        sys.exit(0)
