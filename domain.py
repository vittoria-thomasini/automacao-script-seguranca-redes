import string
import sys
import socket
import os
import sublist3r 
import subprocess
dic_subs = {}
list_ip = []
list_assetfinder = []
list_sublister = []
list_subfinder = []

# input_domain = input('Dominio:')

def exec_tools(input_domain, f_name):

    print(f">> Enumerando o sub {input_domain}")
    print(f">> Assetfinder")

    assetfinder_result = os.popen(f"assetfinder -subs-only {input_domain} >>assetfinder.txt")
    assetfinder_output = assetfinder_result.read()
    assetfinder_result.close()

    # print(f">> Sublist3r")
    # sublister_result = sublist3r.main(input_domain, 40, savefile= None, ports= None, silent=False, verbose= False, enable_bruteforce= False, engines=None)
    # list_sublister.append(sublister_result)
    print(f">> Sublist3r o sub {input_domain}")
    sublister_result = os.popen("sublist3r -d "+input_domain+" -o sublister.txt")
    sublister_output = sublister_result.read()
    sublister_result.close()

    print(f">> Subfinder o sub {input_domain}")
    subfinder_result = os.popen("subfinder -d "+input_domain+" -silent -o subfinder.txt")
    subfinder_output = subfinder_result.read()
    subfinder_result.close()


    salve_txt(input_domain, assetfinder_output, subfinder_output, sublister_output, f_name)

def resolv_ip(sub):
    try:
        ip = socket.gethostbyname(sub)
        dic_subs[sub] = ip
        if(ip not in list_ip):
            list_ip.append(ip)
    except:
        pass

def salve_txt(input_domain, assetfinder_output, subfinder_output, sublister_output, f_name):

    with open(f_name, "a") as arquivo:
        arquivo.write(f" Relatorio dominio {input_domain}")
        arquivo.write(f" Relatorio ASSETFINDER {input_domain}")
        arquivo.write(assetfinder_output) 
        arquivo.write(f" Relatorio SUBFINDER{input_domain}")
        arquivo.write(subfinder_output) 
        arquivo.write(f" Relatorio SUBLISTER {input_domain}")
        arquivo.write(sublister_output) 
        # for sublister_output in list_sublister:
        #     list_assetfinder.write("%s\n" % sublister_output )
#     # Importing difflib
# duas formas de gerar o arquivo sem duplicacao
#ou gerar 3 arquivos e comparar as saidas e criar um arquivo novo sem duplicacao ou fazer a validacao
# utilizando as variaveis
# import difflib
  
# with open('file1.txt') as file_1:
#     file_1_text = file_1.readlines()
  
# with open('file2.txt') as file_2:
#     file_2_text = file_2.readlines()
  
# # Find and print the diff:
# for line in difflib.unified_diff(
#         file_1_text, file_2_text, fromfile='file1.txt', 
#         tofile='file2.txt', lineterm=''):
#     print(line)

# def main():
#     exec_tools()

# if __name__ == "__main__":
#     main()