import random
import string
print("Welcome to Random Password generator!")
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digits=string.digits
symbols=string.punctuation

n_lower=int(input("How many Lowercase Letters You Want in Your Password?"))
n_upper=int(input("How many Uppercase Letters you Want in Your Password?"))
n_digits=int(input("How many Digits You Want in Your Password?"))
n_symbols=int(input("How many Symbols You Want in Your Password?"))

password_list=[] 
for i in range(1,n_lower+1):
    char=random.choice(lower)
    password_list += char
for i in range(1,n_upper+1):
        char=random.choice(upper)
        password_list += char
for i in range(1,n_digits+1):
            char=random.choice(digits)
            password_list += char
for i in range(1,n_symbols+1): 
                char=random.choice(symbols)
                password_list += char
#print(password_list)
random.shuffle(password_list)
#print(password_list)
password=""
for char in password_list:
    password += char
print("Your Random password is:" , password)
#print(password)

print("Thank you!")
            



