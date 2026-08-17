import pandas as pd

from tools import (
    get_total_revenue,
    get_best_region,
    find_at_risk_customers,
    forecast_next_month,
    get_risk_summary
)


# Load customer data
df = pd.read_csv("data/sales_data.csv")


def run_agent(user_question):
    """
    Decide which tool to use based on the user's question.
    """

    question = user_question.lower().strip()

    # Tool 1: Total Revenue
    if any(word in question for word in [
        "total revenue",
        "how much revenue",
        "revenue are we making",
        "monthly income",
        "our revenue"
    ]):
        result = get_total_revenue(df)

        return f"Total monthly revenue is ₹{result:,.0f}."


    # Tool 2: Best Region
    elif any(word in question for word in [
        "best region",
        "best performing region",
        "top region",
        "which area",
        "where are we performing best"
    ]):
        region, revenue = get_best_region(df)

        return (
            f"The best-performing region is {region} "
            f"with revenue of ₹{revenue:,.0f}."
        )


    # Tool 3: Risk Summary
    elif any(word in question for word in [
        "risk",
        "at risk",
        "might churn",
        "inactive customers",
        "need attention",
        "revenue at risk"
    ]):
        summary = get_risk_summary(df)

        return (
            f"There are {summary['customer_count']} high-risk customers: "
            f"{summary['customer_ids']}. "
            f"Monthly revenue at risk is "
            f"₹{summary['revenue_at_risk']:,.0f}. "
            f"Priority customer: "
            f"{summary['priority_customer_id']} "
            f"with ₹{summary['priority_customer_revenue']:,.0f} "
            f"in monthly revenue. "
            f"Recommended action: Contact "
            f"{summary['priority_customer_id']} first with a "
            f"retention-focused offer because it represents the "
            f"highest monthly revenue among the at-risk customers."
        )


    # Tool 4: Revenue Forecast
    elif any(word in question for word in [
        "forecast",
        "next month",
        "future revenue",
        "predict revenue",
        "revenue can we expect",
        "how much will we make",
        "what will our revenue be",
        "predict next month's revenue",
        "expected revenue",
        "revenue prediction"
    ]):
        forecast = forecast_next_month()

        return (
            f"Current revenue is "
            f"₹{forecast['current_revenue']:,.0f}. "
            f"Predicted revenue for next month is "
            f"₹{forecast['predicted_revenue']:,.0f}. "
            f"Expected increase is "
            f"₹{forecast['expected_increase']:,.0f}, "
            f"which represents an expected growth of "
            f"{forecast['expected_growth']:.2f}%."
        )


    # Unknown question
    else:
        return "I don't know which tool to use for that question."


# Run interactive agent only when this file is executed directly
if __name__ == "__main__":

    question = input("Ask RevOpsAI: ")

    answer = run_agent(question)

    print("\nRevOpsAI:")
    print(answer)
    