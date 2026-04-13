balance = 1000

while True:
    print("\n--- Банкомат ---")
    print("1. Проверить баланс")
    print("2. Снять деньги")
    print("3. Пополнить счет")
    print("4. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        print("Ваш баланс:", balance)

    elif choice == "2":
        amount = int(input("Сколько снять: "))
        if amount <= balance:
            balance -= amount
            print("Снятие успешно")
        else:
            print("Недостаточно средств")

    elif choice == "3":
        amount = int(input("Сколько внести: "))
        balance += amount
        print("Пополнение успешно")

    elif choice == "4":
        print("До свидания!")
        break

    else:
        print("Неверный выбор")
    
