def maxSommaSubarray(array):

    lenght = len(array)

    max_curr_sum = 0
    max_glob_sum = -100000000000

    for i in range(0, lenght):

        max_curr_sum = max_curr_sum + array[i]
        
        if(max_curr_sum > max_glob_sum):
            max_glob_sum = max_curr_sum

        if(max_curr_sum < 0):
            max_curr_sum = 0
        
    return max_glob_sum

def readTestFile(path):

    file = open(path, "r")

    testsList = []

    for line in file:
        if line.strip() == "END":
            break
        testsList.append([int(x) for x in line.split(' ')])
    
    return testsList

if __name__ == "__main__":

    testsList = readTestFile(path="./test_file.txt")

    for test in testsList:
        array = test[:]
        maxSum = maxSommaSubarray(array)
        print(maxSum)