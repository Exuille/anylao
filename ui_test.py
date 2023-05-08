import sympy as sp

def AboutPage():
    pass

def TopicsPage():
    pass

def FormulasPage():
    pass

def CalcPage():
    print("Derrivative Calculator Menu")
    print("[ 1 ] Algebraic Functions")
    print("[ 2 ] Transcendental Function")
    ch = int(input("Choose: "))
    if ch == 1:
        alge_func()
    elif ch == 2:
        tran_func()

def alge_func():
    x = sp.symbols('x')
    print("[ 1 ] Constant Rule       |  [ 2 ] Power Rule                           |  [ 3 ] Constant Multiple Rule")
    print("[ 4 ] Sum Rule            |  [ 5 ] Product Rule                         |  [ 6 ] Quotient Rule")
    print("[ 7 ] General Power Rule  |  [ 8 ] Derrivative of a Composite Function  |  [ 9 ] Chain Rule")
    ch = int(input("Please Choose what topic you want of Derivatives of Algebraic Functions you want to use: "))

    if ch == 1:
        # Constant Rule
        problem = input("Please input an Algebraic Funtion: ")
        expr = sp.sympify(problem)
        result = sp.diff(expr, x)
        print(result)
    elif ch == 2:
        # Power Rule
        problem = input("Please input an Algebraic Funtion: ")
        expr = sp.sympify(problem)
        result = sp.diff(expr, x)
        print(result)
    elif ch == 3:
        # Constant Multiple Rule
        problem = input("Please input an Algebraic Funtion: ")
        expr = sp.sympify(problem)
        result = sp.diff(expr, x)
        print(result)
    elif ch == 4:
        # Sum Rule
        problem = input("Please input an Algebraic Funtion: ")
        expr = sp.sympify(problem)
        result = sp.diff(expr, x)
        print(result)
    elif ch == 5:
        # Product Rule
        problem = input("Please input an Algebraic Funtion: ")
        expr = sp.sympify(problem)
        result = sp.diff(expr, x)
        print(result)
    elif ch == 6:
        # Quotient Rule
        problem = input("Please input an Algebraic Funtion: ")
        expr = sp.sympify(problem)
        result = sp.diff(expr, x)
        print(result)
    elif ch == 7:
        # General Power Rule
        problem = input("Please input an Algebraic Funtion: ")
        expr = sp.sympify(problem)
        result = sp.diff(expr, x)
        print(result)
    elif ch == 8:
        # Derivative of a Composite Function
        f = input("Please input the outer function: ")
        g = input("Please input the inner function: ")
        expr = sp.sympify(f.replace("x", g))
        result = sp.diff(expr, x)
        result = result.subs(g, sp.symbols('g'))
        print(result)
    elif ch == 9:
        # Chain Rule
        f = input("Please input the outer function: ")
        g = input("Please input the inner function: ")
        g = g.replace("^", "**")
        x = sp.symbols('x')
        expr = sp.sympify(f.replace("x", f"{g}"))
        dg = sp.diff(sp.sympify(g), x)
        result = sp.diff(expr, x) * dg
        print(result)
    else:
        print("Invalid Choice")

def tran_func():
    pass

def QuizPage():
    pass

while True:
    print("Main Menu")
    print("[ 1 ] About")
    print("[ 2 ] Topics")
    print("[ 3 ] Formulas")
    print("[ 4 ] Calculator")
    print("[ 5 ] Quiz")
    print("[ 6 ] Exit")
    choice = int(input("Choose Page: "))

    if choice == 1:
        AboutPage()
    elif choice == 2:
        TopicsPage()
    elif choice == 3:
        FormulasPage()
    elif choice == 4:
        CalcPage()
    elif choice == 5:
        QuizPage()
    elif choice == 6:
        break

