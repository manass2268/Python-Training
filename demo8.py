
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("The triangle is VALID.")
else:
    
    print("The triangle is NOT VALID.")
