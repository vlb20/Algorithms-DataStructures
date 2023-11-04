import sys

def is_valid_move(x, y, prec_x, prec_y):
    #controllo se la cella (x,y) è all'interno della griglia
    return 0 <= x < R and 0 <= y < C and grid[x][y] <= grid[prec_x][prec_y]
    #oltretutto noi dobbiamo trovare un perocroso che va solo "in discesa"
    #quindi il movimento è valido solo se porta ad una cella con un valore o uguale

def longest_run(x, y):
    if sol[x][y] != -1: #controllo se la max_run del percorso a partire da (x,y) è già stata calcolata
        return sol[x][y] #se è così, restituisce immediatamente quel valore
    #Questo per velocizzare le ricorsioni
    
    max_run = 1#Questo inizializza la lunghezza massima del percorso a 1

    for dx, dy in directions: #iteriamo su tutte le direzioni in cui ci possiamo muovere
        new_x, new_y = x+dx, y+dy #calcolo le coordinate della cella a cui arriviamo

        if is_valid_move(new_x, new_y, x, y): #controllo se il movimento è valido
            # calcolo la lunghezza del percorso da new_x e new_y (aggiungo 1 per contare la cella (x,y))
            max_run = max(max_run, 1 + longest_run(new_x, new_y)) #se è maggiore aggiorno max_run
        
    sol[x][y] = max_run #memorizza la max_run a partire da (x, y)
    return max_run #e la restituisco

if __name__ == "__main__":

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #(-1 0) vai in alto: riga precedente, stessa colonna
    #(1 0) vai in basso: riga successiva, stessa colonna
    #(0 -1) vai a sinistra: stessa riga, colonna precedente
    #(0 1) vai a destra: stessa riga, colonna successiva

    with open("./test_file.txt") as file:

        num_test = int(file.readline().strip())#leggo il numero di test case

        sys.setrecursionlimit(10**7)

        while num_test > 0:

            data = file.readline().strip().split() #rimuovo spazi bianchi a inizio e fine riha, la divido in lista di sottostringhe

            name_test, R, C = data[0], int(data[1]), int(data[2])

            grid = [list(map(int, file.readline().strip().split())) for _ in range(R)]
            #Leggo le prossime R righe del file, ogni riga la divido in una lista di stringhe
            #Ogni stringa viene convertita in un intero, e infine ogni lista di interi la aggiungo a grid
            print("grid=")
            for row in grid:
                print(row)

            #Creo una matrice RxC (lista di liste) piena di -1
            #per memorizzare le soluzioni del problema
            sol = [[-1 for _ in range(C)] for _ in range(R)]
            print("sol=")
            for row in sol:
                print(row)
            
            #itero su ogni cella della griglia
            max_run = 0
            for i in range(R):
                for j in range(C):
                    max_run = max(max_run, longest_run(i,j))
                #calcolo il longest run che INIZIA DA QUELLA CELLA
                #aggiorno il max_run se è necessario

            print("sol=")
            for row in sol:
                print(row)

            print(f"{name_test}:{max_run}")

            num_test -=1