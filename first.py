import os

os.system("sudo apt-get install figlet")
os.system("sudo apt-get install cowsay")
os.system("sudo apt-get install python3")
os.system("sudo apt-get install pip")

os.system("sudo apt-get update")
print()
print()
port=input("Enter the port number :")

print()
print()
os.system("figlet TST")
print("Twin Sai Tech")
print()
print()
print("Press 'contrl+shift+t' and run 'python3 sec.py'")
print()
print()
print()
os.system("python3 -m http.server "+port)

