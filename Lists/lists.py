thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Looping through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Check if item exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# List length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Adding items to list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# To add to a specific index use the insert() method
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Remove item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)