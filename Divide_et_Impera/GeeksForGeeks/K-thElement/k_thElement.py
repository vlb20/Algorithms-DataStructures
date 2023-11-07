#Time Complexity: O(log n1 + log n2)
def findKthElement(array1, array2, n1, n2, k):

    # se uno degli array ha solo un elemento
    if n1 == 1 or n2 == 1:
        if n2 == 1:  # se array 2 ha un solo elemento
            # scambiamo gli array per fare in modo che array1 sia quello con l'unico elemento
            array2, array1 = array1, array2
            n2 = n1
        if k == 1:  # se cerchiamo il primo elemento
            return min(array1[0], array2[0])  # allora sarà il minimo di uno dei 2 array
        elif k == n2 + 1:  # può accadere solo se entrambi gli array hanno dimensione 1
            # quindi k=2 (altrimenti andiamo out of range -> 0 based index)
            return max(array1[0], array2[0])

        else:  # se non è ne' l'elemento più piccolo nè più grande
            if array2[k - 1] < array1[0]:  # ci sono k-1 elementi più piccolo di k e sicuro più piccoli di array1
                return array2[k - 1]  # k-esimo elemento (0 based index)
            else:
                # ci sono almeno k elementi nei 2 array che combinati sono più piccoli di esso
                return max(array1[0], array2[k - 2])

    # Calcolo i mediani
    mid1 = (n1 - 1) // 2
    mid2 = (n2 - 1) // 2

    # se la somma dei mesiani +1 è minore di k -> k si trova nella metà superiore
    # di uno dei 2 array
    if mid1 + mid2 + 1 < k:
        if array1[mid1] < array2[mid2]:  # elimino la metà inferiore di array1
            return findKthElement(array1[mid1 + 1:], array2, n1 - mid1 - 1, n2, k - mid1 - 1)
        else:  # elimino la metà superiore di array2
            return findKthElement(array1, array2[mid2 + 1:], n1, n2 - mid2 - 1, k - mid2 - 1)

    else:  # k si trova nella metà inferiore di uno dei 2 array
        # Il k esimo elemento non può essere tra array2[mid2+1:n2-1] (elimino metà superiore)
        if array1[mid1] < array2[mid2]:
            return findKthElement(array1, array2[:mid2 + 1], n1, mid2 + 1, k)
        # Il k esimo elemento non può essere tra array1[mid1+1:n1-1] (elimino metà superiore)
        else:
            return findKthElement(array1[:mid1 + 1], array2, mid1 + 1, n2, k)
        

if __name__ == "__main__":

    with open("./test_file.txt") as file:

        num_test = int(file.readline())

        while num_test > 0:

            array1 = []
            array1 = [int(x) for x in file.readline().split(' ')]

            print(array1)

            array2 = []
            array2 = [int(x) for x in file.readline().split(' ')]

            print(array2)

            k = int(file.readline())

            print(k)

            result = findKthElement(array1, array2, len(array1), len(array2), k)

            print(result)


            num_test -= 1