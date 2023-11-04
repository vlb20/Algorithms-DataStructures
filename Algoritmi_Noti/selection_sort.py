#Time Complexity: O(N^2)
def selectionSort(array):

    N = len(array)

    for i in range(N):
        
        min_index = i #indice del valore minimo non ordinato

        for j in range(i+1, N): #ricerca del minimo
            #seleziona il minimo elemento ad ogni iterazione
            if array[j] < array[min_index]:
                min_index = j
            
        #swap degli elementi per ordintare l'array
        (array[i], array[min_index]) = (array[min_index], array[i])

if __name__ == "__main__":

    array = [40, 30, -2, 20, 18, 35, 89]
    selectionSort(array)
    print(array)
