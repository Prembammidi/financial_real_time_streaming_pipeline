import json
import csv
import time
from kafka import KafkaConsumer
from data_transformation import transform_stock_data  # Import the function from data_transformation.py

# Create consumer with a group
consumer = KafkaConsumer(
    'alpha-vantage-topic',    # Topic
    group_id='alpha-vantage-group',
    enable_auto_commit=True,   # Consumer group
    auto_offset_reset='earliest',  # Ensure we start from the earliest message
    bootstrap_servers=['localhost:9092'],
    max_poll_records=100 
)

# Open the CSV file in append mode
with open('transformed_stock_data.csv', mode='a', newline='', encoding='utf-8') as file:
    # Create a CSV writer object
    csv_writer = csv.DictWriter(file, fieldnames=['symbol', 'last_refreshed', 'open', 'high', 'low', 'close'])
    
    # Write the header if the file is empty
    file.seek(0, 2)  # Move the cursor to the end of the file
    if file.tell() == 0:
        csv_writer.writeheader()  # Write the header if the file is empty

    # Consume messages and transform them
    for message in consumer:
        try:
            # Decode the message value and load it as JSON
            stock_data = json.loads(message.value.decode('utf-8'))
            
            # Apply transformation from the imported function
            transformed_data = transform_stock_data(stock_data)
            
            # Print or further process the transformed data
            print(f"Transformed stock data: {transformed_data}")
            
            # Write the transformed data to the CSV file
            csv_writer.writerow(transformed_data)
            file.flush()  # Ensure data is immediately written to the file
            time.sleep(1)  # Add a small delay to help with real-time updates (adjust as needed)

        except json.JSONDecodeError:
            print(f"Skipping invalid message: {message.value.decode('utf-8')}")
        except Exception as e:
            print(f"Error processing message: {str(e)}")
