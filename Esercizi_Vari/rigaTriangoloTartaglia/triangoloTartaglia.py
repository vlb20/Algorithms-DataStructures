#Time complexity: O(n^2)
def printRowTartaglia(nrow):

    currRow = []

    #Il primo elemento di ogni riga è sempre 1
    currRow.append(1)

    #Controlliamo che la riga da ritornare
    #sia la prima del triangolo
    if nrow == 0:
        return currRow

    #ricorsivamente genero la riga precedente
    #per ricavarmi la successiva
    precRow = printRowTartaglia(nrow - 1)

    #scorro la prima riga dal secondo elemento alla fine
    for i in range(1, len(precRow)):

        #sommiamo sempre a 2 a 2 gli elementi per
        #generare quelli correnti
        curr_num = precRow[i-1] + precRow[i]
        currRow.append(curr_num)

    #l'ultimo elemento di ogni riga è sempre 1
    currRow.append(1)

    return currRow

if __name__ == "__main__":

    with open("./test_file.txt") as file:

        while(True):

            nrow = int(file.readline())

            if nrow == 0:
                break

            currRow = printRowTartaglia(nrow)

            for i in range(len(currRow)):
                print(currRow[i], end=" ")
            print()

