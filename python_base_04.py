proceed = float(input('Введите значение выручки: '))
cost = float(input('Введите значение издержек: '))

if cost < proceed:
    people = int(input('Введите количество сотрудников: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {((proceed - cost) / people):.2f}')
    print(f'Рентабельность выручки: {((proceed - cost) / proceed * 100):.2f}%') # приводим к 2 зн после запятой
elif cost == proceed:
    print('Фирма работает в ноль.')
else:
    print('Фирма работает в убыток!')