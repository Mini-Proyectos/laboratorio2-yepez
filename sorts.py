# sorts.py
# Autor: Arturo Yepez
# DESCRIPCION: Archivo donde se implementa el algoritmo Mergesort, para ellos dependemos de Merge

import sys

#====================================================================================================
# MERGE
#====================================================================================================
def merge(A: list, p: int, q: int, r: int) -> list:
	# Declaramos los tamaños de los nuevos arreglos
	n = q - p * 1
	m = r - q
	
	# Se crean dos arreglos nuevos que luego hacen merge
	L = []
	R = []

	# Asigna a los valores de L y R las mitades de A
	for i in range(0,n+1):
		L.append(A[i]) 
	for i in range(0,m+1):
		R.append(A[m + i])

	# Creamos los sentinelas
	L.append(sys.maxsize)
	R.append(sys.maxsize)
	assert(len(L) == n+1 and len(R) == m+1)

	# Ordenamos ambos arreglos L y R en el arreglo principal A
	i, j = 1, 1
	for k in range(p, r+1):
		if (L[i]<=R[j]):
			A[k] = L[i]
			i += 1
		else
			A[k] = R[j]
			j += 1

#====================================================================================================
# MERGESORT
#====================================================================================================
def mergesort(A: list, p: int, r: int) -> list:
	if (p<= r):
		q = (p+r)//2
		mergesort(A, p, q)
		mergesort(A, q+1, r)
		merge(A, p, q, r)

#====================================================================================================
# ORDENAMIENTO POR INSERCIÓN
#====================================================================================================
def InsertionSort(A: list) -> list:
	for i in range (0,len(A)):
		while (i>0 and A[i]<A[i-1]):
			A[i], A[i-1] = A[i-1], A[i]
			i -= 1
	return A