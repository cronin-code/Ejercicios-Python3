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

Dado un número entero n, escriba un programa para generar un diccionario que contenga todos los pares entre (i, i * i) y (n, n * n), ambos incluidos. Suponga que al programa se le da como entrada el valor 8, entonces la salida deberia ser {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

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

------

### Ejercicio 4

Escriba un programa que acepte por consola una secuencia de numeros separados por coma, para generar luego una lista y una tupla que contengan la secuencia ingresada. Supongamos que le damos la siguiente entrada al programa: 32,67,55,33,12,98, entonces la salida debería ser:
```python
['34','67','55','33','12','98']
('34','67','55','33','12','98')
```

<details>
    <summary>Pista</summary>
    <pre>
        En casos donde a la pregunta se le suministran datos de entrada, suponemos que son entradas de consola.
        El método tuple() puede convertir la lista a tupla.
    </pre>
</details>

<details>
    <summary>Solución en la fuente</summary>
    <pre>
        lst = input().split(',')
        tup = tuple(lst)
        print(lst)
        print(tup)
    </pre>
</details>

------

### Ejercicio 5

Defina una clase que tenga al menos los siguientes dos métodos:

1. **get_string**: Obtiene una entrada de la consola.
2. **print_string**: Imprime la cadena en mayúsculas.

<details>
    <summary>Pista</summary>
    <pre>
        Use el método __init__ para construir algunos parámetros.
    </pre>
</details>

<details>
    <summary>Solución en la fuente</summary>
    ```
        class InputOutputString:
            def __init__(self):
                self.string = ''

            def get_string(self):
                self.string = input()

            def print_string(self):
                print(self.string)

        obj = InputOutputString()
        obj.get_string()
        obj.print_string()
    ```
</details>

------

### Ejercicio 6

Escriba un método que pueda calcular el cuadrado de un número dado por consola.

<details>
    <summary>Pista</summary>
    <pre>
        Use el operador **
    </pre>
</details>

<details>
    <summary>Solución en la fuente</summary>
    ```
        def sqr(n):
            return n**2

        num = int(input())
        print(sqr(num))
    ```
</details>

-----

### Ejercicio 7

Python tiene muchas funciones prediseñadas, y si no sabes como usarlas, puedes leer la documentación online o buscar algún libro. Sin embargo, python tiene una función documento prediseñada para toda función prediseñada.

Escriba un programa que imprima la función documento prediseñado en Python para los métodos abs(), int() e input(), y agrege un documento para su propia función.

<details>
    <summary>Pista</summary>
    <pre>El método prediseñado del método documento es __doc__</pre>
</details>

<details>
    <summary>Solución en la fuente</summary>
    ```
        print(abs.__doc__)
        print(int.__doc__)
        print(input.__doc__)

        def square(num):
            """ Return the square value of the input number.
            The input number must be integer.
            """
            return num**2

        print(square(2))
        print(square.__doc__)
    ```
</details>

-----

### Ejercicio 8

Defina una función que pueda calcular la suma de dos números.
Por ejemplo:
```Python
Input:
4 3
Outpu:
7
```

<details>
    <summary>Pista</summary>
    <pre>
        Define una función con dos argumentos. Puedes calcular la suma dentro de la función y devolver su valor.
    </pre>
</details>

<details>
    <summary>Solución en la fuente</summary>
    ```
        def sum_function(n1, n2):
            return n1 + n2 

        num1, num2 = map(int, input().split())
        print(sum_function(num1, num2))
    ```
</details>

-----

### Ejercicio 9

Defina una función que pueda convertir un entero a string, luego imprimirlo en consola.

<details>
    <summary>Pista</summary>
    <pre>
        Use str() para convertir un número a string.
    </pre>
</details>

<details>
    <summary>Solución en la fuente</summary>
    ```
        def int_to_str(i):
            return str(i)

        n = int(input())
        print(int_to_str)
    ```
</details>