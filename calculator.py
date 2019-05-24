from sys import exit

def addition():
    user_input_a = input ("Enter first number 'A =' ")
    user_input_b = input ("Enter second number 'B =' ")
    try:
        if "." in  user_input_a :
            a = float(user_input_a)
           # print("Yes, user input nomber 'A' is a float number.")
           # print("the Input number 'A' value is: ", a)
        else:
            a = int(user_input_a)
           # print("Yes, input string 'A' is an Integer.")
           # print("the Input number 'A' value is: ", a)
    except ValueError:
        print("Please, enter a number for 'A'!")

    try:
        if "." in  user_input_b :
            b = float(user_input_b)
           # print("Yes, user input number 'B' is a float number.")
           # print("the Input number 'B' value is: ", b)
        else:
            b = int(user_input_b)
           # print("Yes, input string 'B' is an Integer.")
           # print("the Input number 'B' value is: ", b) 
    except ValueError:
        print("Please, enter a number for 'B'!")
    print("summa A + B =", a + b)


def substraction():
    user_input_a = input ("Enter first number 'A =' ")
    user_input_b = input ("Enter second number 'B =' ")
    try:
        if "." in  user_input_a :
            a = float(user_input_a)
        else:
            a = int(user_input_a)
    except ValueError:
        print("Please, enter a number for 'A'!")
    try:
        if "." in  user_input_b :
            b = float(user_input_b)
        else:
            b = int(user_input_b)
    except ValueError:
        print("Please, enter a number for 'B'!")
    print("A - B =", a - b)


def multiplication():
    user_input_a = input ("Enter first number 'A =' ")
    user_input_b = input ("Enter second number 'B =' ")
    try:
        if "." in  user_input_a :
            a = float(user_input_a)
        else:
            a = int(user_input_a)
    except ValueError:
            print("Please, enter a number for 'A'!")
    try:
            if "." in  user_input_b :
                b = float(user_input_b)
            else:
                b = int(user_input_b)
    except ValueError:
            print("Please, enter a number for 'B'!")
    print("A * B =", a * b)


def division():
    user_input_a = input ("Enter first number 'A =' ")
    user_input_b = input ("Enter second number 'B =' ")
    try:
        if "." in  user_input_a :
            a = float(user_input_a)
        else:
            a = int(user_input_a)
    except ValueError:
            print("Please, enter a number for 'A'!")
    try:
            if "." in  user_input_b :
                b = float(user_input_b)
            else:
                b = int(user_input_b)
    except ValueError:
            print("Please, enter a number for 'B'!")
    print("A / B =", a / b)
 
def stop(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("If you need addition please, write a '+' ")
    print("If you need subtraction please, write a '-'")
    print("If you need multiplication please, write a '*'")
    print("If you need division please, write a '/'")

    choice = input("> ")
    if choice == "+":
        addition()
    elif choice == "-":
        substraction()
    elif choice == "*":
        multiplication()
    elif choice == "/":
        division()
    else:
       stop("Write correctly what you want!")

start()
