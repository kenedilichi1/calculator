
def add(x, y):
    ''' Adds 2 numbers '''
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


isRunning = True

while isRunning:
    choice = input("operator: ")

    if choice in ('add', 'subtract', 'multiply', 'divide'):
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))

        if choice == 'add':
            result = add(num1, num2)
            
            print(int(result))
        
        elif choice == 'subtract':
            result = subtract(num1, num2)
            print(int(result))
        
        elif choice == 'multiply':
            result = multiply(num1, num2)
            
            print(int(result))
        
        elif choice == 'divide':
            result = divide(num1, num2)
            
            print(int(result))
    else:
        print("Input error")
    