def checkIfPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if 0 == numberToCheck % x:
            return False
    return True