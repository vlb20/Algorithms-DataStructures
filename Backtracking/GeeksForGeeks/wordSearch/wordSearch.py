def wordSearch(r, c, i):

    #Caso base: se i=lunghezza della parola
    #allora abbiamo trvato la parola
    if i == len(word):
        return True
    #Vediamo se la mossa e valida
    if (r < 0 or c < 0 or #se la posizione (r,c) è fuori dalla griglia
        r >= m or c >= n or
        word[i] != grid[r][c] or #o il carattere i della parola non corrisponde alla posizione (r,c)
        (r, c) in sol): #o la posizione (r, c) è già stata visitata
        return False
    
    #aggiungiamo la posizione (r, c) al set dellle soluzioni
    sol.add((r, c))
    #eseguiamo la ricerca nelle quattro direzioni
    result = (wordSearch(r+1, c, i+1) or
            wordSearch(r-1, c, i+1) or
            wordSearch(r, c+1, i+1) or
            wordSearch(r, c-1, i+1))
    #se una delle chiamate restituisce True -> finisce
    #altrimenti Backtrack rimuovendo la posizione dal set
    sol.remove((r,c))
    return result
    

if __name__ == "__main__":

    with open("./test_file.txt") as file:

        num_test = int(file.readline().strip())

        while num_test > 0:

            sol = set() #creo un set delle soluzioni vuoto

            data = file.readline().strip().split()

            m = int(data[0]) #numero righe
            n = int(data[1]) #numero colonne

            grid = [list(map(str, file.readline().strip().split())) for _ in range(m)]


            text = file.readline().strip()
            word = [char for char in text]

            found = False
            #per ogni posizione della griglia
            #faccio partire il wordSearch
            for r in range(m):
                for c in range(n):
                    if wordSearch(r, c, 0):
                        found = True
                        print(True)
                        break
                if found:
                    break
            
            if not found:
                print(False)
            
            num_test -= 1