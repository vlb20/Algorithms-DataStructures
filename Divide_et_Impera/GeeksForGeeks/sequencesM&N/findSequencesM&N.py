def findSequencesM_N(m,n):

    if m<n:
        return 0
    
    if n==0:
        return 1
    
    result = (findSequencesM_N(m-1,n) + findSequencesM_N(m//2,n-1))
    return result

def readTestFile(path):

    file = open(path, 'r')

    testsList = []

    for line in file:

        testsList.append([int(x) for x in line.split(' ')])

    return testsList

if __name__ == "__main__":

    testsList = readTestFile(path="./test_file.txt")

    for test in testsList:

        m = test[0]
        n = test[1]
        result = findSequencesM_N(m,n)
        print(result)