#Time Complexity: O(log n)
def findMissingUtil(array, low, high, diff):

    while low <= high:

        #troviamo l'indice dell'elemento mediano
        mid = low + (high - low) //2

        #[1, 3, 5, 7, 11] -> mid=2 array[mid]=5
        #if (5-1)/2=2 (== mid) allora l'elemento mancante
        #sarà nella metà destra dell'array
        if(array[mid]-array[0])//diff == mid:
            low = mid + 1
        else: #sarà nella metà sinistra
            high = mid - 1

    #Usciamo dal loop quando low > high
    #dunque il nostro elemento sarà ad:
    return array[high] + diff

def findMissing(array, n):

    #Se manca esattamente 1 elemento, possiamo
    #trovare il passo della progrssione con la seguente formula.
    #Ex: [1, 3, 5, 7, 11] -> diff= (11-1)//5 =2
    diff = (array[n-1] - array[0])//n

    return findMissingUtil(array, 0, n-1, diff)

if __name__ == "__main__":

    with open("./test_file.txt") as file:

        num_test = int(file.readline().strip())

        while num_test > 0:

            n = int(file.readline().strip())

            data = file.readline().strip().split()
            array = [int(x) for x in data]

            result = findMissing(array, n)
            print(result)

            num_test -= 1

