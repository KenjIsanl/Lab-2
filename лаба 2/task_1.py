money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
if money_capital + salary < spend:
    debt_free_counter = 0
else:
    debt_free_counter = 0
    while money_capital + salary >= spend:
        spend += spend * increase
        money_capital -= spend - salary
        debt_free_counter += 1
print("Количество месяцев, которое можно протянуть без долгов:", debt_free_counter)
