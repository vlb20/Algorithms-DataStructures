#MEMOIZATION -> O(m*n)
def lcsM(X, Y, m, n, dp):
	
		#Se una delle due stringhe è vuota, la LCS è 0
		if(m == 0 or n == 0):
				return 0
		
		#Se il valore è già stato calcolato, lo restituisce
		if(dp[m][n] != -1):
				return dp[m][n]

		#se gli ultimi due caratteri delle 2 stringhe sono uguali,
		#la lunghezza della LCS aumenta di 1
		if X[m-1] == Y[n-1]:
				dp[m][n] = 1 + lcsM(X, Y, m-1, n-1, dp)
				return dp[m][n]


		# Se gli ultimi caratteri delle due stringhe non sono uguali,
        # la lunghezza della LCS sarà il massimo tra la LCS di X[0..m-1] e Y[0..n]
        # e la LCS di X[0..m] e Y[0..n-1]
		dp[m][n] = max(lcsM(X, Y, m, n-1, dp), lcsM(X, Y, m-1, n, dp))
		return dp[m][n]

#Bottom Up
def lcsBU(X, Y, m, n):
	
		#Matrice per salvare i valori DP -> (m+1) x (n+1)
		L = [[None]*(n+1) for i in range(m+1)]
		
		#Costruisco la matrice L[m+1][n+1] in maniera ascendente
		#Nota: L[i][j] contiene la lungezza della LCS di X[0..i-1] e Y[0..j-1]
		for i in range(m+1):
				for j in range(n+1):
						#se una delle due stringhe è vuota -> LCS=0
						if i == 0 or j == 0:
								L[i][j] = 0
						#Se gli ultimi caratteri corrispodono-> LCS = LCS senza ultimo carattere + 1
						elif X[i-1] == Y[j-1]:
								L[i][j] = L[i-1][j-1]+1
						#LCS è il massimo tra la lunghezza della LCS di X senza l’ultimo carattere e Y
						else: #, e la lunghezza della LCS di X e Y sena ultimo carattere
								L[i][j] = max(L[i-1][j], L[i][j-1])

		#L[m][n] contiene la lunghezza della LCS di X[0..n-1] & Y[0..m-1]
		return L[m][n]

if __name__ == "__main__":
		
		T = int(input("Inserisci il numero di casi di test: "))
		for _ in range(T):
				X = input("Inserisci la prima stringa: ")
				Y = input("Inserisci la seconda stringa: ")
				m = len(X)
				n = len(Y)
				dp = [[-1 for i in range(n+1)] for j in range(m+1)]
				
				res = lcsBU(X, Y, m, n)  #Bottom Up
				#res = lcsM(X, Y, m, n, dp) #Memoization

				print("La lunghezza della LCS è: " + str(res))
