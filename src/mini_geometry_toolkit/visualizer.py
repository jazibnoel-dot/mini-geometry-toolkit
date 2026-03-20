import matplotlib.pyplot as plt
import numpy as np

# 🔵 Circle Plot
def plot_circle(radius):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    plt.figure()
    plt.plot(x, y, color='blue')
    plt.fill(x, y, alpha=0.2)  # optional fill
    plt.title(f"Circle (r={radius})")
    plt.axis('equal')
    plt.show()


# 🟩 Square Plot
def plot_square(side):
    # Square corners
    x = [0, side, side, 0, 0]
    y = [0, 0, side, side, 0]

    plt.figure()
    plt.plot(x, y, color='green')
    plt.fill(x, y, alpha=0.2)
    plt.title(f"Square (side={side})")
    plt.axis('equal')
    plt.show()


# ▭ Rectangle Plot
def plot_rectangle(length, width):
    # Rectangle corners
    x = [0, length, length, 0, 0]
    y = [0, 0, width, width, 0]

    plt.figure()
    plt.plot(x, y, color='red')
    plt.fill(x, y, alpha=0.2)
    plt.title(f"Rectangle (L={length}, W={width})")
    plt.axis('equal')
    plt.show()