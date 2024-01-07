#O(n) - Bottom Up
def minimumCost(cost, n):
	
		#array per le soluzioni
		dp = [None]*n
		
		#base case
		if n == 1:
				return cost[0]
		
		#si può iniziare o dal primo o dal secondo gradino
		dp[0] = cost[0]
		dp[1] = cost[1]
	
		# Per ogni gradino successivo, il costo minimo per raggiungere quel gradino 
		#è il minimo tra il costo per raggiungere il gradino precedente 
		#e il costo per raggiungere il gradino due gradini prima, 
		#più il costo del gradino corrente.
		for i in range(2, n):
			dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
	
		#Infine, il costo minimo per raggiungere l'ultimo gradino è il minimo tra 
		#il costo per raggiungere l'ultimo gradino e il costo per raggiungere il penultimo.	
		return min(dp[n-2], dp[n-1])

if __name__ == "__main__":
	
    T = int(input("Inserisci il numero di casi di test: "))
    for _ in range(T):
        n = int(input("Inserisci il numero di gradini: "))
        cost = []
        for i in range(n):
            cost.append(int(input("Inserisci il costo del gradino {}: ".format(i+1))))

        min_cost = minimumCost(cost, n)
        print("Il costo minimo per raggiungere l'ultimo gradino è: ", min_cost)