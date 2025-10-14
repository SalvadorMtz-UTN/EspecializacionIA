print("ejemplo_2")

print("Datos numericos")

a = 5       #int
b = 5.3     #float
c = 5 + 2j  #complejo

print(a, b, c)

print(type(a))
print(type(b))
print(type(c))

b = int(5.3)
print(b,type(b))


print("Datos tipo secuencia")
string_1 = "Casa"
string_2 = 'Auto'
string_3 = '''
Linea1
Linea2
'''
string_4 = "Hola gran mundo            "

print(string_1,string_1.upper())
print(string_1,string_1.lower())
print(string_4,string_4.strip(),string_1)
print(string_4,string_4.split())
#print(string_2)
#print(string_3)

string_5 = string_1 + string_2
string = string_1 +  " "+ string_2
print(string_5)

name = "Salvador"
age = 51
string_6 = "Hola {}, tienes {} años".format(name,age)
string_7 = f"Hola {name}, tienes {age} años"
print(string_6)
print(string_7)
string_8 = "Hola \na \ntodos"
print(string_8)

print("Datos tipo secuencia: Listas")

list1 =[5, 8, 9, 10, 1, 2, 3]
print(list1)
list1[3] = 55
print(list1)
list2 = [True, "Auto", 3.5, 5, 8, 9, 2, 10, 10, 10]
print(list2)

print(len(list1))
print(len(list2))
print(list2.index(10))
list1.sort()
print(list1)

list1.pop()
print(list1)

list1.pop(2)
print(list1)

list1.pop(list1.index(8))
print(list1)

list1.reverse()
print(list1)

list1.append("Auto")
print(list1)

list1.insert(3,"Auto")
print(list1)

print(list1.count(8))
print(list2.count(10))

list1.remove("Auto") #Todas las apariciones de "Auto"
print(list1)

del list1[0]
print(list1)

print("Datos tipo secuencia: Tuplas")

tupla1 = (20, 80, 60)
print(tupla1, type(tupla1))
tupla2 = ("Car", 3.5, 8, 9)
print(tupla2[0])
#tupla2[0] = "Auto"

tupla2 = ("Auto", 3.5, 8)
print(tupla2)

print("Datos mapping")

dict1 = {"a":10,"b":3.5,"key3":5,"x":0}
print(dict1)
print(dict1["a"])
print(len(dict1))

del dict1["a"]
print(dict1)

dict1["key3"] = "Hoja"
print(dict1)

print(dict1.keys())
#print(type(dict1.keys()))

list2 = list(dict1.keys())
print(list2)
print(type(list2))

set_1 = {8, 9, 10, 11, 12}
set_2 = frozenset({9, 17, 20})

print(set_1,type(set_1))

set_1.add(7)
print(set_1,type(set_1))

print("Tipo boleano")

a = True
b = True

print(a, b)
