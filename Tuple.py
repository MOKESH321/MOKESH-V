print()
mytuple = (1, 2, 3)
print("Original Tuple: ", mytuple)

print()
print("Adding a new element")
new = 4
update = mytuple + (new,)
mytuple = update
print(update)

print()
print("Removing an element")
update = mytuple[:0] + mytuple[1:]
print(update)

print()
new = 5
update = mytuple[:3] + (new,) + mytuple[4:]
print(update)
