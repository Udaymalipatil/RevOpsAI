import pandas as pd
from sklearn.linear_model import LinearRegression


def get_total_revenue(df):
    """
    Calculate the total monthly revenue from all customers.
    """
    total_revenue = df["monthly_revenue"].sum()

    return total_revenue


def get_best_region(df):
    """
    Find the region with the highest total monthly revenue.
    """
    revenue_by_region = df.groupby("region")["monthly_revenue"].sum()

    best_region = revenue_by_region.idxmax()
    best_region_revenue = revenue_by_region.max()

    return best_region, best_region_revenue


def find_at_risk_customers(df):
    """
    Identify customers with low engagement and long periods
    since their last purchase.
    """
    at_risk = df[
        (df["last_purchase_days"] > 60)
        & (df["engagement_score"] < 60)
    ]

    return at_risk


def forecast_next_month():
    """
    Train a baseline Linear Regression model and calculate
    next month's revenue forecast and expected growth.
    """

    # Load historical revenue data
    df = pd.read_csv("data/forecast/revenue_history.csv")

    # Create numerical time feature
    df["month_number"] = range(1, len(df) + 1)

    # Separate input and output
    X = df[["month_number"]]
    y = df["revenue"]

    # Create and train the model
    model = LinearRegression()
    model.fit(X, y)

    # Current revenue = latest month in our dataset
    current_revenue = df["revenue"].iloc[-1]

    # Next month number
    next_month_number = len(df) + 1

    # Create input for next month
    next_month = pd.DataFrame({
        "month_number": [next_month_number]
    })

    # Predict next month's revenue
    predicted_revenue = model.predict(next_month)[0]

    # Calculate expected increase
    expected_increase = predicted_revenue - current_revenue

    # Calculate expected growth percentage
    expected_growth = (
        expected_increase / current_revenue
    ) * 100

    return {
        "current_revenue": current_revenue,
        "predicted_revenue": predicted_revenue,
        "expected_increase": expected_increase,
        "expected_growth": expected_growth
    }
def get_risk_summary(df):
    """
    Generate a business summary for high-risk customers.
    """

    # Find high-risk customers
    at_risk = find_at_risk_customers(df)

    # Count high-risk customers
    customer_count = len(at_risk)

    # Calculate monthly revenue associated with high-risk customers
    revenue_at_risk = at_risk["monthly_revenue"].sum()

    # Get customer IDs
    customer_ids = ", ".join(at_risk["customer_id"])

    # Find the highest-value at-risk customer
    priority_customer = at_risk.loc[
        at_risk["monthly_revenue"].idxmax()
    ]

    priority_customer_id = priority_customer["customer_id"]
    priority_customer_revenue = priority_customer["monthly_revenue"]

    return {
        "customer_count": customer_count,
        "revenue_at_risk": revenue_at_risk,
        "customer_ids": customer_ids,
        "priority_customer_id": priority_customer_id,
        "priority_customer_revenue": priority_customer_revenue
    }