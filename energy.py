<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv(".venv/assets/energy_usage.csv")

X = df[["temperature", "humidity", "hour", "is_weekend"]]
y = df["consumption"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.figure(figsize=(8,5))
plt.plot(range(len(y_test)), y_test.values)
plt.plot(range(len(y_test)), y_pred)
plt.title("Actual vs Predicted Consumption")
plt.legend(["Actual", "Predicted"])
plt.xlabel("Sample")
plt.ylabel("Consumption")
plt.tight_layout()
plt.show()
=======
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv(".venv/assets/energy_usage.csv")

X = df[["temperature", "humidity", "hour", "is_weekend"]]
y = df["consumption"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.figure(figsize=(8,5))
plt.plot(range(len(y_test)), y_test.values)
plt.plot(range(len(y_test)), y_pred)
plt.title("Actual vs Predicted Consumption")
plt.legend(["Actual", "Predicted"])
plt.xlabel("Sample")
plt.ylabel("Consumption")
plt.tight_layout()
plt.show()
>>>>>>> 377a7d2e62a3336d1abfcc99bc439b220aee4b54
