#Time Complexity: O(8^(R*C))
def isValidMove(grid, visited, row, col):
    #Controlliamo che la cella da visitare non esca dalla griglia e che non sia mai stata visitata
    return ((row >= 0) and (row < len(grid)) and (col >= 0)
            and (col < len(grid[0])) and visited[row][col] == 0)

def find_word(grid, word, visited,row, col, path):
    #controlla se la lunghezza del percorso è uguale alla lunghezza della parola
    #In quel caso abbiamo trovato la parola nella griglia
    if len(path) == len(word):
        return True
    
    #lista delle direzioni possibili
    directions = [(0, -1), (-1, 0), (0, 1),
                (1, 0), (-1, -1), (-1, 1),
                (1, -1), (1, 1)]
    
    #per ogni direzione
    for dx, dy in directions:
        r, c = row+dx, col+dy

        #controllo se la mossa e valida e se il carattere in quella cella
        #corrisponde al carattere corrente della parola che stiamo cercando
        if isValidMove(grid, visited, r, c) and grid[r][c] == word[len(path)]:
            #impostiamo la cella come visitata
            visited[r][c] = 1
            #aggiungiamo le nuove coordinate al percorso delle soluzioni
            path.append((r,c))
            #chiamo ricorsivamente la funzione con le nuove coordinate
            if find_word(grid, word, visited, r, c, path):
                #se ritorna true -> abbiamo trovato la soluzione
                return True
            #Backtrack
            #rimuoviamo le coordinate dal percorso
            path.pop()
            #segnamo la cella come non visitata
            visited[r][c] = 0
    return False

def search_word(grid, word, R, C):

    visited = [[0]*C for _ in range(R)]

    path = []

    #cerco il primo carattere della parola in ogni cella
    for r in range(R):
        for c in range(C):
            if grid[r][c] == word[0]:
                #appena lo trovo faccio partire la ricerca
                visited[r][c] = 1
                path.append((r,c))
                if find_word(grid, word, visited, r, c, path):
                    return path
                #Backtrack se non va a buon fine
                path.pop()
                visited[r][c] = 0
    
    return None


if __name__ == "__main__":

    with open("./test_file.txt") as file:

        num_test = int(file.readline().strip())

        while num_test > 0:

            text = file.readline().strip()
            word = [char for char in text]

            data = file.readline().strip().split()
            R, C = int(data[0]), int(data[1])

            grid = [list(map(str, file.readline().strip().split())) for _ in range(R)]
            
            path = search_word(grid, word, R, C)
            if path:
                for r, c in path:
                    print(r+1, c+1)
            else:
                print("parola non trovata")

            print("END")
            
            num_test -= 1