# Custom exception
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"You tried to withdraw ${amount}, but only ${balance} is available.")


# Start of program
try:
    name = input("Enter your name: ")
    balance = float(input("Enter starting balance: "))
    print(f"Welcome, {name}! Your starting balance is ${balance}.")

    while True:
        action = input("Do you want to deposit or withdraw? (type 'exit' to quit): ").strip().lower()

        if action == 'exit':
            break
        elif action not in ['deposit', 'withdraw']:
            print("Please type 'deposit', 'withdraw', or 'exit'.")
            continue

        amount = float(input(f"Enter amount to {action}: "))
        if amount <= 0:
            raise ValueError("Amount must be more than 0.")

        if action == 'deposit':
            balance += amount
            print(f"You deposited ${amount}. New balance: ${balance}")
        elif action == 'withdraw':
            if amount > balance:
                raise InsufficientFundsError(balance, amount)
            balance -= amount
            print(f"You withdrew ${amount}. Remaining balance: ${balance}")

except InsufficientFundsError as e:
    print(f"Bank error: {e}")
except ValueError as ve:
    print(f"Input error: {ve}")
finally:
    print("Thanks for using the bank system.")
