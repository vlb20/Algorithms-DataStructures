#Time complexity: O(N * N!)
# Ci sono N! permutazioni e richiede O(N) per stampare una permutazione

def permute(string, l, r):

    if l==r: #l è stato incrementato fino alla fine della stringa
        print(''.join(string)) #converto la lista di caratter in una stringa e la stampo
    else:
        for i in range(l, r):
            string[l], string[i] = string[i], string[l]
            permute(string, l+1, r)
            string[l], string[i] = string[l], string[i] #riscambio (backtrack)

def readTestFile(path):

    file = open(path, 'r')

    testsList = []

    for line in file:
        testsList.append(line.strip())

    return testsList

if __name__ == "__main__":

    testsList = readTestFile(path="./test_file.txt")

    for test in testsList:
        string = list(test)
        permute(string, 0, len(string))