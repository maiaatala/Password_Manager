from cryptography.fernet import Fernet, InvalidToken
from pathlib import Path
#imports needed to make master password work
import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
#end of imports

# Path to the key file and the password files.
path = Path(".\\PS_Bin")
key_file = Path(".\\PS_Bin\\key.key")
pass_file = Path(".\\PS_Bin\\passwords.txt")

# Function that will write the key, must be run only once for one unique key
def write_salt():
    s = os.urandom(16)  # a random 16 bit
    with open(key_file, "wb") as file: # with open closes the file automatically
        file.write(s)
        #the salt must be stored, that is the random value that is being used WITH the master pwd to create an unique criptography

# Function that will read the unique key
def load_salt():
    with open(key_file, "rb") as file:
        s = file.read()
    return s

def get_key():
    try:
        salt = load_salt()
    except FileNotFoundError:
        write_salt()
        salt = load_salt()
    
    while True:
        # needs to be inside the loop ryptography.exceptions.AlreadyFinalized: PBKDF2 instances can only be used once.
        kdf = PBKDF2HMAC( 
            algorithm = hashes.SHA256(),  # default
            length = 32,  # default
            salt = salt,
            iterations = 100000  # default
        )
        master_pwd = input("What is the master Password? ")
        master_pwd = master_pwd.encode() #we need to enconde it, cuz it need to be passed as a bites value
        key = base64.urlsafe_b64encode(kdf.derive(master_pwd))
        F = Fernet(key)  # generates the key with the salt + master password
    #block to catch invalid keys
        try:
        #verify if a file with the password exists
            if pass_file.is_file():
                with open(pass_file, 'r') as f:
                    # if the file exists, it tries to decode all the passwords in it
                    for line in f.readlines():
                        data = line.rstrip()
                        loc, user, passw = data.split("|@!")
                        F.decrypt(passw.encode()).decode()  # tries to decrypt all the passwords on the file to guarantee it is the right key
        except InvalidToken:
            print("Wrong master Password, Try again\n")
            continue  # continues the loop if invalid token error happened
        else:
            break  # exists the loop if nothing wrong happened
    return(F)

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


if not os.path.isdir(path):
    os.mkdir(path)

fer = get_key()

print("\n-x-x-x- Password Manager Program -x-x-x-")
print("       ¶ Made by: Ana C. M. Atala\n")

mode = {  # dictionary with the functions handle
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