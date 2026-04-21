# Create a calculator using Tkinter

import tkinter as tk

# Create a main window
root = tk.Tk()
# Create a windows title
root.title("Advanced Calculator")
# Create a windows size
root.geometry("400x750")
# Create a label widget
label = tk.Label(root, text="Advanced Calculator", font=("Arial", 19), fg="blue")
# Set a position with border and content and provdide padding from all side
label.pack(pady=25)

label1 = tk.Label(root, text="Enter first number", font=("Arial", 12), fg="blue")
label1.pack(pady=10)

# Create a entry widget
entry1 = tk.Entry(root, font=("Arial", 17))
entry1.pack(pady=10)

label2 = tk.Label(root, text="Enter second number", font=("Arial", 12), fg="blue")
label2.pack(pady=10)

entry2 = tk.Entry(root, font=("Arial", 17)) 
entry2.pack(pady=10)

# Create a label for operation selection
label3 = tk.Label(root, text="Select Operation", font=("Arial", 12), fg="blue")
label3.pack(pady=15)

# Variable to store the selected operation
operation = tk.StringVar(value="add")

# Create radio buttons for operation selection
addition_radio = tk.Radiobutton(root, text="Addition (+)", variable=operation, value="add", font=("Arial", 11))
addition_radio.pack(pady=5)

subtraction_radio = tk.Radiobutton(root, text="Subtraction (-)", variable=operation, value="subtract", font=("Arial", 11))
subtraction_radio.pack(pady=5)

multiplication_radio = tk.Radiobutton(root, text="Multiplication (*)", variable=operation, value="multiply", font=("Arial", 11))
multiplication_radio.pack(pady=5)

division_radio = tk.Radiobutton(root, text="Division (/)", variable=operation, value="divide", font=("Arial", 11))
division_radio.pack(pady=5)

# Create a button widget
button = tk.Button(root, text="Calculate", font=("Arial", 17), command=lambda: calculate(), bg="green", fg="white")
button.pack(pady=25)

# Create a label widget to display the result
result_label = tk.Label(root, text="", font=("Arial", 14), fg="red")
result_label.pack(pady=20)

# Create a function to calculate the result
def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        selected_operation = operation.get()
        
        if selected_operation == "add":
            result = a + b
            operation_symbol = "+"
        elif selected_operation == "subtract":
            result = a - b
            operation_symbol = "-"
        elif selected_operation == "multiply":
            result = a * b
            operation_symbol = "*"
        elif selected_operation == "divide":
            if b == 0:
                result_label.config(text="Error: Cannot divide by zero!", fg="red")
                return
            result = a / b
            operation_symbol = "/"
        
        result_label.config(text=f"{a} {operation_symbol} {b} = {result:.2f}", fg="green")
    
    except ValueError:
        result_label.config(text="Error: Please enter valid numbers!", fg="red")

# Print a Window
root.mainloop()
