# Password_Manager

## Table Of Content

- [Password_Manager](#password_manager)
  - [Table Of Content](#table-of-content)
  - [Introduction](#introduction)
  - [The program](#the-program)
  - [Acknowledgments](#acknowledgments)

## Introduction

The Project is an offline password manager that utilizes cryptography to save them inside a file on the computer.
There are two versions, [the first version](password_manager_no_master_psw.py) just saves the data with an encryption key and doesn't require any other password or authentication to acess them.
[The second version](password_manager.py) requires the user to create and use a master password to encrypt and decrypt the data, being a lot safer than the first version. There's an [executable file](password_manager.exe) of this version available.

Programming language used: Python

Program date: August 2021.

Made by: Ana C Maia Atala. :e-mail: @ ana.atala@unemat.br

## The program

If using the master password version, the program will start by asking for the user to input their master password, if it is their first time using the program, any master password will be accepted, this password **must be remembered** as it will be used during the encryption and decryption process. *There's no recovery if said password is forgotten*. If the user has already set an master password, the program will stay in a loop until the correct master password is written.

After running the program for the first time, a file named ```key.key``` will be created inside a folder named ``PS_Bin``, this file is just as importante as the master passsword, it is crucial to the encrypiton and decryption process and (as with the master password), *There's no recovery if said file is deleted/altered*

In both versions, the program will ask if the user wants to ```view``` existing passwords or ```add``` new passwords to the file data.

If ```add``` is written, the program will ask for the name of the site/game the account is from, the username and the passwords, then it will save the first two informations with the encrypted password in a new file named ```passwords```. *If this file gets deleted, all the data gets lost, if the file is altered, the program may not be able read it again.*

If ```view``` is written, the program will show all the information saved in the ```passwords``` file. with all the passwords being decrypted and redable.

The user may quit the program by writing something other than ```add``` or  ```view```.

## Acknowledgments

I want to end by thanking two very special friends, who hype me up and listen to my endless rant on programming (and lately, Python). I'd also like to thank you for testing my programs and showing support in my endevours.
[Henry](https://github.com/HenryWork555) And [João](https://github.com/jpzinho2004) :blue_heart: :computer:
