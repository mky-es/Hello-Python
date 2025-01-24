### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)    

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scaped_string = "\\tEste es un String \\n escapado"
print(my_scaped_string)

# Formateo

print ("Mi nombre es Antonio Jose García")

name, surname, age  = "Antonio", "García", 45

print ( "Mi nomre es {} {} y mi edad es {}".format(name, surname, age))
print ( "Mi nomre es %s %s y mi edad es %s"%(name, surname, age))


print (f"Mi nomre es {name} {surname} y mi edad es {age}")

### Desempaquetado de caracteres ###
language = "Python"
a , b , c , d, e, f = language
print(a)
print(e)
