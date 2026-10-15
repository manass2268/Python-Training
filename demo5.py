Num = int(input("Enter a Year to check if it's a leap year or not: "))
if (Num % 4 == 0 and Num % 100 != 0) or (Num % 400 == 0):
    print("Leap Year:", Num)
else:
    print("Not a Leap year:", Num)
