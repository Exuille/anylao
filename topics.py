import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

# Set the screen to Topics Screen

# Set the layout and stuff for the Topics Screen
root.title("diffCALC")
root.geometry('450x580')
root.configure(bg='white')

# Create frames for each topic
algeFrame = tk.Frame(root)
tranFrame = tk.Frame(root)
topicFrame = tk.Frame(root)

# Hide the frames
topicFrame.pack()
algeFrame.pack_forget()
tranFrame.pack_forget()

# Functions for when the Topics are chosen
def on_alge_click():
    algeFrame.pack(fill="both", expand=True)
    topicFrame.pack_forget()
    tranFrame.pack_forget()

def on_tran_click():
    tranFrame.pack(fill="both", expand=True)
    topicFrame.pack_forget()
    algeFrame.pack_forget()

def on_topic_click():
    topicFrame.pack(fill="both", expand=True)
    topicFrame.pack_propagate(False)
    topicFrame.pack(anchor="center", side="left")
    algeFrame.pack_forget()
    tranFrame.pack_forget()


# Add 2 Options to choose if Algebraic or Transcedental
algeButton = tk.Button(topicFrame, text="Algebraic Functions", width=20, height=2, command=on_alge_click)
algeButton.pack(pady=20)

tranButton = tk.Button(topicFrame, text="Transcedental Functions", width=20, height=2, command=on_tran_click)
tranButton.pack(pady=20)

# Algebraic Functions 
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

# Button for calculator page
calcButton = tk.Button(topicFrame, text="Calculator", width=20, height=2)
calcButton.pack(pady=20)

# Button for Topic Page
topicButton1 = tk.Button(algeFrame, text="Back to Topics Page", width=20, height=2, command=on_topic_click)
topicButton1.pack()
topicButton2 = tk.Button(tranFrame, text="Back to Topics Page", width=20, height=2, command=on_topic_click)
topicButton2.pack()

# Button for Home Page
homeButton = tk.Button(topicFrame, text="Home", width=20, height=2)
homeButton.pack(pady=20)

# Center the buttons vertically
topicFrame.pack(expand=True, fill="both")
topicFrame.pack_propagate(False)
topicFrame.pack(anchor="center", side="left")

# Start tkinter event loop
root.mainloop()
