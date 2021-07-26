import requests 
import subprocess
import os

#os.system('cls' if os.name == 'nt' else 'clear')

on = input("entrada: ")
if(on == "this"):
    print("correrto")
elif(int(on) == 0):
    print("el 0 tambien es correcto")
else:
    print("incorrecto")
