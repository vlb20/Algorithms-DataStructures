from collections import defaultdict
def findTargetSum(nums, target):
    
    #Inizializziamo dp come un dizionario con valore predefinito 0
    dp = defaultdict(int)#se cerchiamo un valore chiave che non esiste nel dizionario otteniamo 0 invece che un errore

    #dp={somma: modi_di_ottenerlo}

    #c'è solo un modo per ottenere una somma di 0 (non scegliendo nessun numero)
    dp[0] = 1 #dp={0: 1}

    #Iteriamo su ogni numero in nums
    for num in nums:
        #Creiamo un nuovo dizionario temporaneo per il prossimo stato di dp
        new_dp = defaultdict(int)
        #Itero su ogni possibile somma che abbiamo ottenuto finora
        for sum in dp:
            #Aggiorno new_dp aggiungendo il numero di modi in cui possiamo ottenere
            #n+num e n-num
            new_dp[sum + num] += dp[sum]
            new_dp[sum - num] += dp[sum]
        #aggiorno dp per il prossimo ciclo
        dp = new_dp
    
    #Restituiamo il numero di modi in cui possiamo ottenere la somma target
    return dp[target]

def findTargetSumWays(nums, target):
    # Calcola la somma di tutti gli elementi nella lista di input
    summ = sum(nums)
    # Se l'obiettivo è maggiore della somma di tutti gli elementi o la loro differenza assoluta è dispari,
    # non c'è modo di formare la somma obiettivo aggiungendo o sottraendo elementi dalla lista di input.
    if summ < abs(target) or (summ + target) & 1:
        return 0

    def knapsack(target):
        # Crea una lista con una lunghezza pari alla somma di tutti gli elementi nella lista di input più uno,
        # dove il primo elemento è inizializzato a 1 e il resto è inizializzato a 0.
        # Questa lista sarà utilizzata per tenere traccia del numero di modi per sommare fino a ogni possibile obiettivo.
        dp = [1] + [0] * summ
        print(dp)

        # Per ogni elemento nella lista di input,
        for num in nums:
            print(num)
            # Itera all'indietro attraverso la lista dp dalla fine all'elemento corrente (incluso),
            # in modo che i valori dp per l'elemento corrente siano basati solo sugli elementi precedenti
            # nella lista, e non sull'elemento corrente o su qualsiasi elemento successivo.
            for j in range(summ, num - 1, -1):
                print(j)
                # Aggiungi il valore dp per l'elemento precedente all'indice corrente, j - num,
                # al valore dp per l'indice corrente, j.
                # Questo perché ci sono dp[j - num] modi per sommare fino all'obiettivo utilizzando tutti gli elementi
                # fino a e compreso l'elemento corrente, e stiamo aggiungendo quei modi ai modi esistenti
                # per sommare fino all'obiettivo utilizzando tutti gli elementi fino a ma non compreso l'elemento corrente.
                dp[j] += dp[j - num]
                print(dp)

        # Restituisci il valore dp per la somma obiettivo.
        return dp[target]

    # Chiama la funzione knapsack con la somma obiettivo divisa per 2, perché stiamo contando il numero
    # di modi per formare la somma obiettivo utilizzando l'aggiunta e la sottrazione, e le due operazioni possono annullarsi
    # a vicenda, il che significa che la somma obiettivo può essere raggiunta solo se è un numero pari.
    return knapsack((summ + target) // 2)

if __name__ == "__main__":

    T = int(input("Numero casi di test: "))
    for _ in range(T):
        nums = list(map(int, input("Inserisci array nums: ").split()))
        target = int(input("Inserisci valore target: "))

        #print("Il risultato è:", findTargetSum(nums, target))
        print("Il risultato è:", findTargetSumWays(nums, target))