#O(N^2) -> N stati ed in ogni stato, c'è un loop di size N come limite superiore

def is_palindrome(i, j, s):

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def f(i, n, s, dp):

    #Caso base:
    #Se raggiungiamo la fine della stringe, non ci serve un'ulteriore partizione
    if i == n:
        return 0

    if dp[i] != -1:
        return dp[i]

    min_cost = float('inf')

    #Itero attraverso le possibili sottostringhe iniziando dall'indice i
    for j in range(i, n):
        if is_palindrome(i, j, s):
            #Se s[i...j] è un palindromo, calcoliamo il costo
            cost = 1 + f(j+1, n, s, dp)
            min_cost = min(min_cost, cost)

    dp[i] = min_cost
    return dp[i]

def palindrome_partitioning(s):

    n = len(s)
    dp = [-1] * n
    return f(0, n, s, dp) - 1 #Sottraggo l'1 per escludere l'iniziale stringa non partizionata

if __name__ == "__main__":

    T = int(input("Numero casi di test:"))
    for _ in range(T):

        s = input("Inserisci la stringa:")
        print("Numero di partizioni:", palindrome_partitioning(s))