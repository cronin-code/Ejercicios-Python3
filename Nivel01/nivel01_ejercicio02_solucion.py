def factIterativo(n):
    f1 = 1
    while(n>0):
        f1 = f1*n
        n = n-1
    
    return f1


def factRecursivo(n):
    if n == 1 or n == 0:
        return 1
        
    return factRecursivo(n-1)*n

print("Calcula el n factorial de un número.")
n = int(input("Ingrese n: "))
if n < 0:
    print("ERROR - n debe ser un entero positivo")
else:
    print( "(iterativo) %d!: %d" % (n, factIterativo(n)) )
    print( "(recursivo) %d!: %d" % (n, factRecursivo(n)) )

