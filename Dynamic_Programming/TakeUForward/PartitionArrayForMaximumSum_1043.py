#O(N*k) -> ci sono N stato e per ogni stato abbiamo un ciclo da 0 a k
def max_sum_after_partitioning(num, k):

    # Calcola la lunghezza dell'array num
    n = len(num)
    # Inizializza un array dp di lunghezza n con tutti gli elementi impostati a -1
    dp = [-1]*n

    # Funzione ricorsiva per calcolare la somma massima
    def f(ind):

        # Caso base: se ind è uguale a n, ritorna 0
        if ind == n:
            return 0

        # Se dp[ind] non è -1, significa che il risultato è già stato calcolato, quindi ritorna quel valore
        if dp[ind] != -1:
            return dp[ind]

        # Inizializza len_val a 0, max_val a -infinito e max_ans a infinito
        len_val = 0
        max_val = float('-inf')
        max_ans = float('inf')

        # Per ogni j nell'intervallo da ind a min(ind + j, n)
        for j in range(ind, min(ind + j, n)):
            # Incrementa len_val di 1
            len_val += 1
            # Aggiorna max_val con il massimo tra max_val e num[j]
            max_val = max(max_val, num[j])
            # Calcola la somma come il prodotto della somma del sottoarray + il sottoproblema
            summation = len_val * max_val + f(j+1)
            # Aggiorna max_ans con il massimo tra max_ans e la somma
            max_ans = max(max_ans, summation)

        # Memorizza max_ans in dp[ind]
        dp[ind] = max_ans
        # Ritorna max_ans
        return dp[ind]

    # Chiama la funzione f con ind impostato a 0 e ritorna il suo risultato
    return f(0)

if __name__ == "__main__":

    # Legge il numero di casi di test
    T = int(input("Numero casi di test:"))
    for _ in range(T):

        # Legge l'array num
        num = list(map(int, input("Inserisci array numerico: ").split()))
        # Legge k
        k = int(input("Inserisci k:"))
        # Calcola la somma massima
        max_sum = max_sum_after_partitioning(num, k)
        # Stampa la somma massima
        print("La somma massima è:", max_sum)
