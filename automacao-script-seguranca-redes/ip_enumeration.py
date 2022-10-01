import socket

def enumerate_ips(input_file_name, output_file_name):
    ip_set = set()
    print("Iniciando enumeracao de ips")

    input_file = open(input_file_name, 'r')
    domains = input_file.readlines()

    ip = None
    for domain in domains:
        domain = domain.rstrip()
        try:
            ip = socket.gethostbyname(domain)
            ip_set.add(ip)
        except socket.gaierror as e:
            print(f"Erro ao consultar o dominio {domain}, {e}. Seguindo outros dominios")
            pass
        except UnicodeError as e:
            print(f"Erro ao consultar o dominio {domain}, {e}. Seguindo outros dominios")
            pass
        except Exception as e:
            print(f"Outro erro não tratado {e}")
            pass

    with open(output_file_name, "a") as output_file:
        for ip in ip_set:
            output_file.write(f'{ip}\n')

    print("Resultado da enumeracao de ips", ip_set)
