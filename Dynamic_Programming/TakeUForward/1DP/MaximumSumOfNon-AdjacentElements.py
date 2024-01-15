#O(N) -> N sottoproblemi risolti in tempo costante
def solveUtil(ind, arr, dp):

    #Vediamo se la soluzione è stata già calcolata
    if dp[ind] != -1:
        return dp[ind]

    #Caso base, se l'indice è pari a 0 ritorno il valore a quell'indicie
    if ind == 0:
        return arr[ind]

    #Caso base: se l'indice è negativo -> ritorno 0 (out of bound)
    if ind < 0:
        return 0

    #Calcolo il valore massimo quando scelgo l'elemento corrente
    pick = arr[ind] + solveUtil(ind-2, arr, dp)

    #Calcolo il valore massimo quando non scelgo l'elemento corrente
    nonPick = 0 + solveUtil(ind-1, arr, dp)

    #Salvo il valore massimo delle 2 scelte nella tabella DP
    dp[ind] = max(pick, nonPick)

    #Restituisco il valore massimo per l'indice corrente
    return dp[ind]

#Funzione per risolvere il problema per il dato array
def solve(n, arr):
    #Inizializzo la tabella DP per salvare i risultati intermedi
    dp = [-1 for i in range(n)]

    return solveUtil(n-1, arr, dp)

if __name__ == "__main__":

    T = int(input("Casi di test:"))
    for _ in range(T):

        arr = list(map(int, input("Array:").split()))

        n = len(arr)

        print(solve(n, arr))