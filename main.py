import whois
import vt
import requests
# 0f335d7fe4386004a706de2ec00914abff5bdac10fa57a261b53784a8997e91f

def menu():
    print(" ")
    print("[1] whois Lookup")
    print("[2] VirusTotal Lookup")
    print("[3] Shodan Lookup")
    print("[4] Exit")
    print(" ")

def whoisFunc():
    url = input('Enter: ')
    query = whois.whois(url)
    print("Domain: ", query.domain)
    print("Registrar: ", query.get('registrar'))
    print("Organisation: ", query.get('org'))
    print("City: ", query.get('city'))
    print("State: ", query.get('state'))
    print("Country:", query.get('country'))

def vtFunc():
    url = input('Enter: ')
    client = vt.Client("0f335d7fe4386004a706de2ec00914abff5bdac10fa57a261b53784a8997e91f")
    url_id = vt.url_id(url)
    url = client.get_object("/urls/{}".format(url_id))
    results = list(url.last_analysis_stats.values())[1]
    TSum = sum(url.last_analysis_stats.values())

    print("VirusTotal Report:", results, '/', TSum)

def shodanFunc():
    Address = "https://internetdb.shodan.io/"
    IP = input("Enter:")
    Full = Address + IP

    host = requests.get(Full).json()
    port = list(host.values())[3]
    ip = list(host.values())[2]
    print ("IP: ", ip)
    print("Ports: ", port)


#def readFile():
    
menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        whoisFunc()
    elif option == 2:
        vtFunc()
    elif option == 3:
        shodanFunc()
    elif option == 4:
        exit()
    else:
        print("Invalid option.")

    menu()
    option = int(input("Enter your option: "))

