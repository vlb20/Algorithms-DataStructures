def mazeObstaclesUtil(i, j , maze, dp):

    #Caso base: se siamo fuori dai bordi o incontiamo un ostaco -> ritorniamo 0
    if i<0 or j<0 or maze[i][j] == -1:
        return 0

    #Caso base: se raggiungiamo lo starting point -> ritorniamo 1 (abbiamo trovato un percorso)
    if i==0 and j==0:
        return 1

    #Se abbiamo già calcolato il numero di percorsi per questa posizione la ritorniamo
    if dp[i][j] != -1:
        return dp[i][j]


    #Muoviamoci su e a sinistra nel labirinto e ricorsivamente calcoliamo il numero di percorsi
    up = mazeObstaclesUtil(i-1, j, maze, dp)
    left = mazeObstaclesUtil(i, j-1, maze, dp)

    #Salvo il risultato nella tabella DP e lo restituisco
    dp[i][j] = up + left
    return dp[i][j]

def mazeObstacles(n, m, maze):

    dp = [[-1 for j in range(m)] for i in range(n)]

    return mazeObstaclesUtil(n-1, m-1, maze, dp)

if __name__ == "__main__":

    n = int(input("Inserisci numero righe: "))
    m = int(input("Inserisci numero colonne: "))
    maze = [list(map(int, input("Inserisci la riga " + str(i+1) + ": ").split())) for i in range(n)]

    print(mazeObstacles(n, m, maze))