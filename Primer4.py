#Петя впервые пришел на урок физкультуры в новой школе. Перед началом 
# урока ученики выстраиваются по росту, в порядке невозрастания. 
# Напишите программу, которая определит на какое место в шеренге Пете 
# нужно встать, чтобы не нарушить традицию, если заранее известен рост 
# каждого ученика и эти данные уже расположены по невозрастанию 
# (то есть каждое следующее число не больше предыдущего). Если в 
# классе есть несколько учеников с таким же ростом, как у Пети, то
# программа должна расположить его после них.

import sys
def dataInput(st):
    try:
      n = int(input(st)) # Число N
      if n==0:
        print("Вы ввели 0")
        sys.exit()  
    except ValueError:
        print("Вы ввели не число")
        sys.exit() 
    return n  

def dataRost(x):
    a = []
    try:
        for i in range(x):
            a.append(int(input(f"Введите рост всех учеников: {i+1} ученик. ")))
    except ValueError:
        print("Вы ввели не число")
        sys.exit()
    return a       
        
student=dataInput("Введите количество учеников - ")
rostSt=dataRost(student)
rost=dataInput("Введите рост Пети - ")

rostSt.sort()
# print (rostSt)
j=0
for i in range(student):
    if rostSt[i]<= rost: #and rost < rostSt[i+1]
         j=i+1
    
rostSt.insert(j,rost)
print(rostSt)
print (f"{j+1} - Место")
        