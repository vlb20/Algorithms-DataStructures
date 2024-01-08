# O(n^2) - Bottom Up
def printSubStr(st, low, high): # Funzione di stampa della sottostringa
    print(st[low : high+1])

def longestPalSubstr(st):
    n = len(st) # Lunghezza della stringa in input

    # Creo una tabella dove table[i][j] sarà False(0)
    # se la sottostringa str[i..j] non è palindroma.
    # Altrimenti sarà True
    table = [[0 for _ in range(n)] for _ in range(n)]

    # Tutte le stringhe di lunghezza 1 sono palindrome
    maxLength = 1
    for i in range(n):
        table[i][i] = True # Diagonale pari a 1

    # Controlla le sottostringhe di lunghezza 2
    start = 0
    for i in range(n-1):
        if (st[i] == st[i+1]):
            table[i][i+1] = True
            start = i
            maxLength = 2

    # Controlla le sottostringhe di lunghezza 3 a n
    for k in range(3, n+1):
        for i in range(n - k + 1):
            # Ottengo l'indice finale della sottostringa
            # da l'indice di inizio i e lunghezza k
            j = i + k - 1

            # Verifica della presenza di sottostringhe da
            # dall'i-esimo indice al j-esimo indice se
            # st[i + 1] a st[(j-1)] è un palindromo
            if(table[i+1][j-1] and st[i] == st[j]):
                table[i][j] = True

                if(k > maxLength):
                    start = i # Aggiorno l'indice di inizio della stringa pal. più lunga
                    maxLength = k # Aggiorno la lunghezza massima

    print("La sottostringa palindorma più lunga e': ", end="")
    printSubStr(st, start, start + maxLength - 1)

    return maxLength

if __name__ == "__main__":

    t = int(input("Inserisci il numero di casi di test: "))

    for _ in range(t):
        st = input("Inserisci la stringa: ")

        print("La lunghezza della sottostringa palindroma più lunga è: ", longestPalSubstr(st))

