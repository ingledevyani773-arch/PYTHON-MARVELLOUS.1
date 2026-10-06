from sklearn.linear_model import LinearRegression

# Features
X = [
    [1, 7],
    [2, 6],
    [3, 7],
    [4, 6],
    [5, 8]
]

# Target
y = [50, 55, 60, 65, 70]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Print coefficients
print("Study Hours Coefficient:", model.coef_[0])
print("Sleep Hours Coefficient:", model.coef_[1])

# Print intercept
print("Intercept:", model.intercept_)