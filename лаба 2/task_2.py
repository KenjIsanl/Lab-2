salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
while months > 0:
    money_capital += spend - salary
    months -= 1
    spend += spend * increase
round_money_capital = int(money_capital // 1) + (1 if money_capital % 1 > 0 else 0)
print(f"Подушка безопасности, чтобы протянуть 10 месяцев без долгов:", round_money_capital)
