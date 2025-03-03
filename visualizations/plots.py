import matplotlib.pyplot as plt
import plotly.graph_objects as go


def plot_time_series(data, asset, column, title):
    """Plot time series data."""
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data[column], label=column, color="blue")
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(column)
    plt.legend()
    plt.grid(True)
    plt.savefig(f"visualizations/plots/{asset}_{column}_time_series.png")
    plt.close()


def plot_volatility_analysis(data, asset, window):
    """Plot rolling mean and standard deviation."""
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["Rolling_Mean"], label="Rolling Mean", color="green")
    plt.plot(data.index, data["Rolling_Std"], label="Rolling Std", color="red")
    plt.title(f"{asset} Volatility Analysis (Window={window})")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"visualizations/plots/{asset}_volatility_analysis.png")
    plt.close()


def plot_forecast(data, forecast, asset):
    """
    Plots historical data and forecasted prices with confidence intervals.

    Args:
        data (pd.DataFrame): Historical data.
        forecast (pd.DataFrame): Forecasted data with confidence intervals.
        asset (str): Name of the asset.
    """
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=data.index, y=data["Adj Close"], mode="lines", name="Historical Prices"
        )
    )
    fig.add_trace(
        go.Scatter(
            x=forecast.index, y=forecast["Forecast"], mode="lines", name="Forecast"
        )
    )
    fig.add_trace(
        go.Scatter(
            x=forecast.index,
            y=forecast["lower Adj Close"],
            fill=None,
            mode="lines",
            line_color="gray",
            name="Lower CI",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=forecast.index,
            y=forecast["upper Adj Close"],
            fill="tonexty",
            mode="lines",
            line_color="gray",
            name="Upper CI",
        )
    )
    fig.update_layout(
        title=f"{asset} Price Forecast", xaxis_title="Date", yaxis_title="Price"
    )
    fig.write_image(f"visualizations/plots/{asset}_forecast.png")
