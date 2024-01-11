#O(m*n)
def uniquePaths(m, n):
    # Inizializza una matrice DP di dimensione m x n.
    # Ogni cella dp[i][j] rappresenta il numero di percorsi unici per raggiungere la cella (i, j).
    # Se i = 0 o j = 0 (cioè, siamo sulla prima riga o sulla prima colonna), ci può essere solo un percorso unico,
    # quindi impostiamo dp[i][j] a 1. Altrimenti, impostiamo dp[i][j] a 0.
    dp = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]

    # Ora, scorriamo ogni cella della matrice a partire dalla cella (1, 1).
    for i in range(1, m):
        for j in range(1, n):
            # Il numero di percorsi unici per raggiungere la cella (i, j) è la somma del numero di percorsi unici
            # per raggiungere la cella sopra (i-1, j) e la cella a sinistra (i, j-1).
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # Infine, restituiamo il numero di percorsi unici per raggiungere l'angolo in basso a destra della griglia,
    # che è dp[-1][-1] (cioè, l'ultima cella della matrice DP).
    return dp[-1][-1]

if __name__ == "__main__":

    t = int(input("Numero di casi di test: "))
    for _ in range(t):
        m = int(input("Inserisci valore m: "))
        n = int(input("Inserisci valore n: "))

        print("Numero di percorsi unici: ", uniquePaths(m,n))
