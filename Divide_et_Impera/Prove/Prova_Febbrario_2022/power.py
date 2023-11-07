#Time Complexity: O(log n)
def power(x, y):

    temp = 0
    if y == 0:
        return 1
    
    temp = power(x, y//2)
    if y%2 == 0:
        return temp * temp
    else:
        return x*temp*temp
    
def readTestFile(path):

    file = open(path, 'r')

    testsList = []

    for line in file:

        testsList.append([int(x) for x in line.split(' ')])

    return testsList

if __name__ == "__main__":

    testsList = readTestFile("./test_file.txt")

    for test in testsList:

        x = test[0]
        y = test[1]

        result = power(x, y)
        print(result)
