# importing modules

from random import randint
from os import remove, rename

# The following function is for getting the user's score

def getUserPoint(userName):
    try:
        input = open('userScores.txt', 'r')
        for line in input:
            content = line.split(',')
            if content[0] == userName:
                input.close()
                return content[1]
            input.close()
            return "-1"
    except IOError:
        print("\nFile userScores.txt not found. A new file will be created.")
        input = open('userScores.txt', 'w')
        input.close()
        return "-1"

# updating the user's score

def updateUserPoints(newUser, userName, score):
    if newUser:
        input = open('userScores.txt', 'a')
        input.write('\n' + userName + ',' + score)
        input.close()
    else:
        input = open('userScores.txt', 'r')
        output = open('userScores.tmp', 'w')
    for line in input:
        content = line.split(',')
        if content[0] == userName:
            content[1] = score
            line = content[0] + ', ' + content[1] + '\n'
        output.write(line)
    input.close()
    output.close()

    remove('userScore.txt')
    rename('userScores.tmp', 'userScores.txt')

# Generating the questions

def generateQuestion():
    operandList = [0, 0, 0, 0, 0]
    operatorList = ['', '', '', '']
    operatorDict = {1: ' + ', 2: ' - ', 3: '*', 4: '**'}

# Updating operandList with Random Numbers

    for index in range(0, 5):
        operandList = randint(1, 9)

    for index in range(0, 4):
        if index > 0 and operatorList[index-1] != '**':

# The problem is, when we have two consecutive exponent operators in Python, such as 2**3**2,
# Python interprets it as 2**(3**2) instead of (2**3)**2. In the first case, the answer is 2 to the
# power of 9 (i.e. 29) which is 512. In the second case, the answer is 8 to the power of 2 (i.e. 82)
# which is 64. Hence when we present a question like 2**3**2, the user will get the answer wrong if he interprets it as (2**3)**2.

            operator = operatorDict[randint(1, 4)]
        else:
            operator = operatorDict[randint(1, 3)]
        operatorList[index] = operator
    questionString = str(operatorList[0])
    for index in range(1, 5):
        questionString = questionString + operatorList[index-1] + str(operatorList[index])
    result = eval(questionString)
    questionString =questionString.replace("**", "^")

    print('\n' + questionString)

    userResult = input('Answer: ')

    while True:
        try:
            if int(userResult) == result:
                print("So Smart")
                return 1
            else:
                print("Sorry, wrong answer. The correct answer is", result)
                return 0
        except Exception as e:
            print("You did not enter a number. Please try again.")
            userResult = input('Answer: ')