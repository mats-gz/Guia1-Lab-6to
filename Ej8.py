num = int(input("Ingrese un número:"))

def numCualidades(num):
    if num > 0:
        return print("Es positivo")
    elif num < 0:
        return print("Es negativo")
    elif num == 0:
        return print("Es cero")
    
def ParImpar(num):
    if num % 2 == 0:
        return print("Es par")
    elif num % 2 != 0:
        return print("Es impar")
    elif num == 0:
        return print("Es cero, no es par ni impar")
    
numCualidades(num)
ParImpar(num)
       