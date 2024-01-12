def minDistance(word1, word2):

    dp = [[float("inf")] * (len(word2)+1) for i in range(len(word1) + 1)]

    #Casi base
    for j in range(len(word2)+1):
        dp[len(word1)][j] = len(word2) - j
    for i in range(len(word1)+1):
        dp[i][len(word2)] = len(word1) - i

    for i in range(len(word1)-1, -1, -1):
        for j in range(len(word2)-1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

    for row in dp:
        print(row)
    return dp[0][0]

if __name__ == "__main__":

    T = int(input("Numero casi di test: "))

    for _ in range(T):
        word1 = input("Word1: ")
        word2 = input("Word2: ")

        print("Numero minimo di mosse:", minDistance(word1, word2))