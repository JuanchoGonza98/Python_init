num = int(input("Ingrese el n termino que quiere: "))


def fibonacci(n):
    if n <= 1: #caso base
        return n
    return fibonacci(n - 1) + fibonacci(n - 2) #formula recursiva para realizar la sucesion y extraer el n-esimo termino
result = fibonacci(num)
print("F(",num,") es: ",result)

