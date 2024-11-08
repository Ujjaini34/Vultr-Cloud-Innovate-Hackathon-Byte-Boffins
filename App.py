from flask import Flask, jsonify, request
from pandas import DataFrame
from prophet import Prophet  # Use 'fbprophet' for older versions
from sklearn.ensemble import IsolationForest
import requests
import pandas as pd

app = Flask(__name__)

# DataProcessor, CostForecaster, AnomalyDetector, and RealTimeOptimizer classes remain the same

@app.route('/api/forecast', methods=['POST'])
def forecast_costs():
    data = request.json
    df = pd.DataFrame(data)
    
    forecaster = CostForecaster()
    forecast = forecaster.forecast_costs(df)
    
    if forecast.empty:
        return jsonify({"message": "No valid forecast data found"}), 400
    return jsonify(forecast.to_dict(orient='records'))

@app.route('/api/anomalies', methods=['POST'])
def detect_anomalies():
    data = request.json
    df = pd.DataFrame(data)
    
    detector = AnomalyDetector()
    anomalies = detector.detect_anomalies(df)
    
    if anomalies.empty:
        return jsonify({"message": "No anomalies detected"}), 400
    return jsonify(anomalies.to_dict(orient='records'))

@app.route('/api/optimize', methods=['POST'])
def optimize_resources():
    data = request.json
    df = pd.DataFrame(data)
    
    optimizer = RealTimeOptimizer()
    suggestions = optimizer.optimize_resources(df)
    
    return jsonify({"suggestions": suggestions})

if __name__ == '__main__':
    app.run(debug=True)
