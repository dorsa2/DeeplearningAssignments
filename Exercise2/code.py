import matplotlib.pyplot as plt

# Function to minimize: f(x) = (x - 1)^2 + 2
def f(x):
    return (x - 1)**2 + 2

# Derivative of the function
def df(x):
    return 2 * (x - 1)

# Gradient Descent Parameters
x0 = 3               # Initial guess
learning_rate = 0.1  # Step size
epsilon = 1e-6       # Convergence criterion
max_iter = 100       # Max number of iterations

x = x0
x_history = [x]

for i in range(max_iter):
    grad = df(x)
    new_x = x - learning_rate * grad
    x_history.append(new_x)
    if abs(new_x - x) < epsilon:
        break
    x = new_x

print(f"Minimum found at x = {x:.6f}")
print(f"Minimum value f(x) = {f(x):.6f}")

# Plotting
x_vals = [i * 0.1 for i in range(-10, 40)]
y_vals = [f(i) for i in x_vals]
plt.plot(x_vals, y_vals, label='f(x) = (x - 1)^2 + 2')
plt.plot(x_history, [f(xi) for xi in x_history], 'ro--', label='Gradient Descent Path')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gradient Descent Optimization')
plt.legend()
plt.grid(True)
plt.show()
