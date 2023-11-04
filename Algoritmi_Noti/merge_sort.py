#Time Complexity: O(n*log n)
def merge(array, p, q, r):
    
    n1 = q-p+1
    n2 = r-q

    #creo gli array temporanei
    #array[p..q]
    L = [0] * (n1) #lista di lunghezza n1 inizializzata a 0
    #array[q+1..r]
    R = [0] * (n2)

    #copio i dati negli array temporanei
    for i in range(0, n1):
        L[i] = array[p+i]

    for j in range(0, n2):
        R[j] = array[q+1+j]
    
    #Merge degli array temporanei nell'array[p...r]
    i = 0 #Indice iniziale del primo sottoarray
    j = 0 #Indice iniziale del secondo sottoarray
    k = p #Indice iniziale del sottoarray merged

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    
    #Copio i restanti elementi di L[], se rimasti
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    
    #Copio i restanti elementi di R[], se rimasti
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1

def mergeSort(array, p, r):

    if p < r:

        q = p + (r - p) //2 #equivalente a (p+r)//2 ma evitiamo overflow

        mergeSort(array, p, q)
        mergeSort(array, q+1, r)
        merge(array, p, q, r)

if __name__ == "__main__":

    array = [20, 10, 15, 5, 30]

    mergeSort(array, 0, len(array)-1)

    print(array)
