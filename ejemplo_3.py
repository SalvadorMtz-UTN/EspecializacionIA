print("Conversion de tipos de datos")
int_a = 20
print(int_a,type(int_a))
float_a = float(int_a)
print(float_a,type(float_a))

string_a = str(int_a)
print(string_a, type(string_a))

complex_a = complex(int_a)
print(complex_a,type(complex_a))

bool_a = bool(int_a)
print(bool_a,type(bool_a))

print("Operaciones")
a = 5
b = 10

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# operaciones de comparacion
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

print("Operaciones logicas")
c = True
d = False

# Operaciones logicas
print(c or d)
print(a > 10) and (a > b)
#print(a xor b)
#print(a nand b)

print("Operaciones de asignacion")
x = 5
print(x)

x += 10 # x = x + 10
print(x)

x ** 2 # x = x * x
print(x)

print("Membership operators")

list1 = [8, 20, 19, 16]
print(8 not in list1)

print("Indexacion")

list_1 = [80, 20, 18, 19, 17]
list_1 = "Python"

# 0, 1, 2, 3, 4
# -5, -4, -3, -2, -1
print(list_1[0])
print(list_1[0:4])      # 0:3
print(list_1[-5:-1])    # -5:-2
