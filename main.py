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


def forecast_future_trends(processed_data):
    """
    Forecasts future market trends for each asset.

    Args:
        processed_data (dict): Dictionary of processed data for assets.
    """
    for asset, data in processed_data.items():
        print(f"Forecasting future prices for {asset}...")
        forecaster = TimeSeriesForecaster(data, asset)
        train_data, _ = forecaster.train_test_split()
        order = forecaster.optimize_arima(train_data)
        model_fit = forecaster.train_arima(train_data, order)
        forecast = forecaster.forecast_future_prices(model_fit, steps=180)
        forecast.to_csv(f"data/processed/{asset}_forecast.csv", index=False)
        print(f"Saved forecast for {asset} to data/processed/{asset}_forecast.csv")


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


def train_and_evaluate_forecasting_models(processed_data):
    """
    Trains and evaluates time series forecasting models for each asset.

    Args:
        processed_data (dict): Dictionary of processed data for assets.
    """
    for asset, data in processed_data.items():
        print(f"Training ARIMA model for {asset}...")
        forecaster = TimeSeriesForecaster(data, asset)
        train_data, test_data = forecaster.train_test_split()
        order = forecaster.optimize_arima(train_data)
        model_fit = forecaster.train_arima(train_data, order)
        metrics = forecaster.evaluate_model(model_fit, test_data)
        print(f"{asset} Model Metrics: {metrics}")


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
    train_and_evaluate_forecasting_models(processed_data)

    # Step 4: Optimize portfolio weights
    optimize_portfolio_weights(processed_data)


if __name__ == "__main__":
    main()
