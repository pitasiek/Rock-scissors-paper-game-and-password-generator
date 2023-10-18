#Day 5, today's project's name is 'password-generator'. It makes a password that is difficult to hack.
#Made by Piotr Zięba on 17.10.2023.
import random
test = False
#random available options just to make three lists with letters, symbols and numbers.
letters = ["a", "A", "d", "D", "l", "L", "r", "R", "x", "X", "m", "M", "o", "O", "i", "I", "z", "Z", "w", "W", "q", "Q", "b", "B", "c", "C", "e", "E", "f", "F", "g", "G", "h", "H", "j", "J", "k", "K", "n", "N", "p", "P", "s", "S", "t", "T", "u", "U", "v", "V", "y", "Y"]
symbols = ["#", "!", "$", "&", "*", "-", "+", "%"]
numbers = ["1", "3", "5", "7", "9", "0", "2", "4", "6", "8"]
length = int(input("Welcome to password generator. How long should be your password? We recommend 12 characters.\n"))
if length <= 0:
    print("Your number is 0 or smaller. This program won't work with your input. Please, select number from range: 1 to 20.")
    length = int(input())
    test = (length <= 0) or (length > 20)
    while test:
        length = int(input())
        test = (length <= 0) or (length > 20)
elif length > 20:
    print("This password might be too long. We recommend maximum 20 characters and minimum 1.")
    length = int(input())
    test = (length > 20) or (length <= 0)
    while test:
        length = int(input())
        test = (length > 20) or (length <= 0)
symbols_number = int(input("How many symbols should it contain? We recommend at least 2.\n"))
if length < symbols_number:
    print("Your input is too big. Number of symbols can't be bigger than the password length or smaller than 0.")
    symbols_number = int(input())
    test = (length < symbols_number) or (symbols_number < 0)
    while test:
        symbols_number = int(input())
        test = (length < symbols_number) or (symbols_number < 0)
elif symbols_number < 0:
    print("Input can't be smaller than 0 or bigger than 20.")
    symbols_number = int(input())
    test = (length < symbols_number) or (symbols_number < 0)
    while  test:
        symbols_number = int(input())
        test = (length < symbols_number) or (symbols_number < 0)
number = int(input("How many numbers should it contain? We recommend at least 2.\n"))
if (number >= (length - symbols_number)):
    info = length - symbols_number
    print("Your input is too big. You can't put more numbers than the remaining length which is:" + str(info))
    number = int(input())
    test = (number > (length - symbols_number))
    while test:
        number = int(input())
        test = (number > (length - symbols_number))
elif number < 0:
    info = length - symbols_number
    print("Input can't be smaller than 0 or bigger than remaining length:" + str(info) )
    number = int(input())
    test = (number > (length - symbols_number)) or (number < 0)
    while  test:
        number = int(input())
        test = (number > (length - symbols_number)) or (number < 0)
#At this point I have length, number of symbols and numbers.
password = []
length = length - symbols_number - number #Gives me selected length.
for char in range(length):
    password.append(random.choice(letters))
for char in range(symbols_number):
    password.append(random.choice(symbols))
for char in range(number):
    password.append(random.choice(numbers))
#'For' loops for each input, they pick random characters from lists and append them to a new list named password.
random_password = "" #Random final password for the user.
random.shuffle(password) #Mixing numbers randomly.
for char in range(len(password)): #Appends characters from password after mixing them to random_password.
    random_password = random_password + password[char]
print(f"Your new password: {random_password}") #Display.
end = input("Press any button to end...")
#I've added extra features which prevent the user from using too small and too big numbers.
