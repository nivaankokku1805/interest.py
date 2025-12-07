import tkinter as tk
from tkinter import messagebox

# Function to calculate Simple Interest
def calculate_si(principal, rate, time):
    return (principal * rate * time) / 100

# Function to calculate Compound Interest
def calculate_ci(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal

# Function to handle button click
def calculate_interest():
    try:
        # Get and validate inputs
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        if principal < 0 or rate < 0 or time < 0:
            raise ValueError("Negative values are not allowed.")

        # Calculate interests
        si = calculate_si(principal, rate, time)
        ci = calculate_ci(principal, rate, time)

        # Display results
        label_result_si.config(text=f"Simple Interest: ₹{si:.2f}")
        label_result_ci.config(text=f"Compound Interest: ₹{ci:.2f}")

    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {e}")

# Create main window
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x300")
root.resizable(False, False)

# Labels and Entry fields
tk.Label(root, text="Principal Amount (₹):").pack(pady=5)
entry_principal = tk.Entry(root)
entry_principal.pack()

tk.Label(root, text="Rate of Interest (% per annum):").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Time Period (years):").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack()

# Calculate Button
tk.Button(root, text="Calculate", command=calculate_interest, bg="lightblue").pack(pady=10)

# Result Labels
label_result_si = tk.Label(root, text="Simple Interest: ₹0.00", font=("Arial", 10, "bold"))
label_result_si.pack(pady=5)

label_result_ci = tk.Label(root, text="Compound Interest: ₹0.00", font=("Arial", 10, "bold"))
label_result_ci.pack(pady=5)

# Run the application
root.mainloop()