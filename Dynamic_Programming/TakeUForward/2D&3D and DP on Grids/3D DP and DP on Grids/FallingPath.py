
import sys

# Recursive function to find the maximum path sum starting from cell (i, j)
def getMaxUtil(i, j, m, matrix, dp):
    # Base case: If j is out of bounds, return a large negative value
    if j < 0 or j >= m:
        return -int(1e9)

    # Base case: If we are at the top row (i == 0), return the value in the current cell
    if i == 0:
        return matrix[0][j]

    # Check if the maximum path sum for this cell has already been computed
    if dp[i][j] != -1:
        return dp[i][j]

    # Calculate three possible moves: going up, going up-left, and going up-right
    up = matrix[i][j] + getMaxUtil(i - 1, j, m, matrix, dp)
    leftDiagonal = matrix[i][j] + getMaxUtil(i - 1, j - 1, m, matrix, dp)
    rightDiagonal = matrix[i][j] + getMaxUtil(i - 1, j + 1, m, matrix, dp)

    # Store the maximum of the three moves in the memoization table
    dp[i][j] = max(up, max(leftDiagonal, rightDiagonal))
    return dp[i][j]

# Function to find the maximum path sum in the matrix
def getMaxPathSum(matrix):
    n = len(matrix)  # Number of rows
    m = len(matrix[0])  # Number of columns
    dp = [[-1 for j in range(m)] for i in range(n)]  # Initialize a memoization table
    maxi = -sys.maxsize  # Initialize the maximum sum to a large negative value

    # Iterate through the first row and find the maximum path sum starting from each cell
    for j in range(m):
        ans = getMaxUtil(n - 1, j, m, matrix, dp)
        maxi = max(maxi, ans)

    return maxi  # Return the maximum path sum

def main():
    # Define the input matrix
    matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]

    # Call the getMaxPathSum function and print the result
    print(getMaxPathSum(matrix))

if __name__ == "__main__":
    main()
