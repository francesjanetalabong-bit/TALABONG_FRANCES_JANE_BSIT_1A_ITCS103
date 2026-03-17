import tkinter as tk

window = tk.Tk()
window.title(" PROFILE BUILDER")
window.config(bg = "lightpink")
label = tk.Label(window, text = "Profile Builder", font = ("Times New Roman", 12, "bold"), bg ="light pink")
label.pack()
frame = tk.Frame(window, bg= "yellow")
frame.pack(padx = 10, pady = 10)
first_name = tk.Entry(frame)
first_name.grid(column = 0, row = 0, columnspan=2, padx=5, pady = 5)
middle_name = tk. Entry(frame)
middle_name.grid(column = 2, row = 0, columnspan=2, padx=5, pady = 5)
last_name = tk. Entry(frame)
last_name.grid(column = 4, row = 0, columnspan=2, padx=5, pady = 5)
first_name_label = tk.Label(frame, text = "First Name", bg= "yellow")
first_name_label.grid(column=0, row=1, columnspan=2 )
middle_name_label = tk.Label(frame, text = "Middle Name", bg = "yellow")
middle_name_label.grid(column=2, row = 1, columnspan = 2)
last_name_label = tk.Label(frame, text ="Last Name", bg = "yellow")
last_name_label.grid(column=4, row = 1, columnspan = 2)
birth = tk.Entry(frame)
birth.grid(column = 0, row = 2, columnspan=2, padx=5, pady = 5)
display_label= tk.Label(frame,text = "text information", bg="yellow")
display_label.grid(column = 2, row = 4, columnspan=4, padx=5, pady = 5)
birthday_label = tk.Label(frame, text="Birthday", bg = "yellow")
birthday_label.grid(column = 0, row = 4)
gender_label = tk.Label(frame, text="Gender", bg = "yellow")
gender_label.grid(column = 0, row = 5)

varr = tk.IntVar()
male = tk.Radiobutton(frame, text="Male", value= 0, variable=varr)
male.grid(column=2, row = 5, pady=5)
female = tk.Radiobutton(frame, text="Female", value= 1, variable=varr)
female.grid(column=3, row = 5, pady=5)




def hello ():
    now = tk.IntVAr()
    top_level = tk. Toplevel(window)
    stid = tk.Label( top_level,text = "Student Identification")
    stid.pack
    top_level_frame = tk.Frame(top_level, bg="purple")
    top_level_frame.pack
    name = tk.Label(top_level_frame, text = "Name: ")
    name.grid(column=0, row=0)
    name1 = tk.Label(top_level_frame, text = "Name: ")
    name1.grid(column=1, row=0, )
    









window.mainloop()
