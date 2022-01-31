import random


def is_valid(num):

    #Проверяет, что num является целым числом от 1 до 100
    
    if num.isdigit():
        if 1 <= int(num) <= 100:
            return True
        else:
            print("А может быть все-таки введем целое число от 1 до 100?'")
            return False
    else:
        print("А может быть все-таки введем целое число от 1 до 100?'")
        return False
    
number = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку!")

print("Программа сгенерировала число от 1 до 100, ваша задача угадать его как можно быстрее")

while True:
    num = input('Ваше предполагаемое число равно =')
    if is_valid(num) == True:
        if num == number:
            print("Вы угадали, поздравляем!")
        elif num > number:
            print("Ваше число больше загаданного, попробуйте еще разок")
        else:
            print("Ваше число меньше загаданного, попробуйте еще разок")

    