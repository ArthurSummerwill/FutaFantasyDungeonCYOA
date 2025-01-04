# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import json
import random
import generate_npc
import load_player

npc_params = pd.read_json('npc_parameters.json')
race_list = list(npc_params['Race'].keys())
print(random.choice(race_list))
print(generate_npc.generate_npc())
print(load_player.player_description())

'''while True:
    response = input("Enter text: ")
    response = response.lower()
    if response == 'quit' or response == 'q' or response == 'exit':
        break'''

'''npc_params = json.load(open('npc_parameters.json'))

fetishes = pd.DataFrame(npc_params['Fetishes'])
#print(npc_params['Fetishes'][1])

new_text = 'txt '+ npc_params['Fetishes'][1] + ' end'

#print(new_text)

#get titles of dicts
print(npc_params['Race'].keys())
print(npc_params['Race']['Human'].keys())'''