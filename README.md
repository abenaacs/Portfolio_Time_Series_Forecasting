# Time Series Forecasting for Portfolio Management Optimization: Task 1

## Overview

This project focuses on **Task 1** of the portfolio management optimization challenge: **Preprocessing and Exploratory Data Analysis (EDA)**. The goal is to clean, preprocess, and analyze historical financial data for three key assets:

- **TSLA**: High-growth, high-risk stock.
- **BND**: Bond ETF providing stability and income.
- **SPY**: S&P 500 ETF offering diversified market exposure.

The dataset spans from **January 1, 2015, to January 31, 2025**, sourced from Yahoo Finance using the `yfinance` library. This task lays the foundation for building predictive models and optimizing portfolios in subsequent stages of the project.

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
│   └── plots/        # Visualization outputs (e.g., time series plots, volatility analysis)
│
├── utils/            # Utility functions for data processing and analysis
│   └── data_preprocessing.py  # Functions for fetching and preprocessing data
│
├── main.py           # Main script to execute Task 1
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

### Fetching Data

The project retrieves historical financial data for TSLA, BND, and SPY from **January 1, 2015, to January 31, 2025**, using the `yfinance` library. The raw data is saved in the `data/raw/` directory.

#### Example:

```python
import yfinance as yf

# Fetch data for TSLA
data = yf.download("TSLA", start="2015-01-01", end="2025-01-31")
print(data.head())
```

### Preprocessing

The raw data undergoes preprocessing to ensure it is ready for analysis. Key steps include:

- Handling missing values using forward-fill (`ffill`) and backward-fill (`bfill`).
- Calculating daily returns, rolling means (30-day window), and standard deviations.
- Saving cleaned data in the `data/processed/` directory.

#### Example:

```python
# Calculate daily returns
data['Daily_Return'] = data['Adj Close'].pct_change()

# Rolling mean and standard deviation
data['Rolling_Mean'] = data['Adj Close'].rolling(window=30).mean()
data['Rolling_Std'] = data['Adj Close'].rolling(window=30).std()
```

### Exploratory Data Analysis (EDA)

The project performs EDA to uncover insights into the data:

1. **Visualizing Closing Prices**:

   - Plot adjusted closing prices over time to identify trends.
   - Example: Use `plotly` for interactive visualizations.

2. **Analyzing Volatility**:

   - Compute rolling statistics (mean and standard deviation) to assess short-term trends and fluctuations.

3. **Time Series Decomposition**:
   - Decompose time series into trend, seasonal, and residual components using `statsmodels`.

#### Example:

```python
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

# Decompose time series
decomposition = seasonal_decompose(data['Adj Close'], model='additive', period=30)
decomposition.plot()
plt.show()
```

## Features

### Data Preprocessing

- **Missing Value Handling**: Missing values are addressed using forward-fill (`ffill`) and backward-fill (`bfill`) methods.
- **Feature Engineering**: Daily returns, rolling means, and standard deviations are calculated to enrich the dataset.

### Exploratory Data Analysis (EDA)

- **Interactive Visualizations**: Interactive plots using `plotly` for better engagement and exploration.
- **Volatility Analysis**: Rolling statistics provide insights into short-term trends and fluctuations.
- **Time Series Decomposition**: Decompose time series into trend, seasonal, and residual components to understand underlying patterns.

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

Ensure your code adheres to the project’s coding standards and includes appropriate tests.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## Contact

For questions, feedback, or collaboration, feel free to reach out:

- **Email**: abenezernigussiecs@gmail.com
- **GitHub**: [Abenezer Nigussie](https://github.com/abenaacs)
