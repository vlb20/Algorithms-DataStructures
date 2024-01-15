def count_squares(n, m, arr):
    # Inizializza una matrice dp di dimensione nxm con tutti gli elementi impostati a 0
    dp = [[0]*m for _ in range(n)]

    # Imposta la prima riga e la prima colonna di dp uguale alla prima riga e alla prima colonna di arr
    for j in range(m):
        dp[0][j] = arr[0][j]
    for i in range(n):
        dp[i][0] = arr[i][0]

    # Per ogni cella in arr a partire dalla seconda riga e dalla seconda colonna
    for i in range(1, n):
        for j in range(1, m):
            # Se la cella corrente in arr è 0, allora la cella corrente in dp è 0
            if arr[i][j] == 0:
                dp[i][j] = 0
            else:
                # Altrimenti, la cella corrente in dp è 1 più il minimo tra la cella sopra, la cella a sinistra e la cella in alto a sinistra in dp
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])

    # Calcola la somma di tutte le celle in dp
    total = sum(sum(row) for row in dp)
    # Ritorna la somma totale
    return total

if __name__ == "__main__":

    n = int(input("Inserisci numero righe (n):"))
    m = int(input("Inserisci numero colonne (m):"))
    arr = [list(map(int, input("Inserisci la riga " + str(i+1) + ": ").split())) for i in range(n)]

    squares = count_squares(n, m, arr)
    print("Il numero di quadrati è:", squares)