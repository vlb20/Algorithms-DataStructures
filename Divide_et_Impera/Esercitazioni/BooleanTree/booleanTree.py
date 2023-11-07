#O(log n)
def getStoppingNode(depth, lanci, nodeNumber):

    #se siamo ad un nodo foglia, ritorniamo il nodo
    if depth == 1:
        return nodeNumber
    
    if lanci % 2 == 1:#se il numero di lanci è dispari, esploro il sottoalbero di sinistra
        result = getStoppingNode(depth-1, lanci//2 + 1, 2*nodeNumber)
    else: #se il numero di lanci è pari, esploro il sottoalbero di destra
        result = getStoppingNode(depth-1, lanci/2, 2*nodeNumber+1)

    return result

if __name__ == "__main__":

    with open("./test_file.txt") as file:

        num_test = int(file.readline().strip())

        while num_test > 0:

            data = file.readline().strip().split()

            depth = int(data[0])
            lanci = int(data[1])

            result = getStoppingNode(depth, lanci, 1)

            print(result)

            num_test -= 1