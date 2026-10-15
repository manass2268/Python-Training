st = input("Enter an Alphabet: ")

vow = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

if st in vow:
    print("Your input is a vowel:", st)
else:
    print("Your input is a consonant:", st)
