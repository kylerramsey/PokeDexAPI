import requests
from pprint import pprint

your_pokemon = None
p = {}


class Pokemon:
    global your_pokemon, p

    def __init__(self, poke_name, type, ability1, ability2, height, weight, Pic_of_me):
        self.poke_name = poke_name
        self.type = type
        self.ability1 = ability1
        self.ability2 = ability2
        self.height = height
        self.weight = weight
        self.Pic_of_me = Pic_of_me

    def __repr__(self):
        return f'<Pokemon: {self.poke_name}>'


class Pokedex:
    global your_pokemon, p

    def __init__(self):
        self.pokemon_list = []

    def add_pokemon(self, your_pokemon):
        self.api_link = f"https://pokeapi.co/api/v2/pokemon/{your_pokemon}/"
        self.data = requests.get(self.api_link).json()

        p = Pokemon(
            poke_name=self.data["name"],
            type=self.data["types"][0]["type"]["name"],
            ability1=self.data["abilities"][0]["ability"]["name"],
            ability2=self.data["abilities"][1]["ability"]["name"],
            height=self.data["height"],
            weight=self.data["weight"],
            Pic_of_me=self.data["sprites"]["front_default"],
        )
        self.pokemon_list.append(p)

    def poke_details(self):
        for i in self.pokemon_list:
            print(f'\n{i.__dict__}')

    def individual(self):
        detail_name = input("\nWhich one? ")
        for each in self.pokemon_list:
            if each.poke_name == detail_name:
                pprint(each.__dict__)


run_time = Pokedex()


def selection():
    global your_pokemon, pokemon_list
    choice = input("""\nWelcome to your Pokedex! Let's get started. You've got a couple of choices: \n
     Type 'add' to add a new pokemon, Type 'Pokedex' to view your whole Pokedex, Type 'specific' to get \n
     info on one specific pokemon, or to move on for now, Type 'quit' to quit. : """).lower()
    if choice == 'add':
        your_pokemon = input("\nChoose a pokemon to add to your Pokedex: ")
        run_time.add_pokemon(your_pokemon)
        selection()
    elif choice == 'specific':
        run_time.individual()
        selection()
    elif choice == 'pokedex':
        run_time.poke_details()
        selection()
    elif choice == "quit":
        print("\nHave a good one!")
        quit()


selection()
