'''
NAME:KELVIN NZIOKA
REG_NO: PA106/G/9983/20
'''

# Function to check if a number is even or odd
def is_odd_even(x):
    return x % 2 == 0

# Input a number from the user
user_input = int(input("Enter number: "))

# Check if the number is even or odd using the is_odd_even function
if is_odd_even(user_input):
    print("The number is even.")
else:
    print("The number is odd.")
