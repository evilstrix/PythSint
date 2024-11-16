try:
    import requests
    import os
    import webbrowser
    import colorama
    import json
except ImportError:
    os.system('pip install requests')
    os.system('pip install webbrowser')
    os.system('pip install colorama')

from colorama import Fore

class utils:
    c: str = Fore.BLUE
    q: str = Fore.RED
    o: str = Fore.GREEN

    @staticmethod
    def clear():
        os.system("clear||cls") # clears the terminal
    
    @staticmethod
    def title():
        os.system("title pythsint")

# defines a variable for the ascii art
banner = f""" 
 {utils.c}██████╗ ███████╗██╗███╗   ██╗████████╗
██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██║   ██║███████╗██║██╔██╗ ██║   ██║   
██║   ██║╚════██║██║██║╚██╗██║   ██║   
╚██████╔╝███████║██║██║ ╚████║   ██║   
 ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
                                       """

def main(): # main function
    utils.clear()
    utils.title()
    print(banner) # prints the ascii art 
    print(f"{utils.c}1: Ip Lookup")
    print(f"{utils.c}2: Ip Pinger")
    print(f"{utils.c}3: Name Seeker (Stalking)")

    choice = input(f"{utils.c}Option: ")

    if choice == "1":
        ip = input(f"{utils.c}ip: ")
        response = requests.get("https://demo.ip-api.com/json/{ip}?fields=status,message,country,countryCode,region,regionName,city,zip,lat.lon,isp,org,asname,query&lang=en") # requests
        data = response.json()

        ip = data['query']
        lat = data['lon']
        long = data['long']
        zip = data['zip']
        country = data['country']

        print(f"{utils.c}{ip}")
        print(f"{utils.c}{lat}")
        print(f"{utils.c}{long}")
        print(f"{utils.c}{zip}")
        print(f"{utils.c}{country}")
        input(f"{utils.c}Press Enter")

    elif choice == "2":
        ip = input(f"{utils.c}Ip: ")
        os.system('ping {ip}')

    elif choice == "3":
        name = input(f"{utils.c}Name: ")
        webbrowser.open("https://www.facebook.com/{name}") # opens the sites
        webbrowser.open("https://www.tiktok.com/@{name}")
        webbrowser.open("https://twitter.com/{name}")
        webbrowser.open("https://www.instagram.com/{name}")
        webbrowser.open("https://www.youtube.com/@{name}")
        webbrowser.open("https://www.linkedin.com/in/{name}")
        webbrowser.open("https://www.pinterest.com/%name%")
        input(f"{utils.c}Press enter")


if __name__ == "__main__":
    main()

