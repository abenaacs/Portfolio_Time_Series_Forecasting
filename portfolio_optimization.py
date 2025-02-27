import numpy as np
import pandas as pd
from scipy.optimize import minimize

def optimize_portfolio(data):
    """Optimize portfolio weights using Efficient Frontier."""
    returns = pd.DataFrame({asset: data[asset]['Daily_Return'] for asset in data.keys()})
    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    # Objective function: Minimize portfolio variance
    def portfolio_variance(weights):
        return np.dot(weights.T, np.dot(cov_matrix, weights))

    # Constraints: Sum of weights = 1
    constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})

    # Bounds: Weights between 0 and 1
    bounds = [(0, 1) for _ in range(len(mean_returns))]

    # Initial guess: Equal weights
    initial_guess = [1 / len(mean_returns)] * len(mean_returns)

    # Optimize
    result = minimize(portfolio_variance, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)
    return result.x