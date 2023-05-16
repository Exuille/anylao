import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

questions = [
    {
        "question": "If y=sin(x^3), find dy/dx.",
        "options": ["3x^2 cosx^3", "-3x^2 cosx^3", "3x^2 cosx^2", "3x^3 cosx^3"],
        "answer": "3x^2 cosx^3",
        "solution" : "solutions/sol_1.png"
    },
    {
        "question": "Compute the derivative of the function y = arcsin(2x + 1), or  y = sin-1(2x + 1).",
        "options": [" 2/√[-x(x + 2)]", "-1/√[-x(x + 1)]", "1/√[-x(x + 1)]", "1/√[-x(x + 2)]"],
        "answer": "1/√[-x(x + 1)]",
        "solution" : "solutions/sol_2.png"
    },
    {
        "question": "Find g' (t), when g (t) = - 325. ",
        "options": ["-325", "0", "325", "1"],
        "answer": "0",
        "solution" : "solutions/sol_3.png"
    },
    {
        "question": "Differentiate log e (x^2 + 3x + 1).",
        "options": ["1/((x^2 + 3x + 1)", "2x+3", "(2x+3)/(x^2+3x+1)", "1/((x^2 + 3x + 1)"],
        "answer": "(2x+3)/(x^2+3x+1)",
        "solution" : "solutions/sol_4.png"
    },
    {
        "question" : "Solve the equation: 2 cosh 2x +10sinh 2x = 5",
        "options" : ["4/3ln(1/2)", "1/2ln(4/3)", "3/4ln(1/2)", "1/2ln(3/4)"],
        "answer" : "1/2ln(4/3)",
        "solution" : "solutions/sol_5.png"
    },
    {
        "question" : "e^xcos(x)",
        "options" : ["e^xcos(x)+e^xsin(x)", "e^xcos(x)-e^xsin(x)", "e^xsin(x)-e^xcos(x)", "e^xsin(x)cos(x)"],
        "answer" : "e^xcos(x)-e^xsin(x)",
        "solution" : "solutions/sol_6.png"
    },
    {
        "question" : "sech(5x^3+x^2-2)",
        "options" : ["-sech(5x^3+x^2-2)tanh(5x^3+x^2-2)(15x^2+2x)", "-sech(5x^3+x^2-2)tanh(5x^3+x^2-2)(5x^3+x^2-2)", "sech(5x^3+x^2-2)tanh(5x^3+x^2-2)(15x^2+2x)", "sech(5x^3+x^2-2)tanh(5x^3+x^2-2)(5x^3+x^2-2)"],
        "answer" : "sech(5x^3+x^2-2)tanh(5x^3+x^2-2)(15x^2+2x)",
        "solution" : "solutions/sol_7.png"
    },
    {
        "question" : "log10(x^13)",
        "options" : ["13ln(10)x", "13/ln(10)x", "10/ln(13)x", "10ln(13)x"],
        "answer" : "13/ln(10)x",
        "solution" : "solutions/sol_8.png"
    },
    {
        "question" : "e^x^3 + x^2 -6",
        "options" : ["e^x^3-x^2+6(3x^2+3x)","e^x^3+x^2-6(3x^2+2x)","e^x^3+x^2-6(2x^3+2x)", "e^x^3+x^2-6(2x^3-2x)"],
        "answer" : "e^x^3+x^2-6(3x^2+2x)",
        "solution" : "solutions/sol_9.png"
    },
    {
        "question" : "sin^2(x)",
        "options" : ["cos(2x)", "sin(2x)", "sin(x)cos(2x)", "sin(2x)cos(2x)"],
        "answer" : "sin(2x)",
        "solution" : "solutions/sol_10.png"
    },
    {
        "question" : "Use Logarithmic Differentiation to Find the Derivative y=(2x-6)^2/(3x-2)^2",
        "options" : ["y’ = - 56(x-3)/ (3x-2)^3", "y’ = 56(x-3)/ (3x-2)^3", "y’ = 56(x-3)/ (3x-2)^4", "y’ = -56(x-3)/ (3x-2)^4"],
        "answer" : "y’ = 56(x-3)/ (3x-2)^3",
        "solution" : "solutions/sol_11.png"
    },
    {
        "question" : "Find the derivative of y= -4x^3e^2x^3",
        "options" : ["-4x^2e^2x^2(4x^2+5)", "4x^2e^2x^2(4x^2+3)", "5x^2e^2x^2(4x^2+3)", "-4x^2e^2x^2(4x^2+3)"],
        "answer" : "-4x^2e^2x^2(4x^2+3)",
        "solution" : "solutions/sol_12.png"
    },
    {
        "question" : "Find the derivative of y= -6e^3x",
        "options" : ["18e^3x", "18e", "-18e^4x", "-18e^3x"],
        "answer" : "-18e^3x",
        "solution" : "solutions/sol_13.png"
    },
    {
        "question" : "Find the derivative of y = 5^-2x^3",
        "options" : ["-6x^2(ln5)5^-2x", "6x^2(ln5)5^-2x", "-6x^2(ln5)5^", "-6x(ln5)5^-2x"],
        "answer" : "-6x^2(ln5)5^-2x",
        "solution" : "solutions/sol_14.png"
    },
    {
        "question" : "y= 3^1/x",
        "options" : ["(3ln 3)/x^2", "(3^1/xln 3)/x^2", "(3ln 2)/x^2", "(-3^1/xln 3)/x^2"],
        "answer" : "(3^1/xln 3)/x^2",
        "solution" : "solutions/sol_15.png"
    },
    {
        "question" : "Differentiate y=2 sinh x cosh x + 3 csch x",
        "options" : ["y'=3sinh^2 - 2cosh^2x + 3csch x coth x", "y'=2sinh^2 - 2cosh^2x + 3csch x coth x", "y'=2sinh^2 + 2cosh^2x - 3csch x coth x", "y'=3sinh^2 + 3cosh^2x - 2csch x coth x"],
        "answer" : "y'=2sinh^2 + 2cosh^2x - 3csch x coth x",
        "solution" : "solutions/sol_16.png"
    },
    {
        "question" : " d/dx[√cos^-1(x)]",
        "options" : ["1/cos^-1(x)√1-x^2", "-1/2√cos^-1(x)√1-x^2", "1/-sin(cos^-1(x))", "1/2√cos^-1(x)√1-x^2"],
        "answer" : "-1/2√cos^-1(x)√1-x^2",
        "solution" : "solutions/sol_17.png"
    },
    {
        "question" : "d/dx [ln(tan^-1(x))]",
        "options" : ["1/tan^-1(x)(1+x^2)", "1/tan^-1(x)", "1/2(1+x^2)", "1/x+x(ln(x))^2"],
        "answer" : "1/tan^-1(x)(1+x^2)",
        "solution" : "solutions/sol_18.png"
    },
    {
        "question" : "d/dx[xsin^-1(ln(x))]",
        "options" : ["sin^-1(ln(x))", "1/√1-(ln(x))^2", "sin^-1(ln(x)) - 1/√1-(ln(x))^2", "sin^-1(ln(x)) + 1/√1-(ln(x))^2"],
        "answer" : "sin^-1(ln(x)) + 1/√1-(ln(x))^2",
        "solution" : "solutions/sol_19.png"
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
    question_label.configure(text="Quiz Finished")
    option_a.pack_forget()
    option_b.pack_forget()
    option_c.pack_forget()
    option_d.pack_forget()
    confirm_button.pack_forget()
    next_button.pack_forget()
    show_solution_button.pack_forget()
    exit_button.pack()
    result_label.configure(text="Your Final Score: " + str(score) + "/" + str(len(questions)), font=("RobotoCondensed", 20))
    exit_button.configure(state=tk.NORMAL)
    congratulation_label = tk.Label(root, text="Congratulations!", font=("RobotoCondensed", 24))
    congratulation_label.pack(pady=10)

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

root = tk.Tk()
root.geometry("450x800")
root.title("Math Quiz")
root.resizable(False, False)

score_top_label = tk.Label(root, text="Score: 0", font=("RobotoCondensed", 14))
score_top_label.pack(pady=20)
result_label = tk.Label(root, text="", font=("RobotoCondensed", 14))
result_label.pack(pady=10)

question_label = tk.Label(root, text="", font=("RobotoCondensed", 16), pady=40)
question_label.pack()

option_a = tk.Button(root, text="", font=("RobotoCondensed", 14), width=30, command=lambda: check_choice("A"))
option_a.pack(pady=10)
option_b = tk.Button(root, text="", font=("RobotoCondensed", 14), width=30, command=lambda: check_choice("B"))
option_b.pack(pady=10)
option_c = tk.Button(root, text="", font=("RobotoCondensed", 14), width=30, command=lambda: check_choice("C"))
option_c.pack(pady=10)
option_d = tk.Button(root, text="", font=("RobotoCondensed", 14), width=30, command=lambda: check_choice("D"))
option_d.pack(pady=10)

confirm_button = tk.Button(root, text="Confirm Answer", font=("RobotoCondensed", 14), width=15, state=tk.DISABLED,command=check_answer)
confirm_button.pack(pady=10)

next_button = tk.Button(root, text="Next", font=("RobotoCondensed", 14), width=15, command=next_question, state=tk.DISABLED)
next_button.pack(pady=30)

show_solution_button = tk.Button(root, text="Show Solution", font=("RobotoCondensed", 14), width=15,state=tk.DISABLED, command=show_solution)
show_solution_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit Quiz", font=("RobotoCondensed", 14), width=15, command=exit_quiz,state=tk.DISABLED)
exit_button.pack(pady=10)

ask_question()

root.mainloop()