import time

class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.history = []

    def check_pin(self, pin):
        return self.pin == pin  # Verifies the entered PIN

    def check_balance(self):
        print(f"Your total balance is: Rs.{self.balance:.2f}\n")  # Displays the balance
        self.history.append(f"{time.ctime()}: Checked balance")

    def cash_deposit(self, amount):
        if amount <= 0:
            print("Please enter a valid amount to deposit.\n")
            return
        self.balance += amount  # Cash deposit into the account
        print(f"You have deposited Rs.{amount:.2f}")
        print(f"Your total balance is Rs.{self.balance:.2f}\n")
        self.history.append(f"{time.ctime()}: Deposited Rs.{amount:.2f}")

    def cash_withdrawal(self, amount):
        if amount <= 0:
            print("Please enter a valid amount to withdraw.\n")
            return
        if amount > self.balance:  # Checks if there is sufficient balance to withdraw the entered amount
            print("Insufficient balance in your account.\n")
        else:
            self.balance -= amount  # Cash withdrawal from the account
            print(f"You have withdrawn Rs.{amount:.2f}")
            print(f"Your total balance is Rs.{self.balance:.2f}\n")
            self.history.append(f"{time.ctime()}: Withdrawn Rs.{amount:.2f}")

    def change_pin(self, new_pin):
        if len(str(new_pin)) != 4 or not str(new_pin).isdigit():
            print("PIN must be a 4-digit number.\n")
            return
        self.pin = new_pin  # Changes the user's PIN
        print("PIN changed successfully.\n")
        self.history.append(f"{time.ctime()}: Changed PIN")

    def transaction_history(self):
        if not self.history:  # Checks if there is any transaction history
            print("No transactions yet.\n")
        else:
            print("Transaction History:")  # If there is, it displays the transaction history
            for history in self.history:
                print(history)
            print()  # For better formatting


def main():
    atm = ATM(pin=1234, balance=5000.00)  # Initializes default PIN and account balance

    max_attempts = 3
    attempts = 0

    # Loop to verify PIN, allowing a maximum of 3 attempts
    while attempts < max_attempts:
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin.isdigit() and atm.check_pin(int(entered_pin)):
            break # Exit loop if PIN is correct
        else:
            attempts += 1
            print(f"Incorrect PIN. {max_attempts - attempts} attempt(s) left.\n")
    else:
        print("Too many incorrect attempts. Exiting.")
        return # Exit the program after too many incorrect attempts

    # Main loop to display ATM options and perform actions
    while True:
        print("\n**** Welcome to the ATM ****")
        print("1: Check Balance")
        print("2: Deposit")
        print("3: Withdraw")
        print("4: Change PIN")
        print("5: Transaction History")
        print("6: Exit\n")
        choice = input("Choose an option: ")

        if choice == "1":
            atm.check_balance()

        elif choice == "2":
            amount = input("Enter amount to deposit: Rs.")
            if amount.replace('.', '', 1).isdigit():
                atm.cash_deposit(float(amount))
            else:
                print("Invalid amount. Please enter a numeric value.\n")

        elif choice == "3":
            amount = input("Enter amount to withdraw: Rs.")
            if amount.replace('.', '', 1).isdigit():
                atm.cash_withdrawal(float(amount))
            else:
                print("Invalid amount. Please enter a numeric value.\n")

        elif choice == "4":
            new_pin = input("Enter a new 4-digit PIN: ")
            if new_pin.isdigit():
                atm.change_pin(int(new_pin))
            else:
                print("PIN must be a 4-digit number.\n")

        elif choice == "5":
            atm.transaction_history()

        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main() # Run the main function to start the program