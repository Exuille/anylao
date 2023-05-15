import tkinter as tk
from tkinter import messagebox
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
        algeFrame.pack()
        tranFrame.pack_forget()
        quizFrame.pack_forget()
        menu_frame.place(x=-900,y=0)

def show_calculator():
        calculator_screen.pack()
        algeFrame.pack_forget()
        tranFrame.pack_forget()
        quizFrame.pack_forget()
        menu_frame.place(x=-900,y=0)

def show_quiz():
        calculator_screen.pack_forget()
        algeFrame.pack_forget()
        tranFrame.pack_forget()
        quizFrame.pack()
        menu_frame.place(x=-900,y=0)


menu_frame=tk.Frame(root,width=380,height=865,bg='#5E7CAE')
button = tk.Button(menu_frame,text='D E R I V A T I V E S', width = 42, height = 2,command= show_deriv)
button.place(x=35, y = 117)
button = tk.Button(menu_frame,text='C A L C U L A T O R', width = 42, height = 2,command= show_calculator)
button.place(x=35, y = 172)
button = tk.Button(menu_frame,text='P R A C T C E   Q U I Z', width = 42, height = 2,command= show_quiz)
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

algeFrame = tk.Frame(root,width = 450, height = 800, bg='#ebe3d3')
algeFrame.pack()
tranFrame = tk.Frame(root,width = 450, height = 800, bg='#ebe3d3')

# Functions for when the Topics are chosen
def show_alge():
    algeFrame.pack(fill="both", expand=True)
    tranFrame.pack_forget()

def show_tran():
    tranFrame.pack(fill="both", expand=True)
    algeFrame.pack_forget()
    calculator_screen.pack_forget()

 
def show_image(image_path, frame, button):
    global image_label
    # Check if the image label already exists
    if image_label is not None:
        # If it does, remove the label from the frame and delete the reference to the label
        image_label.pack_forget()
        image_label = None
    else:
        # If it doesn't, create a new image label and store a reference to it on the button object
        tk_image = ImageTk.PhotoImage(Image.open(image_path))
        image_label = tk.Label(frame, image=tk_image)
        image_label.image = tk_image
        image_label.pack()
    
image_label = None
# Algebraic Buttons
btn1 = tk.Button(algeFrame, text="Constant Rule", width=30, height=2, command=lambda: show_image("formula_png/alge_func/ConstantRule.png", algeFrame, btn1))
btn1.pack()
btn2 = tk.Button(algeFrame, text="Power Rule", width=30, height=2, command=lambda: show_image("formula_png/alge_func/PowerRule.png", algeFrame, btn2))
btn2.pack()
btn3 = tk.Button(algeFrame, text="Constant Multiple Rule", width=30, height=2, command=lambda: show_image("formula_png/alge_func/CMRule.png", algeFrame, btn3))
btn3.pack()
btn4 = tk.Button(algeFrame, text="Sum Rule", width=30, height=2, command=lambda: show_image("formula_png/alge_func/SumRule.png", algeFrame, btn4))
btn4.pack()
btn5 = tk.Button(algeFrame, text="Product Rule", width=30, height=2, command=lambda: show_image("formula_png/alge_func/ProductRule.png", algeFrame, btn5))
btn5.pack()
btn6 = tk.Button(algeFrame, text="Quotient Rule", width=30, height=2, command=lambda: show_image("formula_png/alge_func/QuotientRule.png", algeFrame, btn6))
btn6.pack()
btn7 = tk.Button(algeFrame, text="General Power Rule", width=30, height=2, command=lambda: show_image("formula_png/alge_func/GPRule.png", algeFrame, btn7))
btn7.pack()
btn8 = tk.Button(algeFrame, text="Derivative of a Composite Function", width=30, height=2, command=lambda: show_image("formula_png/alge_func/DCF.png", algeFrame, btn8))
btn8.pack()
btn9 = tk.Button(algeFrame, text="Chain Rule", width=30, height=2, command=lambda: show_image("formula_png/alge_func/ChainRule.png", algeFrame, btn9))
btn9.pack()

# Transcendental Functions Buttons
btn10 = tk.Button(tranFrame, text="Derivatives of Trigonometric Functions", width=45, height=2, command=lambda: show_image("formula_png/tran_func/DTF.png", tranFrame, btn10))
btn10.pack()
btn11 = tk.Button(tranFrame, text="Chain Rule of the Derivatives of Trigonometric Functions", width=45, height=2, command=lambda: show_image("formula_png/tran_func/CRDTF.png", tranFrame, btn11))
btn11.pack()
btn12 = tk.Button(tranFrame, text="Derivatives of Inverse Trigonometric Functions", width=45, height=2, command=lambda: show_image("formula_png/tran_func/DITF.png", tranFrame, btn12))
btn12.pack()
btn13 = tk.Button(tranFrame, text="Derivatives of Logarithmic Functions", width=45, height=2, command=lambda: show_image("formula_png/tran_func/DLF.png", tranFrame, btn13))
btn13.pack()
btn14 = tk.Button(tranFrame, text="Derivatives Exponential Functions", width=45, height=2, command=lambda: show_image("formula_png/tran_func/DEF.png", tranFrame, btn14))
btn14.pack()
btn15 = tk.Button(tranFrame, text="Chain Rule of the Derivatives of Exponential Functions", width=45, height=2, command=lambda: show_image("formula_png/tran_func/CRDEF.png", tranFrame, btn15))
btn15.pack()
btn16 = tk.Button(tranFrame, text="Derivatives of Hyperbolic Functions", width=45, height=2, command=lambda: show_image("formula_png/tran_func/DHF.png", tranFrame, btn16))
btn16.pack()
btn17 = tk.Button(tranFrame, text="Chain Rule of the Derivatives of Hyperbolic Functions ", width=45, height=2, command=lambda: show_image("formula_png/tran_func/CRDHF.png", tranFrame, btn17))
btn17.pack()

topicButton1 = tk.Button(algeFrame, text="Next", width=20, height=2, command=show_tran)
topicButton1.pack()
topicButton2 = tk.Button(tranFrame, text="Back", width=20, height=2, command=show_alge)
topicButton2.pack()

algeFrame.pack(expand=True, fill="both")
algeFrame.pack_propagate(False)
algeFrame.pack(anchor="center", side="left")

calculator_screen = tk.Frame(root)

ROW_OFFSET = 2

expression = ""


def display_equation(diff=False):
    global expression
    
    label = tk.Label(
        calculator_screen, 
        text=expression,
        font=("RobotoCondensed", 16),    
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
questions = [
    {
        "question": "If y=sin(x^3), find dy/dx.",
        "options": ["3x^2 cosx^3", "-3x^2 cosx^3", "3x^2 cosx^2", "3x^3 cosx^3"],
        "answer": "3x^2 cosx^3",
        "solution" : "sol_1.png"
    },
    {
        "question": "Compute the derivative of the function y = arcsin(2x + 1), or  y = sin-1(2x + 1).",
        "options": [" 2/√[-x(x + 2)]", "-1/√[-x(x + 1)]", "1/√[-x(x + 1)]", "1/√[-x(x + 2)]"],
        "answer": "1/√[-x(x + 1)]",
        "solution" : "sol_2.png"
    },
    {
        "question": "Find g' (t), when g (t) = - 325. ",
        "options": ["-325", "0", "325", "1"],
        "answer": "0",
        "solution" : "sol_3.png"
    },
    {
        "question": "Differentiate log e (x^2 + 3x + 1).",
        "options": ["1/((x^2 + 3x + 1)", "2x+3", "(2x+3)/(x^2+3x+1)", "1/((x^2 + 3x + 1)"],
        "answer": "(2x+3)/(x^2+3x+1)",
        "solution" : "sol_4.png"
    },
    {
        "question" : "Solve the equation: 2 cosh 2x +10sinh 2x = 5",
        "options" : ["4/3ln(1/2)", "1/2ln(4/3)", "3/4ln(1/2)", "1/2ln(3/4)"],
        "answer" : "1/2ln(4/3)",
        "solution" : "sol_5.png"
    },
    {
        "question" : "e^xcos(x)",
        "options" : ["e^xcos(x)+e^xsin(x)", "e^xcos(x)-e^xsin(x)", "e^xsin(x)-e^xcos(x)", "e^xsin(x)cos(x)"],
        "answer" : "e^xcos(x)-e^xsin(x)",
        "solution" : "sol_6.png"
    },
    {
        "question" : "sech(5x^3+x^2-2)",
        "options" : ["-sech(5x^3+x^2-2)tanh(5x^3+x^2-2)(15x^2+2x)", "-sech(5x^3+x^2-2)tanh(5x^3+x^2-2)(5x^3+x^2-2)", "sech(5x^3+x^2-2)tanh(5x^3+x^2-2)(15x^2+2x)", "sech(5x^3+x^2-2)tanh(5x^3+x^2-2)(5x^3+x^2-2)"],
        "answer" : "sech(5x^3+x^2-2)tanh(5x^3+x^2-2)(15x^2+2x)",
        "solution" : "sol_7.png"
    },
    {
        "question" : "log10(x^13)",
        "options" : ["13ln(10)x", "13/ln(10)x", "10/ln(13)x", "10ln(13)x"],
        "answer" : "13/ln(10)x",
        "solution" : "sol_8.png"
    },
    {
        "question" : "e^x^3 + x^2 -6",
        "options" : ["e^x^3-x^2+6(3x^2+3x)","e^x^3+x^2-6(3x^2+2x)","e^x^3+x^2-6(2x^3+2x)", "e^x^3+x^2-6(2x^3-2x)"],
        "answer" : "e^x^3+x^2-6(3x^2+2x)",
        "solution" : "sol_9.png"
    },
    {
        "question" : "sin^2(x)",
        "options" : ["cos(2x)", "sin(2x)", "sin(x)cos(2x)", "sin(2x)cos(2x)"],
        "answer" : "sin(2x)",
        "solution" : "sol_10.png"
    },
    {
        "question" : "Use Logarithmic Differentiation to Find the Derivative y=(2x-6)^2/(3x-2)^2",
        "options" : ["y’ = - 56(x-3)/ (3x-2)^3", "y’ = 56(x-3)/ (3x-2)^3", "y’ = 56(x-3)/ (3x-2)^4", "y’ = -56(x-3)/ (3x-2)^4"],
        "answer" : "y’ = 56(x-3)/ (3x-2)^3",
        "solution" : "sol_11.png"
    },
    {
        "question" : "Find the derivative of y= -4x^3e^2x^3",
        "options" : ["-4x^2e^2x^2(4x^2+5)", "4x^2e^2x^2(4x^2+3)", "5x^2e^2x^2(4x^2+3)", "-4x^2e^2x^2(4x^2+3)"],
        "answer" : "-4x^2e^2x^2(4x^2+3)",
        "solution" : "sol_12.png"
    },
    {
        "question" : "Find the derivative of y= -6e^3x",
        "options" : ["18e^3x", "18e", "-18e^4x", "-18e^3x"],
        "answer" : "-18e^3x",
        "solution" : "sol_13.png"
    },
    {
        "question" : "Find the derivative of y = 5^-2x^3",
        "options" : ["-6x^2(ln5)5^-2x", "6x^2(ln5)5^-2x", "-6x^2(ln5)5^", "-6x(ln5)5^-2x"],
        "answer" : "-6x^2(ln5)5^-2x",
        "solution" : "sol_14.png"
    },
    {
        "question" : "y= 3^1/x",
        "options" : ["(3ln 3)/x^2", "(3^1/xln 3)/x^2", "(3ln 2)/x^2", "(-3^1/xln 3)/x^2"],
        "answer" : "(3^1/xln 3)/x^2",
        "solution" : "sol_15.png"
    },
    {
        "question" : "Differentiate y=2 sinh x cosh x + 3 csch x",
        "options" : ["y'=3sinh^2 - 2cosh^2x + 3csch x coth x", "y'=2sinh^2 - 2cosh^2x + 3csch x coth x", "y'=2sinh^2 + 2cosh^2x - 3csch x coth x", "y'=3sinh^2 + 3cosh^2x - 2csch x coth x"],
        "answer" : "y'=2sinh^2 + 2cosh^2x - 3csch x coth x",
        "solution" : "sol_16.png"
    },
    {
        "question" : " d/dx[√cos^-1(x)]",
        "options" : ["1/cos^-1(x)√1-x^2", "-1/2√cos^-1(x)√1-x^2", "1/-sin(cos^-1(x))", "1/2√cos^-1(x)√1-x^2"],
        "answer" : "-1/2√cos^-1(x)√1-x^2",
        "solution" : "sol_17.png"
    },
    {
        "question" : "d/dx [ln(tan^-1(x))]",
        "options" : ["1/tan^-1(x)(1+x^2)", "1/tan^-1(x)", "1/2(1+x^2)", "1/x+x(ln(x))^2"],
        "answer" : "1/tan^-1(x)(1+x^2)",
        "solution" : "sol_18.png"
    },
    {
        "question" : "d/dx[xsin^1(ln(x))]",
        "options" : ["sin^-1(ln(x))", "1/√1-(ln(x))^2", "sin^-1(ln(x)) - 1/√1-(ln(x))^2", "sin^-1(ln(x)) + 1/√1-(ln(x))^2"],
        "answer" : "sin^-1(ln(x)) + 1/√1-(ln(x))^2",
        "solution" : "sol_19.png"
    }
]

question_num = 0
score = 0

def ask_question():
    global question_num
    question = questions[question_num]
    question_label.configure(text=question["question"], wraplength=435)
    option_a.configure(text="A) " + question["options"][0], state=tk.NORMAL, wraplength=300)
    option_b.configure(text="B) " + question["options"][1], state=tk.NORMAL, wraplength=300)
    option_c.configure(text="C) " + question["options"][2], state=tk.NORMAL, wraplength=300)
    option_d.configure(text="D) " + question["options"][3], state=tk.NORMAL, wraplength=300)
    show_score()
    disable_next_button()
    exit_button.pack_forget()

def enable_next_button():
    next_button.configure(state=tk.NORMAL)
    if question_num == len(questions) - 1:
        next_button.configure(text="Finish")

def disable_next_button():
    next_button.configure(state=tk.DISABLED)

def disable_choices():
    option_a.configure(state=tk.DISABLED)
    option_b.configure(state=tk.DISABLED)
    option_c.configure(state=tk.DISABLED)
    option_d.configure(state=tk.DISABLED)
    confirm_button.configure(state=tk.DISABLED)

def enable_choices():
    option_a.configure(state=tk.NORMAL)
    option_b.configure(state=tk.NORMAL)
    option_c.configure(state=tk.NORMAL)
    option_d.configure(state=tk.NORMAL)
    confirm_button.configure(state=tk.NORMAL)

def check_choice(choice):
    global selected_choice
    selected_choice = choice
    confirm_button.configure(state=tk.NORMAL)

def show_score():
    score_top_label.configure(text="Score: " + str(score) + "/" + str(len(questions)))

def check_answer():
    global score
    question = questions[question_num]
    if question["answer"] == question["options"][ord(selected_choice) - ord("A")]:
        score += 1
        result_label.configure(text="Correct!", fg="green")

    else:
        result_label.configure(text="Incorrect!", fg="red")
    
    disable_choices()
    enable_next_button()
    show_solution_button.pack()
    show_solution_button.configure(state=tk.NORMAL)

def next_question():
    global question_num
    question_num += 1
    if question_num < len(questions):
        ask_question()
    else:
        show_final_score_screen()

def show_final_score_screen():
    score_top_label.pack_forget()
    question_label.configure(text="Quiz Finished")
    option_a.pack_forget()
    option_b.pack_forget()
    option_c.pack_forget()
    option_d.pack_forget()
    confirm_button.pack_forget()
    next_button.pack_forget()
    show_solution_button.pack_forget()
    exit_button.pack
    result_label.configure(text="Your Final Score: " + str(score) + "/" + str(len(questions)), font=("RobotoCondensed", 20))
    exit_button.configure(state=tk.NORMAL)
    congratulation_label = tk.Label(quizFrame, text="Congratulations!", font=("RobotoCondensed", 24))
    congratulation_label.pack(pady=10)

def exit_quiz():
    answer = messagebox.askyesno("Exit Quiz", "Are you sure you want to exit the quiz?")
    if answer:
        root.destroy()

def show_solution():
    messagebox.showinfo("Solution", "Solution not available")

quizFrame =tk.Frame(root,width=450,height=800)
score_top_label = tk.Label(quizFrame, text="Score: 0", font=("RobotoCondensed", 14))
score_top_label.pack(pady=20)
result_label = tk.Label(quizFrame, text="", font=("RobotoCondensed", 14))
result_label.pack(pady=10)

question_label = tk.Label(quizFrame, text="", font=("RobotoCondensed", 16), pady=40)
question_label.pack()

option_a = tk.Button(quizFrame, text="", font=("RobotoCondensed", 14), width=30, command=lambda: check_choice("A"))
option_a.pack(pady=10)
option_b = tk.Button(quizFrame, text="", font=("RobotoCondensed", 14), width=30, command=lambda: check_choice("B"))
option_b.pack(pady=10)
option_c = tk.Button(quizFrame, text="", font=("RobotoCondensed", 14), width=30, command=lambda: check_choice("C"))
option_c.pack(pady=10)
option_d = tk.Button(quizFrame, text="", font=("RobotoCondensed", 14), width=30, command=lambda: check_choice("D"))
option_d.pack(pady=10)

confirm_button = tk.Button(quizFrame, text="Confirm Answer", font=("RobotoCondensed", 14), width=15, state=tk.DISABLED,command=check_answer)
confirm_button.pack(pady=10)

next_button = tk.Button(quizFrame, text="Next", font=("RobotoCondensed", 14), width=15, command=next_question, state=tk.DISABLED)
next_button.pack(pady=30)

show_solution_button = tk.Button(quizFrame, text="Show Solution", font=("RobotoCondensed", 14), width=15,state=tk.DISABLED, command=show_solution)
show_solution_button.pack(pady=10)

exit_button = tk.Button(quizFrame, text="Exit Quiz", font=("RobotoCondensed", 14), width=15, command=exit_quiz,state=tk.DISABLED)
exit_button.pack(pady=10)

ask_question()


root.mainloop()