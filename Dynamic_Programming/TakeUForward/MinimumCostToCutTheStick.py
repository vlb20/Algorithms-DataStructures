#O(N*N*N) poichè ci sono 2 variabili i e j -> N*N stati
    #e per ogni stato c'è un loop che può scorrere fino a N volte
def min_cost(n, c, cuts):

    #matrice per salvare i risultati intermedi
    dp = [[-1]*(c+1) for _ in range(c+1)]

    #Estendo la lista dei tagli con 0 e n, e lo ordino
    cuts = [0] + cuts + [n]
    cuts.sort()

    #funzione ricorsiva per trovare il minimo costo
    def f(i,j):

        #caso base
        if i>j: #se i>j non ci sono tagli da fare
            return 0

        #Se il risultato è già stato calcolato lo ritorna
        if dp[i][j] != -1:
            return dp[i][j]

        #Variabile per tenere taccia del costo minimo
        #Impostata a inf per garantire che qualsiasi costo sarà minore
        mini = float('inf')

        #Per ogni indice nell'intervallo calcolo il costo minimo
        for ind in range(i, j+1):
            #tagliando il bastone in due sottoproblemi e aggiungendo il costo per tagliare il bastone
            ans = cuts[j+1] - cuts[i-1] + f(i, ind-1) + f(ind+1, j)
            mini = min(mini, ans) #se l'ans è minore del minimo costo -> l'aggiorniamo

        dp[i][j] = mini
        return mini #ritorniamo il minimo costo

    return f(1, c)

if __name__ == "__main__":

    T = int(input("Numero casi di test:"))
    for _ in range(T):

        cuts = list(map(int, input("Inserisci array cuts").split()))
        c = len(cuts)
        n = int(input("Inserisci lunghezza bastone: "))
        print("Il minimo costo e':", min_cost(n, c, cuts))