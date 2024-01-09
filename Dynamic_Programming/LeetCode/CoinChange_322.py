import sys

def minCoins(coins, n, target, dp):
    # Caso Base: se il valore target è 0, non è necessaria alcuna moneta
    if target == 0:
        return 0

    # Se un sottoproblema è già stato risolto, ritorna il valore dalla tabella DP
    if dp[target] != -1:
        return dp[target]

    res = sys.maxsize

    for i in range(n):
        if coins[i] <= target:
            # chiamata ricorsiva per risolvere il valore rimanente target - coins[i]
            sub_res = minCoins(coins, n, target - coins[i], dp)

            # Se il sottoproblema ha una soluzione valida e
            # il numero totale è minore del risultato corrente -> lo updatiamo
            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1

    # Salvo il risultato nella tabella DP
    dp[target] = res

    return res if res != sys.maxsize else -1

#------------

#O(target * n) - Bottom Up
#O(target * n) - Bottom Up
def minCoinsBU(coins, n, target):

    dp = [sys.maxsize]*(target+1) #0....target
    
    dp[0] = 0 #non sono necessarie monete per un importo pari a 0

    for t in range(1, target+1):#itero su tutti gli importi da 1 a target
        for c in coins: #per ogni moneta
            if t - c >= 0:#se il valore della moneta corrente è minore dell'importo corrente
								#calcolo il numero minimo di monete utilizzando la soluzione del sottoproblema t-c
                dp[t] = min(dp[t], 1 + dp[t - c]) #la aggiorno se è minore del val corrente

    return dp[target] if dp[target] != sys.maxsize else -1

if __name__ == "__main__":
    t = int(input("Inserisci il numero di casi di test: "))

    for _ in range(t):
        coins = list(map(int, input("Inserisci l'array di monete: ").split()))
        target = int(input("Inserisci il valore target: "))
        #dp = [-1] * (target + 1)
        print(minCoinsBU(coins, len(coins), target))