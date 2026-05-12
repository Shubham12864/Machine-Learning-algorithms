

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
y = [15,20,25,30,35,40,45,50,55,60,65,70,75,80,85]
m = 0
b = 0
lr = 0.01
epochs = 1400

def predict(x, m, b):
    return m * x + b

def compute_loss(x, y, m, b):
    total_error = 0
    for i in range(len(x)):
        y_predict = predict(x[i], m, b)
        total_error += (y[i] - y_predict) ** 2
    return total_error / len(x)

def gradient_descent(x, y, m, b, lr):
    m_grad = 0
    b_grad = 0
    n = len(x)
    for i in range(n):
        y_predict = predict(x[i], m, b)
        m_grad += -(2 / n) * x[i] * (y[i] - y_predict)
        b_grad += -(2 / n) * (y[i] - y_predict)
    m = m - lr * m_grad
    b = b - lr * b_grad
    return m, b

for epoch in range(epochs):
    m, b = gradient_descent(x, y, m, b, lr)
    if epoch % 10 == 0:
        loss = compute_loss(x, y, m, b)
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

print("\nFinal Parameters:")
print(f"m (slope): {m:.4f}")
print(f"b (intercept): {b:.4f}")

test_x = float(input("Enter your value: "))
prediction = predict(test_x, m, b)
print(f"\nPrediction for x={test_x}: {prediction:.2f}")

y_predict = []
for i in x:
    y_predict.append(predict(i, m, b))








