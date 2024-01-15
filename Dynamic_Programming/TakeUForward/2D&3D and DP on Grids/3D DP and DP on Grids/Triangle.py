
def minimumPathSumUtil(i, j, triangle, n, dp):
    # Check if we have already computed the minimum path sum for this cell
    if dp[i][j] != -1:
        return dp[i][j]

    # If we are at the bottom of the triangle, return the value in the current cell
    if i == n - 1:
        return triangle[i][j]

    # Calculate the minimum path sum by considering two possible moves: down and diagonal
    down = triangle[i][j] + minimumPathSumUtil(i + 1, j, triangle, n, dp)
    diagonal = triangle[i][j] + minimumPathSumUtil(i + 1, j + 1, triangle, n, dp)

    # Store the computed minimum path sum in the memoization table
    dp[i][j] = min(down, diagonal)
    return dp[i][j]

# Define a wrapper function to initialize memoization table and start the computation
def minimumPathSum(triangle, n):
    dp = [[-1 for j in range(n)] for i in range(n)]  # Initialize a memoization table with -1
    return minimumPathSumUtil(0, 0, triangle, n, dp)  # Start the recursive computation

# Define the main function where you set up the triangle and call the minimumPathSum function
def main():
    # Inizializza una lista vuota per il tuo triangolo
    triangle = []

    # Chiedi all'utente quanti livelli vuole nel triangolo
    n = int(input("Inserisci il numero di livelli del triangolo: "))

    # Itera per ogni livello del triangolo
    for i in range(n):
        # Inizializza una lista vuota per il livello corrente
        level = []

        # Chiedi all'utente di inserire i numeri per il livello corrente
        print(f"Inserisci {i+1} numeri per il livello {i+1}: ")
        for j in range(i+1):
            num = int(input())
            level.append(num)

        # Aggiungi il livello corrente al triangolo
        triangle.append(level)

    # Ora la variabile 'triangle' contiene l'input dell'utente
    print("Il tuo triangolo è: ", triangle)


    # Call the minimumPathSum function and print the result
    print(minimumPathSum(triangle, n))

# Check if this script is the main program entry point
if __name__ == "__main__":
    main()  # Call the main function to start the program
