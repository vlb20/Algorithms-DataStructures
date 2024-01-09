#O(n) - Bottom Up
def countDecodings(st):
    n = len(st)

    if n == 0 or st[0] == '0':
        return 0

    dp = [0]*(n+1)
    dp[0] = 1  # esiste 1 modo per decodificare una stringa vuota
    dp[1] = 1  # esiste 1 modo per decodificare una stringa di lunghezza 1

    for i in range(2, n+1):
        # converto le attuali sottostringe a una cifra e due cifre in interi
        one_digit = int(st[i-1])
        two_digits = int(st[i-2:i])

        # Se la sottostringa a una cifra non è 0
        # -> possiamo considerarla come singolo carattere
        if one_digit != 0:
            dp[i] += dp[i-1]

        # possiamo considerare le due cifre come un singolo carattere
        if 10 <= two_digits <= 26:
            dp[i] += dp[i-2]

    return dp[n]

if __name__ == "__main__":
    t = int(input("Inserisci il numero di casi di test: "))
    for _ in range(t):
        s = input("Inserisci la stringa di numeri: ")
        print(countDecodings(s))
