# Python program to check Armstrong

# Function to count digit in number
def count_digit(n):
    count = 0
    while n:
        n //= 10
        count += 1
    return count

# Function to check Armstrong
def check_armstrong(n):
    number_copy = n
    arm_sum = 0
    digit = count_digit(n)
    while n:
        remainder = n%10
        arm_sum += remainder**digit
        n //= 10

    return arm_sum == number_copy

# Reading number
number = int(input('Enter number: '))

# Making decision
if check_armstrong(number):
    print('%d is ARMSTRONG.' %(number))
else:
    print('%d is NOT ARMSTRONG.' %(number))
