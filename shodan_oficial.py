import os
import shodan
import time
import sys

file = open("shodan.txt", "w")

def showdam():
    if os.path.exists("./shodan_key.txt") and os.path.getsize("./shodan_key.txt") > 0:
        with open("shodan_key.txt", "r") as file:
            shodan_api_key = file.readline().rstrip("\n")
    else:
        file = open("shodan_key.txt", "w")
        os.system("stty -echo")
        shodan_api_key = input("[!] \033[34mInsira uma API Key valida: \033[0m")
        os.system("stty echo")
        file.write(shodan_api_key)
        print ("\n[~] \033[34mArquivo criado: ./shodan_key.txt \033[0m")
        file.close()

    api = shodan.Shodan(shodan_api_key)
    time.sleep(0.4)

    limit = 888
    counter = 1

    try:
        print ("[~] \033[34mChecking Shodan.io API Key... \033[0m")
        api.search("b00m")
        print ("[✓] \033[34mAPI Key Authentication:\033[0m SUCCESS..!")
        time.sleep(0.5)
        
        b00m = input("\n[+] \033[34mEnter your keyword(s):\033[0m ")
        counter = counter + 1
        for banner in api.search_cursor(b00m):
            print ("[+] \033[1;31mIP: \033[1;m" + (banner["ip_str"]))
            print ("[+] \033[1;31mPort: \033[1;m" + str(banner["port"]))
            print ("[+] \033[1;31mOrganization: \033[1;m" + str(banner["org"]))
            print ("[+] \033[1;31mLocation: \033[1;m" + str(banner["location"]))
            print ("[+] \033[1;31mLayer: \033[1;m" + (banner["transport"]))
            print ("[+] \033[1;31mLayer: \033[1;m" + (banner["transport"]))
            print ("[+] \033[1;31mDomains: \033[1;m" + str(banner["domains"]))
            print ("[+] \033[1;31mHostnames: \033[1;m" + str(banner["hostnames"]))
            print ("[+] \033[1;31mThe banner information for the service: \033[1;m\n\n" + (banner["data"]))
            print ("\n[✓] Result: %s. Search query: %s" % (str(counter), str(b00m)))

            data = ("\nIP: " + banner["ip_str"]) + ("\nPort: " + str(banner["port"])) + ("\nOrganisation: " + str(banner["org"])) + ("\nLocation: " + str(banner["location"])) + ("\nLayer: " + banner["transport"]) + ("\nDomains: " + str(banner["domains"])) + ("\nHostnames: " + str(banner["hostnames"])) + ("\nData\n" + banner["data"])
            logger(data)
            time.sleep(0.1)
            print ("\n" + "  " + "»" * 78 + "\n")

            counter += 1
            if counter >= limit:
                exit()

    except shodan.APIError as oeps:
            print ("[✘] \033[1;31mError: %s \033[0m" % (oeps))
            sha_api = input("[*] \033[34mWould you like to change the API Key? <Y/N>:\033[0m ").lower()
            if sha_api.startswith("y" or "Y"):
                file = open("api.txt", "w")
                os.system("stty -echo")
                shodan_api_key = input("[✓] \033[34mPlease enter valid Shodan.io API Key:\033[0m ")
                os.system("stty echo")
                file.write(shodan_api_key)
                print ("\n[~] \033[34mFile written: ./api.txt\033[0m")
                file.close()
                print ("[~] \033[34mRestarting the Platform, Please wait...\033[0m \n")
                time.sleep(1)
                showdam()
            else:
                print ("")
                print ("[•] Exiting Platform... \033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
                sys.exit()

# =====# Main #===== #
if __name__ == "__main__":
    showdam()

