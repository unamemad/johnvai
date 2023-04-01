import requests
import re
from colorama import Fore, Back, Style, init

print("""
========================================
         Reverse ip lookup 
          TG(@DevidLuice)
========================================
""")
# Read IP addresses from ip.txt
with open('ip.txt', 'r') as ip_file:
    ip_addresses = ip_file.readlines()

# Function to get domain from request data
def extract_domain(data):
    regex_pattern = r'</th>\n<td>(.+?)</td>'
    domains = re.findall(regex_pattern, data)
    return domains
    
    

# Create or empty domains.txt file

with open('domains.txt', 'a') as f:
    f.write("")

# Send request for each IP address and save domains in domains.txt
for ip in ip_addresses:
    ip = ip.strip()
    url = f'https://rapiddns.io/s/{ip}?full=1'
    response = requests.get(url)

    if response.status_code == 200:
        domains = extract_domain(response.text)
        print ("[+] "+Fore.WHITE + ip+ Fore.GREEN + " Domain Founded ==> ",Style.RESET_ALL,len(domains),'\n')


        with open('domains.txt', 'a') as domain_file:
            for domain in domains:
                domain_file.write(f'{domain}\n')
    else:
        print("[-] "+ip+ Fore.RED + " Dead bro  ",Style.RESET_ALL)
