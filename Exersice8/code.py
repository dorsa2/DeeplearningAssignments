import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Define the symbol
x = sp.symbols('x')

# 1. Sigmoid function and its derivative
sigmoid = 1 / (1 + sp.exp(-x))
sigmoid_derivative = sp.diff(sigmoid, x)

# 2. Tanh function and its derivative
tanh = (sp.exp(x) - sp.exp(-x)) / (sp.exp(x) + sp.exp(-x))
tanh_derivative = sp.diff(tanh, x)

# 3. Softplus function and its derivative
softplus = sp.log(1 + sp.exp(x))
softplus_derivative = sp.diff(softplus, x)

# Print symbolic derivatives
print("Sigmoid Derivative:", sigmoid_derivative.simplify())
print("Tanh Derivative:", tanh_derivative.simplify())
print("Softplus Derivative:", softplus_derivative.simplify())

# Optional: Plot functions and their derivatives
f_sigmoid = sp.lambdify(x, sigmoid, "numpy")
f_sigmoid_deriv = sp.lambdify(x, sigmoid_derivative, "numpy")

f_tanh = sp.lambdify(x, tanh, "numpy")
f_tanh_deriv = sp.lambdify(x, tanh_derivative, "numpy")

f_softplus = sp.lambdify(x, softplus, "numpy")
f_softplus_deriv = sp.lambdify(x, softplus_derivative, "numpy")

x_vals = np.linspace(-5, 5, 400)

plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.plot(x_vals, f_sigmoid(x_vals), label="sigmoid(x)")
plt.title("Sigmoid Function")
plt.grid(True)

plt.subplot(3, 2, 2)
plt.plot(x_vals, f_sigmoid_deriv(x_vals), label="sigmoid'(x)", color='orange')
plt.title("Sigmoid Derivative")
plt.grid(True)

plt.subplot(3, 2, 3)
plt.plot(x_vals, f_tanh(x_vals), label="tanh(x)")
plt.title("Tanh Function")
plt.grid(True)

plt.subplot(3, 2, 4)
plt.plot(x_vals, f_tanh_deriv(x_vals), label="tanh'(x)", color='orange')
plt.title("Tanh Derivative")
plt.grid(True)

plt.subplot(3, 2, 5)
plt.plot(x_vals, f_softplus(x_vals), label="softplus(x)")
plt.title("Softplus Function")
plt.grid(True)

plt.subplot(3, 2, 6)
plt.plot(x_vals, f_softplus_deriv(x_vals), label="softplus'(x)", color='orange')
plt.title("Softplus Derivative")
plt.grid(True)

plt.tight_layout()
plt.show()
