from random import randrange 
import sys
from time import sleep
print("Подождите Игра Загружается...")
sleep(2)
print("Камень,Ножницы,Бумага")
print("=====================")
print("______________")
print("|v4.4        |")
print("|1.Играть    |")
print("|2.Обновления|")
print("|3.Кредиты   |")
print("|4.Мануал    |")
print("|5.Выйти     |")
print("______________")
b =  int(input("Введи Число: "))
if b == 1:
    print("Выбери Режим")
    print("1.Игра Против Бота")
    o = int(input("Введи Число: "))
    if o == 1:
        print("1.Камень")
        print("2.Ножницы")
        print("3.Бумага")
        a = int(input("Выбери Предмет: "))
        if a == 1:
            print("Ваш Выбор Камень")
            sleep(1)

        if a == 2:
            print("Ваш Выбор Ножницы")
            sleep(1)

        if a == 3:
            print("Ваш Выбор Бумага")
            sleep(1)

        if o == 1:
            comp = randrange(3) + 1
            if comp == 1:
                print("Выбор Компьютера КАМЕНЬ")
                sleep(1)

            elif comp == 2:
                  print("Выбор Компьютера НОЖНИЦЫ")
                  sleep(1)

            elif comp == 3:
                  print("Выбор Компьютера БУМАГА")
                  sleep(1)

            if comp == a:
                  print("НИЧЬЯ")
            

            elif comp == 1 and a == 2 or comp == 2 and a == 3 or comp == 3 and a == 1:
                print("Компуктер Победил") 


            elif comp == 2 and a == 1 or comp == 3 and a == 2 or comp == 1 and a == 3:
                print("Ты Победил")

if b == 2:
    print("     ЧейнжЛоги ")
    print("     ========= ")
    print("     1. ChangeLog v2.1")
    print("0.Выйти")
    q = int(input("Выбери Действие: "))
    if q == 1: 
        print("Версия 2.1 Одно Из Самых Крупных Обновлений.В Этом Обновлении Полностью Обновился Интерфейс Добавились Новые Вкладки В Том Числе И Вкладка Обновления Откуда Вы Читаете Данный Текст")
        print("1.Выйти")
        n = int(input("Выберите Действие: "))
        if n == 1:
            sleep(1)
            print("Сохранение...")
            sleep(1)
            print("Выход")
            sys.exit()
    if q == 0:
        sys.exit()
        

        
elif b == 3:
    print("Автор Игры: Исайка")
    sleep(2)
    print("Помощь В Создании: Негр(Линар)")
    sleep(2)
    print("Действия")
    sleep(2)
    print("0.Выход")
    f = int(input("Выберите Действие: "))
    if f == 0:
        print("Сохранение...")
        sleep(1)
        print("Выход...")
        sleep(1)
        sys.exit()



elif b == 4:
    print("    МАНУАЛ")
    print("    ======")
    sleep(3)
    print("Чтобы начать играть выберите пункт 1.")
    sleep(3)
    print("Далее выберите пункт 1.Одиночная Игра")
    sleep(3)
    print("Затем выберите предмет камень ножницы или бумага")
    sleep(2)
    print("Действия: ")
    print("1.Выйти")
    u = int(input("Выберите Действие: "))
    if u == 1:
        sys.exit()



elif b == 5:
    print("Сохранение...")
    sleep(1)
    print("Выход...")
    sleep(1)
    sys.exit()
