# sorts.py
# Autor: Arturo Yepez
# DESCRIPCION: Archivo donde se implementa el algoritmo Mergesort e InsertionSort, para ellos 
#	dependemos de Merge.

#====================================================================================================
# LIBRERIAS
#====================================================================================================
import sys

#====================================================================================================
# MERGE
#====================================================================================================
def Merge(A: list, p: int, q: int, r: int) -> list:
	n = q - p + 1
	m = r - q

	# Creamos los arreglos de almacenamiento provisionales que luego haran Merge
	L = []
	R = []

	# Asignamos los valores de A en estos arreglos provisionales L y R
	for i in range(0,n):
		L.append(A[p+i])
	for i in range (0,m):
		R.append(A[q+i+1])

	# Creamos los sentinelas
	L.append(sys.maxsize)
	R.append(sys.maxsize)

	# Ordenamos los elementos de los arreglos provisionales de vuelta en A
	i, j = 0, 0
	for k in range(p, r+1):
		if (L[i]<=R[j]):
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
	return A


#====================================================================================================
# MERGESORT
#====================================================================================================
def MergeSort(A: list, p: int, r: int) -> list:
	if (p < r):
		q = (p+r)//2
		MergeSort(A, p, q)
		MergeSort(A, q+1, r)
		Merge(A, p, q, r)
	return A

#====================================================================================================
# ORDENAMIENTO POR INSERCIÓN
#====================================================================================================
def InsertionSort(A: list) -> list:
	for i in range (0,len(A)):
		while (i>0 and A[i]<A[i-1]):
			A[i], A[i-1] = A[i-1], A[i]
			i -= 1
	return A