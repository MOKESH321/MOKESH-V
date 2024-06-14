print()

mylist  = [1,2,3,4,5]
print("Original list: ", mylist)
print()

print("APPEND")
mylist.append(10)
print(mylist)
print()

print("REMOVE")
mylist.remove(2)
print(mylist)

print()
print("Inserting value using index")
mylist[0] = 20
print(mylist)

print()
print("Modifying the list")
mylist.insert(4, "hi")
print(mylist)