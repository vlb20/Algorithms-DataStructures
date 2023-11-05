#Time Complexity: O(N)
def isJolly(array, N):

    #Creo un vettore booleano a False
    #per raggruppare il set di differenze trovate
    #lungo N perchè dobbiamo trovare tutto l'intervallo [1;N-1]
    differenze = [False] * N

    #Scorro tutti gli elementi del vettore
    for i in range(0, N-1):

        #Trovo la differenza assoluta tra
        #i 2 elementi adiacenti
        absDiff = abs(array[i] - array[i+1])

        #Se la differenza è fuori dall'intervallo [1;N-1]
        #Oppure è ripetuta (devono essere uniche)
        #ritorniamo falso
        if (absDiff == 0 or absDiff>N-1 or differenze[absDiff] == True):
            return False
        
        #Lo inseriamo nel vettore ponendo a true il flag al suo indice
        differenze[absDiff] = True

    return True

def readTestFile(path):

    file = open(path, 'r')

    testsList = []

    for line in file:

        testsList.append([int(x) for x in line.split(' ')])
    
    return testsList

if __name__ == "__main__":
        
    testsList = readTestFile("./test_file.txt")

    for test in testsList:

        array = test[0:]
        
        result = isJolly(array, len(array))

        if result == True:
            print("Jolly")
        else:
            print("Not Jolly")

