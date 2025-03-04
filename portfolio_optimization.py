import pandas as pd
import numpy as np
from scipy.optimize import minimize


def combine_forecasts(asset_forecasts):
    """
    Combines forecasts for multiple assets into a single DataFrame.

    Args:
        asset_forecasts (dict): Dictionary of forecasted data for assets.

    Returns:
        pd.DataFrame: Combined forecast DataFrame.
    """
    combined = pd.DataFrame()
    for asset, forecast in asset_forecasts.items():
        combined[asset] = forecast["Forecast"]
    return combined


def calculate_portfolio_metrics(combined_data):
    """
    Calculates portfolio metrics (returns, covariance matrix).

    Args:
        combined_data (pd.DataFrame): Combined forecast data.

    Returns:
        tuple: Mean returns, covariance matrix.
    """
    returns = combined_data.pct_change().mean() * 252  # Annualized returns
    cov_matrix = combined_data.pct_change().cov() * 252  # Annualized covariance
    return returns, cov_matrix


def optimize_portfolio(returns, cov_matrix):
    """
    Optimizes portfolio weights to maximize Sharpe Ratio.

    Args:
        returns (pd.Series): Mean returns for assets.
        cov_matrix (pd.DataFrame): Covariance matrix of returns.

    Returns:
        np.ndarray: Optimized portfolio weights.
    """
    num_assets = len(returns)
    args = (returns, cov_matrix)
    constraints = {"type": "eq", "fun": lambda x: np.sum(x) - 1}
    bounds = [(0, 1) for _ in range(num_assets)]
    initial_guess = [1 / num_assets] * num_assets
    result = minimize(
        negative_sharpe_ratio,
        initial_guess,
        args=args,
        method="SLSQP",
        bounds=bounds,
        constraints=constraints,
    )
    return result.x


def negative_sharpe_ratio(weights, returns, cov_matrix):
    """
    Negative Sharpe Ratio for optimization.

    Args:
        weights (np.ndarray): Portfolio weights.
        returns (pd.Series): Mean returns for assets.
        cov_matrix (pd.DataFrame): Covariance matrix of returns.

    Returns:
        float: Negative Sharpe Ratio.
    """
    portfolio_return = np.dot(weights, returns)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = portfolio_return / portfolio_volatility
    return -sharpe_ratio
