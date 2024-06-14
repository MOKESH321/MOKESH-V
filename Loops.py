print("Loops Program")

n = int(input("Enter the number of times to iterate: "))

print("Enter 1 for FOR LOOP")
print("Enter 2 for WHILE LOOP")

x = int(input("Enter a number: "))
if(x == 1):
    a = 0
    print("FOR LOOP")
    for i in range(n):
        print("Enter the value ", i+1, ":")
        b = int(input())
        a+=b
    print("The total of all values that you have entered: ", a)
    
elif(x == 2):
    print("WHILE LOOP")
    i = 1
    d = 1
    while i<=n:
        print("Enter the value to multiply all ",i,":")
        c = int(input())
        d*=c
        i+=1
    print("The multiplied value of all values: ", d)