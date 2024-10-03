# Function to count digits in a number using a while loop
def count_digits(number):
    count = 0
    
    # If the number is negative, make it positive
    if number < 0:
        number = -number
    
    # Loop to count digits
    while number > 0:
        number //= 10  # Remove the last digit
        count += 1  # Increment the count for each digit
    
    # If the number is 0, it has 1 digit
    if count == 0:
        count = 1
    
    return count

# Input from the user
num = int(input("Enter a number: "))

# Call the function and display the result
total_digits = count_digits(num)
print(f"Total number of digits in {num} are {total_digits}")