import tkinter as tk  

window = tk.Tk()

# welcome_label = tk.Label(window, text="Welcome")
# welcome_label.grid(column=0, row=0)

# label = tk.Label(window, text="User Form")
# label.grid(column=1,row=0, columnspan=3)

# user_label = tk.Label(window, text = "User:")
# user_label.grid(column=1, row=1)

# user_entry_label = tk.Entry(window)
# user_entry_label.grid(column=2, row=1, columnspan=2)

# password_label = tk.Label(window, text="Password")
# password_label.grid(column=1, row=2)

# password_entry = tk.Entry(window)
# password_entry.grid(column = 2, row= 2, columnspan=2)

# button = tk.Button(window, text="Log In")
# button.grid(column=2, row=3)

# header
label = tk.Label(window, text="User Form")
label.place(x = 20, y = 7)
# usernme 
user_label = tk.Label(window, text = "User:") 
user_label.place(x = 10, y = 12)

user_entry_label = tk.Entry(window)
user_entry_label.place(x = 40, y = 12)

password_label = tk.Label(window, text="Pass:")
password_label.place(x = 10 , y = 30)

password_entry = tk.Entry(window)
password_entry.place(x = 40, y = 32 )

button = tk.Button(window, text="Log In")
button.place( x = 75, y = 55)


window.mainloop()











3


























# u_label.grid(column=0,row=0, columnspan=3)
# u_name.grid(column=0, row=1)
# u_entry.grid(column=1, row=1, column =2)
# pwrd.grid(column = 0, row= 2, columnspan=2)
# pwrd_entry.grid(column = 1, row = 3)
# button.grid(column=2, rpw=3)