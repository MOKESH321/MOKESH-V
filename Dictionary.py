print()
mydict = {'Name' : 'Andrew', 'Age' : '40', 'Country' : 'INDIA'}
print("Original Dictionary:", mydict)

print()
print("Adding the Key")
mydict['gender'] = 'Male'
print(mydict)

print()
print("Deleting a key")
del mydict['Country']
print(mydict)

print()
print("Modifying a key")
mydict['Age'] = '35'
print(mydict)