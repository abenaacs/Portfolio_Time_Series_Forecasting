# Time Series Forecasting for Portfolio Management Optimization: Task 1

## Overview

This project focuses on **Task 1** of the portfolio management optimization challenge: **Preprocessing and Exploratory Data Analysis (EDA)**. The objective is to clean, preprocess, and analyze historical financial data for three key assets:

- **TSLA**: High-growth, high-risk stock.
- **BND**: Bond ETF providing stability and income.
- **SPY**: S&P 500 ETF offering diversified market exposure.

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
│   └── plots/
│
├── utils/            # Utility functions for data processing and analysis
│   └── data_preprocessing.py
│
├── main.py           # Main script to execute Task 1
├── README.md         # Project documentation
└── requirements.txt  # List of dependencies
```

## Installation

### Prerequisites

- Python 3.8 or higher
- Git (optional, for cloning the repository)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/abenaacs/Portfolio_Time_Series_Forecasting.git
   cd Portfolio_Time_Series_Forecasting
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the project:
   ```bash
   python main.py
   ```

## Usage

### Fetching Data

The project retrieves historical data for TSLA, BND, and SPY from **2015 to 2025** using `yfinance`. The raw data is saved in `data/raw/`.

### Preprocessing

The raw data undergoes preprocessing to:

- Handle missing values using forward-fill and backward-fill.
- Compute daily returns, rolling means, and standard deviations.
- Store cleaned data in `data/processed/`.

### Exploratory Data Analysis (EDA)

Key analysis steps include:

- Visualizing closing prices over time.
- Assessing volatility with rolling statistics.
- Decomposing time series into trend, seasonal, and residual components.

## Features

### Data Preprocessing

- Missing values handled using forward-fill and backward-fill.
- Calculation of daily returns, rolling means, and standard deviations.

### Exploratory Data Analysis

- Interactive visualizations with `plotly`.
- Time series decomposition into trend, seasonal, and residual components.

## Contributing

We welcome contributions! To contribute:

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

For questions or feedback, reach out via:

- **Email**: abenezernigussiecs@gmail.com
- **GitHub**: [Abenezer Nigussie](https://github.com/abenaacs)
