# for loops
pets = ['cats', 'dogs', 'rabbits', 'hamsters']

for index, myPets in enumerate(pets):
    print(index, myPets)

# assigns each member of the list to the variable myPets

# this example shows how to loop through a string
message = 'Hello'
for i in message:
    print(i)

# looping through a sequence of numbers: the range() function comes in handy
# the range function generates a list of numbers and has the syntax range (start, end, step)
# if the start is not given, the numbers generated would start from zero.

for i in range(5):
    print(i)

# While loops
# a while loop repeatedly executes instructions inside the loop while a condition remains valid
counter = 5
while counter > 0:
    print("Counter = ", counter)
    counter = counter - 1
j = 0
for i in range(5):
    j = j + 2
    print('i = ', i, ', j = ', j)
    if j == 6:
        break

# nested control system: using a for loop in an if statement, etc..
# continue: the rest of the loop after the keyword is skipped for that iteration

j = 0
for i in range(5):
    j = j + 2
    print('\ni = ', i, ', j = ', j)
    if j == 6:
        continue
    print('I will be skipped over if j = 6')

# Try, effect: The statement controls now the program proceeds when an error occurs

''' try:
        do something
    except:
            do something'''

try:
    answer = 12 / 0
    print(answer)
except ZeroDivisionError:
    print("An error occurred")

try:
    userInput1 = int(input("Please enter a number: "))
    userInput2 = int(input("Please enter another number: "))

    answer = userInput1 / userInput2
    print("The answer is ", answer)
    # myFile = open("missing.txt", 'r')
except ValueError:
    print("Error: You did not enter a number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except Exception as e:
    print("Unknown error: ", e)

# Functions - pre-written code that perform a certain task and modules
print("Hello World".replace("World", "Universe"))

# Defining your own functions:
# Syntax for defining our own function:
'''
 def functionName(parameters):
    code detailing what the function should do
    return [expression]'''


def checkIfPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if numberToCheck % x == 0:
            return False
    return True


answer = checkIfPrime(13)
print(answer)


# Variable Scope - variables defined inside a function are treated differently from variables defined outside

message1 = "Global Variable"

def myFunction():
    print("\nINSIDE THE FUNCTION")
    # Global variables are accessible inside a function
    print(message1)
    # Declaring a local variable
    message2 = "Local Variable"
    print(message2)

# Calling the function
myFunction()
print("\nOUTSIDE THE FUNCTION")
# Global variables are accessible outside function
print(message1)
# Local variables are NOT accessible outside function.
print(message2)
