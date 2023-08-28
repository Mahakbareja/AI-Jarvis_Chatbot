import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.animation import FuncAnimation

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
sns.set(style="darkgrid")

# Initialize x and y data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create an empty line plot with dark theme colors
line, = ax.plot(x, y, lw=2, color='cyan')  # You can customize the line color

# Function to update the line data
def update(num, x, y, line):
    line.set_data(x[:num], y[:num])
    return line,

# Set up the animation
ani = FuncAnimation(fig, update, frames=len(x), fargs=(x, y, line), blit=True, repeat=False, interval=1)

# Set dark mode background and text colors
fig.patch.set_facecolor('#121212')  # Dark background color
ax.set_facecolor('#121212')         # Dark plot area background color
ax.spines['bottom'].set_color('gray')
ax.spines['top'].set_color('gray')
ax.spines['right'].set_color('gray')
ax.spines['left'].set_color('gray')
ax.xaxis.label.set_color('gray')
ax.yaxis.label.set_color('gray')
ax.title.set_color('white')

# Customize tick colors
ax.tick_params(axis='x', colors='gray')
ax.tick_params(axis='y', colors='gray')

# Add title and labels with appropriate colors
ax.set_title("Dynamic and Visually Attractive Line Chart", color='white')
ax.set_xlabel("X-Axis", color='gray')
ax.set_ylabel("Y-Axis", color='gray')

# Show the plot
plt.show()
