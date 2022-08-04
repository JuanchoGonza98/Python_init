A = int(input(print("Ingrese el valor del primer numero: ")))
B = int(input(print("Ingrese el valor del segundo numero: ")))

def prod(num1,num2):
    if num2 == 1:
        return num1 #caso base
    if num2 > 0:
        producto = num1 + prod(num1,num2-1)
        return producto

want = prod(A,B)
print("El valor del producto es: ",want)
