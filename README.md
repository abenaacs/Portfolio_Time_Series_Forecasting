# Time Series Forecasting for Portfolio Management Optimization

## Overview

This project focuses on leveraging time series forecasting and portfolio optimization techniques to enhance investment strategies. It consists of four key tasks:

1. **Preprocessing and Exploratory Data Analysis (EDA)**: Clean, preprocess, and analyze historical financial data for three key assets:

   - **TSLA**: High-growth, high-risk stock.
   - **BND**: Bond ETF providing stability and income.
   - **SPY**: S&P 500 ETF offering diversified market exposure.

2. **Time Series Forecasting Models**: Develop predictive models (e.g., ARIMA, SARIMA, LSTM) to forecast future stock prices for TSLA, BND, and SPY.

3. **Forecast Future Market Trends**: Use the trained models to predict future market trends, analyze results, and identify opportunities and risks.

4. **Portfolio Optimization**: Optimize a sample portfolio based on forecasted returns to maximize returns while minimizing risks.

The dataset spans from **January 1, 2015, to January 31, 2025**, sourced from Yahoo Finance using the `yfinance` library.

## Table of Contents

1. [Directory Structure](#directory-structure)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Features](#features)
5. [Contributing](#contributing)
6. [License](#license)
7. [Contact](#contact)

## Directory Structure

```
project/
│
├── data/
│   ├── raw/          # Raw data fetched from Yahoo Finance
│   └── processed/    # Cleaned and preprocessed data
│
├── visualizations/   # Scripts and outputs for visualizations
│   └── plots/        # Visualization outputs (e.g., time series plots, forecasts)
│
├── models/           # Scripts for time series forecasting models
│   └── forecasting_models.py  # ARIMA, SARIMA, or LSTM implementation
│
├── utils/            # Utility functions for data processing and analysis
│   └── data_preprocessing.py  # Functions for fetching and preprocessing data
│
├── portfolio_optimization.py  # Portfolio optimization logic
├── main.py           # Main script to execute the entire pipeline
├── README.md         # Project documentation
└── requirements.txt  # List of dependencies
```

## Installation

### Prerequisites

- Python 3.8 or higher.
- Git (optional, for cloning the repository).

### Steps

1. **Clone the Repository**:

```bash
git clone https://github.com/abenaacs/Portfolio_Time_Series_Forecasting.git
cd Portfolio_Time_Series_Forecasting
```

2. **Install Dependencies**:
   Install the required libraries listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

3. **Run the Project**:
   Execute the main script to run the entire pipeline:

```bash
python main.py
```

## Usage

### Task 1: Preprocessing and Exploratory Data Analysis (EDA)

#### Fetching Data

The project retrieves historical financial data for TSLA, BND, and SPY from **January 1, 2015, to January 31, 2025**, using the `yfinance` library. The raw data is saved in the `data/raw/` directory.

#### Preprocessing

The raw data undergoes preprocessing to ensure it is ready for analysis. Key steps include:

- Handling missing values using forward-fill (`ffill`) and backward-fill (`bfill`).
- Calculating daily returns, rolling means (30-day window), and standard deviations.
- Saving cleaned data in the `data/processed/` directory.

#### Exploratory Data Analysis (EDA)

The project performs EDA to uncover insights into the data:

1. **Visualizing Closing Prices**: Plot adjusted closing prices over time to identify trends.
2. **Analyzing Volatility**: Compute rolling statistics (mean and standard deviation) to assess short-term trends and fluctuations.
3. **Time Series Decomposition**: Decompose time series into trend, seasonal, and residual components using `statsmodels`.

### Task 2: Time Series Forecasting Models

#### Model Development

The project builds time series forecasting models using:

- **ARIMA (AutoRegressive Integrated Moving Average)**: Suitable for univariate time series with no seasonality.
- **SARIMA (Seasonal ARIMA)**: Extends ARIMA by considering seasonality.
- **LSTM (Long Short-Term Memory)**: A type of recurrent neural network (RNN) well-suited for capturing long-term dependencies.

#### Training and Evaluation

- The dataset is split into training (80%) and testing (20%) sets.
- Models are trained on the training set and evaluated on the test set using metrics like:
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)
  - Mean Absolute Percentage Error (MAPE)

### Task 3: Forecast Future Market Trends

#### Generate Forecasts

Use the trained models to forecast future stock prices for 6-12 months. The forecasts include confidence intervals to show the range within which future prices are expected to lie.

#### Visualize Results

Visualize the forecast alongside historical data using `plotly`. Analyze trends, volatility, and potential risks.

### Task 4: Optimize Portfolio Based on Forecast

#### Combine Forecasts

Combine forecasts for TSLA, BND, and SPY into a single DataFrame. Compute annualized returns and covariance matrix to understand how asset returns move together.

#### Portfolio Optimization

Optimize portfolio weights to maximize the Sharpe Ratio, balancing risk and return. Adjust allocations based on forecasted trends and risks.

## Features

### Task 1: Preprocessing and EDA

- Missing value handling using forward-fill and backward-fill.
- Feature engineering: Daily returns, rolling means, and standard deviations.
- Interactive visualizations with `plotly` and time series decomposition.

### Task 2: Time Series Forecasting

- ARIMA, SARIMA, or LSTM models for forecasting.
- Evaluation metrics: MAE, RMSE, MAPE.
- Confidence intervals for forecasts.

### Task 3: Future Market Trends

- Long-term trend analysis (upward, downward, stable).
- Volatility and risk assessment.
- Insights into market opportunities and risks.

### Task 4: Portfolio Optimization

- Combining forecasts for multiple assets.
- Risk-return analysis: Sharpe Ratio, Value at Risk (VaR).
- Optimized portfolio weights to maximize returns and minimize risks.

## Contributing

We welcome contributions to this project! To contribute:

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/YourFeatureName
```

3. Commit your changes:

```bash
git commit -m "Add YourFeatureName"
```

4. Push to the branch:

```bash
git push origin feature/YourFeatureName
```

5. Open a pull request.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## Contact

For questions, feedback, or collaboration, feel free to reach out:

- **Email**: abenezernigussiecs@gmail.com
- **GitHub**: [Abenezer Nigussie](https://github.com/abenaacs)
