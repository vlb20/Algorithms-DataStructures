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

def canYouMake(str1, str2):
    """
    Questa funzione calcola il numero minimo di operazioni necessarie per convertire str1 in str2.
    Lo fa sottraendo la lunghezza della LCS tra str1 e str2 dalla lunghezza di entrambe le stringhe.
    """
    n = len(str1)
    m = len(str2)

    # Calcola la lunghezza della LCS tra str1 e str2
    k = lcs(str1, str2)

    # Le operazioni minime richieste sono la somma delle cancellazioni necessarie in entrambe le stringhe
    return (n - k) + (m - k)

def main():
    """
    Questa è la funzione principale che viene eseguita quando il programma viene eseguito.
    """
    str1 = "abcd"
    str2 = "anc"

    # Calcola e stampa le operazioni minime richieste per convertire str1 in str2
    print("Le operazioni minime richieste per convertire str1 in str2:", canYouMake(str1, str2))

if __name__ == '__main__':
    """
    Questa riga garantisce che la funzione main() venga eseguita solo quando questo script viene eseguito direttamente,
    e non quando viene importato come modulo in un altro script.
    """
    main()