#recursive binary search
#Time complexity: O(log n)
def binary_search(array, low, high, x):

    #Controllo del caso base
    if high >= low:

        mid = (high + low) // 2

        #se l'elemento è presente in mid -> ritorno mid
        if array[mid] == x:
            return mid
        
        #Se l'elemento è più piccolo di mid
        #allora sarà nel sottoarray di sinistra
        elif array[mid] > x:
            return binary_search(array, low, mid-1, x)

        #altrimenti sarà nel sottoarray di destra
        else:
            return binary_search(array, mid+1, high, x)
        
    else:
        #l'elemento non è presente nell'array
        return -1
    
#driver
if __name__ == "__main__":

    array = [1,4,8,20,25]
    x = 20

    res = binary_search(array, 0, len(array)-1, x)

    if res != -1:
        print("L'elemento e' presente all'indice (0-based index):", str(res))
    else:
        print("L'elemento non e' presente nell'array")