import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
import math
import matplotlib.pyplot as plt
import sympy as sp

#Slash Screen Window
splash_root = tk.Tk()
screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()
x = (screen_width - 500) // 2 
y = (screen_height - 500) // 2
splash_root.geometry(f"500x500+{x}+{y}")
splash_root.overrideredirect(True)

splashLogo =ImageTk.PhotoImage(Image.open("splashLogo.png"))

splash_logo = tk.Label(splash_root, image=splashLogo)
splash_logo.pack()

def destroy_splash():
    splash_root.destroy()

splash_root.after(3000, destroy_splash)

splash_root.mainloop()

#Main Window
root = tk.Tk()
root.title("diffCALC")
x = (screen_width - 450) // 2 
y = (screen_height - 865) // 2
root.geometry(f"450x865+{x}+{y}")

navIcon =ImageTk.PhotoImage(Image.open("navIcon.png"))
closeIcon = ImageTk.PhotoImage(Image.open("closeIcon.png"))
logo = ImageTk.PhotoImage(Image.open("navLogo.png"))

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

#Menu Frame 
menu_frame=tk.Frame(root,width=400,height=865,bg='#5E7CAE')
button = tk.Button(menu_frame,text='D E R I V A T I V E S', width = 42, height = 2,command= show_deriv)
button.place(x=45, y = 117)
button = tk.Button(menu_frame,text='C A L C U L A T O R', width = 42, height = 2,command= show_calculator)
button.place(x=45, y = 172)
button = tk.Button(menu_frame,text='P R A C T C E   Q U I Z', width = 42, height = 2,command= show_quiz)
button.place(x=45, y = 227)
button = tk.Button(menu_frame,text='A B O U T', width = 42, height = 2)
button.place(x=45, y = 282)
closeBtn = tk.Button(menu_frame, bg='#5E7CAE', activebackground='#5E7CAE',image=closeIcon,command=dele)
closeBtn.place(x=10, y=18)

#Navigation Bar Frame
navbar = tk.Frame(root, width = 450, height = 65, bg = '#5E7CAE')
navbar.pack()
navLabel = tk.Label(navbar, text="diffCALC", font="RobotoCondensed",bg='#5E7CAE', fg ="white")
navLabel.place(x = 183, y = 20)
navLogo = tk.Label(navbar,bg='#5E7CAE', image= logo)
navLogo.place(x = 400, y= 18)
navbarBtn = tk.Button(navbar, bg='#5E7CAE', activebackground='#5E7CAE',image=navIcon, command=toggle)
navbarBtn.place(x=10, y=18)

#Algebraic and Transcental Frame
algeFrame = tk.Frame(root,width = 450, height = 800, bg='white')
algeFrame.pack()
tranFrame = tk.Frame(root,width = 450, height = 800, bg='white')


# Algebraic Buttons
btn1 = tk.Button(algeFrame, text="Constant Rule", width=30, height=2, command=lambda: show_image("formula_png/alge_func/ConstantRule.png", algeFrame, btn1))
btn1.pack(pady=7)
btn2 = tk.Button(algeFrame, text="Power Rule", width=30, height=2, command=lambda: show_image("formula_png/alge_func/PowerRule.png", algeFrame, btn2))
btn2.pack(pady=7)
btn3 = tk.Button(algeFrame, text="Constant Multiple Rule", width=30, height=2, command=lambda: show_image("formula_png/alge_func/CMRule.png", algeFrame, btn3))
btn3.pack(pady=7)
btn4 = tk.Button(algeFrame, text="Sum Rule", width=30, height=2, command=lambda: show_image("formula_png/alge_func/SumRule.png", algeFrame, btn4))
btn4.pack(pady=7)
btn5 = tk.Button(algeFrame, text="Product Rule", width=30, height=2, command=lambda: show_image("formula_png/alge_func/ProductRule.png", algeFrame, btn5))
btn5.pack(pady=7)
btn6 = tk.Button(algeFrame, text="Quotient Rule", width=30, height=2, command=lambda: show_image("formula_png/alge_func/QuotientRule.png", algeFrame, btn6))
btn6.pack(pady=7)
btn7 = tk.Button(algeFrame, text="General Power Rule", width=30, height=2, command=lambda: show_image("formula_png/alge_func/GPRule.png", algeFrame, btn7))
btn7.pack(pady=7)
btn8 = tk.Button(algeFrame, text="Derivative of a Composite Function", width=30, height=2, command=lambda: show_image("formula_png/alge_func/DCF.png", algeFrame, btn8))
btn8.pack(pady=7)
btn9 = tk.Button(algeFrame, text="Chain Rule", width=30, height=2, command=lambda: show_image("formula_png/alge_func/ChainRule.png", algeFrame, btn9))
btn9.pack(pady=7)

# Transcendental Functions Buttons
btn10 = tk.Button(tranFrame, text="Derivatives of Trigonometric Functions", width=45, height=2, command=lambda: show_image("formula_png/tran_func/DTF.png", tranFrame, btn10))
btn10.pack(pady=7)
btn11 = tk.Button(tranFrame, text="Chain Rule of the Derivatives of Trigonometric Functions", width=45, height=2, command=lambda: show_image("formula_png/tran_func/CRDTF.png", tranFrame, btn11))
btn11.pack(pady=7)
btn12 = tk.Button(tranFrame, text="Derivatives of Inverse Trigonometric Functions", width=45, height=2, command=lambda: show_image("formula_png/tran_func/DITF.png", tranFrame, btn12))
btn12.pack(pady=7)
btn13 = tk.Button(tranFrame, text="Derivatives of Logarithmic Functions", width=45, height=2, command=lambda: show_image("formula_png/tran_func/DLF.png", tranFrame, btn13))
btn13.pack(pady=7)
btn14 = tk.Button(tranFrame, text="Derivatives Exponential Functions", width=45, height=2, command=lambda: show_image("formula_png/tran_func/DEF.png", tranFrame, btn14))
btn14.pack(pady=7)
btn15 = tk.Button(tranFrame, text="Chain Rule of the Derivatives of Exponential Functions", width=45, height=2, command=lambda: show_image("formula_png/tran_func/CRDEF.png", tranFrame, btn15))
btn15.pack(pady=7)
btn16 = tk.Button(tranFrame, text="Derivatives of Hyperbolic Functions", width=45, height=2, command=lambda: show_image("formula_png/tran_func/DHF.png", tranFrame, btn16))
btn16.pack(pady=7)
btn17 = tk.Button(tranFrame, text="Chain Rule of the Derivatives of Hyperbolic Functions ", width=45, height=2, command=lambda: show_image("formula_png/tran_func/CRDHF.png", tranFrame, btn17))
btn17.pack(pady=7)

topicButton1 = tk.Button(algeFrame, text="Transcendental", width=20, height=2, command=show_tran)
topicButton1.pack(pady=7)
topicButton2 = tk.Button(tranFrame, text="Algebraic", width=20, height=2, command=show_alge)
topicButton2.pack(pady=7)

algeFrame.pack(expand=True, fill="both")
algeFrame.pack_propagate(False)
algeFrame.pack(anchor="center", side="left")

#Calculator Screen
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
    
    elif symbol == "OFF":
        algeFrame.pack()
        calculator_screen.pack_forget()

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

#QUIZ FRAME
questions = [
    {
        "question": "questions/ques_1.png",
        "options": ["A","B","C","D"],
        "answer": "A",
        "solution" : "solutions/sol_1.png"
    },
    {
        "question": "questions/ques_2.png",
        "options": ["A", "B", "C", "D"],
        "answer": "C",
        "solution" : "solutions/sol_2.png"
    },
    {
        "question": "questions/ques_3.png",
        "options": ["A", "B", "C", "D"],
        "answer": "B",
        "solution" : "solutions/sol_3.png"
    },
    {
        "question": "questions/ques_4.png",
        "options": ["A", "B", "C", "D"],
        "answer": "B",
        "solution" : "solutions/sol_4.png"
    },
    {
        "question": "questions/ques_5.png",
        "options": ["A", "B", "C", "D"],
        "answer": "C",
        "solution" : "solutions/sol_5.png"
    },
    {
        "question": "questions/ques_6.png",
        "options": ["A", "B", "C", "D"],
        "answer": "A",
        "solution" : "solutions/sol_6.png"
    },
    {
        "question": "questions/ques_7.png",
        "options": ["A", "B", "C", "D"],
        "answer": "B",
        "solution" : "solutions/sol_7.png"
    },
    {
        "question": "questions/ques_8.png",
        "options": ["A", "B", "C", "D"],
        "answer": "A",
        "solution" : "solutions/sol_8.png"
    },
    {
        "question": "questions/ques_9.png",
        "options": ["A", "B", "C", "D"],
        "answer": "B",
        "solution" : "solutions/sol_9.png"
    },
    {
        "question": "questions/ques_10.png",
        "options": ["A", "B", "C", "D"],
        "answer": "A",
        "solution" : "solutions/sol_10.png"
    },
    {
        "question": "questions/ques_11.png",
        "options": ["A", "B", "C", "D"],
        "answer": "A",
        "solution" : "solutions/sol_11.png"
    },
    {
        "question": "questions/ques_12.png",
        "options": ["A", "B", "C", "D"],
        "answer": "A",
        "solution" : "solutions/sol_12.png"
    },
    {
        "question": "questions/ques_13.png",
        "options": ["A", "B", "C", "D"],
        "answer": "D",
        "solution" : "solutions/sol_13.png"
    },
    {
        "question": "questions/ques_14.png",
        "options": ["A", "B", "C", "D"],
        "answer": "C",
        "solution" : "solutions/sol_14.png"
    },
    {
        "question": "questions/ques_15.png",
        "options": ["A", "B", "C", "D"],
        "answer": "A",
        "solution" : "solutions/sol_15.png"
    },
    {
        "question": "questions/ques_16.png",
        "options": ["A", "B", "C", "D"],
        "answer": "B",
        "solution" : "solutions/sol_16.png"
    },
    {
        "question": "questions/ques_17.png",
        "options": ["A", "B", "C", "D"],
        "answer": "C",
        "solution" : "solutions/sol_20.png"
    },
    {
        "question": "questions/ques_18.png",
        "options": ["A", "B", "C", "D"],
        "answer": "D",
        "solution" : "solutions/sol_17.png"
    },
    {
        "question": "questions/ques_19.png",
        "options": ["A", "B", "C", "D"],
        "answer": "A",
        "solution" : "solutions/sol_18.png"
    },
    {
        "question": "questions/ques_20.png",
        "options": ["A", "B", "C", "D"],
        "answer": "D",
        "solution" : "solutions/sol_19.png"
    },
]

question_num = 0
score = 0

def ask_question():
    global question_num
    question = questions[question_num]
    image_path = question["question"]
    image = Image.open(image_path)
    image = image.resize((375, 150), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    image_label.configure(image=photo)
    image_label.image = photo
    option_a.configure(text=question["options"][0], state=tk.NORMAL, wraplength=300)
    option_b.configure(text=question["options"][1], state=tk.NORMAL, wraplength=300)
    option_c.configure(text=question["options"][2], state=tk.NORMAL, wraplength=300)
    option_d.configure(text=question["options"][3], state=tk.NORMAL, wraplength=300)
    show_score()
    disable_next_button()
    show_solution_button.configure(state=tk.DISABLED)
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
        show_score()
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
    image_label.pack_forget()
    question_label.pack()
    question_label.configure(text="Quiz Finished")
    options_frame.pack_forget()
    confirm_button.pack_forget()
    next_button.pack_forget()
    show_solution_button.pack_forget()
    exit_button.pack_forget()

    result_label.configure(text="Your Final Score: " + str(score) + "/" + str(len(questions)), font=("RobotoCondensed", 20))
    congratulation_label = tk.Label(root, text="Congratulations!", font=("RobotoCondensed", 24))
    congratulation_label.pack(pady=10)
    exit_button.configure(state=tk.NORMAL)
    exit_button.pack(pady=10)

def exit_quiz():
    answer = messagebox.askyesno("Exit Quiz", "Are you sure you want to exit the quiz?")
    if answer:
        root.destroy()

def show_solution():
    question = questions[question_num]
    image_path = question["solution"]
    
    solution_window = tk.Toplevel(root)
    solution_window.title("Solution")
    
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    
    solution_label = tk.Label(solution_window, image=photo)
    solution_label.pack()
    
    solution_window.mainloop()

quizFrame =tk.Frame(root,width=450,height=800)

score_top_label = tk.Label(quizFrame, text="Score: 0", font=("RobotoCondensed", 14))
score_top_label.pack(pady=20)
result_label = tk.Label(quizFrame, text="", font=("RobotoCondensed", 14))
result_label.pack(pady=10)

question_label = tk.Label(quizFrame, text="", font=("RobotoCondensed", 20),pady=25)
image_label = tk.Label(quizFrame, text="", font=("RobotoCondensed", 16), pady=25)
image_label.pack()

options_frame = tk.Frame(quizFrame)
options_frame.pack(pady=20)

option_a = tk.Button(options_frame, text="", font=("RobotoCondensed", 14), width=15, command=lambda: check_choice("A"))
option_a.grid(row=0, column=0, padx=10, pady=10)

option_b = tk.Button(options_frame, text="", font=("RobotoCondensed", 14), width=15, command=lambda: check_choice("B"))
option_b.grid(row=1, column=0, padx=10, pady=10)

option_c = tk.Button(options_frame, text="", font=("RobotoCondensed", 14), width=15, command=lambda: check_choice("C"))
option_c.grid(row=0, column=1, padx=10, pady=10)

option_d = tk.Button(options_frame, text="", font=("RobotoCondensed", 14), width=15, command=lambda: check_choice("D"))
option_d.grid(row=1, column=1, padx=10, pady=10)

confirm_button = tk.Button(quizFrame, text="Confirm Answer", font=("RobotoCondensed", 14), width=15, state=tk.DISABLED,command=check_answer)
confirm_button.pack(pady=20)

next_button = tk.Button(quizFrame, text="Next", font=("RobotoCondensed", 14), width=15, command=next_question, state=tk.DISABLED)
next_button.pack(pady=20)

show_solution_button = tk.Button(quizFrame, text="Show Solution", font=("RobotoCondensed", 14), width=15,state=tk.DISABLED, command=show_solution)
show_solution_button.pack(pady=10)

exit_button = tk.Button(quizFrame, text="Exit Quiz", font=("RobotoCondensed", 14), width=15, command=exit_quiz,state=tk.DISABLED)
exit_button.pack(pady=20)

ask_question()


root.mainloop()