#Time complexity: O(N log N)
def findOptimalDistance(array:list, N):

    #ordino l'array
    array.sort()

    #prendo la mediana poichè minimizza le distanze
    if(N%2==0): #se il numero di elementi è pari -> media dei 2 elementi al centro
        mediana = (array[N//2 - 1] + array[N//2])//2
    else:#se il numero di elementi è dispari
        mediana = array[N//2] #elemento centrale

    min_sum = 0
    #per ogni posizione calcolo la distanza dalla mediana
    #e la sommo
    for i in range (0, N):
        min_sum += abs(mediana - array[i])

    return min_sum

def readTestFile(path):

    file = open(path, 'r')

    num_test = int(file.readline())

    testsList = []

    for line in file:

        testsList.append([int(x) for x in line.split(' ')])
    
    return testsList

if __name__ == "__main__":

    testsList = readTestFile("./test_file.txt")

    for test in testsList:

        N = test[0]
        array = test[1:]

        result = findOptimalDistance(array, N)

        print(result)