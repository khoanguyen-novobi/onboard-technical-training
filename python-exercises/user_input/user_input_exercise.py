from datetime import datetime as dt


def exercise_1():
    name, age = input("Please enter your name and age: ").split()
    ans = f"You will be 100 years old in year: {int(dt.now().year) + (100 - int(age))}"
    print(ans)
    iterations = input("How many times you want to print again: ")
    for _ in range(int(iterations)):
        print(ans)


def exercise_2():
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    dob = input("Please enter your dob(mm/dd/yyyy): ")
    gender = input("Please enter your gender: ")
    addr = input("Please enter address: ")

    while 1:
        cmd = input("What would you like to know: ")
        if cmd == "name":
            print(f"Your name is: {name}")
        elif cmd == "age":
            print(f"Your age is: {age}")
        elif cmd == "dob":
            print(f"Your date of birth is: {dob}")
        elif cmd == "gender":
            print(f"Your gender is: {gender}")
        elif cmd == "address":
            print(f"Your address is: {addr}")
        elif cmd == "all":
            print(f"Your name is: {name}")
            print(f"Your age is: {age}")
            print(f"Your date of birth is: {dob}")
            print(f"Your gender is: {gender}")
            print(f"Your address is: {addr}")
        else:
            print("Command not found!")
            break
