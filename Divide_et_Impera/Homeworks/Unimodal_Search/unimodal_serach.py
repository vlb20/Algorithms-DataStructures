def unimodalSearch(array, start, end):

    if end < start:
        return -1

    if end == start:
        return array[start]
    
    mid = start + (end - start) //2

    if array[mid] > array[mid-1] and array[mid] > array[mid+1]:
        return array[mid]
    
    if array[mid]<array[mid-1] and array[mid] > array[mid+1]:
        #ci troviamo nella parte decrescente dell'array
        return unimodalSearch(array, start, mid-1)
    else:
        return unimodalSearch(array, mid+1, end)

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
        result = unimodalSearch(array, 0, len(array)-1)
        print(result)
        
