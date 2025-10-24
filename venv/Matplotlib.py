import numpy as np
import matplotlib.pyplot as plt

# TASK 1: Plot a function
print("Task 1: Function plot")
x1 = np.linspace(-10, 10, 200)
y1 = x1**2 * np.sin(x1)
plt.figure(figsize=(10, 6))
plt.plot(x1, y1, 'b-', linewidth=2)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function: f(x) = x² · sin(x), x ∈ [-10, 10]')
plt.grid(True, alpha=0.3)
plt.show()

# TASK 2: Histogram with normal distribution
print("Task 2: Histogram")
data2 = np.random.normal(loc=5, scale=2, size=1000)
plt.figure(figsize=(10, 5))
plt.hist(data2, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram: Normal Distribution (μ=5, σ=2)')
plt.grid(True, alpha=0.3)
plt.show()

# TASK 3: Pie chart with hobbies
print("Task 3: Pie chart")
hobbies = ['Programming', 'Gaming', 'Reading', 'Sports', 'Music']
time_share = [30, 25, 20, 15, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
plt.figure(figsize=(8, 8))
plt.pie(time_share, labels=hobbies, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('My Hobbies - Time Share')
plt.axis('equal')
plt.show()

# TASK 4: Box plot for fruits
fruit_types = ['Apples', 'Oranges', 'Bananas', 'Strawberries']
apple_mass = np.random.normal(150, 20, 100)
orange_mass = np.random.normal(120, 15, 100)
banana_mass = np.random.normal(100, 12, 100)
strawberry_mass = np.random.normal(12, 3, 100)

data4 = [apple_mass, orange_mass, banana_mass, strawberry_mass]
plt.figure(figsize=(10, 6))
bp = plt.boxplot(data4, labels=fruit_types, patch_artist=True)
for patch, color in zip(bp['boxes'], ['lightblue', 'lightgreen', 'lightyellow', 'lightcoral']):
    patch.set_facecolor(color)
plt.ylabel('Mass (grams)')
plt.title('Mass Distribution of Different Fruits (100 fruits each)')
plt.grid(True, alpha=0.3, axis='y')
plt.show()

# TASK 5: Scatter plot with formatting
print("Task 5: Scatter plot")
x5 = np.random.uniform(0, 1, 100)
y5 = np.random.uniform(0, 1, 100)
plt.figure(figsize=(8, 8))
plt.scatter(x5, y5, color='green', alpha=0.6, s=50)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Scatter Plot: Random Points')
plt.grid(True, alpha=0.3)
plt.show()

# TASK 6: Multiple functions on one plot
print("Task 6: Multiple functions")
x6 = np.linspace(0, 2*np.pi, 200)
y6_sin = np.sin(x6)
y6_cos = np.cos(x6)
y6_sum = np.sin(x6) + np.cos(x6)

plt.figure(figsize=(12, 6))
plt.plot(x6, y6_sin, color='red', label='f(x) = sin(x)', linewidth=2)
plt.plot(x6, y6_cos, color='blue', label='g(x) = cos(x)', linewidth=2)
plt.plot(x6, y6_sum, color='green', label='h(x) = sin(x) + cos(x)', linewidth=2)

plt.xlabel('x (radians)')
plt.ylabel('y')
plt.title('Trigonometric Functions')
plt.legend(loc='best', fontsize=11)
plt.grid(True, alpha=0.3)
plt.show()