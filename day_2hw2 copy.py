# Problem 1

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# Problem 2    
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)

if num1 == num2 == num3:
    print("All numbers are equal.")
elif num1 == num2 or num1 == num3 or num2 == num3:
    equal_numbers = [num for num in [num1, num2, num3] if [num1, num2, num3].count(num) > 1]
    print("Two numbers are equal and the largest.")
    print("The equal numbers are:", ", ".join(map(str, equal_numbers)))
else:
    print("No two numbers are equal.")

print("The smallest number is:", smallest)
print("The largest number is:", largest)

# Problem Three
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")