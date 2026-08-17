import pandas as pd

from tools import (
    get_total_revenue,
    get_best_region,
    find_at_risk_customers,
    forecast_next_month
)

# Load sales data
df = pd.read_csv("data/sales_data.csv")


# Use Tool 1
total_revenue = get_total_revenue(df)

print("Total monthly revenue:", total_revenue)


# Use Tool 2
best_region, best_region_revenue = get_best_region(df)

print("\nBest performing region:", best_region)
print("Revenue:", best_region_revenue)


# Use Tool 3
at_risk_customers = find_at_risk_customers(df)

print("\nCustomers at high risk:")
print(at_risk_customers)

# Use Tool 4
predicted_revenue = forecast_next_month()

print("\nPredicted revenue for next month:", predicted_revenue)