litros = float(input("Capacidad en litros: "))
cm_cubicos = litros*1000
dimensiones = round(pow(cm_cubicos,1/3),2)
print(" ancho:",dimensiones,"cm\n","largo:",dimensiones,"cm\n", "alto:",dimensiones,"cm\n")