"""
Made By :- SANKET ASHOK NIGHOT
Email Id:- sanketnighot25@gmail.com

"""
stack_var = []


def stack(opr, numb=0):
    global stack_var
    num = numb
    if opr == "push":
        stack_var.insert(0, num)
    elif opr == "pop":
        if len(stack_var) != 0:
            ele = stack_var[0]
            del stack_var[0]
            print(f"Element Poped is '{ele}'")
        else:
            temp = "! ! ! Stack Underflow ! ! !"
            print(temp)
    elif opr == "display":
        for t in stack_var:
            if t == stack_var[0]:
                print(f"    -->|  {t}  |")
            else:
                print(f"       |  {t}  |")
        if len(stack_var) == 0:
            print("    -->|     |")
            print("       |=====|")
        else:
            print("       |=====|")


def Stack_Operations():
    status = True
    while status:
        print('''
Choose Operation to be performed on Stack :
        (1) Push
        (2) Pop
        (3) Display
        (4) Exit
        ''')
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            numb = int(input("Enter Number to be Pushed: "))
            print(f"Element {numb} pushed to stack ...")
            stack("push", numb)
        elif choice == 2:
            print("")
            stack("pop")
        elif choice == 3:
            print("")
            stack("display")
        elif choice == 4:
            status = False

        else:
            print("Invalid Choice ... Please Try Again ...")

        print("-----------------------------------------------")


print('''
        ~~~ STACK OPERATIONS ~~~
''')
Stack_Operations()
