#Требуется найти наименьший натуральный делитель целого числа N, 
# отличный от 1.
import sys

try:
    N = int(input("Введиите число N - ")) # Число N
    if N==0 or N==1:
        print("Вы ввели 0 или 1")
        sys.exit()  
except ValueError:
    print("Вы ввели не число")
    sys.exit() 

i = 2
while N%i != 0:
    i += 1
print(i)        