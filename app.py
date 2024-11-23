from flask import Flask, jsonify, render_template, Response
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    data = pd.read_csv('data_daily.csv')
    data['# Date'] = pd.to_datetime(data['# Date'])
    data.set_index('# Date', inplace=True)

    monthly_data = data['Receipt_Count'].resample('M').sum()

    sarima_model = SARIMAX(monthly_data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 4))
    sarima_fit = sarima_model.fit()

    predictions_sarima = sarima_fit.get_forecast(steps=12)
    predicted_mean = predictions_sarima.predicted_mean

    predicted_mean.iloc[0] = monthly_data.iloc[-1] * 1.01 
    predicted_mean.iloc[1] = predicted_mean.iloc[0] * 0.95

    for i in range(2, len(predicted_mean)):
        if i % 4 == 0: 
            predicted_mean.iloc[i] = predicted_mean.iloc[i - 1] * 0.97  
        elif i % 4 == 1:
            predicted_mean.iloc[i] = predicted_mean.iloc[i - 1] * 1.02  

    full_predictions = pd.concat([monthly_data, predicted_mean])

    plt.figure(figsize=(10, 6))
    plt.plot(full_predictions.index, full_predictions, label='Prediction', linestyle='--', marker='x')
    plt.plot(monthly_data.index, monthly_data, label='Actual 2021', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Receipt Count')
    plt.title('2022 Prediction')
    plt.legend()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    actual_data_formatted = monthly_data.map('{:,.0f}'.format)
    predicted_data_formatted = predicted_mean.map('{:,.0f}'.format)

    actual_data_text = actual_data_formatted.to_string()
    predicted_data_text = predicted_data_formatted.to_string()

    return render_template('index.html', plot_url=plot_url, actual_data=actual_data_text, predicted_data=predicted_data_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
