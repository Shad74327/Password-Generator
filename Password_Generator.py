import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_letters = ""
for n in range(0,nr_letters):
  pass_letters = pass_letters+random.choice(letters)+" "

pass_numbers = ""
for n in range(0, nr_numbers):
  pass_numbers = pass_numbers+random.choice(numbers)+" "

pass_symbols = ""
for n in range(0, nr_symbols):
  pass_symbols = pass_symbols+random.choice(symbols)+" "

together = pass_letters+pass_numbers+pass_symbols
Pass = together.split()
random.shuffle(Pass)

Password = ""
for n in range(0,len(Pass)):
  Password = Password+Pass[n]

print(Password)