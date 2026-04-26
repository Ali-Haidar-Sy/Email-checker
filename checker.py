import requests, os, json
os.system('pip install termcolor')
os.system('clear')
from termcolor import colored
domains = [
    "guns.lat", "iusearch.lol", "kuruptd.ink", "lansd.org", 
    "leala.site", "lealaom.xyz", "leenz.art", "lifetalk.us",
    "oxno1.space", "vwh.sh", "wael.fun", "z44d.pro",
    "olyanfood.com", "ougoods.com", "xnxjddj.com", "yasdsgar.com",
    "barid.site", "2thth.com", "aksngmail.com", "deislerlive.com",
    "disbs.com", "dryddtyioo.com", "eisenlog.com", "gmreeeddd.com",
    "gtgidhi.com", "hacktivc.com", "kshcid.com", "lymiddleeast.com"
]
unique_domains = sorted(set(domains))
box_width = 40

print("┌" + "─" * box_width + "┐")
for domain in unique_domains:
    color = 'green' if any(ext in domain for ext in ['.com', '.org', '.net', '.site', '.xyz', '.art', '.us', '.space', '.fun', '.pro']) else 'red'
    domain_text = colored(domain, color)
    print(f"│ {domain_text.ljust(box_width - 2)} │")
print("└" + "─" * box_width + "┘")
print()

email = input('- Email : ')
print()

headers = {
    'authority': 'api.barid.site',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://barid.site',
    'referer': 'https://barid.site/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

params = {'limit': '15',}

try:
    ree = requests.get(f'https://api.barid.site/emails/{email}', params=params, headers=headers)
    print(f"Response: {ree.text}")
    data = ree.json()
    print('-'*15)
    
    if data.get('success') == True:
        print('Good Email ✅')
    else:
        print('Bad Email ❌')
        
except json.JSONDecodeError:
    print("Error")
    print(f"Raw re: {ree.text}")
except requests.exceptions.RequestException as e:
    print(f"Error")
except Exception as e:
    print(f"Error B")
    
