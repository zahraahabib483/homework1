class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest Applied: ${interest:.2f}")
        print(f"New Balance: ${self.balance:.2f}")

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}, Interest Rate: {self.interest_rate}%"

# إنشاء كائن من فئة BankAccount
account = BankAccount("2788", "زهراء")

# إجراء عملية إيداع بمبلغ 1000 دولار
account.deposit(1000)

# إجراء عملية سحب بمبلغ 500 دولار
account.withdraw(500)

print(account)

# إنشاء كائن من فئة SavingsAccount
savings = SavingsAccount("2789", "زهراء حبيب", 35)

# إجراء عملية إيداع بمبلغ 1000 دولار
savings.deposit(1000)

# تطبيق الفائدة وطباعة الرصيد الحالي والمعدل
savings.apply_interest()
print(savings)
