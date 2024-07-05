def add():
    x = int(input("Enter the number:"))
    y = int(input("Enter the number:"))
    print(x+y)

def add2():
    x = int(input("Enter the first number:"))
    y = int(input("Enter the second number:"))
    z = int(input("Enter the third number:"))
    print(x+y+z)

def sub():
    x = int(input("Enter the first number:"))
    y = int(input("Enter the second number:"))
    print(x-y)

def sub2():
    x = int(input("Enter the first number:"))
    y = int(input("Enter the second number:"))
    z = int(input("Enter the third number:"))
    print((x-y)-z)

def mul():
    x = int(input("Enter the number:"))
    y = int(input("Enter the number:"))
    print(x*y)

def div():
    x = int(input("Enter the number:"))
    y = int(input("Enter the number:"))
    print(x/y)

print("1. Addition of 2 numbers")
print("2. Addition of three numbers")
print("3. Subtraction of two numbers")
print("4. Subtraction of three numbers")
print("5. Multiplication")
print("6. Division")
print("Enter the number to do the corresponding function")
ch = int(input("Enter the choice: "))

if(ch==1):
    add()

elif(ch==2):
    add2()

elif(ch==3):
    sub()

elif(ch==4):
    sub2()

elif(ch==5):
    mul()

elif(ch==6):
    div()

else:
    print("Enter the correct choice")