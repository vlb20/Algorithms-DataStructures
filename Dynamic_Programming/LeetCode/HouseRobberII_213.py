#O(n) - Bottom Up
def rob2(houseval, n):
    if n == 0: # se non ci sono case
        return 0 # il bottino massimo è 0
    if n == 1: # se c'è solo una casa
        return houseval[0] # il bottino massimo è il valore di quella casa
    if n == 2: # se ci sono 2 case
        return max(houseval[0], houseval[1]) # max bottino -> max val tra 2 case

    # Calcola il massimo bottino per tutte le case tranne l'ultima
    dp1 = [0]*n
    dp1[0] = houseval[0]
    dp1[1] = max(houseval[0], houseval[1])
    for i in range(2, n-1):
        dp1[i] = max(houseval[i]+dp1[i-2], dp1[i-1])

    # Calcola il massimo bottino per tutte le case tranne la prima
    dp2 = [0]*n
    dp2[1] = houseval[1]
    for i in range(2, n):
        dp2[i] = max(houseval[i]+dp2[i-2], dp2[i-1])

    # Il massimo bottino è il massimo dei due casi
    return max(dp1[-2], dp2[-1])

if __name__ == "__main__":
	
    T = int(input("Inserisci il numero di casi di test: "))
    for _ in range(T):
        n = int(input("Inserisci il numero di case: "))
        houseval = []
        for i in range(n):
            houseval.append(int(input("Inserisci il valore della casa {}: ".format(i+1))))
				
        maxGuad = rob2(houseval, n)
        print("Il guadagno massimo è: ", maxGuad)