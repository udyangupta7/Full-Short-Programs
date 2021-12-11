try:
    import logging as lg
    lg.basicConfig(filename="logging.txt",
                   filemode='a',
                   format='%(asctime)s %(levelname)s -%(message)s',
                   datefmt='%Y-%m-%d %H:%M:%S')

    print("WELCOME. THIS IS A SIMPLE CALCULATOR.\nPRESS:\n\t A FOR ADDITION\n\tS FOR SUBSTRACTION\n\tD FOR DIVISION\n\tM FOR MULTIPLICATION")
    a = int(input("\nEnter the first number: "))
    b = int(input("Enter the second number: "))
    entry = str(input("\nPut your entry here: "))
    entry = entry.upper()
    if entry == "A":
        print("Addition of", a, "&", b, "is:", a + b)
    elif entry == "S":
        print("Difference of", a, "&", b, "is:", a - b)
    elif entry == "M":
        print("Product of", a, "&", b, "is:", a * b)
    elif entry == "D":
        print("Division of", a, "&", b, "leaves the remainder:", a / b)
    else:
        print("Wrong Entry. Try Again.")
    print("THANKS. USE ME AGAIN.")
except (AttributeError, TypeError, ValueError, AssertionError, Exception, ArithmeticError) as e:
    print("Error is: \n", e)
    lg.error("Error found in the code. Pl rectify and try again.")