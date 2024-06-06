import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard level
password=[]
total=nr_letters+nr_numbers+nr_symbols
for i in range(0,nr_letters):
    password.insert(random.randint(0,total),random.choice(letters))
for i in range(0,nr_numbers):
    password.insert(random.randint(0,total),random.choice(numbers))
for i in range(0,nr_symbols):
    password.insert(random.randint(0,total),random.choice(symbols))
passw=""
for i in password:
    passw+=i
print(passw)



#Easy level
# password=[]
# total=nr_letters+nr_numbers+nr_symbols
# for j in range(0,nr_letters):
#     password.insert(j,random.choice(letters))
# for j in range(nr_letters,nr_letters+nr_numbers):
#     password.insert(j,random.choice(numbers))
# for j in range(nr_letters+nr_numbers,nr_letters+nr_numbers+nr_symbols):
#     password.insert(j,random.choice(symbols))
# passw=""
# for i in password:
#     passw+=i
# print(passw)

















