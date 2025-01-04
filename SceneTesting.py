# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 16:20:08 2025

@author: summe
"""

import generate_npc
import load_player
import update_player
from ollama import chat
from ollama import ChatResponse

def is_scene_over(messages):
    response = chat(
      'Mistral',
      messages=messages
      + [
        {'role': 'system', 'content': "Respond with a single word, yes/no. Is the scene over?"},
      ],
    )
    answer = response.message.content.lower()
    #debug print
    print("Is scene over?: " + answer)
    if answer == "yes":
        return True
    else:
        return False

with open('Game_Prompt.txt', 'r') as file:
    system_prompt = file.read()
    
character_prompt = "The player encounters an NPC with the following description. Give her a name and play as her: \n" +generate_npc.generate_npc()

#Debug text printing 
print("The following is for debug purposes:")
print(system_prompt)
print(character_prompt)

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
  exit_test = user_input.lower()
  if exit_test == 'quit' or exit_test == 'q' or exit_test == 'exit':
      break
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
  if is_scene_over(messages):
      break

update_player.check_penis_size(messages)