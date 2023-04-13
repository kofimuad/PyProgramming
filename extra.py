# Variable Scope

message1 = "Global Variable (shares same name as a local variable)"

def myFunction():
    message1 = "Local Variable (shares same name as a global variable)"
    print("\nINSIDE THE FUNCTION")
    print(message1)

# Calling the function
myFunction()

# Printing message1 OUTSIDE the function
print("\nOUTSIDE THE FUNCTION")
print(message1)

# Importing Modules
# Python comes with a lot of built-in functions which are stored in files called modules.

import random as r   # you could use just random or import random as r.
print(r.randrange(1, 10))

'''The third way to import modules is to import specific functions from
the module by writing
from moduleName import name1[, name2[, ...
nameN]].'''

from random import randrange, randint
print(randrange(1, 10))
print(randint(11, 20))

# Creating our Own Module

