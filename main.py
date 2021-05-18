#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letters_list = random.choices (letters, k = nr_letters)
numbers_list = random.choices (numbers, k = nr_numbers)
symbols_list = random.choices (symbols, k = nr_symbols)
pw_list = letters_list + symbols_list + numbers_list
pw = ""
for n in range (0, len(pw_list)):
  pw += pw_list[n]
print (pw)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pw2 =""
# letters_list = random.choices (letters, k = nr_letters)
# numbers_list = random.choices (numbers, k = nr_numbers)
# symbols_list = random.choices (symbols, k = nr_symbols)
pw_list = letters_list + symbols_list + numbers_list
random.shuffle (pw_list)
for m in range (0, len(pw_list)):
  pw2 += pw_list[m]
print (pw2)
