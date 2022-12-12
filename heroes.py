import requests
from pprint import pprint

class Heroes:
    host = "https://akabab.github.io/superhero-api/api/"
    
    def get_list_of_heroes(self):
        uri = '/all.json'
        url = self.host + uri
        response = requests.get(url=url)
        return response.json()


hero = Heroes()
pprint(hero.get_list_of_heroes())
