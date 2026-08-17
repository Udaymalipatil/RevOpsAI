import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load historical revenue data
df = pd.read_csv("data/forecast/revenue_history.csv")


# Create a numerical time feature
df["month_number"] = range(1, len(df) + 1)


# Separate input and output
X = df[["month_number"]]
y = df["revenue"]

# Split data into training and testing sets
X_train = X.iloc[:15]
X_test = X.iloc[15:]

y_train = y.iloc[:15]
y_test = y.iloc[15:]

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)
# Predict revenue for the test data
test_predictions = model.predict(X_test)

# Evaluate the model on unseen data
r2 = r2_score(y_test, test_predictions)

print("\nTest R2 Score:", r2)

# Predict revenue for August 2026
next_month = pd.DataFrame({"month_number": [20]})

predicted_revenue = model.predict(next_month)

print("\nPredicted revenue for August 2026:", predicted_revenue[0])

# Display the data
print("Historical Revenue Data:")
print(df)