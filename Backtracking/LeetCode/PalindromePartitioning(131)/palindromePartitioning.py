def isPalindrome(string, low, high):
    while low < high:
        if string[low] != string[high]:
            return False
        low, high = low + 1, high - 1
    
    return True

def partition(string: str, i, res: list, part: list):

    #se l'indice della stringa è arrivato alla fine
    if i >= len(string):
        res.append(part[:]) #aggiungiamo la partizione corrente a res
        return #e ritorniamo

    temp = [] #Per inserire la sottostringa temporanea
    for j in range(i, len(string)):
        temp = string[i:j+1]
        #print("temp:",temp)

        if(isPalindrome(temp, 0, len(temp)-1)):

            part.append(temp)
            #print("part",part)

            partition(string, j+1, res, part)

            #Backtrack
            part.pop()
            #print("part",part)

def readTestFile(path):

    file = open(path)

    testsList = []

    for line in file:
        testsList.append(line.strip())
    
    return testsList
        

if __name__ == "__main__":

    res = [] #per inserire tutte le partizioni
    part = [] #lista della partizione corrente

    testsList = readTestFile("./test_file.txt")

    for test in testsList:

        string = test

        partition(string, 0, res, part)

        print(res)

        res.clear()

