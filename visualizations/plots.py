import matplotlib.pyplot as plt

def plot_time_series(data, asset, column, title):
    """Plot time series data."""
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data[column], label=column, color='blue')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel(column)
    plt.legend()
    plt.grid(True)
    plt.savefig(f'visualizations/plots/{asset}_{column}_time_series.png')
    plt.close()

def plot_volatility_analysis(data, asset, window):
    """Plot rolling mean and standard deviation."""
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Rolling_Mean'], label='Rolling Mean', color='green')
    plt.plot(data.index, data['Rolling_Std'], label='Rolling Std', color='red')
    plt.title(f"{asset} Volatility Analysis (Window={window})")
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'visualizations/plots/{asset}_volatility_analysis.png')
    plt.close()