import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 100)
line, = ax.plot(x, np.sin(x))

# Function to update the plot in each frame of the animation
def update(frame):
    line.set_ydata(np.sin(x + frame * 0.1))  # Vary the phase for animation
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50)
plt.show()

