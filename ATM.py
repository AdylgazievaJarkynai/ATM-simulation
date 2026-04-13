def display_menu():
    print("\n=== ATM Simulator ===")
    print("1. Check balance")
    print("2. Withdraw money")
    print("3. Deposit money")
    print("4. Exit")


def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a number.")


def check_balance(balance):
    print(f"Your current balance: {balance:.2f}")


def withdraw_money(balance):
    amount = get_valid_amount("Enter amount to withdraw: ")

    if amount > balance:
        print("Insufficient funds.")
        return balance

    balance -= amount
    print("Withdrawal successful.")
    return balance


def deposit_money(balance):
    amount = get_valid_amount("Enter amount to deposit: ")
    balance += amount
    print("Deposit successful.")
    return balance


def main():
    balance = 1000.0

    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = withdraw_money(balance)

        elif choice == "3":
            balance = deposit_money(balance)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()

    
