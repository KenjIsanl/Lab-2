money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
remains = money_capital + salary - spend
debt_free_counter = 1
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while remains > spend:
    remains -= spend
    remains += salary
    debt_free_counter += 1
    spend += increase * spend
print("Количество месяцев, которое можно протянуть без долгов:", debt_free_counter)
