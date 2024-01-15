#O(N^3) dove N^2 sono gli stati totali. E per ogni stato abbiamo un loop di partizione che va per N volte
def maxCoins(a):

    n = len(a)

    #estendo la lista 'a' con 1 alla fine di entrambi
    a.insert(0, 1)
    a.append(1)

    #Creo una matrice DP inizializzata a -1 per salvare i risultati
    dp = [[-1]*(n+2) for _ in range(n+2)]

    def f(i, j):

        if i > j:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        maxi = float('-inf')

        for ind in range(i, j+1):
            cost = a[i-1] * a[ind] * a[j+1] + f(i, ind-1) + f(ind+1, j)
            maxi = max(maxi, cost)

        dp[i][j] = maxi
        return maxi

    return f(1, n)

if __name__ == "__main__":

    T = int(input("Numero casi di test: "))
    for _ in range(T):

        a = list(map(int, input("Inserisci array di palloncini: ").split()))
        print("Il massimo è:", maxCoins(a))