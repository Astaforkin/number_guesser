import random
number = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку!")
print("Программа сгенерировала число от 1 до 100, ваша задача угадать его как можно быстрее")
num = int(input('Ваше предполагаемое число равно ='))
if num == number:
    print("Вы угадали, поздравляем!")
elif num > number:
    print("Слишком много, попробуйте еще раз")
else:
    print("Слишком мало, попробуйте еще раз")