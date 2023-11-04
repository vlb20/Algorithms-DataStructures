#Time Complexity: O(N^2)
def insertionSort(array):

    n = len(array)

    #se l'array ha 0 o 1 elementi, è già ordinato
    if n<=1:
        return

    #itero partendo dal secondo elemento (j=1)
    for j in range(1, n):

        #elemento corrente che sto cercando di inserire nel
        #sottoinsieme ordinato
        key = array[j]

        #inizializzazione dell'indice per la parte ordinata del vettore ->
		#vado verso sinistra
        i = j-1

        #finchè non raggiungiamo l'inizio del vettore
        #o non abbiamo trovato un elemento più grande di key
        while(i>=0 and array[i]>key):

            #l'elemento più grande lo spostiamo avanti nel vettore
            array[i+1] = array[i] #shift degli elementi a destra

            #decrementiamo l'indice per passare all'elemento precedente del vettore
            i -= 1
        
        #Abbiamo trovato la posizione corretta per key -> lo inseriamo
        array[i+1] = key

if __name__ == "__main__":
    
    array = [20, 10, 5, 7, 8]
    insertionSort(array)
    print(array)