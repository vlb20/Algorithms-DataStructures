def calcSubset(A, res, subset, index):
		#Aggiungi il subset corrente alla lista dei risultati
		res.append(subset[:])
	
		#Genero i subsets ricorsivamente includendo ed escludendo elementi
		for i in range(index, len(A)):
				#Includo l'elemento corrente nel subset
				subset.append(A[i])

				#Ricorsivamene genero i subset con l'elemento corrente incluso
				calcSubset(A, res, subset, i+1)

				#Escludo l'elemento corrente dal subset (backtracking)
				subset.pop()

def subsets(A):
		subset = []
		res = []
		index = 0
		calcSubset(A, res, subset, index)
		return res

if __name__ == "__main__":
		array = [1, 2, 3]
		res = subsets(array)

		#stampo i subsets generati
		for subset in res:
				print(subset)
				
#############
# Time Complexity: O(2^N), dove N è la dimensione dell'array