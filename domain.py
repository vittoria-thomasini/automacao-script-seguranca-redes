import sys
import socket
import os

dic_subs = {}
list_ip = []
input_domain = input('Dominio:')

def exec_tools():

            print(f">> Enumerando o sub {input_domain}")
            os.system("assetfinder -subs-only "+input_domain+" ")
            os.system("python3 /opt/Sublist3r/sublist3r.py -d "+input_domain+" -o ")
            os.system("subfinder -d "+input_domain+" -silent -o")

def resolv_ip(sub):
    try:
        ip = socket.gethostbyname(sub)
        dic_subs[sub] = ip
        if(ip not in list_ip):
            list_ip.append(ip)
    except:
        pass

def main():
    exec_tools()

if __name__ == "__main__":
    main()