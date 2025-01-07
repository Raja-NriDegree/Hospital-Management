def is_armstrong_number(num):
    # Convert the number to a string to get the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of the digits raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum of powers equals the original number
    return sum_of_powers == num

# Example usage:
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
