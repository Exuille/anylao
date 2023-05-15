import tkinter as tk

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.question_num = 0
        self.score = 0
        self.questions = [
            {
                "question": "If y = sin x^3, find dy/dx.",
                "options": ["3x^2 cosx^3", "-3x^2 cosx^3", "3x^2 cosx^2", "3x^3 cosx^3"],
                "answer": "3x^2 cosx^3"
            },
            {
                "question": "Compute the derivative of the function y = arcsin(2x + 1), or  y = sin-1(2x + 1).",
                "options": [" 2/√[-x(x + 2)]", "-1/√[-x(x + 1)]", "1/√[-x(x + 1)]", "1/√[-x(x + 2)]"],
                "answer": "1/√[-x(x + 1)]"
            },
            {
                "question": "Find g' (t), when g (t) = - 325. ",
                "options": ["-325", "0", "325", "1"],
                "answer": "0"
            },
            {
                "question" : "Differentiate log e (x^2 + 3x + 1).",
                "options" : ["1/((x^2 + 3x + 1)", "2x+3", "(x^2+3x+1)/(2x+3)", "1/((x^2 + 3x + 1)"],
                "answer" : "(x^2+3x+1)/(2x+3)"
            },
            {
                "question" : "Solve the equation: 2 cosh 2x +10sinh 2x = 5",
                "options" : ["4/3ln(1/2)", "1/2ln(4/3)", "3/4ln(1/2)", "1/2ln(3/4)"],
                "answer" : "1/2ln(4/3)"
            },
            {
                "question" : "e^xcos(x)",
                "options" : ["e^xcos(x)+e^xsin(x)", "e^xcos(x)-e^xsin(x)", "e^xsin(x)-e^xcos(x)", "e^xsin(x)cos(x)"],
                "answer" : "e^xcos(x)-e^xsin(x)"
            },
            {
                "question" : "sech(5x^3+x^2-2)",
                "options" : ["-sech(5x^3+x^2-2)tanh(5x^3+x^2-2)(15x^2+2x)", "-sech(5x^3+x^2-2)tanh(5x^3+x^2-2)(5x^3+x^2-2)", "sech(5x^3+x^2-2)tanh(5x^3+x^2-2)(15x^2+2x)", "sech(5x^3+x^2-2)tanh(5x^3+x^2-2)(5x^3+x^2-2)"],
                "answer" : "sech(5x^3+x^2-2)tanh(5x^3+x^2-2)(15x^2+2x)"
            },
            {
                "question" : "log10(x^13)",
                "options" : ["13ln(10)x", "13/ln(10)x", "10/ln(13)x", "10ln(13)x"],
                "answer" : "13/ln(10)x"
            },
            {
                "question" : "e^x^3 + x^2 -6",
                "options" : ["e^x^3-x^2+6(3x^2+3x)","e^x^3+x^2-6(3x^2+2x)"],
                "answer" : "e^x^3+x^2-6(3x^2+2x)"
            },
            {
                "question" : "sin^2(x)",
                "options" : ["cos(2x)", "sin(2x)", "sin(x)cos(2x)", "sin(2x)cos(2x)"],
                "answer" : "sin(2x)"
            },
        ]

        # create widgets
        self.question_label = tk.Label(master, text="")
        self.question_label.pack()
        self.option_a = tk.Button(master, text="", command=lambda:self.check_answer("A"))
        self.option_a.pack()
        self.option_b = tk.Button(master, text="", command=lambda:self.check_answer("B"))
        self.option_b.pack()
        self.option_c = tk.Button(master, text="", command=lambda:self.check_answer("C"))
        self.option_c.pack()
        self.option_d = tk.Button(master, text="", command=lambda:self.check_answer("D"))
        self.option_d.pack()
        self.score_label = tk.Label(master, text="")
        self.score_label.pack()
        self.next_button = tk.Button(master, text="Next", command=self.next_question)
        self.next_button.pack()
        
        # initialize the quiz
        self.ask_question()

    def ask_question(self):
        question = self.questions[self.question_num]
        self.question_label.configure(text=question["question"])
        self.option_a.configure(text="A) " + question["options"][0])
        self.option_b.configure(text="B) " + question["options"][1])
        self.option_c.configure(text="C) " + question["options"][2])
        self.option_d.configure(text="D) " + question["options"][3])
        
    def check_answer(self, choice):
        question = self.questions[self.question_num]
        if question["answer"] == question["options"][ord(choice)-ord('A')]:
            self.score += 1
        self.show_score()
        
    def show_score(self):
        self.score_label.configure(text="Score: " + str(self.score) + "/" + str(self.question_num+1))

    def next_question(self):
        self.question_num += 1
        if self.question_num >= len(self.questions):
            self.show_final_score()
        else:
            self.ask_question()

    def show_final_score(self):
        self.question_label.configure(text="Quiz complete!")
        self.option_a.destroy()
        self.option_b.destroy()
        self.option_c.destroy()
        self.option_d.destroy()
        self.score_label.configure(text="Final score: " + str(self.score) + "/" + str(len(self.questions)))
        self.next_button.configure(text="Restart", command=self.restart_quiz)

    def restart_quiz(self):
        self.question_num = 0
        self.score = 0
        self.ask_question()
        self.next_button.configure(text="Next")

# create the main window
root = tk.Tk()
root.title("Quiz App")

# create the quiz app
app = QuizApp(root)

# run the main event loop
root.mainloop()
