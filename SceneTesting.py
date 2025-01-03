# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 16:20:08 2025

@author: summe
"""

import generate_npc
from ollama import chat
from ollama import ChatResponse

with open('Game_Prompt.txt', 'r') as file:
    system_prompt = file.read()
    
character_prompt = "The player encounters an NPC with the following description. Give her a name and play as her: \n" +generate_npc.generate_npc()

messages = [
  {
    'role': 'system',
    'content': system_prompt,
  },
  {
    'role': 'system',
    'content': character_prompt,
  },
  {
    'role': 'system',
    'content': 'The user is a boy with white skin and an average cock. The user is playing the role of the player.',
  },
]

while True:
  user_input = input('Chat with history: ')
  response = chat(
    'Mistral',
    messages=messages
    + [
      {'role': 'user', 'content': user_input},
    ],
  )

  # Add the response to the messages to maintain the history
  messages += [
    {'role': 'user', 'content': user_input},
    {'role': 'assistant', 'content': response.message.content},
  ]
  print(response.message.content + '\n')