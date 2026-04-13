def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Сумма должна быть больше нуля.")
            else:
                return amount
        except ValueError:
            print("Ошибка ввода. Введите число.")


def check_balance(balance):
    print(f"Ваш баланс: {balance:.2f}")


def withdraw_money(balance):
    amount = get_valid_amount("Введите сумму для снятия: ")

    if amount > balance:
        print("Недостаточно средств.")
        return balance

    balance -= amount
    print("Снятие успешно.")
    return balance


def deposit_money(balance):
    amount = get_valid_amount("Введите сумму для пополнения: ")
    balance += amount
    print("Пополнение успешно.")
    return balance
