from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import pandas as pd

from tools import (
    get_total_revenue,
    get_best_region,
    get_risk_summary,
    forecast_next_month
)


# Create Flask application
app = Flask(__name__)
CORS(app)
@app.route("/dashboard")
def dashboard():
    return render_template("index.html")
# Load customer data
df = pd.read_csv("data/sales_data.csv")


# Home endpoint
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to RevOpsAI API",
        "status": "running"
    })


# Revenue endpoint
@app.route("/api/revenue")
def revenue():
    total_revenue = get_total_revenue(df)

    return jsonify({
        "total_revenue": int(total_revenue)
    })


# Best region endpoint
@app.route("/api/region")
def region():
    best_region, revenue = get_best_region(df)

    return jsonify({
        "best_region": str(best_region),
        "revenue": int(revenue)
    })


# Risk endpoint
@app.route("/api/risk")
def risk():
    summary = get_risk_summary(df)

    return jsonify({
        "customer_count": int(summary["customer_count"]),
        "customer_ids": str(summary["customer_ids"]),
        "revenue_at_risk": int(summary["revenue_at_risk"]),
        "priority_customer": str(summary["priority_customer_id"]),
        "priority_customer_revenue": int(
            summary["priority_customer_revenue"]
        )
    })

# Forecast endpoint
@app.route("/api/forecast")
def forecast():
    forecast_data = forecast_next_month()

    return jsonify({
        "current_revenue": float(forecast_data["current_revenue"]),
        "predicted_revenue": float(forecast_data["predicted_revenue"]),
        "expected_increase": float(forecast_data["expected_increase"]),
        "expected_growth": float(forecast_data["expected_growth"])
    })

@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.get_json()

    question = data.get("question", "")

    if not question:
        return jsonify({
            "error": "Question is required"
        }), 400

    from agent import run_agent

    answer = run_agent(question)

    return jsonify({
        "question": question,
        "answer": answer
    })


@app.route("/api/revenue-history")
def revenue_history():
    history = pd.read_csv("data/forecast/revenue_history.csv")

    return jsonify({
        "months": history["month"].tolist(),
        "revenue": history["revenue"].astype(float).tolist()
    })
# Start Flask server
if __name__ == "__main__":
    app.run(debug=True)