# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 20:46:54 2025

@author: Arthur Summerwill
"""

from ollama import chat
from ollama import ChatResponse
import pandas as pd

def check_penis_size(messages, fileName='player_profile.json'):
    response = chat(
      'Mistral',
      messages=messages
      + [
        {'role': 'system', 'content': "In inches, return the value for x: playerCockSize = x"},
      ],
    )
    answer = response.message.content.split("=")
    try:
        new_size = int(answer[1])
        profile = pd.read_json(fileName)
        profile["Player"]["Cock size"] = new_size
        pd.to_json(fileName)
        print("Player's cock size changed to " + answer[1])
    except Exception as e:
        print("could not get penis size from response: " + response.message.content)