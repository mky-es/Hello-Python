# 1. Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len().
variable_text = "Aprendiendo Python"
print(len(variable_text))

# 2. Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.
print("Hola" + "Python")

# 3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.
cadena_salto = "Hola\nMundo"
print(cadena_salto)

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
name, surname, age ="Antonio", "García", 45
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# 5. Desempaqueta los caracteres de la palabra “Python” en variables separadas y luego imprímelos uno por uno.
a, b, c, d, e, f = "Python"
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 6. Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.
slice = "Programacion"
language_slice = slice[3:7]
print(language_slice)

# 7. Invierte la cadena “Python” usando slicing y muestra el resultado.
language = "Python"
reversed_languaage = language [::-1]
print(reversed_languaage)

# 8. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.
upper = "aprendiendo python"
print(upper.upper()) 

# 9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.
cadena = "Programación en Python"
print(cadena.count("n"))


# 10. Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado.
cadena = "12345"
print(cadena.isnumeric())
