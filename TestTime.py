import time

n = 1000
j=0
inicio = time.time()

for i in range(1,n):
	j = i+j 
fin = time.time()

tiempoTranscurrido = (fin-inicio) * 1000 # para expresarlo en milisegundos

print("Tiempo: " + str(tiempoTranscurrido))