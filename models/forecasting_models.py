import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error
from pmdarima import auto_arima


class TimeSeriesForecaster:
    """
    A class for building and evaluating time series forecasting models.
    """

    def __init__(self, data, asset):
        """
        Initializes the forecaster with the specified asset's data.

        Args:
            data (pd.DataFrame): Preprocessed data for the asset.
            asset (str): Name of the asset (e.g., 'TSLA').
        """
        self.data = data
        self.asset = asset

    def train_test_split(self, test_size=0.2):
        """
        Splits the data into training and testing sets.

        Args:
            test_size (float): Proportion of data to include in the test set.

        Returns:
            tuple: Training and testing datasets.
        """
        split_index = int(len(self.data) * (1 - test_size))
        train_data = self.data.iloc[:split_index]
        test_data = self.data.iloc[split_index:]
        return train_data, test_data

    def optimize_arima(self, train_data):
        """
        Optimizes ARIMA parameters using auto_arima.

        Args:
            train_data (pd.Series): Training data for the asset.

        Returns:
            tuple: Best (p, d, q) parameters.
        """
        model = auto_arima(
            train_data["Adj Close"], seasonal=False, trace=True, stepwise=True
        )
        return model.order

    def train_arima(self, train_data, order):
        """
        Trains an ARIMA model on the training data.

        Args:
            train_data (pd.Series): Training data for the asset.
            order (tuple): (p, d, q) parameters for ARIMA.

        Returns:
            ARIMA model: Fitted ARIMA model.
        """
        model = ARIMA(train_data["Adj Close"], order=order)
        model_fit = model.fit()
        return model_fit

    def evaluate_model(self, model_fit, test_data):
        """
        Evaluates the ARIMA model on the test data.

        Args:
            model_fit: Fitted ARIMA model.
            test_data (pd.Series): Testing data for the asset.

        Returns:
            dict: Evaluation metrics (MAE, RMSE, MAPE).
        """
        predictions = model_fit.forecast(steps=len(test_data))
        mae = mean_absolute_error(test_data["Adj Close"], predictions)
        rmse = np.sqrt(mean_squared_error(test_data["Adj Close"], predictions))
        mape = (
            np.mean(
                np.abs((test_data["Adj Close"] - predictions) / test_data["Adj Close"])
            )
            * 100
        )
        return {"MAE": mae, "RMSE": rmse, "MAPE": mape}
