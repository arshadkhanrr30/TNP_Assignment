# Name : Arshad khan
# Enrollment : 0176CD231031
# Batch : 5 (MTF)
# Batch time : 10:30 AM

# Conditional Statement 
# 1. Basic if else problem 

#Q1
number = int(input("Enter a number: "))
if(number>0):
    print("The number is Positive.")
elif(number<0):
    print("The number is Negative.")
else:
    print("The number is Zero.")

#Q2
num = int(input("Enter a number: "))
if(num % 2) == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

#Q3
year = int(input("Enter a year: "))
if ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#Q4
a=int(input("enter the number"))
b=int(input("enter the number"))
if(a>b):
    print("A is greater")
else:
    print("B is greater")

#Q5
age=int(input("Enter age"))
if (age>=18):
    print("Person eligible to vote")
else:
    print("Person not eligible to vote")

#Q6
char=input("enter the character")
if(char=="a"or char=="e"or char=="u"or char=="i"or char=="o"):
    print("The Character is a vowel")
else:
    print("character is consonent")

#Q7
num=int(input("Enter number"))
if(num % 5==0):
    print("the number is divisible by 5")
else:
    print("the number is not divisible by 5")

#Q8
num=int(input("Enter number"))
if(num<10):
    print("the number is a one-digit number")
elif(num<100):
    print("the number is a two-digit number")
else:
    print("the number is more than two-digit number")

#Q9
marks=int(input("Enter marks"))
if(marks>=40):
    print("student has Passed")
else:
    print("student has Failed")

#Q10
num=int(input("Enter num"))
if(num%3==0 and num%7==0):
    print("the number is multiple of both 3 and 7")
else:
    print("number is not  multiple of both")



# 2. ladder if & Nested if 

#Q1
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if (a >= b and a >= c):
    print("The greatest number is:", a)
elif (b >= a and b >= c):
    print("The greatest number is:", b)
else:
    print("The greatest number is:", c)

#Q2
age = int(input("Enter age: "))
if(age < 13):
    print("The person is a Child")
elif(13 <= age <= 19):
    print("The person is a Teenager")
elif(20 <= age <= 59):
    print("The person is an Adult")
else:
    print("The person is a Senior")

#Q3
marks = int(input("Enter marks:"))
if(90 <= marks <= 100):
    print("Grade: A")
elif(75 <= marks <= 89):
    print("Grade: B")
elif(50 <= marks <= 74):
    print("Grade: C")
elif(35 <= marks <= 49):
    print("Grade: D")
elif(marks < 35):
    print("Grade: Fail")

#Q4
side1 = int(input("Enter side 1:"))
side2 = int(input("Enter side 2:"))
side3 = int(input("Enter side 3:"))
if(side1==side2==side3):
    print("Equivalent triangle")
elif(side1==side2 or side3==side1 or side2==side3):
    print("Isosceles triangle")
else:
    print("Scalene triangle")

#Q5
char = input("Enter a character:")
if len(char) != 1:
    print("Please enter exactly one character")
else:
    if char.isupper():
        print("The character is Uppercase")
    elif char.islower():
        print("The character is Lowercase")
    elif char.isdigit():
        print("The character is a Digit.")
    else:
        print("The character is a Special Symbol.")

#Q6
units=int(input('enter no of units:'))
if(units<=100):
    bill=units*5
    print("Your electricity bill is:",bill)
elif(units>100 and units<=200):
    bill=units*8
    print("Your electricity bill is:",bill)
else:
    bill=units*10
    print("Your electricity bill is:",bill) 

#Q7
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if(a > b):
    if(a > c):
        if(a > d):
            largest = a
        else:
            largest = d
    else:
        if(c > d):
            largest = c
        else:
            largest = d
else:
    if(b > c):
        if(b > d):
            largest = b
        else:
            largest = d
    else:
        if(c > d):
            largest = c
        else:
            largest = d

print("The largest number is:", largest)


#Q8
year = int(input("Enter year:"))
if(year % 100==0):
    if(year % 400==0 or year % 4==0 ):
        print("Given year is century and also a leap year")
    else:
        print("Year is century but not leap year")
else:
    print("Year is not century")


#Q9
weight = int(input("Enter weight :"))
height = int(input("Enter height :"))

bmi = weight / (height ** 2)
print(f"Your BMI is:",bmi)

if(bmi < 18.5):
    print("BMI: Underweight")
elif(18.5 <= bmi <= 24.9):
    print("BMI: Normal")
elif(25 <= bmi <= 29.9):
    print("BMI: Overweight")
else:
    print("BMI: Obese")

#Q10
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if(a < b):
    if(a < c):
        print("Smallest:",a)
    else:
        print("Smallest:",c)
else:
    if(b < c):
        smallest = b
    else:
        print("Smallest:",c)




# For loop problem

#Q1
print("Armstrong numbers between 100 and 999 are:")
for num in range(100, 1000):
    temp = num
    sum = 0
    while (temp > 0):
        digit = temp % 10       
        sum += digit**3 
        temp //= 10            
    
    if sum == num:
        print(num)

#Q2
n = int(input("Enters Prime you want from 2-100:"))
count = 0  
print("Here All prime number are:")
for num in range(2, 100):   
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        count += 1
    
    if count == n:   
        break
        
#Q3
for num in range(1, 501):
    if num % 3 == 0:   
        sum = 0
        temp = num
        while temp > 0:
            digit=temp%10
            sum +=digit
            temp //= 10
        
        if sum <= 10:
            print(num, end=" ")

#Q4
n = int(input("Enter the height of the pyramid: "))

for i in range(1, n+1):
    for j in range(n - i):
        print(" ",end="")
    for k in range(2 * i - 1):
        print("*",end="")
    print() 
        

#Q5
text = input("Enter a string: ").lower() 
is_pangram = True
for ch in "abcdefghijklmnopqrstuvwxyz":
    if ch not in text:
        is_pangram = False
        break

if is_pangram:
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")



#Q6
print("Twin primes between 1 and 100 are:")

for num in range(2, 100):
    is_num_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_num_prime = False
            break
    
    is_next_prime = True
    next_num = num + 2
    if next_num <= 100:
        for j in range(2, next_num):
            if next_num % j == 0:
                is_next_prime = False
                break
    else:
        continue
    
    if is_num_prime and is_next_prime:
        print(f"({num}, {next_num})")


#Q7
num = int(input("Enter a number: "))
temp = num
sum_of_digits = 0

for digit in str(temp):
    sum_of_digits += int(digit)

if num % sum_of_digits == 0:
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")


#Q8
n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1) 
    print()  

#Q9
n = int(input("Enter the value of n: "))
sum_of_series = 0

for i in range(1, n + 1):
    sum_of_series += i ** 2  

print("The sum of the series is:",sum_of_series)

#Q10
num = int(input("Enter a number: "))
temp = num
sum_of_factorials = 0

for temp_num in [temp]:  
    while temp > 0:
        digit = temp % 10
        fact = 1
        for i in range(1, digit + 1):
            fact *= i
        sum_of_factorials += fact
        temp //= 10

if sum_of_factorials == num:
    print(f"{num} is a Strong number.")
else:
    print(f"{num} is not a Strong number.")



#While Loop Problems:

#Q11
num = int(input("Enter a number: "))
temp = num
reverse_num = 0

while temp > 0:
    digit = temp % 10
    reverse_num = reverse_num * 10 + digit
    temp //= 10

print(f"Reverse of {num} is {reverse_num}")

is_prime = True
if reverse_num < 2:
    is_prime = False
else:
    for i in range(2, int(reverse_num ** 0.5) + 1):
        if reverse_num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{reverse_num} is a Prime number.")
else:
    print(f"{reverse_num} is not a Prime number.")


#Q12
total_sum = 0

while total_sum <= 100:
    num = int(input("Enter a number: "))
    temp = num
    digit_sum = 0
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    total_sum += digit_sum
    print(f"Sum of digits of {num} = {digit_sum}, Total sum = {total_sum}")

print("Stopped! Total sum of digits exceeded 100.")


#Q14
num = int(input("Enter a number: "))
seen = set()   

while num != 1 and num not in seen:
    seen.add(num)   
    sum_of_squares = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum_of_squares += digit * digit
        temp //= 10

    num = sum_of_squares  

if num == 1:
    print("It is a Happy Number.")
else:
    print("It is not a Happy Number.")


#Q15
num = int(input("Enter a number: "))
n = num
largest_prime = -1
factor = 2

while n > 1:
    if n % factor == 0:   
        largest_prime = factor
        n //= factor         
    else:
        factor += 1           

print(f"The largest prime factor of {num} is {largest_prime}")


#Q16
num = int(input("Enter a number: "))
temp = num

if str(num)[0] == "0":
    print(f"{num} is not a Duck number.")
else:
    is_duck = False
    while temp > 0:
        digit = temp % 10
        if digit == 0:
            is_duck = True
            break
        temp //= 10
    
    if is_duck:
        print(f"{num} is a Duck number.")
    else:
        print(f"{num} is not a Duck number.")



#Q17
num = int(input("Enter a number: "))

while num >= 10:   
    sum_digits = 0
    for digit in str(num):  
        sum_digits += int(digit)
    num = sum_digits

print("Digital root:", num)

#Q18
n = int(input("Enter a number: "))

print("Collatz sequence:")
while n != 1:
    print(n, end=" ")
    if n % 2 == 0:  
        n = n // 2
    else:            
        n = 3 * n + 1
print(1)  

#Q19
num = int(input("Enter a number: "))

square = num * num
temp = square
divisor = 1

while divisor <= temp:
    right = temp % (10 ** len(str(divisor)))
    left = temp // (10 ** len(str(divisor)))

    if left + right == num and right != 0:
        print(f"{num} is a Kaprekar number")
        break
    divisor *= 10
else:
    print(f"{num} is not a Kaprekar number")


#Q20
balance = 1000 

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        print(f"Your current balance is: ${balance}")
    elif choice == "2":
        amount = float(input("Enter amount to deposit: $"))
        if amount > 0:
            balance += amount
            print(f"${amount} deposited successfully. New balance: ${balance}")
        else:
            print("Invalid amount!")
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: $"))
        if amount > balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            balance -= amount
            print(f"${amount} withdrawn successfully. Remaining balance: ${balance}")
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")









