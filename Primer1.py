# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а 
# некоторые – гербом. Определите минимальное число монеток, которые 
# нужно перевернуть, чтобы все монетки были повернуты вверх одной и 
# той же стороной.
import random
import sys

a=[]
try:
    x = int(input("Введиите количество монет - ")) # Кол-во монет
    if x==0:
        print("Вы ввели 0")
        sys.exit()  
except ValueError:
    print("Вы ввели не число")
    sys.exit()  
     

for i in range(x): # Разложили монетки в произвольном порядке 0-орел, 1-решка
    a.append(random.randint(0,1))

print (a)
reshka=0
orel=0
for j in range(x): # Разложили монетки в произвольном порядке 0-орел, 1-решка
    if a[j]==1:
        reshka=reshka+1
    else:
         orel=orel+1
print(f"Орел - {orel}")
print(f"Решка - {reshka}")

if reshka>orel:
    print(f"Необходимо перевернуть Орла - {orel} шт.")
else:
     print(f"Необходимо перевернуть Решку - {reshka} шт.")