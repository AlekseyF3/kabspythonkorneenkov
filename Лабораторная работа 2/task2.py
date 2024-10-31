salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = spend - salary
for i in range(1, months):
    spend *= (1 + increase)
    money_capital += spend - salary
    if ((money_capital * 10) % 10 != 0):
        money_capital = int(money_capital) + 1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
