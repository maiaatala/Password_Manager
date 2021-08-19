from cryptography.fernet import Fernet
from pathlib import Path
#imports needed to make master password work
import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
#end of imports

# Path to the key file and the password files.
key_file = Path("key_old.key")
pass_file = Path("passwords_old.txt")

# Function that will write the key, must be run only once for one unique key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: # with open closes the file automatically
        key_file.write(key)

# Function that will read the unique key
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close() # closing the file
    return key

# function that will view the passwords written in the txt file
def view(e_fer):
    if pass_file.is_file():
        with open(pass_file, 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                loc, user, passw = data.split("|@!")
                print("Location:", loc, "| User:", user, "| Password:", e_fer.decrypt(passw.encode()).decode())
    else:
        print("No passwords written")

# Function that will add passwords to the txt file
def add(e_fer):
    location = input("Site/Game: ")
    name = input("Username: ")
    pwd = input("Password: ")
    with open(pass_file, 'a') as f:
        f.write(location + "|@!" + name + "|@!" + e_fer.encrypt(pwd.encode()).decode() + "\n")
        ''' you need to encode = make the string into bites
        so you can encrypt it
        and use the decode so we can read it (take a bite and turn it to string) '''

if not key_file.is_file():
    write_key()

key = load_key()
fer = Fernet(key)

print("-x-x-x- Password Manager Program -x-x-x-")

mode = {
    'view': view,
    'add': add,
}

while True:
    user_i = input("Would you like to view or add passwords? (view/add): ").lower()
    if user_i in mode:
        print()
        mode.get(user_i)(fer)
        print()
    else:
        break

print("Byeeee.")