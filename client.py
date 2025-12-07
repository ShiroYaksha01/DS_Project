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

# ================= UI SETUP =================
window = Tk()
window.title("RPC Calculator")
window.geometry("420x600")
window.configure(bg="#2c2c2c")

equation_var = StringVar()

# Display
display = Label(
    window,
    textvariable=equation_var,
    font=("Segoe UI", 24),
    bg="#1e1e1e",
    fg="white",
    anchor="e",
    height=2
)
display.pack(fill="x")

# Buttons frame (Rectangle area)
frame = Frame(window, bg="#2c2c2c")
frame.pack(expand=True, fill="both", padx=10, pady=10)

btn_font = ("Segoe UI", 16)

# Configure grid to expand evenly
for i in range(5):  # columns
    frame.columnconfigure(i, weight=1)
for i in range(4):  # rows
    frame.rowconfigure(i, weight=1)

def make_button(text, row, col, color, cmd, colspan=1, rowspan=1, fg="white"):
    Button(
        frame,
        text=text,
        bg=color,
        fg=fg,
        font=btn_font,
        bd=0,
        command=cmd
    ).grid(
        row=row, column=col,
        columnspan=colspan, rowspan=rowspan,
        sticky="nsew", padx=5, pady=5
    )

# Numbers
make_button("7", 0, 0, "#dcdcdc", lambda: button_press("7"), fg="black")
make_button("8", 0, 1, "#dcdcdc", lambda: button_press("8"), fg="black")
make_button("9", 0, 2, "#dcdcdc", lambda: button_press("9"), fg="black")

make_button("4", 1, 0, "#dcdcdc", lambda: button_press("4"), fg="black")
make_button("5", 1, 1, "#dcdcdc", lambda: button_press("5"), fg="black")
make_button("6", 1, 2, "#dcdcdc", lambda: button_press("6"), fg="black")

make_button("1", 2, 0, "#dcdcdc", lambda: button_press("1"), fg="black")
make_button("2", 2, 1, "#dcdcdc", lambda: button_press("2"), fg="black")
make_button("3", 2, 2, "#dcdcdc", lambda: button_press("3"), fg="black")

# 0 spans three columns
make_button("0", 3, 0, "#dcdcdc", lambda: button_press("0"), colspan=3, fg="black")

# Operators
make_button("+", 0, 3, "#f39c12", lambda: button_press("+"))
make_button("-", 1, 3, "#f39c12", lambda: button_press("-"))
make_button("*", 2, 3, "#f39c12", lambda: button_press("*"))
make_button("/", 3, 3, "#f39c12", lambda: button_press("/"))

# Equal button (full height)
make_button("=", 0, 4, "#27ae60", equals, rowspan=4)

# Clear button
Button(
    window,
    text="Clear",
    bg="#c0392b",
    fg="white",
    font=("Segoe UI", 14),
    height=2,
    bd=0,
    command=clear_screen
).pack(fill="x", padx=10, pady=10)

window.mainloop()
