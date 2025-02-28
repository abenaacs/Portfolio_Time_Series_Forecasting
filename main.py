import os
import pandas as pd
import yfinance as yf
from utils.data_preprocessing import DataPreprocessor
from models.forecasting_models import TimeSeriesForecaster
from visualizations.plots import plot_time_series, plot_volatility_analysis
from portfolio_optimization import optimize_portfolio


def fetch_and_preprocess_data(assets, start_date, end_date):
    """
    Fetches and preprocesses financial data for the specified assets.

    Args:
        assets (list): List of asset symbols.
        start_date (str): Start date for data fetching.
        end_date (str): End date for data fetching.

    Returns:
        dict: Dictionary of processed data (keys: asset symbols, values: DataFrames).
    """
    preprocessor = DataPreprocessor(assets, start_date, end_date)
    raw_data = preprocessor.fetch_data()
    processed_data = preprocessor.preprocess_data(raw_data)

    # Save processed data for future use
    os.makedirs("data/processed", exist_ok=True)
    for asset, data in processed_data.items():
        data.to_csv(f"data/processed/{asset}_processed.csv", index=False)
    return processed_data


def perform_eda(processed_data):
    """
    Performs exploratory data analysis (EDA) on the processed data.

    Args:
        processed_data (dict): Dictionary of processed data.
    """
    print("Performing Exploratory Data Analysis...")
    for asset, data in processed_data.items():
        plot_time_series(
            data,
            asset,
            column="Adj Close",
            title=f"{asset} Adjusted Close Price Over Time",
        )
        plot_volatility_analysis(data, asset, window=30)


def train_and_evaluate_models(processed_data):
    """
    Trains and evaluates time series forecasting models.

    Args:
        processed_data (dict): Dictionary of processed data.
    """
    forecaster = TimeSeriesForecaster(processed_data)
    forecaster.train_and_evaluate()


def optimize_portfolio_weights(processed_data):
    """
    Optimizes portfolio weights using Efficient Frontier.

    Args:
        processed_data (dict): Dictionary of processed data.

    Returns:
        numpy.ndarray: Optimized portfolio weights.
    """
    print("Optimizing Portfolio...")
    optimized_weights = optimize_portfolio(processed_data)
    print("Optimized Portfolio Weights:", optimized_weights)
    return optimized_weights


def main():
    """
    Main function to execute the project pipeline.
    """
    # Define assets and time range
    assets = ["TSLA", "BND", "SPY"]
    start_date = "2015-01-01"
    end_date = "2025-01-31"

    # Step 1: Fetch and preprocess data
    processed_data = fetch_and_preprocess_data(assets, start_date, end_date)

    # Step 2: Perform EDA
    perform_eda(processed_data)

    # Step 3: Train and evaluate forecasting models
    train_and_evaluate_models(processed_data)

    # Step 4: Optimize portfolio weights
    optimize_portfolio_weights(processed_data)


if __name__ == "__main__":
    main()
