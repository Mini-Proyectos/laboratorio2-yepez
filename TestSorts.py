# TestSorts.py
# Autor: Arturo Yepez
# DESCRIPCION: Es un archivo de prueba donde se mide el tiempo en distintos casos que tardan los algoritmos
#	InsertionSort y MergeSort.



#====================================================================================================
# LIBRERIAS
#====================================================================================================
import time 
import sys
import random
from sorts import MergeSort, InsertionSort


#====================================================================================================
# ENTRADAS
#====================================================================================================

# El str justo despues de la llamada
program = str(sys.argv[1])

# EL int despues del primer elemento
n = int(sys.argv[2])

#====================================================================================================
# CREACION DE ARREGLO GENERICO
#====================================================================================================

# Para crear un arreglo generico utilizamos la libreria de python llamada random y en un rango dado por
#	el usuario se crea un arreglo de numeros random
A = []
for i in range(0,n):
	A.append(random.randint(1,100))


#====================================================================================================
# CALCULO DEL TIEMPO SEGUN EL PROGRAMA
#====================================================================================================

# Utilizamos un selector para seleccionar el algoritmo a medirse el tiempo y el uso de try/except en 
#	caso de que haya errores.
try:
	if (program == 'InsertionSort'):
		inicio = time.time()
		InsertionSort(A)
		fin = time.time()
	elif (program == 'MergeSort'):
		inicio = time.time()
		MergeSort(A, 0, n-1)
		fin = time.time()

	tiempo_trans = (fin - inicio)*1000
except:
	print('Nombre no coincide con ningun algoritmo, pruebe de nuevo')
	sys.exit()


#====================================================================================================
# SALIDA
#====================================================================================================
print(str(program)+' '+str(n)+' '+str(tiempo_trans))