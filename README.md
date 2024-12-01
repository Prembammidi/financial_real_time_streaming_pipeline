
# Financial Real-Time Streaming Pipeline

## Overview
This project implements a real-time financial data streaming pipeline. It is designed to consume live financial data, transform it, and store the processed data for further analysis. The pipeline is built using Python and is integrated with a Producer-Consumer architecture for efficient data streaming.

## Key Features
- **Real-time Streaming**: Uses producers and consumers to simulate a financial data pipeline.
- **Data Transformation**: Raw financial data is transformed into a structured format.
- **Efficient Data Flow**: Uses Python's threading and queue modules for real-time data flow.
- **Scalability**: Can handle a high volume of data, making it suitable for financial institutions.

## Architecture
### Architecture Diagram

![Architecture Diagram](https://github.com/Prembammidi/financial_real_time_streaming_pipeline/blob/master/image.png)


The pipeline consists of three main components:
1. **Producer**: Simulates the generation of financial data and sends it to a queue.
2. **Consumer**: Receives data from the queue and performs data transformation.
3. **Data Storage**: Processed data is saved in a CSV format for easy access.




## File Descriptions

- **`producer.py`**: Contains the logic for simulating the producer that generates live financial data.
- **`consumer.py`**: Consumes data from the queue and performs transformation tasks.
- **`data_transformation.py`**: Defines the functions used to transform raw data into structured, cleaned data.
- **`transformed_stock_data.csv`**: Example of transformed stock data after the pipeline processes it.

## Setup and Installation

To run this project locally, follow these steps:

### Prerequisites
Make sure you have Python 3.7 or higher installed.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Prembammidi/financial_real_time_streaming_pipeline.git
   cd financial_real_time_streaming_pipeline
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the producer and consumer:**
   - Start the producer:
     ```bash
     python producer.py
     ```
   - Start the consumer:
     ```bash
     python consumer.py
     ```

4. **Check the transformed data:**
   - After the pipeline runs, the processed data will be saved in `transformed_stock_data.csv`.

## Contributions
Feel free to fork the repository and submit pull requests. Contributions are always welcome!

---






