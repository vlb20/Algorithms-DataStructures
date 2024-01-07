#O(n) - R&M - è necessaria solo una traversata dell'array originale
def maxLoot(houseval, n, dp):
	
		#caso base
		if(n < 0):
				return 0
		
		if(n == 0):
				return houseval[0]

		#se il sottoproblema è stato già risolto
		#ritorna il suo valore
		if(dp[n] != -1):
				return dp[n]

		#se la casa corrente viene rapinata, quella precedente non può essere rapinata
		pick = houseval[n] + maxLoot(houseval, n-2, dp)
	
		#se la casa corrente non viene rapinata allora quella precedente può essere rapinata
		notPick = maxLoot(houseval, n-1, dp)
	
		#ritorniamo il max di picked e not picked
		dp[n] = max(pick, notPick)
		return dp[n]

if __name__ == "__main__":
	
    T = int(input("Inserisci il numero di casi di test: "))
    for _ in range(T):
        n = int(input("Inserisci il numero di case: "))
        houseval = []
        for i in range(n):
            houseval.append(int(input("Inserisci il valore della casa {}: ".format(i+1))))
				
        dp = [-1 for i in range(n+1)]
        maxGuad = maxLoot(houseval, n, dp)
        print("Il guadagno massimo è: ", maxGuad)

# ------------------------------------------------------------------------------------------------------- #

#O(n) - Bottom Up
def maximize_loot(houseval, n):
		if n == 0: #se non ci sono case
				return 0 #il bottino massimo è 0
		if n == 1: #se c'è solo una casa
				return houseval[0] #il bottino massimo è il valore di quella casa
		if n == 2: #se ci sono 2 case
				return max(houseval[0], houseval[1]) #max bottino -> max val tra 2 case

		#dp[i] rappresenta il massimo valore rapinato avendo raggiunto la casa i-esima
		dp = [0]*n
		
		dp[0] = houseval[0]  ## Il bottino massimo per la prima casa è il suo valore
		# Il bottino massimo per la seconda casa è il valore massimo tra la prima e la seconda
		dp[1] = max(houseval[0], houseval[1])

		# Per ogni casa successiva, abbiamo due opzioni:
		# 1. Rapinare la casa corrente e aggiungere il suo valore al bottino massimo ottenuto fino alla casa i-2
		# 2. Non rapinare la casa corrente e mantenere il bottino massimo ottenuto fino alla casa i-1
		# Scegliamo l'opzione che massimizza il bottino
		for i in range(2, n):
				dp[i] = max(houseval[i]+dp[i-2], dp[i-1])
		# Alla fine, dp[n-1] conterrà il bottino massimo che può essere ottenuto
		return dp[-1]

if __name__ == "__main__":
	
    T = int(input("Inserisci il numero di casi di test: "))
    for _ in range(T):
        n = int(input("Inserisci il numero di case: "))
        houseval = []
        for i in range(n):
            houseval.append(int(input("Inserisci il valore della casa {}: ".format(i+1))))
				
        maxGuad = maxLoot(houseval, n)
        print("Il guadagno massimo è: ", maxGuad)