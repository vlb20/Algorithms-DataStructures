def isValidMove(N, maze, x, y):
    #se x e y non escono dalla griglia e se troviamo 1 nel maze
    if x >= 0 and  x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True
    
    return False

def solveMazeUtil(N, maze, x, y, sol):

    #se (x, y è il goal) ritorna ture
    if x==N-1 and y==N-1:
        sol[x][y] = 1
        return True
    
    # Vediamo se maze[x][y] è valida
    if isValidMove(N, maze, x, y) == True:

        #segno x,y come parte del percorso risolutivo
        sol[x][y] = 1

        #Muoviti verso destra
        if solveMazeUtil(N, maze, x+1, y, sol) == True:
            return True

        #Se muoversi a destra non ci da soluzione
        #muoviti verso il basso
        if solveMazeUtil(N, maze, x, y+1, sol) == True:
            return True
        
        #Se nessuno dei movimenti porta a soluzione
        #BACKTRACK: unmark x,y come parte della soluzione
        sol[x][y]=0
        return False
    

def solveMaze(maze, N):
    #creo una matrice inizializzata a 0 per memorizzare la soluzione
    sol = [[0 for i in range(N)] for i in range(N)]
    sol[0][0] = 1 #imposto la cella di partenza(in alto a sinistra) come parte della soluzione

    if solveMazeUtil(N, maze, 0, 0, sol):#se trovo una soluzione
        #stampo la matrice della soluzione
        print("-----------")
        for i in range(N):
            for j in range(N):
                print(sol[i][j], end=' ')
            print()
    else:
        print("La soluzione non esiste")


    
if __name__ == "__main__":

    with open("./test_file.txt") as file:

        num_test = int(file.readline().strip())

        while num_test > 0:

            data = file.readline().strip().split()

            N = int(data[0])

            maze = [list(map(int, file.readline().strip().split())) for _ in range(N)]
            print("maze=")
            for row in maze:
                print(row)
            
            solveMaze(maze, N)

            num_test =-1