import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt  # Import plt for creating circles
import numpy as np

def plot_vector():
    # Get the length from the entry field
    try:
        length = float(length_entry.get())
    except ValueError:
        length = 5  # Default to 5 if invalid input

    # Define the two points A and B
    A = np.array([1, 1])
    B = np.array([1, 3])

    # Step 1: Create the vector AB
    vector_AB = B - A

    # Step 2: Find the magnitude of vector AB
    magnitude_AB = np.linalg.norm(vector_AB)

    # Step 3: Normalize the vector
    normalized_vector = vector_AB / magnitude_AB

    # Step 4: Scale the normalized vector to the specified length
    scaled_vector = normalized_vector * length

    # Calculate the endpoint of the scaled vector starting from A
    endpoint = A + scaled_vector
    jakpos = B
    # Create a matplotlib figure
    fig = Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)

    # Plot points and vectors
    ax.plot([A[0], B[0]], [A[1], B[1]], 'bo', label='Points A and B')  # Points
    ax.quiver(A[0], A[1], vector_AB[0], vector_AB[1], angles='xy', scale_units='xy', scale=1, color='g', label='Vector AB')  # Original vector AB
    ax.quiver(A[0], A[1], scaled_vector[0], scaled_vector[1], angles='xy', scale_units='xy', scale=1, color='r', label=f'Vector AB (length {length})')  # Scaled vector

    # Draw a circle with a radius of 5 around point A
    circle = plt.Circle(A, 5, color='b', fill=False, linestyle='--', linewidth=1.5, label='Radius 5 Circle')
    ax.add_patch(circle)

    # Annotate the endpoint of the scaled vector
    ax.plot(endpoint[0], endpoint[1], 'ro')  # Mark the endpoint
    ax.text(endpoint[0], endpoint[1], f"({endpoint[0]:.2f}, {endpoint[1]:.2f})", color='red', fontsize=10, ha='right')
    ax.plot(B[0], B[1], 'ro')  # Mark the endpoint
    ax.text(B[0], B[1], f"({B[0]:.2f}, {B[1]:.2f})", color='red', fontsize=10, ha='right')

    # Additional plot settings
    ax.set_xlim(-5, 10)
    ax.set_ylim(-5, 10)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    ax.legend()
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title(f"Vector from Point A to B and Normalized to Length {length}")

    # Display the plot in tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Set up the tkinter window
root = tk.Tk()
root.title("Vector Plot with Radius")
root.geometry("600x650")

# Create input field and label for vector length
length_label = ttk.Label(root, text="Enter vector length:")
length_label.pack()
length_entry = ttk.Entry(root)
length_entry.insert(0, "5")  # Default value of 5
length_entry.pack()

# Create a button to plot the vector and circle
plot_button = ttk.Button(root, text="Plot Vector with Circle", command=plot_vector)
plot_button.pack()

# Start the tkinter main loop
root.mainloop()
