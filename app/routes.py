from app import app
from dataclasses import dataclass
from flask import Blueprint, render_template, request, redirect, url_for
from app.auth.forms import PokeForm
import requests
from  app.models import Pokemon
from flask_login import login_required, login_user, logout_user, current_user



@app.route('/') 
def homePage():
    return render_template('home.html')



@app.route('/catch_em_all', methods=["GET", "POST"])
@login_required
def pokedex():
    form= PokeForm()
    if request.method == "POST":
        if form.validate():
            name= form.name.data

            poke= Pokemon.query.filter(Pokemon.name==name).first()
            
            if poke:
                return render_template('pokedex.html', form = form, poke=poke)
                

            url = f"https://pokeapi.co/api/v2/pokemon/{name}"
            requests.get(url)
            response= requests.get(url)   
        
            if response.ok:
                data = response.json() 
                pokedex = {}
                pokedex[name.title()]= {
                    'sprite': data['sprites']['other']['official-artwork']['front_default'],
                    'base_exp': data['base_experience'],
                    'ability': data['abilities'][0]['ability']['name'],
                    'base_hp': data['stats'][0]['base_stat'],
                    'base_att': data['stats'][1]['base_stat'],
                    'base_def': data['stats'][2]['base_stat'] 
                }
                img_url = pokedex[name.title()]['sprite'] 
                base_exp = pokedex[name.title()]['base_exp']
                ability = pokedex[name.title()]['ability'] 
                base_hp = pokedex[name.title()]['base_hp'] 
                base_att = pokedex[name.title()]['base_att']
                base_def = pokedex[name.title()]['base_def'] 


            poke= Pokemon(name, img_url, base_exp, ability, base_hp, base_att, base_def, current_user.id)
            poke.saveToDB()
        
            return render_template('pokedex.html', form = form, poke=poke)
        else:
            return f'That pokemon does not exist here. If you want that one, make your own game. now pick another name!'
                   
    return render_template('pokedex.html', form = form)

    
    