from sklearn.linear_model import LinearRegression

# Your data
X = [[1], [2], [3], [4], [5]]  # Input features
y = [2, 4, 6, 8, 10]  # Target variable

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Predict using the trained model
X_test = [[6], [7], [8]]  # New input features
y_pred = model.predict(X_test)

print(y_pred)  # Print the predicted values

    