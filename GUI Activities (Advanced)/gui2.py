import tkinter as tk
from tkinter import messagebox

# Function to perform floor division
def act2():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        result = num1 // num2
        result_label.config(text=f"Result: {num1} // {num2} = {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")

# Create the main window
root = tk.Tk()
root.title("Activity2")

# Display the code
code_text = """def act2():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print(num1, "Floor Divide to", num2, "=", num1 // num2)
"""
tk.Label(root, text="Code Display:", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, padx=10, pady=5)
code_display = tk.Text(root, height=7, width=50, wrap="none", bg="#f0f0f0", font=("Courier", 10))
code_display.insert("1.0", code_text)
code_display.config(state="disabled")  # Make it read-only
code_display.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Input fields
tk.Label(root, text="Enter first number:").grid(row=2, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Enter second number:").grid(row=3, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=3, column=1, padx=10, pady=5)

# Button to calculate
calculate_button = tk.Button(root, text="Calculate", command=act2)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 10, "bold"))
result_label.grid(row=5, column=0, columnspan=2, pady=5)

# Run the GUI
root.mainloop()
