import requests 



def catch_a_pokemon():
   
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response= requests.get(url)   
 
    if response.ok:
        data = response.json() 
        pokedex = {}
        pokedex[name.title()]= {
            'name': data['name'],
            'ability': data['abilities'][0]['ability']['name'],
            'base_hp': data['stats'][0]['base_stat'],
            'base_att': data['stats'][1]['base_stat'],
            'base_def': data['stats'][2]['base_stat'],
            'sprite': data['sprites']['other']['official-artwork']['front_default']
        }

        return pokedex
    return f"'{name}' is not found in pokedex. Please check your spelling."
    
