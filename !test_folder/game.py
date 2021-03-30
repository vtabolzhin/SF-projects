import random

count = 0       # счетчик попыток
number = random.randint(100, 100)   # загадываем случайное число
print("Загадано число от 1 до 100")

while True:                 # бескнечый цикл
    predict = int(input())  # пытаемся угадать число вслепую
    count += 1              # добавляем попытку в счетчик попыток
    if number == predict: break # выход из цикла, если угадали
    elif number > predict: print(f"Загаданное число больше {predict}")
    else: print(f"Загаданное число меньше {predict}")
print(f"Вы угадали число за {count} попыток.")

