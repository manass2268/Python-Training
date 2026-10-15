char = input("Enter a character: ")

if 'A' <= char <= 'Z':
    print(f"'{char}' is Uppercase.")
elif 'a' <= char <= 'z':
    print(f"'{char}' is Lowercase.")
else:
    print("Not a standard English letter.")
