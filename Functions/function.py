# Functions


def function_one():
    print("Hello World")


function_one()

# Parameters


def function_two(fname):
    print(fname + " Hartley")


function_two("Cameron")
function_two("Alex")
function_two("Robert")

# Default Parameter Values


def function_three(country="Japan"):
    print("I am from " + country)


function_three()

# Passing a List as a Parameter


def function_four(food):
    for x in food:
        print(x)


fruits = ["Apple", "Orange", "Bananas"]

function_four(fruits)

# Return Values


def function_five(x):
    return 5 * x


print(function_five(3))
print(function_five(5))
print(function_five(7))

# Keyword Arguments


def function_six(child3, child2, child1):
    print("The youngest child is " + child3)


function_six(child1="Naruto", child2="Sasuke", child3="Sakura")

# Arbitrary Arguments


def function_seven(*kids):
    print("The youngest child is " + kids[2])


function_seven("Cameron", "Alex", "Clifford")

# Pass Statement


def function_eight():
    pass

# Recursion


def function_nine(k):
    if(k > 0):
        result = k+function_nine(k-1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
function_nine(6)