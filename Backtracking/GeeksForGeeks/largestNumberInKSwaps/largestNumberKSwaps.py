def findLargestNumberKSwaps(string, K, maxstring, curr):

    N = len(string)#dimensione della stringa

    #se ho finito gli scambi o sono arrivato alla fine della stringa ritorno
    if K==0 or curr==N:
        return maxstring

    #pongo come numero massimo l'elemento corrente della stringa
    #per confrontarlo in seguito
    maxnum = string[curr]

    for i in range(curr+1, N):

        #aggiorno il massimo numero, scorrendo la lista
        if int(string[i]) > int(maxnum):
            maxnum = string[i]
    
    #se il massimo numero non si trova davanti
    if(maxnum != string[curr]):
        K=K-1 #diminuisco gli scambi perchè effettuerò lo swap in seguito

    for i in range(curr, N):

        #quando arrivo al maxnum
        if(string[i] == maxnum):

            #swappo il maxnum con l'indice corrente(lo metto daventi)
            string[curr], string[i] = string[i], string[curr]
            new_str = "".join(string)

            #se la nuova stringa è maggiore della stringa massima
            if int(new_str) > int(maxstring[0]):
                maxstring[0] = new_str #la aggiorno
            
            #richiamo ricorsivamente sull'elemento successivo
            findLargestNumberKSwaps(string, K, maxstring, curr+1)

            #BACKTRACK - altrimenti riscambio le posizioni
            string[curr], string[i] = string[i], string[curr]


if __name__ == "__main__":

    with open("./test_file.txt") as file:

        num_test = int(file.readline())

        while num_test > 0:

            K = int(file.readline())
            
            array = file.readline().strip()
            print(array)

            string = [char for char in array]
            print(string)

            maxstring = [array]
            print(maxstring)

            findLargestNumberKSwaps(string, K, maxstring, 0)
            print(maxstring[0])

            num_test -= 1