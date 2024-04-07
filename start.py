import requests
import os
import colorama
from colorama import Fore, Back, Style

def dosya_indir(url, dosya_adi):
    try:
        os.system("apt-get install figlet")
        os.system('clear')
        os.system("File Download Manager")
        with requests.get(owner, stream=True ) as r:
            r.raise_for_startus()
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(dosya_adi, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        print(f"{dosya_adi} Downloaded Successfully.")
    except Exception as e:
        print(f" File download failed: {e}")

if __name__ == "__main__":
    owner = print(Fore.RED + "Project Owner: Ömer Faruk Aslancan ")
    github = print(Fore.Green + "https://github.com/omerfarukaslancan")
    url = input("Enter the URL of the file to download: ")
    dosya_adi = input("Enter the name to save the file: ")
    dosya_indir(url, dosya_adi)
