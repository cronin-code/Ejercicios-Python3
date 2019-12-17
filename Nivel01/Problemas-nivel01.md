[FUENTE](https://github.com/Abhijeet199/Python3-excercise-questions)

# Ejercicios de categoría nivel 1

### Ejercicio 1

Escriba un programa que encuentre todos aquellos numeros que son divisibles por 7 pero no son múltiplos de 5, entre 2000 y 3000 (ambos incluidos). Los numeros obtenidos deben ser impresos en una única línea separados por el carácter coma.

<details>
	<summary>Pista</summary>
	<pre>
		Considere usar el método range(start, end)
	</pre>
</details>


<details>
	<summary>Solución en la fuente</summary>
	<pre>
		lst = []
		for n in range(2000, 3201):
			if n%7==0 and n%5 !=0:
				lst.append(str(n))
		print(','.join(lst))
	</pre>
</details>

-------

### Ejercicio 2

Escriba un programa que calcule el factorial de un número dado. Suponga que al programa se le da como entrada 8, entonces su salidad deberia ser 40320.

<details>
	<summary>Pista</summary>
	<pre>
		Para los casos donde a la pregunta se le suministran datos de entrada, suponemos que son entradas de consola.
	</pre>
</details>

<details>
	<summary>Solución 1 en la fuente</summary>
	<pre>
		n = int(input())
		f = 1
		for in in range(2, n+1):
			f *= i
		print(f)
	</pre>
</details>

<details>
	<summary>Solución 2 en la fuente</summary>
	<pre>
		def fact(n):
			if n==1:
				return 1
			return n*fact(n-1)
	</pre>
</details>

------

### Ejercicio 3

Dado un número entero n, escriba un programa para generar un diccionario que contenga todos los pares entre (i, i * i) y (n, n * n), ambos incluidos.

<details>
	<summary>Pista</summary>
	<pre>
		Para los casos donde a la pregunta se le suministran datos de entrada, suponemos que son entradas de consola.
	</pre>
</details>

<details>
	<summary>Solución en la fuente</summary>
	<pre>
		n = int(input())
		d = {}
		for i in range(1, n+1):
			d[i] = i*i
		print(d)
	</pre>
</details>