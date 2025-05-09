# Air Quality Time Series Forecasting

This project focuses on forecasting air quality metrics using multivariate time series analysis. The dataset includes various air quality indicators, and the goal is to allow users to forecast selected features over a user-defined time horizon. The application is deployed using Streamlit for interactive use.

## 📊 Project Overview

- **Dataset**: Air Quality Data (with multiple features/variables)
- **Goal**: Forecast selected air quality features based on past data trends
- **Approach**:
  - Exploratory Data Analysis (EDA)
  - Stationarity testing and preprocessing
  - Fitting a **Vector Autoregression (VAR)** model
  - Forecasting future values
  - Deploying an interactive forecasting tool via **Streamlit**

## ✅ Key Features

- Stationarity checks and transformations (if needed)
- Multivariate modeling using the VAR model
- Interactive Streamlit interface:
  - User selects a feature to forecast
  - User chooses the number of future time steps
  - Forecasted results are plotted and displayed

## 🛠️ Tools & Libraries

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Statsmodels (for VAR model)
- Streamlit (for deployment)

