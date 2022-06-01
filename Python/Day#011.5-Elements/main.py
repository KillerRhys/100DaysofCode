""" Elements V1.0
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.05.27-1645 """

import os
import json
import random
import sys
player = ""
player_data = {}
items = {}
spells = []


# TODO: Battle function - Needs new flavor text and enemy adjustment
def battle():
    """ Starts a battle and handles the combat, Calling After battle report when finished """
    battle_finished = False
    turns = 0
    current_hp = player_data["max_hp"]
    enemy_hp = player_data["max_hp"] * random.randint(0, 2)
    while not battle_finished:
        if current_hp >= 1 and enemy_hp >= 1:
            print(f"\n{player} Level:{player_data['level']} Hp:{current_hp}/{player_data['max_hp']} Enemy Hp: {enemy_hp} Satchel:{items}\n")
            move = input(f"What action will you take?\nSpell booK:{spells}\n Action: ")
            cpu_move = random.choice(spells)
            if move == "fire" and cpu_move == "fire":
                current_hp -= 10
                enemy_hp -= 10
                turns += 1
                print("You sling orbs of flame that meet in the middle erupting in a brilliant inferno!")

            elif move == "fire" and cpu_move == "earth":
                current_hp -= 20
                turns += 1
                print("As you cast fire a wall raises from the ground returning your attack to you!")

            elif move == "fire" and cpu_move == "water":
                turns += 1
                print("Your flames are doused with a torrent of water creating a blinding mist.")

            elif move == "fire" and cpu_move == "wind":
                turns += 1
                current_hp -= 30
                print("Your opponent turns your flames on you!")

            elif move == "earth" and cpu_move == "fire":
                turns += 1
                enemy_hp -= 20
                print("Your opponent readies a fireball. You summon a wall of earth to ricochet the attack back!")

            elif move == "earth" and cpu_move == "earth":
                turns += 1
                current_hp -= 10
                enemy_hp -= 10
                print("Like waves two slabs of earth meet and explode in a violent explosion of dust and rock.")

            elif move == "earth" and cpu_move == "water":
                turns += 1
                current_hp -= 10
                enemy_hp -= 10
                print("A flood of water meshes with your wall of earth and creates a mudslide!")

            elif move == "earth" and cpu_move == "wind":
                turns += 1
                enemy_hp - 30
                print("A funnel of wind is redirected to the enemy!")

            elif move == "water" and cpu_move == "fire":
                turns += 1
                print("You quell the enemies flames and shroud the field in mist!")

            elif move == "water" and cpu_move == "earth":
                turns += 1
                current_hp -= 10
                enemy_hp -= 10
                print("You throw everything you have at the rock wall creating a deluge when it gives way!")

            elif move == "water" and cpu_move == "water":
                turns += 1
                current_hp -= 20
                enemy_hp -= 20
                print("The two currents meet and form a whirlpool!")

            elif move == "water" and cpu_move == "wind":
                turns += 1
                current_hp -= 30
                print("The opponents zephyr turns your waters against you!")

            elif move == "wind" and cpu_move == "fire":
                turns += 1
                enemy_hp -= 30
                print("You channel a strong gust to turn the flames against your opponent!")

            elif move == "wind" and cpu_move == "earth":
                turns += 1
                current_hp -= 30
                print("A set of walls funnel your winds back at you!")

            elif move == "wind" and cpu_move == "water":
                turns += 1
                enemy_hp -= 30
                print("You whip up a squall to drown your opponent in their own attack!")

            elif move == "wind" and cpu_move == "wind":
                turns += 1
                current_hp -= 25
                enemy_hp -= 25
                print("Your zephyrs meet and form a strong tempest..")

            elif move == "potion" and items["Potion"] > 0:
                turns += 1
                current_hp += 50

            elif move == "hi-potion" and items["Hi-potion"] > 0:
                turns += 1
                current_hp += 100

            elif move == "giant's brew" and items["Giant's Brew"] > 0:
                turns += 1
                current_hp += 250

            else:
                print("That's not a valid action please try again!")

        else:
            battle_finished = True
            after_battle(turns)


# TODO: After battle report variable issues need repaired
def after_battle(turns):
    """ Gives xp & spoils and calls level up if applicable """
    xp = turns * random.randint(1, 5)
    bonz = turns * random.randint(1, 3)
    items["Bonz"] += bonz
    print(f"You gain {xp} experience points and {bonz} Bonz.")
    player_data['current_xp'] += xp
    if player_data['current_xp'] >= player_data['next_level']:
        player_data['level'] += 1
        hp_up = random.randint(1, 10)
        player_data['max_hp'] += hp_up
        player_data['next_level'] = player_data['next_level'] * 2
        player_data['current_exp'] = 0
        print(f"You reach Level: {player_data['level']} and Hp increased by {hp_up}. {player_data['next_level']} to next level.\n")
        save()
        battle()

    else:
        tnl = player_data['next_level'] - player_data['current_xp']
        print(f"{tnl} til next level-up!\n")
        save()
        battle()


# TODO: Field control function


# TODO: Shop Function


# TODO: Adventure randomizer


# TODO: Save Function
def save():
    filename = player + ".dat"
    with open(filename, 'w') as file:
        file.write(json.dumps(player_data))


# TODO: Load Function
def load():
    player = input("Please input the player name you wish to continue as...: ")
    filename = player + ".dat"
    with open(filename) as file:
        player_data = json.load(file)
        items = {}
        spells = []
        return player, player_data, items, spells


# Vars
get_save = input("Would you like to load a file? ")
if get_save.startswith("y"):
    load()

else:
    player = input("What is your name young one...? ")
    player_data = {"games_played": 0, "games_won": 0, "games_lost": 0, "level": 1, "current_xp": 0, "next_level": 250, "max_hp": 100, "luck": 1}
    items = {"Bonz": 100, "Potion": 1, "Hi-potion": 0, "Giant's Brew": 0}
    spells = ["fire", "earth", "water", "wind"]


battle()