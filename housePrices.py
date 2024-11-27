import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Load data
data = pd.read_csv("Housing.csv")

# Data preprocessing
data = data.fillna(data.mean()) # Handling missing values
X = data.drop("price", axis=1)
y = data["price"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Model evaluation
prediction = model.predict(X_test)
mse = mean_squared_error(y_test, prediction)
print(f"Mean Squared Error: {mse}")

# Serialize the model
joblib.dump(model, "model.pkl")
