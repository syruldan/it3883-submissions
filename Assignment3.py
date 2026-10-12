
# Program Name: Assignment3.py
# Course: IT3883/Section W01
# Student Name: Arvin Van
# Assignment Number: Lab3
# Due Date: 10/10/2026
# Purpose: This program converts Miles per Gallon (MPG) into
# Kilometers per Liter (km/L). The result updates automatically
# whenever the user types a new value. The program also handles
# blank inputs and invalid characters without crashing.
# Resources Used: Python documentation, Tkinter documentation,
# and the assignment instructions.

import tkinter as tk

# Conversion rate from miles per gallon to kilometers per liter
CONVERSION_RATE = 0.425143707


# This function updates the conversion result as the user types
def convert_mpg(*args):
    # Get the value entered in the MPG input box
    mpg_text = mpg_var.get().strip()

    # Handle an empty input box
    if mpg_text == "":
        result_var.set("")
        return

    # Try to convert the input into a number
    try:
        mpg = float(mpg_text)

        # Calculate kilometers per liter
        km_per_liter = mpg * CONVERSION_RATE

        # Display the result with six decimal places
        result_var.set(f"{km_per_liter:.6f}")

    # Handle letters or other invalid input without crashing
    except ValueError:
        result_var.set("Enter a valid number")


# Create the main application window
root = tk.Tk()
root.title("MPG to KM/L Converter")
root.geometry("400x250")
root.resizable(False, False)

# Create variables to track input and output values
mpg_var = tk.StringVar()
result_var = tk.StringVar()

# Automatically call the conversion function whenever input changes
mpg_var.trace_add("write", convert_mpg)

# Add the application heading
title_label = tk.Label(
    root,
    text="MPG to KM/L Converter",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=15)

# Add the MPG input label
mpg_label = tk.Label(
    root,
    text="Miles per Gallon (MPG):",
    font=("Arial", 11)
)
mpg_label.pack()

# Create the input field for MPG
mpg_entry = tk.Entry(
    root,
    textvariable=mpg_var,
    font=("Arial", 12),
    justify="center",
    width=25
)
mpg_entry.pack(pady=5)

# Add the converted result label
result_label = tk.Label(
    root,
    text="Kilometers per Liter (KM/L):",
    font=("Arial", 11)
)
result_label.pack(pady=(10, 0))

# Display the conversion result
result_entry = tk.Entry(
    root,
    textvariable=result_var,
    font=("Arial", 12),
    justify="center",
    width=25,
    state="readonly"
)
result_entry.pack(pady=5)

# Display the conversion formula
formula_label = tk.Label(
    root,
    text="1 MPG = 0.425143707 KM/L",
    font=("Arial", 9)
)
formula_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
