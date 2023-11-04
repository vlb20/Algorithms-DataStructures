def power(N,R):
        
    if N == 0:
        return 0
    
    if R == 0:
        return 1
    
    ans = 0
        
    if R%2==0: #se l'esponente è pari, salvo il risultato della potenza con R/2 in ans e poi faccio ans*ans
        #2^4 viene scomposto in (2^2)*(2^2)
        ans = power(N, R/2)
        ans = (ans * ans) % 1000000007
    else:#se l'esponente è dispari
        ans = N % 1000000007
        #riduciamo di 1 la potenza per renderlo pari.
        #2^3 -> 2*(2^2) -> 2*[(2^1)*(2^1)]
        ans = (ans * power(N, R-1) % 1000000007) %1000000007
    
    
    return ((ans + 1000000007)%1000000007)
    
    #usiamo il modulo 10^9+7 per evitare l'overflow error

def readTestFile(path):

    file = open(path, 'r')

    testsList = []

    for line in file:
        testsList.append([int(x) for x in line.split(' ')])

    return testsList
    
if __name__ == "__main__":

    testList = readTestFile(path="./test_file.txt")

    for test in testList:
        N = test[0]
        R = test[1]
        result = power(N,R)
        print(result)