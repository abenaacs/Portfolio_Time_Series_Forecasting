import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing

class TimeSeriesForecaster:
    def __init__(self, data):
        self.data = data

    def train_and_evaluate(self):
        """Train and evaluate forecasting models."""
        for asset, data in self.data.items():
            print(f"Training model for {asset}...")
            # Decompose time series
            decomposition = seasonal_decompose(data['Adj Close'], model='additive', period=30)
            trend = decomposition.trend
            seasonal = decomposition.seasonal
            residual = decomposition.resid

            # Train Holt-Winters Exponential Smoothing model
            model = ExponentialSmoothing(data['Adj Close'], seasonal='add', seasonal_periods=30)
            model_fit = model.fit()

            # Forecast next 30 days
            forecast = model_fit.forecast(steps=30)

            # Evaluate model performance
            actual = data['Adj Close'][-30:]
            predicted = forecast[:30]
            mse = mean_squared_error(actual, predicted)
            print(f"{asset} Model MSE: {mse:.2f}")
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.metrics import mean_squared_error, mean_absolute_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing

class TimeSeriesForecaster:
    def __init__(self, data):
        self.data = data

    def train_and_evaluate(self):
        """Train and evaluate forecasting models."""
        for asset, data in self.data.items():
            print(f"Training model for {asset}...")
            # Decompose time series
            decomposition = seasonal_decompose(data['Adj Close'], model='additive', period=30)
            trend = decomposition.trend
            seasonal = decomposition.seasonal
            residual = decomposition.resid

            # Train Holt-Winters Exponential Smoothing model
            model = ExponentialSmoothing(data['Adj Close'], seasonal='add', seasonal_periods=30)
            model_fit = model.fit()

            # Forecast next 30 days
            forecast = model_fit.forecast(steps=30)

            # Evaluate model performance
            actual = data['Adj Close'][-30:]
            predicted = forecast[:30]
            mse = mean_squared_error(actual, predicted)
            mae = mean_absolute_error(actual, predicted)
            print(f"{asset} Model MSE: {mse:.2f}, MAE: {mae:.2f}")

            # Save forecast results
            forecast_df = pd.DataFrame({'Forecast': forecast})
            forecast_df.to_csv(f'data/processed/{asset}_forecast.csv', index=False)
            # Save forecast results
            forecast_df = pd.DataFrame({'Forecast': forecast})
            forecast_df.to_csv(f'data/processed/{asset}_forecast.csv', index=False)