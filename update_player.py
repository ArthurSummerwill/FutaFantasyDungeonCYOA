# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 20:46:54 2025

@author: Arthur Summerwill
"""

from ollama import chat
from ollama import ChatResponse
import pandas as pd

def prompt_bot(messages, prompt):
    response = chat(
      'Mistral',
      messages=messages
      + [
        {'role': 'system', 'content': prompt},
      ],
    )
    return response.message.content

def check_penis_size(messages, fileName='player_profile.json'):
    '''response = chat(
      'Mistral',
      messages=messages
      + [
        {'role': 'system', 'content': "Did the player's cock change size during this scene? Respond with yes/no."},
      ],
    )
    answer = response.message.content'''
    #Simply ask if the player's cock size changed during the scene
    answer = prompt_bot(messages, "Did the player's cock change size during this scene? Respond with yes/no.")
    #If the player's cock size did change, then the profile must change
    if 'yes' in answer:
        answer = prompt_bot(messages, "Did the player's cock increase in size? Respond with yes/no.")
        #If the player's cock size increased, then increment it by 1 inch and save
        if 'yes' in answer:
            try:
                profile = pd.read_json(fileName)
                p = dict(profile)
                new_size = str(int(p['Player']["Cock size"])+1)
                p['Player']["Cock size"] = new_size
                p = pd.DataFrame(p)
                p.to_json(fileName)
                print("Player's cock size changed to " + new_size)
            except Exception as e:
                print(e)
                print("could not get penis size from response: " + answer)
        #To save processing: If the size did change and it did not increase, it must have decreased in size
        else:
            try:
                profile = pd.read_json(fileName)
                p = dict(profile)
                size = int(p['Player']["Cock size"])
                if size > 0:
                    new_size = str(int(p['Player']["Cock size"])-1)
                else:
                    print("Your cock would have shrunk, but it's already 0 inches!")
                    new_size = 0
                p['Player']["Cock size"] = new_size
                p = pd.DataFrame(p)
                p.to_json(fileName)
                print("Player's cock size changed to " + new_size)
            except Exception as e:
                print(e)
                print("could not get penis size from response: " + answer)