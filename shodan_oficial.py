import requests
API_KEY = "GFc8vW8EYWEjhTt8hfPJ8ji9r2lgsWD9"

def shodanSearch(ips):
  for ip in ips:
    url = f"https://api.shodan.io/shodan/host/{ip}?key={API_KEY}"
    response = requests.get(url)
    response = response.json()
    cidade = response['city']
    hostname = response['hostnames']
    domains = response['domains']
    org = response['org']
    result = (f'IP: {ip} - Cidade: {cidade} - Hostname: {hostname} - Domains: {domains} - Org: {org}')
    
    file = open("finalInfo.txt", "a")
    file.writelines(f'{result}\n')
    file.close