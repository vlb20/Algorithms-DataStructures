#O(n*sum(nums))
def canPartition(nums):

    #Calcola la somma totale dell'array
    s = sum(nums)

    #Se la somma totale non è pari, restituisce False
    if s % 2 != 0:
        #perchè non può essere divisa equamente
        return False
    
    target = s // 2

    #Creo una tabella DP per memorizzare
    #le somme totali ottenute finora.
    dp = [False] * (s+1)

    #dp[0] True perchè se non si seleziona alcun elemento
    # la somma totale è 0
    dp[0] = True

    #Scorro ogni numero dell'array
    for num in nums:
        #Per ogni numero, aggiorno la tabella DP per valori da 's' a 'num'
        for curr in range(s, num-1, -1):
            #Se la somma corrente (curr) è stata vista prima, allora dp[curr] rimane True

            #Se la curr non è stata vista prima, ma può essere ottenuta
                #selezionando l'elemento corrente -> dp[curr] diventa True
            
            #Se la curr non è stata vista prima e non può essere ottenuta
                #selezionando l'elemento corrente -> dp[curr] diventa False
            
            dp[curr] = dp[curr] or dp[curr-num]

    #restituisco dp[target] (o dp[s//2]).
    #Se dp[target]=True allora l'array può essere suddiviso in due sottonsiemi con la stessa somma
    return dp[target]