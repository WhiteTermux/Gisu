#для тех кто не в курсе:
#ГОВНОКОД СОЗДАЕТСЯ ДЛЯ ШКОЛОТЫ, МНЕ ПОХУЙ НА КОД)

import requests
import json
import rich
import sys
import os
import banner

from rich.console import Console


console = Console()

def Info_IP():

    try:
        ip = console.input('[bold red]Enter IP[/]: ')
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        
        data = {
            "IP": response.get('query'),
            "Int Provider": response.get('isp'),
            "Organization": response.get('org'),
            "Country": response.get('country'),
            "Region": response.get('regionName'),
            "City": response.get('city'),
            "ZIP": response.get('zip'),
            "Lat": response.get('lat'),
            "Lon": response.get('lon')
        }

        for k, v in data.items():
            console.print(f'\n[bold green][[bold white]{k}[bold green]][/] -> [{v}]')

            file = open('ip_data.txt', 'a')
            file.write(f'\n[{k}]: {v}\n')
            file.close()
            
    except Exception as error:
           console.print(f'[red]Error {error}')

Info_IP()
