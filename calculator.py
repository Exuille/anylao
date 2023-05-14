import tkinter as tk

import math
import matplotlib.pyplot as plt
import sympy as sp

# Create the main window
root = tk.Tk()
root.geometry("480x800")
root.title("Calculator")

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

