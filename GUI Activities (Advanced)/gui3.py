import tkinter as tk
from tkinter import messagebox

def act18():
    try:
        # Get the number of triangles from the user
        triangles = int(entry.get())
        output = ""
        
        for x in range(1, 8):
            for y in range(triangles):
                for a in range(1, x + 1):
                    output += "* "
                for b in range(7, x, -1):
                    output += "  "
                output += "  "
            output += "\n"

        # Display the result in the output box
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, output)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create the main GUI window
root = tk.Tk()
root.title("Triangle Pattern Generator")
root.geometry("600x400")

# Create a label and entry for user input
label = tk.Label(root, text="Enter number of triangles:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

# Create a button to generate the pattern
generate_button = tk.Button(root, text="Generate Pattern", font=("Arial", 12), command=act18)
generate_button.pack(pady=10)

# Create a frame to hold the text box and scrollbar
frame = tk.Frame(root)
frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Create a text box to display the output
output_box = tk.Text(frame, wrap="none", font=("Courier", 12), height=15)
output_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a horizontal scrollbar
x_scrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL, command=output_box.xview)
x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Configure the text box to work with the scrollbar
output_box.configure(xscrollcommand=x_scrollbar.set)

# Run the GUI event loop
root.mainloop()
