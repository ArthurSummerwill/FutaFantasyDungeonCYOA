# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 15:26:06 2025

@author: Arthur Summerwill
"""

import pandas as pd
import random

def read_npc_params(fileName='npc_parameters.json'):
    npc_params = pd.read_json(fileName)
    return npc_params

def read_fetishes(fileName='fetishes.json'):
    fetishes = pd.read_json(fileName)
    return fetishes

def get_fetishes(fetishes):
    fetish_list = list(fetishes['Fetishes'].keys())
    fetish1 = random.choice(fetish_list)
    remaining_fetishes = [item for item in fetish_list if item != fetish1]
    fetish2 = random.choice(remaining_fetishes)
    return (fetish1, fetish2)

def get_races(npc_params):
    return list(npc_params['Race'].keys())

def get_race(npc_params):
    races = get_races(npc_params)
    return random.choice(races)

def get_type_mod(npc_params, race):
    mod_list = list(npc_params['Race'][race]["Type Modifier"])
    if len(mod_list) >= 1:
        if random.uniform(0,1) > 0.5:
            return random.choice(mod_list)
        else:
            return ""
    else:
        return ""

def get_physical_description(npc_params, race):
    physical_list = list(npc_params['Race'][race]["Physical Traits"])
    return random.choice(physical_list)
    
def get_personality(npc_params, race):
    personality_list = list(npc_params['Race'][race]["Personality Traits"])
    trait1 = random.choice(personality_list)
    remaining_personality = [item for item in personality_list if item != trait1]
    trait2 = random.choice(remaining_personality)
    return (trait1, trait2)

def get_cock_description(npc_params, race):
    cock_list = list(npc_params['Race'][race]["Cock Traits"])
    return random.choice(cock_list)

def get_breast_description(npc_params, race):
    breast_list = list(npc_params['Race'][race]["Breast Traits"])
    return random.choice(breast_list)

def generate_npc():
    npc_params = read_npc_params()
    race = get_race(npc_params)
    fetishes = read_fetishes()
    race_txt = "She is a " + get_type_mod(npc_params, race) + " " + race
    race_description = npc_params['Race'][race]["Race Description"]
    physical_description = "She is " + get_physical_description(npc_params, race)
    personality_trait1, personality_trait2 = get_personality(npc_params, race)
    personality = "Her personality can be described as " + personality_trait1 + " and " + personality_trait2
    kink1, kink2 = get_fetishes(fetishes)
    her_kinks = "Her kinks are " + kink1 + " and " + kink2
    cock_description = "Her cock is " + get_cock_description(npc_params, race)
    breast_description = "Her breasts are " + get_breast_description(npc_params, race)
    
    npc_description = (race_txt + "\n" + 
                       race_description + "\n" +
                       physical_description + "\n" +
                       personality + "\n" +
                       her_kinks + "\n" +
                       cock_description + "\n" +
                       breast_description)
                       
    return npc_description
    #print(npc_description)
    

    
    
    
