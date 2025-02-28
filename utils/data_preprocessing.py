import pandas as pd
import yfinance as yf


class DataPreprocessor:
    """
    A utility class for fetching and preprocessing financial data from Yahoo Finance.

    Attributes:
        assets (list): List of asset symbols (e.g., ['TSLA', 'BND', 'SPY']).
        start_date (str): Start date for data fetching in 'YYYY-MM-DD' format.
        end_date (str): End date for data fetching in 'YYYY-MM-DD' format.
    """

    def __init__(self, assets, start_date, end_date):
        """
        Initializes the DataPreprocessor with the specified assets and date range.

        Args:
            assets (list): List of asset symbols.
            start_date (str): Start date for data fetching.
            end_date (str): End date for data fetching.
        """
        self.assets = assets
        self.start_date = start_date
        self.end_date = end_date

    def fetch_data(self):
        """
        Fetches historical financial data for the specified assets using yfinance.

        Returns:
            dict: A dictionary where keys are asset symbols and values are pandas DataFrames.
        """
        try:
            raw_data = {}
            for asset in self.assets:
                data = yf.download(asset, start=self.start_date, end=self.end_date)
                if data.empty:
                    raise ValueError(
                        f"No data fetched for {asset}. Check the date range or asset symbol."
                    )
                raw_data[asset] = data
            return raw_data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def preprocess_data(self, raw_data):
        """
        Cleans and preprocesses raw financial data.

        Args:
            raw_data (dict): Dictionary of raw data (keys: asset symbols, values: DataFrames).

        Returns:
            dict: Dictionary of processed data (keys: asset symbols, values: DataFrames).
        """
        processed_data = {}
        for asset, data in raw_data.items():
            # Handle missing values
            data = data.fillna(method="ffill").fillna(method="bfill")

            # Add daily percentage change
            data["Daily_Return"] = data["Adj Close"].pct_change()

            # Calculate rolling mean and standard deviation
            data["Rolling_Mean"] = data["Adj Close"].rolling(window=30).mean()
            data["Rolling_Std"] = data["Adj Close"].rolling(window=30).std()

            # Drop rows with NaN values after calculations
            data = data.dropna()

            processed_data[asset] = data
        return processed_data
