num_lista = [3,5,12,24,8]
def sumar(lista):
    if len(lista) == 1:
        return lista[0] ##caso base
    else:
        return lista[0] + sumar(lista[1:]) ##funcion recursiva

print("Total Sumado: ", sumar(num_lista))