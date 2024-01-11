#O(amount * len(coins))
def coinChange(amount, coins):
    # Crea un array DP di dimensione `amount + 1` per memorizzare il numero di modi
    # in cui si può ottenere ogni importo da 0 a `amount`.
    dp = [0]*(amount+1)

    # C'è solo un modo per ottenere 0 come importo, che è non prendere alcuna moneta.
    dp[0] = 1

    # Ora, scorre ogni moneta nell'array `coins`.
    for curr_coin in coins:
        # Per ogni moneta, aggiorna `dp[j]` per ogni `j` da `coin` a `amount`.
        for j in range(curr_coin, amount+1):
            # Il numero di modi per ottenere l'importo `j` è la somma del numero di modi
            # per ottenere l'importo `j` senza usare la moneta corrente (cioè, `dp[j]`)
            # e il numero di modi per ottenere l'importo `j - coin` (cioè, `dp[j - coin]`).
            dp[j] += dp[j-curr_coin]

    # Infine, restituisce il numero di modi per ottenere l'importo `amount`, che è `dp[amount]`.
    return dp[amount]

if __name__ == "__main__":

    T = int(input("Numero casi di test: "))
    for _ in range(T):
        amount = int(input("Inserisci importo: "))
        coins = list(map(int, input("Inserisci array di monete:").split()))
        print("Modi di ottenere l'importo:", coinChange(amount, coins))