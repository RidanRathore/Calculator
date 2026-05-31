print("welcome to the calculator 😁")
def add(x, y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "error: division by zero"
    else:
        return x / y

while True:

    try:

        g = input("continue? (y/n): ").lower()

        if g == "quit" or g == "q" or g == "exit" or g == "no" or g == "n":
            print("thanks for using the calculator 😛")
            break

        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))

        op = input("enter the opration:").lower()

        if op == "+" or op == "add":
            print("the sum is: ", end="")
            a = add(x, y)
            print(a)

        elif op == "-" or op == "subtract":
            print("the difference is: ", end="")
            b = subtract(x, y)
            print(b)

        elif op == "*" or op == "multiply":
            print("the product is: ", end="")
            c = multiply(x, y)
            print(c)

        elif op == "/" or op == "divide":
            print("the quotient is: ", end="")
            d = divide(x, y)
            print(d)

    except ValueError as e:
        print("invalid input:", e)


