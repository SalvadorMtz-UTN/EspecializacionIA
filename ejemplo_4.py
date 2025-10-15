'''
x = 2
i = 0

while x < 10:
   i += 1
   print(i,x)
   x += 2


x = 2
i = 0

while True:  #Corrida sin fin"
   i += 1
   print(i,x)
   x += 2


print(x < 10)

while True:
   i += 1
   print(i,x)
   x += 2
   if x > 10:
    break
   
   '''

x = 2
i = 0

while x < 12:
   i += 1
   x += 2
   if x == 8:
      continue
   print(i,x)
   

for x in range(6):
    if x == 2:
        continue
    print(x)

arreglo = list(range(2,5))
print(arreglo)

for x in range(10):
    if x in arreglo:
        continue
    print(x)