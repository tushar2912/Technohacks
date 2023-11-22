class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your balance is ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"${amount} deposited successfully. Your new balance is ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds. Withdrawal failed."
        else:
            self.balance -= amount
            return f"${amount} withdrawn successfully. Your new balance is ${self.balance}"

def main():
    atm = ATM()

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(atm.check_balance())
        elif choice == "2":
            amount = float(input("Enter the amount to deposit: $"))
            print(atm.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter the amount to withdraw: $"))
            print(atm.withdraw(amount))
        elif choice == "4":
            print("Exiting the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()