#O(nlogn)
def countOccurences(array, start, end, K):

    if start==end: #array con un elemento
        return int(array[start] == K) #se l'elemento è uguale a K restituisce 1
    
    if(end > start):

        mid = start + (end - start) //2

        c1 = countOccurences(array, start, mid, K)
        c2 = countOccurences(array, mid+1, end, K)

        return c1+c2

def readTestFile(testFilePath):

    file = open(testFilePath, "r")

    testNumber = int(file.readline())

    testsList = []
    
    for i in range(testNumber+1):
        line = file.readline()
        testsList.append([int(x) for x in line.split(' ')])
        #Questo comando divide la stringa line in una lista di sottostringhe
        # ogni volta che incontra uno spazio. Ad esempio, se line è "1 2 3", allora line.split(' ') restituirà ['1', '2', '3'].
        # list comprehension che prende la lista di sottostringhe (come ['1', '2', '3']) e applica la funzione int(x) a ciascuna sottostringa per convertirla in un intero. 
        # Quindi, se la lista di input è ['1', '2', '3'], allora l’output sarà [1, 2, 3].
        # Aggiungiamo infine la lista di interi appena creata alla fine della lista testsList.

    return (testNumber, testsList)

if __name__ == "__main__":

    testNumber, testList = readTestFile(testFilePath="./test_file.txt")
    
    for test in testList:
        valueToCount = test[0]
        valueListToCheck = test[1:]
        numberOfOccurences = countOccurences(valueListToCheck, 0, len(valueListToCheck) - 1, valueToCount)
        print(numberOfOccurences)