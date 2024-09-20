from random import randint
from decouple import config

start = int(config('ATTEMPS'))
diap1 = int(config('DIAPASON'))
diap2 = int(config('DIAPASONDVA'))
initial_balance = int(config('START_CAPITAL'))

def logic():

    global initial_balance
    secret = randint(diap1, diap2)
    print(' "Угадай число"!')
    print("Я загадала число от", diap1, "до", diap2)
    print(f'Ваш баланс {initial_balance}')

    while initial_balance > 0:
        print("На какую цифру вы хотите поставить ставку ?")
        syfra = int(input())
        if syfra < diap1 or syfra > diap2:
            print("Неверный ввод")
            break

        print("Введите сколько вы хотите поставить на эту цифру ?")
        suma = int(input())
        if suma > initial_balance or suma < 1:
            print("Неверный ввод")
            break

        if syfra == secret:
            print(f" Вы угадали число: {secret} и получили {suma} баллов\n")
            initial_balance += suma
        else:
            print(f" вы не угадали число: {secret} и потеряли {suma} баллов\n")
            initial_balance -= suma

        if initial_balance > 0:
            play = input(f'Хотите ли вы поставить еще ставку? Ваш баланс {initial_balance}.\n(yes/)')
            if play == 'yes':
                continue
            elif play == 'q':
                break
        else:
            print("У вас закончились баллы.")

    print("\nИгра завершена. Поздравляем! Ваш баланс:", initial_balance)

if __name__ == '__main__':
    logic()