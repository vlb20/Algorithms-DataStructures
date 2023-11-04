def merge(array, start, mid, end):

    #liste per memorizzare i due sotto-array da fondere
    leftElements = []
    rightElements = []

    for i in range(mid - start+1): #copio gli elementi da start a mid in leftElements
        leftElements.append(array[start+i])
    for j in range(end - mid):
        rightElements.append(array[mid+1+j])

    inv_count = 0 #per contare il numero di inversioni
    # indici per scorrere le due liste
    i=0
    j=0
    isCounted = False #per garantire che le inversioni vengano contate una sola volta per ogni elemento in rightList

    for k in range(start, end+1): #end+1 perchè vogliamo iterare fino al valore finale incluso
        #se entrambi gli indici non hanno raggiunto la fine delle rispettive liste, confronto gli elementi correnti
        if i < len(leftElements) and j < len(rightElements):

            #se l'elemento in rightElement è minore di quello in left allora...
            if rightElements[j] < leftElements[i] and not isCounted:
                inv_count += len(leftElements) - i #...tutti gli elementi rimanenti in leftElement sono maggiori dell'elemento corrente in rightElements
                #dunque vengono aggiunte al conteggio
                isCounted = True #le inversioni per l'elemento corrente in rightElement sono state contate
            
            #aggiungo all'array l'elemento più piccolo e incremento il rispettivo indice
            if leftElements[i] <= rightElements[j]:
                array[k] = leftElements[i]
                i = i+1
            else:
                array[k] = rightElements[j]
                j = j+1
                isCounted = False #le inversioni per il prossimo elemento in rightElements non sono state ancora contate
        
        else: #se uno degli indici ha raggiunto la fine della lista
            #copio il resto dell'altra lista nell'array

            if i <len(leftElements):
                array[k] = leftElements[i]
                i = i+1
            else:
                array[k] = rightElements[j]
                j = j+1

    return inv_count

def sortInvCount(array, start, end):

    inv_count = 0 #variabile per tenere traccia del numero di inversioni

    if start < end: #se ci sono almeno due elementi nell'array
        
        # modo sicuro per calcolare il punto medio dell'array
        # evitando un possibile overflow di intero
        mid = start + (end - start) // 2 #// divisione intera

        inv_count += sortInvCount(array, start, mid) # calcola ricorsivamente il numero di inversioni nella prima metà dell’array
        inv_count += sortInvCount(array, mid+1, end) # calcola ricorsivamente il numero di inversioni nella seconda metà dell’array
        inv_count += merge(array, start, mid, end) #fonde le due metà dell’array in un unico array ordinato e conta il numero di inversioni tra le due metà

    return inv_count
    
def readTest(path):

    testFile = open(path)

    testList = [] #lista per memorizzare tutti i test case
    tempList = [] #lista per memorizzare temporaneamente ciascun test case

    sizeOfSequence = 0 #variabile usata per tenere traccia del numero di elementi rimanenti nel test case corrente
    newTestCase = True #flag per indicare l'inizio di un nuovo test case

    for line in testFile:
        if newTestCase: #se il flag è vero la riga contiene la dimensione del prossimo test case
            sizeOfSequence = int(line) #la assegno castandola ad intero
            newTestCase = False
        else:
            tempList.append(int(line))
            sizeOfSequence -= 1
            if sizeOfSequence == 0: #quando finisco il numero di elementi del test case
                testList.append(tempList) #aggiungiamo la lista del singolo test case a quella di tutti i test case
                tempList = [] #svuoto la lista temporanea
                newTestCase = True #indico che la prossima riga rappresenterà l'inizio di un nuovo testcase

    return testList

if __name__ == "__main__":

    testList = readTest("./testCases1.txt")

    for test in testList:

        inv_count = sortInvCount(test, 0, len(test)-1)
        print(inv_count)
