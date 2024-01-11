#O(n)
def maxProfit(prices):
    if not prices:
        return 0

    n = len(prices)
    # Crea due array, `buy` e `sell`, di lunghezza `n`.
    buy = [0] * n
    sell = [0] * n

    # Imposta `buy[0]` a `-prices[0]` perché si spende `prices[0]` per comprare l'azione il primo giorno.
    buy[0] = -prices[0]

    for i in range(1, n):
        # Aggiorna `buy[i]` al massimo tra `buy[i - 1]` (cioè, non comprare un'azione il giorno `i`)
        # e `(sell[i - 2] if i >= 2 else 0) - prices[i]` (cioè, vendere un'azione il giorno `i-2` e comprarne una il giorno `i`).
        # Se `i` è minore di `2`, allora `sell[i - 2]` non esiste, quindi usiamo `0` come profitto iniziale.
        buy[i] = max(buy[i - 1], (sell[i - 2] if i >= 2 else 0) - prices[i])

        # Aggiorna `sell[i]` al massimo tra `sell[i - 1]` (cioè, non vendere un'azione il giorno `i`)
        # e `buy[i - 1] + prices[i]` (cioè, comprare un'azione il giorno `i-1` e venderla il giorno `i`).
        sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])

    # Restituisce il massimo profitto dopo `n` giorni, che è `sell[-1]`.
    return sell[-1]

if __name__ == "__main__":

    t = int(input("Numero di casi di test: "))

    for _ in range(t):
        prices = list(map(int, input("Inserisci l'array di prezzi: ").split()))
        print("Il profitto massimo e':", maxProfit(prices))