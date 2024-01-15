def lcs(s1, s2):
    """
    Questa funzione calcola la lunghezza della sottosequenza comune più lunga (LCS) tra due stringhe s1 e s2.
    Utilizza la programmazione dinamica per risolvere il problema.
    """
    n = len(s1)
    m = len(s2)

    # Inizializza un array 2D per memorizzare la lunghezza della LCS
    dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]

    # Casi base: quando una delle stringhe è vuota, la lunghezza della LCS è 0.
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(m + 1):
        dp[0][i] = 0

    # Riempie l'array dp usando la programmazione dinamica
    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
            else:
                dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

    # Il valore finale in dp sarà la lunghezza della LCS
    return dp[n][m]

def longestPalindromeSubsequence(s):
    """
    Questa funzione calcola la lunghezza della sottosequenza palindromica più lunga di una stringa.
    Lo fa trovando la LCS tra la stringa e la sua inversione.
    """
    # Inverte la stringa di input
    t = s
    s = s[::-1]

    # Trova la lunghezza della LCS tra s e la sua inversione
    return lcs(s, t)

def minInsertion(s):
    """
    Questa funzione calcola il numero minimo di inserimenti necessari per rendere una stringa un palindromo.
    Lo fa sottraendo la lunghezza della sottosequenza palindromica più lunga dalla lunghezza della stringa.
    """
    n = len(s)

    # Calcola la lunghezza della sottosequenza palindromica più lunga
    k = longestPalindromeSubsequence(s)

    # Il numero minimo di inserimenti necessari per rendere la stringa un palindromo è la differenza tra la sua lunghezza e la lunghezza della sua sottosequenza palindromica più lunga
    return n - k

def main():
    """
    Questa è la funzione principale che viene eseguita quando il programma viene eseguito.
    """
    s = "abcaa"
    print("Il numero minimo di inserimenti necessari per rendere la stringa un palindromo:", minInsertion(s))

if __name__ == '__main__':
    """
    Questa riga garantisce che la funzione main() venga eseguita solo quando questo script viene eseguito direttamente,
    e non quando viene importato come modulo in un altro script.
    """
    main()