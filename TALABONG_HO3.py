import tkinter as tk 

window = tk.Tk()
window.title("Simple Calculator")
window.config(bg="blue")

frame = tk.Frame(window,bg="red")
frame.pack(padx=10,pady=10)

# Title
label = tk.Label(frame,text="Simple Calculator",font=("Times New Roman",12,"bold"),bg="white",width=25,height=2)
label.grid(column=0,row=0,columnspan=3)

answer = tk.Label(frame,text="",font=("Times New Roman",10),bg="white",width=35)
answer.grid(column=0,row=1,columnspan=3,pady=5)

def addition():
    value = eval(enter.get())
    value2 = eval(enter2.get())
    total = value + value2
    answer['text'] = f"The sum of {value} and {value2} is {total}"
    
def subt():
    value = eval(enter.get())
    value2 = eval(enter2.get())
    total = value - value2
    answer['text'] = f"The difference of {value} and {value2} is {total}"

def mult():
    value = eval(enter.get())
    value2 = eval(enter2.get())
    total = value * value2
    answer['text'] = f"The product of {value} and {value2} is {total}"

def divd():
    value = eval(enter.get())
    value2 = eval(enter2.get())
    total = value / value2
    answer['text'] = f"The quotient of {value} and {value2} is {total}"

firstLabel = tk.Label(frame,text="Enter 1st Number:",font=("Times New Roman",10),bg="lightgrey")
firstLabel.grid(column=0,row=2,columnspan=2,pady=5)

enter = tk.Entry(frame)
enter.grid(column=2,row=2,pady=5)

secondLabel = tk.Label(frame,text="Enter 2nd Number:",font=("Times New Roman",10),bg="lightgrey")
secondLabel.grid(column=0,row=3,columnspan=2,pady=5)

enter2 = tk.Entry(frame)
enter2.grid(column=2,row=3,pady=5)

button_Add = tk.Button(frame,text="Addition",command=addition, font=("Times New Roman",10),relief="groove",fg="black",bg="gray")
button_Add.grid(column=0,row=4,columnspan=2,pady=5)

button_Sub = tk.Button(frame,text="Subtraction",command=subt,font=("Times New Roman",10),relief="groove",fg="black",bg="gray")
button_Sub.grid(column=2,row=4,pady=5)

button_Mul = tk.Button(frame,text="Multiplication",command=mult,font=("Times New Roman",10),relief="groove",fg="black",bg="gray")
button_Mul.grid(column=0,row=5,columnspan=2,pady=5)

button_Div = tk.Button(frame,text="Division",command=divd,font=("Times New Roman",10),relief="groove",fg="black",bg="gray")
button_Div.grid(column=2,row=5,pady=5)

window.mainloop()