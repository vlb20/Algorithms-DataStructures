#Time Complexity: Worst O(N^2) Average O(N log N)

def partition(array, low, high):

    #scelgo l'ultimo elemento dell'array come pivot
    pivot = array[high]

    i = low-1

    #scorro tutti gli elementi del vettore
    #e li comparo con il pivot
    for j in range(low, high):

        if array[j] <= pivot:

            #se troviamo un elemento più piccolo
            #del pivot -> lo scambiamo con l'elemento
            #più grande puntato da i
            i += 1

            #swap
            (array[i], array[j]) = (array[j], array[i])

    #scambio il pivo con l'elemento più grande puntato da i
    #(lo metto in mezzo)
    (array[i+1], array[high]) = (array[high], array[i+1])

    #ritorno l'indice del pivot
    return i+1

def quickSort(array, low, high):

    if low<high:
        
        #Cerco il pivot tale che
        #gli elementi più piccoli del pivot sono alla sua sinistra
        #gli elementi più grandi del pivot sono alla sua destra
        pivot = partition(array, low, high)

        quickSort(array, low, pivot-1)

        quickSort(array, pivot+1, high)

if __name__ == "__main__":

    array = [20, 30, 12, 7, 29, 31]

    N = len(array)

    quickSort(array, 0, N-1)

    print(array)