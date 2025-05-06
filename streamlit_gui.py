import pandas as pd
import streamlit as st
import pickle as pkl
import matplotlib.pyplot as plt

# Load once into session state
if 'model' not in st.session_state or 'data' not in st.session_state:
    try:
        with open('Time_Series_Model.pkl', 'rb') as f:
            st.session_state.model = pkl.load(f)

        st.session_state.data = pd.read_csv("forecast_data.csv", index_col=0, parse_dates=True)

    except Exception as e:
        st.error(f"❌ Error loading model or data: {e}")


def forecast_future(model, train_data, steps):
    input_data = train_data.values[-model.k_ar:]
    forecast_diff = model.forecast(y=input_data, steps=steps)

    forecast_diff_df = pd.DataFrame(forecast_diff, columns=train_data.columns)
    last_train_values = train_data.iloc[-1]
    forecast = forecast_diff_df.cumsum().add(last_train_values.values)

    return forecast

def predict_and_plot(model, data, selected_feature, steps):
    cutoff = data.index.max() - pd.Timedelta(days=2)
    train = data[data.index <= cutoff]
    forecast = forecast_future(model, train, steps)

    forecast.index = pd.date_range(start=train.index[-1] + pd.Timedelta(hours=1), periods=steps, freq='H')

    #Get the last 48 hours up to the forecast start time
    recent_actual = data[selected_feature][train.index[-1] - pd.Timedelta(hours=47):train.index[-1]]

    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(recent_actual, label='Actual')
    ax.plot(forecast[selected_feature], label='Forecast', linestyle='--')
    ax.set_title(f'Forecast vs Actual for {selected_feature}')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)



st.title("📈 Multivariate Time Series Forecasting")

# If model and data are available
if 'model' in st.session_state and 'data' in st.session_state:
    model = st.session_state.model
    data = st.session_state.data

    steps = st.number_input("🔢 Enter number of hours to forecast:", min_value=1, max_value=500, value=24)
    selected_feature = st.selectbox("📌 Select feature to forecast:", data.columns)

    if st.button("📊 Forecast"):
        predict_and_plot(model, data, selected_feature, steps)

    else:
        st.warning("Model and data must be available to proceed.")
