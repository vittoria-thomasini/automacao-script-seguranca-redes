import socket
import os

dic_subs = {}
list_ip = []
def exec_tools(input_domain, f_name):

    print(f">> Enumerando o sub {input_domain}")
    print(f">> Assetfinder")
    assetfinder_result = os.popen(f"assetfinder -subs-only {input_domain} >> output/assetfinder.txt")
    assetfinder_output = assetfinder_result.read()
    assetfinder_result.close()

    print(f">> Sublist3r o sub {input_domain}")
    sublister_result = os.popen("sublist3r -d "+input_domain+" -o output/sublister.txt")
    sublister_output = sublister_result.read()
    sublister_result.close()

    print(f">> Subfinder o sub {input_domain}")
    subfinder_result = os.popen("subfinder -d "+input_domain+" -silent -o output/subfinder.txt")
    subfinder_output = subfinder_result.read()
    subfinder_result.close()

    print(f">> Nmap Portas e Serviços o sub {input_domain}")
    nmap_result = os.popen("nmap -sV -O "+input_domain+" -oN  output/nmap.txt")
    nmap_output = nmap_result.read()
    nmap_result.close()

    salve_txt(input_domain, assetfinder_output, subfinder_output, sublister_output, nmap_output, f_name)

def resolv_ip(sub):
    try:
        ip = socket.gethostbyname(sub)
        dic_subs[sub] = ip
        if(ip not in list_ip):
            list_ip.append(ip)
    except:
        pass

def salve_txt(input_domain, assetfinder_output, subfinder_output, sublister_output, nmap_output, f_name):

    with open(f_name, "a") as arquivo:
        arquivo.write(f" Relatorio dominio {input_domain}")
        arquivo.write(f" Relatorio ASSETFINDER {input_domain}")
        arquivo.write(assetfinder_output) 
        arquivo.write(f" Relatorio SUBFINDER{input_domain}")
        arquivo.write(subfinder_output) 
        arquivo.write(f" Relatorio NMAP {input_domain}")
        arquivo.write(nmap_output)        
        arquivo.write(f" Relatorio SUBLISTER {input_domain}")
        arquivo.write(sublister_output) 


def verificaFinal():
    print("iniciando gravação do arquivo final")
    with open("output/finalfinal.txt", "a") as arquivo:

        arquivo.writelines(["ENUMERACAO SUBDOMINIOS", "\n"])
        with open("output/relatorio_final.txt", "r") as output:
            arquivo.writelines(output)   
        arquivo.writelines(["\n\n\n\n\n", "------------------------", "\n"])

        arquivo.writelines(["ENUMERACAO DE IPS", "\n"])
        with open("output/ips.txt", "r") as output:
            arquivo.writelines(output)   
        arquivo.writelines(["\n\n\n\n\n", "------------------------", "\n"])

        arquivo.writelines(["CONSULTA SHODAN", "\n"])
        with open("output/shodan.txt", "r") as output:
            arquivo.writelines(output)   
        arquivo.writelines(["\n\n\n\n\n", "------------------------", "\n"])
      
    print("finalizando gravação do arquivo final")