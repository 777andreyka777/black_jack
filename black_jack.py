import random

cards = [6,7,8,9,10,2,3,4,11] * 4

random.shuffle(cards)

print('Поиграем в очко? ')
count = 0

while True:
    choice = input('Будете брать карту? y/n: ')
    if choice == 'y':
        current = cards.pop()
        print(f'Вам попалась карта достроинтсвом {current}')
        count += current
        if count > 21:
            print('Не повезло! вы проиграли!')
            break
        elif count == 21:
            print('Поздравляю. Вы победили')
            break
        else:
            print(f'У вас {count} очков')   
    elif choice == 'n':
        print(f'У вас {count} очков. Вы завершили игру.')
        break
    else:
        print('Выберите пожалуйста "y" или "n" ')
print('До свидание. Хорошего дня')
    