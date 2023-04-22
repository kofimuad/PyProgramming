try:

    import myPythonFunctions as m
    
    userName = input('''Please enter your user name or 
    create a new one if this is the first time you are running this program: ''')

    userScore = int(m.getUserPoint(userName))

    if userScore == -1:
        newUser = True
        userScore = 0
    else:
        newUser = False
    
    userChoice = 0

    while userChoice != '-1':

        userScore += m.generateQuestion()
    print("Current Score = ", userScore)
    userChoice = input("Press Enter to Continue or -1 to Exit: ")

    m.updateUserPoints(newUser, userName, str(userScore))

except Exception as e:
    print("An unexpected error occured. Program will be exited.")