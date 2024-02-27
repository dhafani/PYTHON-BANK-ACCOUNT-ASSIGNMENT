
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print("Current balance:", self.balance)

    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Balance:", self.balance)


# Example usage:
if __name__ == "__main__":
    # Creating a BankAccount object
    account = BankAccount("1234567890", 1000, "2024-02-27", "shaban chai")

    # Depositing and checking balance
    print("Deposited:", account.deposit(500))
    account.check_balance()

    # Withdrawing and checking balance
    print("Withdrawn:", account.withdraw(200))
    account.check_balance()

    # Trying to withdraw more than balance
    print("Withdrawn:", account.withdraw(2000))

    # Printing customer details
    account.customer_details()





