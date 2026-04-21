import tkinter as tk

# Create a main window 
root = tk.Tk()

# Crete a windows title

root.title("Simple Windows Desktop App")

# Crete a windows size

root.geometry("350x300")

# Create a label widget

label = tk.Label(root, text="Hello I am Brijesh", font=("Arial", 19), fg="blue")


#Set a position with border and content and provdide padding from all side

label.pack(pady=25)



# print a Window 

root.mainloop()

