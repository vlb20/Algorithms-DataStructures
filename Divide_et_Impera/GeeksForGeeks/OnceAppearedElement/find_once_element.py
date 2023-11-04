def findOnceElement(array, start, end):

    if end<start:
        return -1
    
    if start==end:
        return array[start]

    mid = start + (end-start)//2

    #se mid è pari e l'elemento successivo è uguale
    #significa che c'è una discontinuità a destra
    #quindi bisogna cercare nella restante parte destra
    #ex: 112233445 mid=4 ma array[mid]=3 ==array[mid+1]==3 -> 5 è a destra
    if mid%2==0:
        if array[mid] == array[mid+1]:
            return findOnceElement(array, mid+2, end)
        else:
            return findOnceElement(array, start, mid)
    
    else:
        if array[mid]==array[mid-1]:#nessuna discontinuità a sinistra
            return findOnceElement(array, mid+1, end)
        else:
            return findOnceElement(array, start, mid-1)


def readTestFile(path):

    file = open(path, 'r')

    testsList = []

    for line in file:
        testsList.append([int(x) for x in line.split(' ')])

    return testsList

if __name__ == "__main__":

    testsList = readTestFile(path="./test_file.txt")

    for test in testsList:
        array = test[0:]
        result = findOnceElement(array, 0, len(array)-1)
        print(result)