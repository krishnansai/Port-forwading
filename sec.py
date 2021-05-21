import os

os.system("sudo unzip ngrok-stable-linux-amd64.zip")
os.system("sudo chmod +x *")
os.system("sudo mv ngrok /usr/local/bin")
os.system("sudo apt-get update")
print()
os.system("cowsay -f eyes 'TST'")
print()
port=input("Enter the same port number :")
print("copy The http with end with .io share with your friends")
os.system("ngrok http "+port)

