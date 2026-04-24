class BankAccount:
    def __init__(self, owner, initial_balance=0.0):
        self.owner = owner
        self.__balance = initial_balance  # Private attribute

    def check_balance(self):
        """Check current balance."""
        print(f"\n{'='*35}")
        print(f"  Account Owner : {self.owner}")
        print(f"  Current Balance: ₹{self.__balance:,.2f}")
        print(f"{'='*35}")
        return self.__balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            print("❌ Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"✅ ₹{amount:,.2f} deposited successfully.")
        print(f"   New Balance: ₹{self.__balance:,.2f}")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print(f"❌ Insufficient funds! Available balance: ₹{self.__balance:,.2f}")
            return
        self.__balance -= amount
        print(f"✅ ₹{amount:,.2f} withdrawn successfully.")
        print(f"   Remaining Balance: ₹{self.__balance:,.2f}")


# ──────────────────────────────────────────
# Main Menu
# ──────────────────────────────────────────
def main():
    name = input("Enter account holder name: ")
    initial = float(input("Enter initial deposit amount (₹): "))
    account = BankAccount(name, initial)

    while True:
        print("\n--- Bank Menu ---")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            account.check_balance()

        elif choice == "2":
            amount = float(input("Enter withdrawal amount (₹): "))
            account.withdraw(amount)

        elif choice == "3":
            amount = float(input("Enter deposit amount (₹): "))
            account.deposit(amount)

        elif choice == "4":
            print("Thank you for banking with us. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()