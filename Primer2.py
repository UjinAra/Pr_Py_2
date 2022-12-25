# Требуется посчитать сумму целых чисел, расположенных между числами 
# 1 и N включительно.
import sys

try:
    x = int(input("Введиите число N - ")) # Число N
    if x==0:
        print("Вы ввели 0")
        sys.exit()  
except ValueError:
    print("Вы ввели не число")
    sys.exit() 
sum=0
if x>0:
    for i in range(x+1):
       sum = sum+i
else:
    sum=1
    for i in range(-x+1):
       sum = sum-i

print(f"Сумма целых чисел - {sum}")