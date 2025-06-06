#TASK 1: Simple Calculator
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error! Divison by zero."
    return a/b


def main():
    print("Simple Calculator")
    try:
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
    except ValueError:
        print("Invalid input, Please enter numeric value")
        return
     
    #Display the operation
    print("Select operation")
    print("1 Add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")  
    
    #User Input
    choice=input("Enter choice (1/2/3/4):")
    if choice== '1':
            print(f"{num1} + {num2} = {add(num1 , num2)}")
    elif choice=='2':
            print(f"{num1} - {num2} = {subtract(num1 , num2)}")
    elif choice=='3':
            print(f"{num1} * {num2} = {multiply(num1 , num2)}")
    elif choice=='4':
            result=divide(num1,num2)
            print(f"{num1} / {num2} = {result}")
    else:
            print("Invalid choice.Please select a valid operation")     

if __name__=="__main__":
    main()   