
#### CI2692

## Laboratorio2
## Merge sort


#### Resumen
El objetivo de este laboratorio es implementar el algoritmo de ordenamiento Merge Sort, 
y evaluar su comportamiento. 


#### Actividades

1) Implemente el algoritmo de Merge Sort, siguiendo el pseudo-código de las láminas de la clase de teoría (https://bonetblai.github.io/courses/ci2612/handouts/ci2612-lec03.pdf). 

Dicha implementación debe realizarse en una función dentro del archivo 
`Sorts.py`; y debe cumplir con la firma:   `MergeSort(A, p,  r)`, 
donde `A` es el arreglo a ser ordenado, `p`  es el índice inferior de la sección del arreglo a ser ordenado y `r`es el índice superior de dicho arreglo. 

Mueva su implementación de ordenamiento por inserción al archivo 
`Busquedas.py`. La misma deberá  denominarse `InsertionSort(A, p, r)`  donde `A` es el arreglo a ser ordenado, `p`  es el índice inferior de la sección del arreglo a ser ordenado y `r` es el índice superior de dicho arreglo. 


2) Implemente un programa de prueba denominado "TestSorts.py". 

Este programa debe ejecutarse con el siguiente comando:
> python3 TestSorts.py nombre_algoritmo n\_elementos

`nombre\_algoritmo` está en el conjunto: \{"InsertionSort", "MergeSort"}

Un ejemplo de llamada al programa de prueba:
> python3 TestSorts.py InsertionSort 100



La salida de este programa deberá imprimir por pantalla el nombre del algoritmo, el número de elementos y el tiempo en milisegundos que empleó el programa para ordenar un arreglo de n\_elementos. Un ejemplo de salida es: 

> InsertionSort 100 1.9629726409912109

En el archivo `TestTime.py` pueden encontar un ejemplo del uso de la funcion `time()` para calcular el tiempo de ejecución de una función o bloque de código.  

Dentro del programa se deberá crear un arreglo "desordenado" de n elementos, en cada llamada este arreglo debe ser diferente. 



