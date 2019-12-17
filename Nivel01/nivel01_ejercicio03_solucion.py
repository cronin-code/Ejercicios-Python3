n = int(input("Ingrese un entero positivo n: "))
if n < 0:
	print("ERROR - n debe ser un entero positivo")
else:
	d = {}
	for i in range(1, n+1):
		d[i] = i*i

	print(d)