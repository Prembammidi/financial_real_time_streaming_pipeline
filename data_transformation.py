# data_transformation.py

def transform_stock_data(stock_data):
    """
    Extract and transform the stock data from the raw JSON received from Kafka.

    Args:
    stock_data (dict): Raw stock data in JSON format.

    Returns:
    dict: Transformed stock data containing symbol, open, high, low, close, etc.
    """
    # Extract metadata and time series from the raw data
    meta_data = stock_data.get('Meta Data', {})
    time_series = stock_data.get('Time Series (5min)', {})

    # Extract the latest record (first record)
    last_record = list(time_series.items())[0][1]  # Get the first record

    # Create a structured dictionary with useful stock information
    stock_info = {
        'symbol': meta_data.get('2. Symbol'),
        'last_refreshed': meta_data.get('3. Last Refreshed'),
        'open': last_record.get('1. open'),
        'high': last_record.get('2. high'),
        'low': last_record.get('3. low'),
        'close': last_record.get('4. close')
    }

    return stock_info
