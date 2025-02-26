import pandas as pd
import yfinance as yf

class DataPreprocessor:
    def __init__(self, assets, start_date, end_date):
        self.assets = assets
        self.start_date = start_date
        self.end_date = end_date

    def fetch_data(self):
        """Fetch historical data from YFinance."""
        try:
            raw_data = {}
            for asset in self.assets:
                data = yf.download(asset, start=self.start_date, end=self.end_date)
                if data.empty:
                    raise ValueError(f"No data fetched for {asset}. Check the date range or asset symbol.")
                raw_data[asset] = data
            return raw_data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def preprocess_data(self, raw_data):
        """Clean and preprocess the raw data."""
        processed_data = {}
        for asset, data in raw_data.items():
            # Ensure no missing values
            data = data.fillna(method='ffill').fillna(method='bfill')

            # Add daily percentage change
            data['Daily_Return'] = data['Adj Close'].pct_change()

            # Calculate rolling mean and standard deviation
            data['Rolling_Mean'] = data['Adj Close'].rolling(window=30).mean()
            data['Rolling_Std'] = data['Adj Close'].rolling(window=30).std()

            # Drop rows with NaN values after calculations
            data = data.dropna()

            processed_data[asset] = data
        return processed_data