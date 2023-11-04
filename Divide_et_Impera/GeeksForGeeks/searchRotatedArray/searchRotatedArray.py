def binarySearch(array, start, end , key):

    if end<start:
        return -1
    
    mid = start + (end - start) //2
    
    if key == array[mid]:
        return mid
    
    if key > array[mid]:
        return binarySearch(array, (mid+1), end, key)
    return binarySearch(array, start, (mid-1), key)

#Funzione per ottenere il pivot.
#Per un array 3,4,5,6,1,2 -> ritorna 3 (indice di 6)
#dove è avvenuta la rotazione
def findPivot(array, start, end):

    #casi basi
    if end<start:
        return -1
    if end==start:
        return start
    
    mid = start + (end - start) //2

    if mid < end and array[mid]>array[mid+1]:
        return mid
    if mid > start and array[mid]<array[mid-1]:
        return (mid-1)
    
    if array[start] >= array[mid]:
        return findPivot(array, start, mid-1)
    return findPivot(array, mid+1, end)


def findIndexKey(N, array, key):

    pivot = findPivot(array, 0, N-1)

    #se non abbiamo trovato un pivot
    #l'array non è ruotato
    if pivot == -1:
        return binarySearch(array, 0, N-1, key)
    
    #Se troviamo un pivot,
    #prima compariamo la chiave con il pivot
    #e poi ricerchiamo nei due sottoarray attorno al pivot
    if array[pivot] == key:
        return pivot
    if array[0] <= key:
        return binarySearch(array, 0, pivot-1, key)
    return binarySearch(array, pivot+1, N-1, key)

def readTestFile(path):

    file = open(path, 'r')

    testList = []

    for line in file:

        testList.append([int(x) for x in line.split(' ')])
    
    return testList

if __name__ == "__main__":

    testsList = readTestFile(path="./test_file.txt")

    for test in testsList:

        N = test[0]
        key = test[1]
        array = test[2:]
        result = findIndexKey(N, array, key)
        print(result)
        


