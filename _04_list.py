### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [45, 40, 38, 14, 12, 12, 18]
print(my_list)  
print(len(my_list))

my_other_list = ["Hola", "Mundo", "Python", 2021, 3.14]
print(my_other_list)
print(len(my_other_list))

print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1]) # Forma de obtener el último elemento
print(my_other_list[-4])

print(my_list.count(12))

#age, height, name, surname = my_other_list


print(my_list + my_other_list)

my_other_list.append("MKY")
print(my_other_list)

my_other_list.insert(1, "insert")
print(my_other_list)

my_other_list.remove("MKY")
print(my_other_list)

print(my_list.pop())
print(my_list)

del my_list[2]
print(my_list)

my_other_list[1] = "Mundo 2"
print(my_other_list)

my_new_list =my_list.copy()
print(my_new_list)

my_list.clear()
print(my_list)  
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:4])