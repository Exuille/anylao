import tkinter as tk
from PIL import ImageTk,Image
import math
import matplotlib.pyplot as plt
import sympy as sp

splash_root = tk.Tk()
splash_root.geometry('500x500')
splash_root.overrideredirect(True)

applogo =ImageTk.PhotoImage(Image.open("appLogo.png"))
splash_logo = tk.Label(splash_root, image=applogo )
splash_logo.pack()

def destroy_splash():
    splash_root.destroy()

splash_root.after(3000, destroy_splash)

splash_root.mainloop()

root = tk.Tk()
root.title("diffCALC")
root.geometry('450x865')

navIcon =ImageTk.PhotoImage(Image.open("navIcon.png"))
closeIcon = ImageTk.PhotoImage(Image.open("closeIcon.png"))
logo = ImageTk.PhotoImage(Image.open("logo.png"))

def dele():
        menu_frame.place(x=-900,y=0)

def toggle():   
        menu_frame.tkraise()
        menu_frame.place(x=0,y=0)

def show_deriv():
        calculator_screen.pack_forget()
        deriv_frame.pack()
        menu_frame.place(x=-900,y=0)

def show_calculator():
        calculator_screen.pack()
        deriv_frame.pack_forget()
        menu_frame.place(x=-900,y=0)


menu_frame=tk.Frame(root,width=380,height=865,bg='#5E7CAE')
button = tk.Button(menu_frame,text='D E R I V A T I V E S', width = 42, height = 2,command= show_deriv)
button.place(x=35, y = 117)
button = tk.Button(menu_frame,text='C A L C U L A T O R', width = 42, height = 2,command= show_calculator)
button.place(x=35, y = 172)
button = tk.Button(menu_frame,text='P R A C T C E   Q U I Z', width = 42, height = 2)
button.place(x=35, y = 227)
button = tk.Button(menu_frame,text='A B O U T', width = 42, height = 2)
button.place(x=35, y = 282)
closeBtn = tk.Button(menu_frame, bg='#5E7CAE', activebackground='#5E7CAE',image=closeIcon,command=dele)
closeBtn.place(x=10, y=18)


navbar = tk.Frame(root, width = 450, height = 65, bg = '#5E7CAE')
navbar.pack()
navLabel = tk.Label(navbar, text="diffCALC", font="RobotoCondensed",bg='#5E7CAE', fg ="white")
navLabel.place(x = 165, y = 18)
navLogo = tk.Label(navbar,bg='#5E7CAE', image= logo)
navLogo.place(x = 400, y= 18)
navbarBtn = tk.Button(navbar, bg='#5E7CAE', activebackground='#5E7CAE',image=navIcon, command=toggle)
navbarBtn.place(x=10, y=18)

deriv_frame = tk.Frame(root, width = 450, height = 865)
deriv_frame.pack()
button = tk.Button(deriv_frame,text='D E R I V A T I V E S', width = 42, height = 2)
button.place(x=35, y = 117)
button = tk.Button(deriv_frame,text='C A L C U L A T O R', width = 42, height = 2)
button.place(x=35, y = 172)
button = tk.Button(deriv_frame,text='P R A C T C E   Q U I Z', width = 42, height = 2)
button.place(x=35, y = 227)
button = tk.Button(deriv_frame,text='A B O U T', width = 42, height = 2)
button.place(x=35, y = 282)

calculator_screen = tk.Frame(root)

ROW_OFFSET = 2

expression = ""


def display_equation(diff=False):
    global expression
    
    label = tk.Label(
        calculator_screen, 
        text=expression,
        font=("Arial", 16),    
    )
    label.grid(row=0, column=0, columnspan=5, pady=12, sticky="nsew")

    try:
        if diff:
            x = sp.Symbol('x')
            fx = sp.sympify(expression)
            dx = sp.diff(fx, x)
            expression = str(dx)

        # Create a SymPy expression
        expr = sp.sympify(expression if expression != "" else 0)

        # Convert the expression to a LaTeX string
        eq_latex = sp.latex(expr)

        fig, ax = plt.subplots()
        fig.set_size_inches(4, 1.5)
        ax.text(0.5, 0.5, f"${eq_latex}$", fontsize=20, ha='center', va='center')
        ax.axis('off')
        plt.savefig('equation.png')
        img = tk.PhotoImage(file='equation.png')
        render = tk.Label(calculator_screen, image=img)
        render.image = img
        render.grid(row=1, column=0, columnspan=5, pady=8, sticky="nsew")
    except:
        return


def process_symbol(symbol):
    global expression

    ops = ["+", "-", "*", "/", "^", "(", ")"]

    funcs = [
        "sin",
        "cos",
        "tan",
        "csc",
        "sec",
        "cot",
        "sinh",
        "cosh",
        "tanh",
        "asin",
        "acos",
        "atan",
        "acsc",
        "asec",
        "acot",
        "asinh",
        "acosh",
        "atanh",
        "ln",
        "log",
    ]

    vars = ["x", "y", "z"]

    diff = False

    if symbol.isnumeric() or symbol in ops:
        expression += symbol

    elif symbol in vars:
        expression += symbol

    elif symbol == "DEL":
        expression = expression[:-1]

    elif symbol == "AC":
        expression = ""

    elif symbol in funcs:
        expression += f"{symbol}("

    elif symbol == "e":
        expression += "e"

    elif symbol == "π":
        expression += "pi"

    elif symbol == "INV":
        buttons = [
            ["x", "y", "z", "REG", "OFF"],
            ["asinh", "acosh", "atanh", "e", "π"],
            ["acsc", "asec", "acot", "ln", "log"],
            ["asin", "acos", "atan", "(", ")"],
            ["7", "8", "9", "DEL", "AC"],
            ["4", "5", "6", "*", "/"],
            ["1", "2", "3", "+", "-"],
            ["0", ".", "d/dx", "^", "="],
        ]
        create_buttons(buttons)

    elif symbol == "REG":
        buttons = [
            ["x", "y", "z", "INV", "OFF"],
            ["sinh", "cosh", "tanh", "e", "π"],
            ["csc", "sec", "cot", "ln", "log"],
            ["sin", "cos", "tan", "(", ")"],
            ["7", "8", "9", "DEL", "AC"],
            ["4", "5", "6", "*", "/"],
            ["1", "2", "3", "+", "-"],
            ["0", ".", "d/dx", "^", "="],
        ]
        create_buttons(buttons)

    elif symbol == "d/dx":
        diff = True

    display_equation(diff)


def create_button(label, row, col, row_span=1, col_span=1):
    button = tk.Button(
        master=calculator_screen,
        padx=16,
        pady=16,
        font=("Arial", 14),
        text=label,
        command=lambda sym=label: process_symbol(sym),
    )

    button.grid(
        row=row,
        column=col,
        rowspan=row_span,
        columnspan=col_span,
        sticky="nsew"
    )

    return button


def create_numkeys():    
    for i in range(10):
        row = math.ceil(i / 3)
        col = (i - 1) % 3 if i != 0 else 0
        create_button(f"{i}", row, col)


buttons = [
    ["x", "y", "z", "INV", "OFF"],
    ["sinh", "cosh", "tanh", "e", "π"],
    ["csc", "sec", "cot", "ln", "log"],
    ["sin", "cos", "tan", "(", ")"],
    ["7", "8", "9", "DEL", "AC"],
    ["4", "5", "6", "*", "/"],
    ["1", "2", "3", "+", "-"],
    ["0", ".", "d/dx", "^", "="],
]

def create_buttons(buttons):
    for i, row in enumerate(buttons):
        for j, label in enumerate(row):
            create_button(label, i + ROW_OFFSET, j)



create_buttons(buttons)
display_equation()

calculator_screen.pack()
root.mainloop()