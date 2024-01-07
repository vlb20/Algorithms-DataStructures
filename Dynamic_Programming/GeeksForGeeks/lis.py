#T(n)=O(n^2)
def LIS(arr):
	n = len(arr) #calcolo la lungheza dell'array
	
	#dichiaro la list (array) per LIS e
	#inizializzo i valori LIS per ogni indice
	lis = [1]*n
	
	# Questo doppio ciclo for confronta ogni elemento dell'array 
	# con tutti gli elementi precedenti
	for i in range(1,n): #inizio dal secondo elemento
			for j in range(0,i): #dal primo elemento dell'array fino al precedente di i
				# Se l'elemento corrente è maggiore dell'elemento precedente
				# e la LIS all'indice corrente è minore della LIS all'indice precedente +1
				if arr[i] > arr[j] and lis[i] < lis[j]+1:
						lis[i] = lis[j]+1 #aggiorno la LIS all'indice corrente

	#inizializzo il massimo a 0 per ottenere
	# il massimo di tutte le LIS
	maximum = 0
	
	#Scelgo il massimo
	for i in range(n):
			maximum = max(maximum, lis[i])

	return maximum