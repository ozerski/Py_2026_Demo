# ДЗ 01_02_2
def calculate_annuity_payment(amount: int | float, annual_rate: float, months: int) -> float:
    print(amount)
    print(annual_rate)
    print(months)
    # Переводим годовую ставку в месячную (десятичная дробь)
    monthly_rate = annual_rate / 100 / 12
    print(monthly_rate)
    # Рассчитываем коэффициент аннуитета
    coefficient = (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    print(coefficient)
    # Рассчитываем ежемесячный платеж
    payment = amount * coefficient
    print(payment)
    # Округляем результат до двух знаков после запятой
    return round(payment, 2)

amount = 500000  # Сумма кредита
annual_rate = 15.5  # Годовая ставка (15.5%)
months = 24  # Срок кредита (24 месяца)
print(calculate_annuity_payment(amount, annual_rate, months))  # Output: 24349.16