import tkinter as tk

root = tk.Tk()
root.title("Differential Calculus Calculator")

canvas = tk.Canvas(root, width=720, height=540)

def show_menu():
    menu_frame.grid(row=0, column=0)
    about_frame.grid_forget()
    topic_frame.grid_forget()
    formulas_frame.grid_forget()
    calculator_frame.grid_forget()
    quiz_frame.grid_forget()

def show_about():
    menu_frame.grid_forget()
    about_frame.grid(row=0, column=0)
    topic_frame.grid_forget()
    formulas_frame.grid_forget()
    calculator_frame.grid_forget()
    quiz_frame.grid_forget()

def show_topics():
    menu_frame.grid_forget()
    about_frame.grid_forget()
    topic_frame.grid(row=0, column=0)
    formulas_frame.grid_forget()
    calculator_frame.grid_forget()
    quiz_frame.grid_forget()

def show_formula():
    menu_frame.grid_forget()
    about_frame.grid_forget()
    topic_frame.grid_forget()
    formulas_frame.grid(row=0, column=0)
    calculator_frame.grid_forget()
    quiz_frame.grid_forget()

def show_calculator():
    menu_frame.grid_forget()
    about_frame.grid_forget()
    topic_frame.grid_forget()
    formulas_frame.grid_forget()
    calculator_frame.grid(row=0, column=0)
    quiz_frame.grid_forget()

def show_quiz():
    menu_frame.grid_forget()
    about_frame.grid_forget()
    topic_frame.grid_forget()
    formulas_frame.grid_forget()
    calculator_frame.grid_forget()
    quiz_frame.grid(row=0, column=0)

menu_frame = tk.Frame(root, width=720, height=540)
menu_frame.pack_propagate(0)
menu_frame.grid()

button = tk.Button(menu_frame, text="About!", width=15, height= 2, command=show_about)
button.place(x=300, y=125)
button = tk.Button(menu_frame, text="Topics", width=15, height= 2, command=show_topics)
button.place(x=300, y=175)
button = tk.Button(menu_frame, text="Formulas", width=15, height= 2, command=show_formula)
button.place(x=300, y=225)
button = tk.Button(menu_frame, text="Calculator", width=15, height= 2, command=show_calculator)
button.place(x=300, y=275)
button = tk.Button(menu_frame, text="Practice Quiz", width=15, height= 2, command=show_quiz)
button.place(x=300, y=325)


about_frame = tk.Frame(root, width=720, height=540)
about_frame.pack_propagate(0)
about_title = tk.Label(about_frame, text='ABOUT', font=('Arial', 14, 'bold'))
about_title.pack()
button = tk.Button(about_frame, text="Back", width=15, height= 2, command=show_menu)
button.place(x=300, y=450)

topic_frame = tk.Frame(root, width=720, height=540)
topic_frame.pack_propagate(0)
topic_title = tk.Label(topic_frame, text='TOPICS', font=('Arial', 14, 'bold'))
topic_title.pack()
button = tk.Button(topic_frame, text="Back", width=15, height= 2, command=show_menu)
button.place(x=300, y=450)

formulas_frame = tk.Frame(root, width=720, height=540)
formulas_frame.pack_propagate(0)
formulas_title = tk.Label(formulas_frame, text='FORMULAS', font=('Arial', 14, 'bold'))
button = tk.Button(formulas_frame, text="Back", width=15, height= 2, command=show_menu)
button.place(x=300, y=450)
formulas_title.pack()

calculator_frame = tk.Frame(root, width=720, height=540)
calculator_frame.pack_propagate(0)
calculator_title = tk.Label(calculator_frame, text='CALCULATOR', font=('Arial', 14, 'bold'))
button = tk.Button(calculator_frame, text="Back", width=15, height= 2, command=show_menu)
button.place(x=300, y=450)
calculator_title.pack()

quiz_frame = tk.Frame(root, width=720, height=540)
quiz_frame.pack_propagate(0)
quiz_title = tk.Label(quiz_frame, text='PRACTICE QUIZ', font=('Arial', 14, 'bold'))
button = tk.Button(quiz_frame, text="Back", width=15, height= 2, command=show_menu)
button.place(x=300, y=450)
quiz_title.pack()

root.mainloop()