import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title("diffCALC")
root.geometry('450x580')

navIcon =ImageTk.PhotoImage(Image.open("navIcon.png"))
closeIcon = ImageTk.PhotoImage(Image.open("closeIcon.png"))
logo = ImageTk.PhotoImage(Image.open("logo.png"))

label = "DERIVATIVES"
navbar = tk.Frame(root, width = 450, height = 65, bg = '#5E7CAE')
navbar.place(x=0, y=0)
navLabel = tk.Label(navbar, text=label, font="RobotoCondensed",bg='#5E7CAE', fg ="white")
navLabel.place(x = 165, y = 18)
navLogo = tk.Label(navbar,bg='#5E7CAE', image= logo)
navLogo.place(x = 400, y= 18)

def show_calculator():
    calculator_frame.tkraise()
    navbar.lift()

def show_quiz():
    quiz_frame.tkraise()
    navbar.lift()

def show_about():
    about_frame.tkraise()
    navbar.lift()

def toggle_win():
    global menu_frame
    menu_frame = tk.Frame(root,width=380,height=580,bg='#5E7CAE')
    menu_frame.place(x=0,y=0)

    button = tk.Button(menu_frame,text='D E R I V A T I V E S', width = 42, height = 2)
    button.place(x=35, y = 117)
    button = tk.Button(menu_frame,text='C A L C U L A T O R', width = 42, height = 2, command=show_calculator)
    button.place(x=35, y = 172)
    button = tk.Button(menu_frame,text='P R A C T C E   Q U I Z', width = 42, height = 2, command=show_quiz)
    button.place(x=35, y = 227)
    button = tk.Button(menu_frame,text='A B O U T', width = 42, height = 2, command=show_about)
    button.place(x=35, y = 282)

    closeBtn = tk.Button(menu_frame, bg='#5E7CAE', activebackground='#5E7CAE',image=closeIcon,command=menu_frame.destroy)
    closeBtn.place(x=10, y=18)


def add_navbar(frame):
    navbar = tk.Frame(frame, width = 450, height = 65, bg = '#5E7CAE')
    navbar.place(x=0, y=0)
    navLabel = tk.Label(navbar, text=label, font="RobotoCondensed",bg='#5E7CAE', fg ="white")
    navLabel.place(x = 165, y = 18)
    navLogo = tk.Label(navbar,bg='#5E7CAE', image= logo)
    navLogo.place(x = 400, y= 18)
    navbarBtn = tk.Button(navbar, bg='#5E7CAE', activebackground='#5E7CAE',image=navIcon,command=toggle_win)
    navbarBtn.place(x=10, y=18)

derivframe = tk.Frame(root, width = 450, height = 580)
add_navbar(derivframe)
derivframe.pack()

calculator_frame = tk.Frame(root, width=450, height=580)
add_navbar(calculator_frame)
calculator_frame.pack()

quiz_frame = tk.Frame(root, width=450, height=580)
add_navbar(quiz_frame)
quiz_frame.pack()

about_frame = tk.Frame(root, width=450, height=580)
add_navbar(about_frame)
about_frame.pack()

root.mainloop()