
def digitSum(n):
    ans = 0
    while (n > 0):
        rem = n % 10
        ans = ans+rem
        n = n//10
    print(f'The sum of digits is : {ans}')


def rev(n):
    ans = 0
    while(n > 0):
        rem = n % 10
        ans = ans*10+rem
        n = n//10
    print(f'Reverse of number is: {ans}')
    return ans


def primeCheck(n):
    for i in range(2, n):
        if(n % i == 0):
            print(f'The entered number {n} is NOT PRIME')
            break
        else:
            print(f'The entered number {n} is PRIME')
            break


def palindrome(n):
    # r =
    if(n == rev(n)):
        print(f'The number {n} is PALINDROME')
    else:
        print(f'The number {n} is NOT PALINDROME')


n = int(input("ENTER THE NUMBER: "))
print("\n\t****MENU****")
choice = 1
while(choice != 0):
    print("\n1. Sum of digits of number\n2. Reverse of number\n3. Checking number is prime or not\n4. Checking for palindrome\n0. EXIT\n")
    choice = int(input("ENTER CHOICE: "))
    print("\n")
    if(choice == 1):
        digitSum(n)
    elif(choice == 2):
        rev(n)
    elif(choice == 3):
        primeCheck(n)
    elif(choice == 4):
        palindrome(n)
    elif(choice == 0):
        print("EXITING!......")
    else:
        print("Enter correct option!....")
