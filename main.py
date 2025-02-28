import os
import pandas as pd
import yfinance as yf
from utils.data_preprocessing import DataPreprocessor
from models.forecasting_models import TimeSeriesForecaster
from visualizations.plots import plot_time_series, plot_volatility_analysis
from portfolio_optimization import optimize_portfolio

# Main script to execute the project
def main():
    # Step 1: Define assets and time range
    assets = ['TSLA', 'BND', 'SPY']
    start_date = '2015-01-01'
    end_date = '2025-01-31'

    # Step 2: Fetch and preprocess data
    preprocessor = DataPreprocessor(assets, start_date, end_date)
    raw_data = preprocessor.fetch_data()
    processed_data = preprocessor.preprocess_data(raw_data)

    # Save processed data for future use
    os.makedirs('data/processed', exist_ok=True)
    for asset, data in processed_data.items():
        data.to_csv(f'data/processed/{asset}_processed.csv', index=False)

    # Step 3: Exploratory Data Analysis (EDA)
    print("Performing Exploratory Data Analysis...")
    for asset, data in processed_data.items():
        plot_time_series(data, asset, column='Adj Close', title=f"{asset} Adjusted Close Price Over Time")
        plot_volatility_analysis(data, asset, window=30)

    # Step 4: Build and evaluate forecasting models
    forecaster = TimeSeriesForecaster(processed_data)
    forecaster.train_and_evaluate()

    # Step 5: Portfolio Optimization
    print("Optimizing Portfolio...")
    optimized_weights = optimize_portfolio(processed_data)
    print("Optimized Portfolio Weights:", optimized_weights)

if __name__ == "__main__":
    main()