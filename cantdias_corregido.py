day = 1
month = 1
year = 1980
def esbisiesto(A): #Verificando si el año base es bisiesto
    if A % 4 == 0 and A % 100 != 0 or A % 4 == 0:
        flag = True
    else:
        flag = False
    return flag
meses = [31,28,31,30,31,30,31,31,30,31,30,31]
i = 0
if esbisiesto(year) == True :
    meses[1] = 29
cant_dias = int(input("Ingrese la cantidad de dias: "))
if cant_dias < meses[i]:
    day = day + cant_dias
if cant_dias >= meses[i]:
    while cant_dias >= meses[i] :
        month = month + 1
        cant_dias = cant_dias - meses [i]
        if cant_dias < meses[i]:
            day = day + cant_dias
        i = i+1
        if i > 11:
            year = year + 1
            month = 1
            i = 0
            if esbisiesto(year):
                meses[1] = 29
print("La fecha despues de esos dias es: ",day,"/",month,"/",year)