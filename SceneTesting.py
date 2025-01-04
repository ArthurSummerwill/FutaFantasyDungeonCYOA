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
        {'role': 'user', 'content': "Do not explain. Respond with only 'Yes' or 'No': Is the scene over? If your answer is longer than one word, it is incorrect."},
      ],
    )
    answer = response.message.content.lower()
    #debug print
    print("Is scene over?: " + answer)
    if "yes" in answer:
        return True
    else:
        return False

with open('Game_Prompt.txt', 'r') as file:
    system_prompt = file.read()
    
player = load_player.player_description()
character_prompt = "The player encounters an NPC with the following description. Give her a name and play as her: \n" +generate_npc.generate_npc()

#Debug text printing 
print("The following is for debug purposes:\n")
print(system_prompt)
print()
print(player)
print()
print(character_prompt)
print()

messages = [
  {
    'role': 'system',
    'content': 'START SYSTEM PROMPT:\n'+system_prompt+'END SYSTEM PROMPT\n',
  },
  {
    'role': 'system',
    'content': 'START PLAYER DESCRIPTION:\n'+player+'END PLAYER DESCRIPTION\n',
  },
  {
    'role': 'system',
    'content': 'START NPC DESCRIPTION:\n'+character_prompt+'END NPC DESCRIPTION\n',
  },
  {
    'role': 'system',
    'content': 'The user is playing the role of the player.',
  },
]

response: ChatResponse = chat(model='Mistral', messages=[
  {
    'role': 'system',
    'content': 'Start the game by describing the setting of the first encounter only.',
  },
])

print(response.message.content)

messages += [
  {'role': 'system', 'content': 'Start the game by describing the setting of the first encounter only.'},
  {'role': 'assistant', 'content': response.message.content},
]

while True:
  user_input = input('Input your response: ')
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