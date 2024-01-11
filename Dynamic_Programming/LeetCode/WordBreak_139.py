#O(n^2*m)
def wordBreak(s, wordDict):
    # Crea una tabella DP per memorizzare i risultati dei sottoproblemi.
    # Il valore di dp[i] sarà True se la stringa `s` può essere segmentata in parole del dizionario da 0 a i.
    dp = [False] * (len(s) + 1)

    # Caso base: una stringa vuota può sempre essere segmentata, quindi dp[len(s)] è True.
    dp[len(s)] = True

    # Parte dalla fine della stringa `s` e itera per ogni indice fino a i=0.
    for i in range(len(s)-1, -1, -1):
        # Per ogni indice `i`, verifica ogni parola nel dizionario.
        for w in wordDict:
            # Se l'indice i + la lunghezza della parola `w` non sfora la lunghezza della stringa `s`,
            # e se la sottostringa che parte da `i` e arriva a `i+len(w)` coincide con `w`,
            # allora dp[i] diventa dp[i + len(w)].
            if (i + len(w)) <= len(s) and s[i : i+len(w)] == w:
                dp[i] = dp[i + len(w)]
            # Se dp[i] diventa True, interrompe il ciclo.
            if dp[i] == True:
                break

    # Restituisce dp[0]. Se dp[0] è True, significa che la stringa `s` può essere segmentata in parole del dizionario.
    return dp[0]

if __name__ == "__main__":
    t = int(input("Inserisci il numero di casi di test: "))
    for _ in range(t):
        s = input("Inserisci la stringa: ")
        wordDict = input("Inserisci le parole del dizionario separate da uno spazio: ").split()
        print(wordBreak(s, wordDict))

#---------
def wordBreakAlt(s, wordDict):
    dp = [False] * (len(s) + 1)

    dp[0] = True

    for i in range(1, len(s) + 1):

        for w in wordDict:

            if dp[i - len(w)] and s[i - len(w) : i] == w:

                dp[i] = True

    return dp[-1]