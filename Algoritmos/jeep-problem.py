def jeep_problem(n_bidones, distancia):
    if n_bidones == 1:
        return distancia
    elif n_bidones == 2:
        return distancia*2
    else:
        return distancia/(n_bidones*2-3) + jeep_problem(n_bidones-1, distancia)

n_bidones = int(input("Numero de bidones: "))
distancia = int(input("Distancia: "))
print(jeep_problem(n_bidones, distancia),"km")