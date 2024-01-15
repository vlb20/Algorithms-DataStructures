import sys
#matrice per memorizzare i risultati intermedi del problema
dp = [[-1 for i in range(100)] for j in range(100)]

#O(N^3)
def matrixChainMemoised(p, i, j):

    if i == j: #se abbiamo solo una matrice -> 0 operazioni
        return 0

    #Se il risultato è stato calcolato -> ritorna True
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = sys.maxsize

    #Per ogni k nell'intervallo da i a j, calcoliamo il costo minimo
    #di moltiplicazione dividendo il problema in 2 sottoproblemi
    for k in range(i,j):
        #moltiplichiamo le matrici da i a k e da k+1 a j aggiungendo il costo di moltiplicazione delle 2 matrici
        dp[i][j] = min(dp[i][j], matrixChainMemoised(p, i, k) + matrixChainMemoised(p, k+1, j) + p[i-1]*p[k]*p[j])

    return dp[i][j]

#Funzione wrapper che prende in input l'array di dimensioni e la lunghezza
def matrixChainOrder(p,n):
    i = 1
    j = n-1
    return matrixChainMemoised(p, i, j)

if __name__ == "__main__":

    T = int(input("Numero casi di test: "))

    for _ in range(T):
        array = list(map(int, input("Inserisci array di dimensioni: ").split()))
        n = len(array)
        print("Numero minimo di moltiplicazioni: ", matrixChainOrder(array, n))