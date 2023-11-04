def longestCommonPrefix(str1, str2): #prendo 2 stringhe in input da comparare

    result = ""

    minLenght = min(len(str1), len(str2))

    i = 0

    while i < minLenght: #scorro fintantochè non arrivo alla fine della stringa più corta

        if str1[i]!=str2[i]:#esco dal while appena un carattere non corrisponde
            break

        result += str1[i]
        i = i+1
    
    return result #restituisco il prefisso comune più lungo

def findLCP(array, start, end): #approccio divide et impera (in input do l'array di test, indice iniziale e finale dell'array di strighe)

    if start == end: #c'è solo una stringa nell'array
        return array[start] #restituisco la stringa come prefisso comune più lungo
    
    if(end > start): #se ci sono almeno 2 stringhe nell'array

        # modo sicuro per calcolare il punto medio dell'array
        # evitando un possibile overflow di intero
        mid = start + (end - start) // 2 #// divisione intera

        str1 = findLCP(array, start, mid) #Chiamiamo la funzione ricorsivamente per prima metà dell’array
        str2 = findLCP(array, mid+1, end) #Chiamiamo la funzione ricorsivamente per la seconda metà dell’array

        return longestCommonPrefix(str1, str2) #Troviamo il prefisso comune più lungo per le 2 stringhe
    
    return "" #se nessuna delle condizioni precedenti è soddisfatta -> restituiamo una stringa vuota

def readTest(path):

    testFile = open(path)

    testList = []   #lista per memorizzare i test case letti da file

    numeroTestCase = int(testFile.readline()) #leggo il numero di test

    tempList = []   #lista per memorizzare le stringhe di un singolo test case.

    for line in testFile:       #leggo una alla volta ogni riga del file
        if line.strip() == "END": #se la riga contiene "END" (con strip rimuovo gli spazi all'inizio e alla fine) significa che è la fine di un test case
            testList.append(tempList)   #aggiungo la lista del singolo test case alla lista dei test case
            tempList = []   #svuoto la lista temporanea del singolo test case
        else:
            tempList.append(line.strip())   #aggiungo la riga a tempList
    
    return testList
        

if __name__ == "__main__":

    testList = readTest("./testCases.txt")

    for test in testList: #per ogni test case
        result = findLCP(test, 0, len(test) -1) #trovo il prefisso comune più lungo
        print(result)


