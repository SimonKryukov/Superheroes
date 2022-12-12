import requests

class Heroes:
    host = "https://akabab.github.io/superhero-api/api/"
    
    def get_hero_id(self, name):
        uri = '/all.json'
        url = self.host + uri
        response = requests.get(url=url)
        heroes_data = response.json()
        id = [i['id'] for i in heroes_data if i['name'] == name]
        print(f'Номер {name}: {id}')

    def get_hero_powerstats(self, id):
        uri = f'/id/{id}.json'
        url = self.host + uri
        response = requests.get(url=url)
        return response.json()
        
if __name__ == '__main__':
    hero = Heroes()
    hero.get_hero_id('Hulk'), hero.get_hero_id('Captain America'), hero.get_hero_id('Thanos')
    list_of_heroes = [hero.get_hero_powerstats('332'), hero.get_hero_powerstats('149'), hero.get_hero_powerstats('655')]
    newlist = sorted(list_of_heroes, key=lambda d: d['powerstats']['intelligence'], reverse=True)
    print("Самый умный из супергероев:", newlist[0]['name'])
    
    
    
