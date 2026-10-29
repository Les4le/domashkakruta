
class BankAccount:
    def __init__(self, owner, account_number, balance, currency):
        if not owner.strip():
            raise ValueError("Ім'я власника не може бути порожнім")

        if not account_number.strip():
            raise ValueError("Номер рахунку не може бути порожнім")

        if balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")

        if not currency.strip():
            raise ValueError("Валюта не може бути порожньою")

        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance
        self.__currency = currency

    @property
    def owner(self):
        return self.__owner

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @property
    def currency(self):
        return self.__currency

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сума поповнення має бути додатною")

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сума зняття має бути додатною")

        if amount > self.__balance:
            raise ValueError("Недостатньо коштів на рахунку")

        self.__balance -= amount

    def transfer(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise ValueError("Одержувач має бути банківським рахунком")

        if other_account is self:
            raise ValueError("Не можна переказати кошти на той самий рахунок")

        if self.__currency != other_account.currency:
            raise ValueError("Валюти рахунків мають збігатися")

        if amount <= 0:
            raise ValueError("Сума переказу має бути додатною")

        if amount > self.__balance:
            raise ValueError("Недостатньо коштів для переказу")

        self.__balance -= amount
        other_account.deposit(amount)

    def has_funds(self, amount):
        if amount <= 0:
            raise ValueError("Сума має бути додатною")

        return self.__balance >= amount

    def show_info(self):
        print(f"Власник: {self.__owner}")
        print(f"Номер рахунку: {self.__account_number}")
        print(f"Баланс: {self.__balance:.2f} {self.__currency}")
