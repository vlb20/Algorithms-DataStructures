#O(n) - REC+MEM
def countModi(n, dp):
		
		if (n <= 1): #se c'è solo uno scalino
				return 1 #posso fare solo un passo

		if(dp[n] != -1): #se la soluzione per raggiungere l'n-esimo scalino è stata calcolata
				return dp[n] #restituisco quel valore (MEMOIZED)
	
		dp[n] = countModi(n-1, dp) + countModi(n-2, dp)
		return dp[n]

if __name__ == "__main__":
    T = int(input("Inserisci il numero di casi di test: "))
    
    for _ in range(T):
        n = input("Inserisci il numero di gradini: ")
        
        dp = [-1 for i in range(n+1)]
        
        res = countModi(n, dp)

        print("Risultato: " + str(res))
		
#O(n) - Bottom-Up
def countModi(n):
		
			dp = [0 for x in range(n+1)]
			dp[0], dp[1] = 1, 1
			
			for i in range(2, n+1):
					dp[i] = dp[i-1]+dp[i-2]
			return dp[n]

if __name__ == "__main__":
	T = int(input("Inserisci il numero di casi di test: "))
	for _ in range(T):
            n = input("Inserisci il numero di gradini: ")
            
            res = countModi(n)
			
            print("Risultato: " + str(res))