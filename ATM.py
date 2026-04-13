from operations import check_balance, withdraw_money, deposit_money


def display_menu():
    print("\n=== Банкомат ===")
    print("1. Проверить баланс")
    print("2. Снять деньги")
    print("3. Пополнить счет")
    print("4. Выход")


def main():
    balance = 1000.0

    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = withdraw_money(balance)

        elif choice == "3":
            balance = deposit_money(balance)

        elif choice == "4":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
