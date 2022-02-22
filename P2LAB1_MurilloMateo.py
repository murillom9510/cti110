userInt = int(input("Enter integer (32 - 126):\n"))
userFloat = float(input("Enter float:\n"))
userCharacter = input("Enter character:\n")[0]
userString = input("Enter string:\n")
print(str(userInt) + " " + str(userFloat) + " " + userCharacter + " " + userString)
print(userString + " " + userCharacter + " " + str(userFloat) + " " + str(userInt))
print(str(userInt) + " converted to a character is " + str(chr(userInt)))