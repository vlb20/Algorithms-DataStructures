def minDistance(word1, word2):
		#Riga e colonna in più vuota per memorizzare i casi base
    dp = [[float("inf")] * (len(word2)+1) for i in range(len(word1) + 1)]

    #Casi base
		#riempie l'ultima riga e l'ultima colonna della matrice con i valori appropriati
    for j in range(len(word2)+1):
        dp[len(word1)][j] = len(word2) - j
    for i in range(len(word1)+1):
        dp[i][len(word2)] = len(word1) - i
		
		#Riempo il resto della matrice
    for i in range(len(word1)-1, -1, -1):
        for j in range(len(word2)-1, -1, -1):
						#Se i caratteri corrispondono è come se muovessimo i e j di 1, quindi
						#copio il valore della cella diagonale successiva
            if word1[i] == word2[j]:
                dp[i][j] = dp[i+1][j+1]
						#Altrimenti aggiungiamo 1 (costo dell'operazione da fare)
						#E preno il minimo tra insert, delete e replace(muovendo gli indici)
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

    return dp[0][0]

if __name__ == "__main__":

    T = int(input("Numero casi di test: "))

    for _ in range(T):
        word1 = input("Word1: ")
        word2 = input("Word2: ")

        print("Numero minimo di mosse:", minDistance(word1, word2))