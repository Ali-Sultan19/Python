# Custom exception
class TooSmallError(Exception):
    pass

# Program that uses the custom error
try:
    number = int(input("Enter a number greater than 10: "))
    if number <= 10:
        raise TooSmallError("The number is too small!")
    print("Thank you! The number is acceptable.")
except TooSmallError as e:
    print(f"Custom Error: {e}")
except ValueError:
    print("Please enter a valid number.")
finally:
    print("Program finished.")
