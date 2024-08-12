import random

# Define the cost function (simple quadratic function)
def cost_function(x):
    return x**2 + 4*x + 4

# Define the gradient of the cost function
def gradient(x):
    return 2*x + 4

# Gradient Descent function
def gradient_descent(starting_point, learning_rate, iterations):
    x = starting_point
    for i in range(iterations):
        grad = gradient(x)
        x = x - learning_rate * grad
        cost = cost_function(x)
        print(f"Iteration {i+1}: x = {x:.5f}, cost = {cost:.5f}")
    return x

# Generate a random starting point between -10 and 10
starting_point = random.uniform(-10, 10)
learning_rate = 0.1  # You can adjust the learning rate
iterations = 100  # Number of iterations

# Perform Gradient Descent
final_x = gradient_descent(starting_point, learning_rate, iterations)

print(f"Final value after {iterations} iterations: x = {final_x:.5f}")
