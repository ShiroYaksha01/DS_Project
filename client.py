from tkinter import *
import xmlrpc.client

# Connect to RPC server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

equation_text = ""

def button_press(value):
    global equation_text
    equation_text += str(value)
    equation_var.set(equation_text)

def equals():
    global equation_text

    try:
        # Detect operator used
        if "+" in equation_text:
            a, b = equation_text.split("+")
            result = proxy.add(float(a), float(b))

        elif "-" in equation_text:
            a, b = equation_text.split("-")
            result = proxy.subtract(float(a), float(b))

        elif "*" in equation_text:
            a, b = equation_text.split("*")
            result = proxy.multiply(float(a), float(b))

        elif "/" in equation_text:
            a, b = equation_text.split("/")
            result = proxy.divide(float(a), float(b))

        else:
            equation_var.set("Invalid")
            equation_text = ""
            return
        
        equation_var.set(str(result))
        equation_text = str(result)

    except Exception:
        equation_var.set("Error")
        equation_text = ""

def clear_screen():
    global equation_text
    equation_text = ""
    equation_var.set("")


# UI Setup
window = Tk()
window.title("RPC Calculator")
window.geometry("580x415")

equation_var = StringVar()

display = Label(window, textvariable=equation_var, font=('Times New Roman',20), bg="white", width=38, height=2) 
display.pack()

frame = Frame(window)
frame.pack()

# Number Buttons 0–9
buttons = [
    (7,0,0), (8,0,1), (9,0,2),
    (4,1,0), (5,1,1), (6,1,2),
    (1,2,0), (2,2,1), (3,2,2),
    (0,2,3)
]

for (num, r, c) in buttons:
    if num == 0:
        Button(frame, text=str(num), font=35, height=4, width=15,
               command=lambda n=num: button_press(n)).grid(row=r, column=c)
    else:
        Button(frame, text=str(num), font=35, height=4, width=9,
               command=lambda n=num: button_press(n)).grid(row=r, column=c)

# Operation Buttons
ops = [
    ("+", 0, 3),
    ("-", 1, 3),
    ("*", 0, 4),
    ("/", 1, 4),
]

for (op, r, c) in ops:
    Button(frame, text=op, font=35, height=4, width=15,
           command=lambda o=op: button_press(o)).grid(row=r, column=c)

# Equals Button
Button(frame, text="Enter", font=35, height=4, width=15,
       command=equals).grid(row=2, column=4)

# Clear Button
Button(window, text="Clear", font=35, height=4, width=61,
       command=clear_screen).pack()

window.mainloop()
