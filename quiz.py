import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

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

root = tk.Tk()
root.geometry("450x800")
root.title("Math Quiz")
root.resizable(False, False)

score_top_label = tk.Label(root, text="Score: 0", font=("RobotoCondensed", 14))
score_top_label.pack(pady=20)
result_label = tk.Label(root, text="", font=("RobotoCondensed", 14))
result_label.pack(pady=10)

question_label = tk.Label(root, text="", font=("RobotoCondensed", 20),pady=25)
image_label = tk.Label(root, text="", font=("RobotoCondensed", 16), pady=25)
image_label.pack()

options_frame = tk.Frame(root)
options_frame.pack(pady=20)

option_a = tk.Button(options_frame, text="", font=("RobotoCondensed", 14), width=15, command=lambda: check_choice("A"))
option_a.grid(row=0, column=0, padx=10, pady=10)

option_b = tk.Button(options_frame, text="", font=("RobotoCondensed", 14), width=15, command=lambda: check_choice("B"))
option_b.grid(row=1, column=0, padx=10, pady=10)

option_c = tk.Button(options_frame, text="", font=("RobotoCondensed", 14), width=15, command=lambda: check_choice("C"))
option_c.grid(row=0, column=1, padx=10, pady=10)

option_d = tk.Button(options_frame, text="", font=("RobotoCondensed", 14), width=15, command=lambda: check_choice("D"))
option_d.grid(row=1, column=1, padx=10, pady=10)

confirm_button = tk.Button(root, text="Confirm Answer", font=("RobotoCondensed", 14), width=15, state=tk.DISABLED,command=check_answer)
confirm_button.pack(pady=20)

next_button = tk.Button(root, text="Next", font=("RobotoCondensed", 14), width=15, command=next_question, state=tk.DISABLED)
next_button.pack(pady=20)

show_solution_button = tk.Button(root, text="Show Solution", font=("RobotoCondensed", 14), width=15,state=tk.DISABLED, command=show_solution)
show_solution_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit Quiz", font=("RobotoCondensed", 14), width=15, command=exit_quiz,state=tk.DISABLED)
exit_button.pack(pady=20)

ask_question()

root.mainloop()