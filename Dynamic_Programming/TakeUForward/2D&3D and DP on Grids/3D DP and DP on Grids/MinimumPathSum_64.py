def minSumPathUtil(i, j, matrix, dp):

    #Caso base se siamo al top left corner
    if i == 0 and j == 0:
        return matrix[0][0]

    #Caso base: out of bound
    if i<0 or j<0:
        return int(1e9)

    #Se è già stata calcolata la somma minima per questa cella
    if dp[i][j] != -1:
        return dp[i][j]

    #Calcola il percorso a somma minima ricorsivamento considerando
    #le mosse in alto e a destra
    up = matrix[i][j] + minSumPathUtil(i-1, j, matrix, dp)
    left = matrix[i][j] + minSumPathUtil(i, j-1, matrix, dp)

    #Prendo il minimo dei due percorsi
    dp[i][j] = min(up, left)
    return dp[i][j]


def minSumPath(n, m, matrix):

    dp = [[-1 for j in range(m)] for i in range(n)]

    return minSumPathUtil(n-1, m-1, matrix, dp)

if __name__ == "__main__":

    n = int(input("Inserisci n:"))
    m = int(input("Insersci m:"))
    matrix = [list(map(int, input("Inserisci la riga " + str(i+1) + ": ").split())) for i in range(n)]

    print(minSumPath(n,m,matrix))