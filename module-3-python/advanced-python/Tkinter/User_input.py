import tkinter as tk
import tkinter.messagebox as MSB
#function for user input
def input_user():
    user_input = entry.get()
    # print("User input is: ", user_input)
    # return MSB.showinfo("User Input", f"User input is: {user_input}")
    label1 = tk.Label(root, text=f"Hello, {user_input} ", font=("Arial", 19), fg="blue")
    label1.pack(pady=25)

root = tk.Tk()

root.title("User Input")

root.geometry("300x500")
label = tk.Label(root, text="Enter your name", font=("Arial", 19), fg="blue")


# create input field
entry = tk.Entry(root, font=("Arial",17))

label.pack(pady=25)
entry.pack(pady=25)

#create a Button 



button = tk.Button(root, text="submit",font=("Arial", 17), command=input_user)
button.pack(pady=25)




root.mainloop()