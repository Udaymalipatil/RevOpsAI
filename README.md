# RevOpsAI

## AI-Powered Revenue Operations Intelligence Platform

RevOpsAI is a full-stack business intelligence platform that analyzes sales and customer data to provide revenue insights, regional performance analysis, customer churn-risk identification, and revenue forecasting.

The platform combines a **React frontend**, **Flask REST API backend**, **Python-based business intelligence tools**, **Pandas**, and **Scikit-learn** to provide an interactive revenue operations dashboard.

---

## 🚀 Features

### 📊 Revenue Analytics
- Calculates total monthly revenue.
- Displays overall revenue performance.
- Provides revenue trend visualization.

### 🌎 Regional Performance
- Groups revenue by region.
- Identifies the best-performing region.
- Displays regional revenue.

### ⚠️ Customer Churn Risk
- Identifies customers with low engagement.
- Detects customers with long periods since their last purchase.
- Calculates total revenue at risk.
- Identifies the highest-value at-risk customer.
- Provides a recommended retention action.

### 📈 Revenue Forecasting
- Uses Linear Regression to analyze historical revenue.
- Predicts revenue for the next month.
- Calculates expected revenue increase.
- Calculates expected percentage growth.

### 🤖 AI Business Agent
Users can ask questions such as:

- "How much revenue are we making?"
- "Which is the best performing region?"
- "Which customers might churn?"
- "What is the forecast for next month?"

The agent determines which business analysis tool should process the question and returns a business-focused response.

---

## 🏗️ System Architecture

```text
                    React Frontend
                         │
                         │ REST API
                         ▼
                   Flask Backend
                         │
                         ▼
                   RevOpsAI Agent
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
     Revenue Tool   Risk Analysis   Forecast Tool
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                Pandas + Scikit-learn
                         │
                         ▼
                    CSV Datasets
