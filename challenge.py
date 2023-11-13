import re

L = ['&', '#', '@', ',', '^', '-', '*', '=', '+', '§', '%']
password = input("enter the passeword :")

if len(password) < 8:
    print("Le mot de passe doit contenir au moins 8 caractères.")
else:
    if not re.search("[A-Z]", password):
        print("passewor doesn't contain uper letters")
    elif not re.search("[a-z]", password):
        print("passewor doesn't contain lower letters")
    elif not re.search("[0-9]", password):
        print("passewor doesn't contain numbers")
    elif not any(char in L for char in password):
        print("passewor doesn't contain caracters")
    else:
        print("passeword is strong")
