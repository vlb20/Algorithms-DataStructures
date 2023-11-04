import math

set = [] #vettore per salvare gli N candidati con somma S
numeriPrimi = [] #vettore per i candidati(>P e <S)

#funzione per controllare che un numero sia primo
def isPrimo(x):

    #radice quadrata di x -> poichè possiamo limitare i numeri
	#che controlliamo alla radice quadrata di x (per maggior efficienza)
    sqroot_x = int(math.sqrt(x))

    #visto che 1 non è un numero primo
    if(x == 1):
        return False
    
    #se troviamo un numero per cui x è divisibile -> non è primo
    for i in range(2, sqroot_x+1):
        if(x % i == 0):
            return False
    
    return True

#funzione per stampare gli N numeri primi la cui somma è uguale a S
# cioè per stampare la SOLUZIONE
def stampaPrimi():

    global set, numeriPrimi
    lenght = len(set)
    for i in range(0, lenght):
        print (set[i], end = " ")
    print()

#funzione per calcolare tutti i possibili N numeri primi
#la cui somma è pari a S (tutti i possibili subsets)
def generaSommaPrimi(currentSum, N, S, index):

    global set, numeriPrimi

    #se la somma corrente totale è uguale a S
    #e il numero di elementi del set è pari a N
    #abbiamo trovato la SOLUZIONE
    if(currentSum == S and len(set) == N):
        #stampo gli N primi -> soluzione
        stampaPrimi()
        return
    
    #se invece la somma corrente totale è maggiore di S
    # oppure l'indice ha raggiunto l'ultimo elemento dei candidati
    #significa che NON C'E' SOLUZIONE
    if(currentSum > S or index == len(numeriPrimi)):
        return
    
    #aggiungo il candidato corrente al set
    set.append(numeriPrimi[index])

    #Ricorsivamente genero i subsets con l'elemento corrente incluso
    generaSommaPrimi(currentSum + numeriPrimi[index], N, S, index+1)

    #Escludo l'elemento corrente dal subset (backtracking)
    set.pop()

    #Ricorsivamente genero i subset escludendo l'elemnto corrente
    generaSommaPrimi(currentSum, N, S, index+1)


# funzione per generare tutti i primi >P e <S (candidati)
def allPrimi(N, S, P):

    global set, numeriPrimi

    #genero tutti i primi maggiori di P e minore di S
    for i in range(P+1, S+1):

        #se i è primo lo aggiungo al vettore dei numeri primi
        if(isPrimo(i)):
            numeriPrimi.append(i)

    #Abbiamo trovato i possibili candidati

    #se i primi sono minori di N -> non esiste soluzione
    if(len(numeriPrimi) < N):
        return
    
    #Altrimenti vediamo gli N che soddisfano la somma S
    generaSommaPrimi(0, N, S, 0)

def readTestFile(path):

    file = open(path, "r")

    testsList = []

    for row in file:
        testsList.append([int(x) for x in row.split(' ')])

    return testsList

if __name__ == "__main__":

    testsList = readTestFile(path="./test_file.txt")
    counter = 0
    for test in testsList:
        counter = counter+1
        print("CASO DI TEST " + str(counter))
        S = test[0]
        N = test[1]
        P = test[2]
        allPrimi(N, S, P)
        #resetto lo stato del programma per il prossimo test
        set.clear()
        numeriPrimi.clear()
    