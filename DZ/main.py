
from finance import BankAccount

try:
    account1 = BankAccount(
        "Олена",
        "UA1001",
        5000,
        "UAH"
    )

    account2 = BankAccount(
        "Андрій",
        "UA1002",
        1500,
        "UAH"
    )

    print("Початковий стан:")
    account1.show_info()

    print("\nПоповнення рахунку:")
    account1.deposit(1000)
    print(f"Баланс: {account1.balance:.2f} UAH")

    print("\nЗняття коштів:")
    account1.withdraw(500)
    print(f"Баланс: {account1.balance:.2f} UAH")

    print("\nПереказ 2000 UAH Андрію:")
    account1.transfer(account2, 2000)

    print("Рахунок Олени:")
    account1.show_info()

    print("\nРахунок Андрія:")
    account2.show_info()

    print("\nПеревірка коштів:")
    print(account1.has_funds(1000))

    # Перевірка обробки помилок
    account1.withdraw(100000)

except ValueError as error:
    print(f"Помилка: {error}")
