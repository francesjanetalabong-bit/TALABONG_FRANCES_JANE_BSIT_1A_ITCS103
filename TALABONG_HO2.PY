import tkinter as tk 

window = tk.Tk()

window.title("My Profile App")

window.geometry("600x600")

window.resizable(False,True)

window.configure(bg="light pink",cursor="arrow")

title_label = tk.Label (window,text="My Profile",font=("Times New Roman", 21, "bold"),fg="black", bg="pink", anchor = "center")
title_label.pack(pady=20)

name_label = tk.Label (window,text="Full Name: Frances Jane A. Talabong",font=("Times New Roman", 14,),fg="black", bg="pink")
name_label.pack(anchor = "w", padx= 20, pady=10)

age_label = tk.Label (window,text="Age: 18 yrs.old",font=("Times New Roman", 14,),fg="black", bg="pink")
age_label.pack(anchor = "w", padx= 20, pady=10)

course_section_label = tk.Label (window,text="Course & section: BSIT-1A",font=("Times New Roman", 14,),fg="black", bg="pink")
course_section_label.pack(anchor = "w", padx= 20, pady=10)

birthday_label = tk.Label (window,text="Birthday: August 21, 2007",font=("Times New Roman", 14,),fg="black", bg="pink")
birthday_label.pack(anchor = "w", padx= 20, pady=10)

Motto_label = tk.Label (window,text="Motto in life: Always do your best and let God do the rest",font=("Times New Roman", 14,),fg="black", bg="pink")
Motto_label.pack(anchor = "w", padx= 20, pady=10)

window.mainloop()

