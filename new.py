import tkinter as tk 

window = tk.Tk()
window.title("My First Window")
window.geometry("500x500")
window.resizable(True,True)
window.configure(bg="lightpink",cursor="cross")


menu_bar = tk.Menu(window)
window['menu'] = menu_bar
# add-cascade top section
file_dropdown = tk.Menu(menu_bar, tearoff=0)
file_dropdown.add_command(label="New")
file_dropdown.add_command(label="Open")
file_dropdown.add_command(label="Exit")

view_menu = tk.Menu(menu_bar,tearoff=1)
view_menu.add_command(label="Zoom")
view_menu.add_command(label="Resize")

menu_bar.add_cascade(label="File",menu=file_dropdown)


menu_bar.add_cascade(label="File",menu=view_menu)

popup=tk.Toplevel()
top_label = tk.Label(popup, text="This is the top level",fg ="white",bg="blue", activebackground="lightpink")
top_label.pack(pady=5)

popup.transient(window)
popup.grab_set()

label = tk.Label (window, text="Hello User!", bg="lightpink", font=("Poppins",25,"bold"))
label.pack(pady=5)

frame = tk.Frame(window, bg="lightpink")
frame.pack()

name_label = tk.Label (frame,text="Username:",bg="lightpink", font=("Poppins",16,"bold"))
name_label.pack()

name_entry = tk.Entry(frame)
name_entry.pack(padx=10,pady=10)

pass_label = tk.Label (frame,text="Password:",bg="lightpink", font=("Poppins",16,"bold"))
pass_label.pack()

pw_entry = tk.Entry(frame,show="*")
pw_entry.pack(padx=10,pady=10)
def show():
    name = name_entry.get()
    gender=radio_val.get()

    label ['text'] = f"Hello,{name}.Your Gender is{gender}"
    if check_val.get()== 1 :
        label2 =tk.Label(window, text="Remember Me is Clicked!")
        label2.pack()
    else:
        label2 =tk.Label(window, text="Remember Me is NOT Clicked!")
        label2.pack()


radio_val=tk.IntVar()

female = tk.Radiobutton(frame,text="Female", variable=radio_val,value=0)
female.pack()

male = tk.Radiobutton(frame,text="Male", variable=radio_val,value=1)
male.pack()

check_val=tk.IntVar()

check_btn = tk.Checkbutton(frame, text = "Remember Me", variable=check_val)
check_btn.pack()

button = tk.Button(window, text="Submit", command=show,fg ="white",bg="blue", activebackground="lightpink")
button.pack(pady=5)



listbox_lbl = tk.Label(frame,text="Chose a hoouse:")
listbox_lbl.pack()

scroll = tk.Scrollbar(frame)
scroll.pack(side="right",fill="y")

listbox =tk.Listbox(frame,selectmode="multiple", yscrollcommand=scroll.set)
listbox.insert(0, "Pythonnbvucs cnxmxlka mcv nb,ncsmdnkjsvbskPythonnbvucs cnxmxlka mcv nb,ncsmdnkjsvbsk")
listbox.insert(1, "java")
listbox.insert(2, "C#")
listbox.insert(3, "Perl")
listbox.insert(4, "Python")
listbox.insert(5, "java")
listbox.insert(6, "C#")
listbox.insert(7, "Perl")
listbox.insert(8, "Python")
listbox.insert(9, "java")
listbox.insert(10, "C#")
listbox.insert(11, "Perl")
listbox.insert(12, "Python")
listbox.insert(13, "java")
listbox.insert(14, "C#")
listbox.insert(15, "Perl")
listbox.insert(0, "Pythonnbvucs cnxmxlka mcv nb,ncsmdnkjsvbskPythonnbvucs cnxmxlka mcv nb,ncsmdnkjsvbsk")
listbox.insert(1, "java")
listbox.insert(2, "C#")
listbox.insert(3, "Perl")
listbox.insert(4, "Python")
listbox.insert(5, "java")
listbox.insert(6, "C#")
listbox.insert(7, "Perl")
listbox.insert(8, "Python")
listbox.insert(9, "java")
listbox.insert(10, "C#")
listbox.insert(11, "Perl")
listbox.insert(12, "Python")
listbox.insert(13, "java")
listbox.insert(14, "C#")
listbox.insert(15, "Perl")
listbox.pack()




window.mainloop()
