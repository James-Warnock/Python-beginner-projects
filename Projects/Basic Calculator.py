#Greetings
print("\nGreetings huzz or bruzz, welcome to my calc (short for calculator)")

#math?
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error, cannot divide by 0"
    return x / y

#Main programme
while True: 
    print("\nSelect Operation ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("\nChoose a number (1-5): ")

    if choice == '5':
        print("cya mate")
        break

    #get user input
    if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
    
    #Result based on input
    if choice == '1':
        print("Result: ", add(num1, num2))
    elif choice == '2':
        print("Result: ", subtract(num1, num2))
    elif choice == '3':
        print("Result: ", multiply(num1, num2))
    elif choice == '4':
        print("Result: ", divide(num1, num2))
    else:
        print("Error. Please choose a number 1-5")


    







