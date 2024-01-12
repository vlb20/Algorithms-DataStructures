#O(len(s1)*len(s2))
def isInterleave(s1, s2, s3):

    #Se la somma delle lunghezze delle due stringhe non è pari lla lunghezza della s3
    #allora sicuro non possono essere intrecciate
    if len(s1) + len(s2) != len(s3):
        return False
    
    #dp[i][j] True se s3[i+j:] è un intrecco per s1[i:] e s[j:]
    dp = [[False]*(len(s2)+1) for i in range(len(s1)+1)]

    #Una stringa vuota può essere considerata un intreccio di altre due strighe vuote
    dp[len(s1)][len(s2)] = True

    #Iteriamo su ogni cella di dp partendo da in basso a destra
    for i in range(len(s1), -1, -1):
        for j in range(len(s2), -1, -1):
            #se i è inbound(j può essere fuori dal bound)
            #e il carattere in s1 è uguale al carattere in s3
            #e la cella a destra (carttere da s1 preso) era una possibile soluzione
            if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                dp[i][j] = True
            if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                dp[i][j] = True
    return dp[0][0]

if __name__ == "__main__":

    T = int(input("Numero casi di test: "))
    for _ in range(T):
        s1 = input("Inserisci s1: ")
        s2 = input("Inserisci s2: ")
        s3 = input("Inserisci s3: ")
        print(isInterleave(s1,s2,s3))