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
      'dolphin-mixtral:8x7b',
      messages=messages
      + [
        {'role': 'user', 'content': "Do not explain. Respond with only 'Yes' or 'No': Is the scene over (e.g., did the player make the NPC orgasm yet)? If your answer is longer than one word, it is incorrect."},
      ],
    )
    answer = response.message.content.lower()
    #debug print
    print("IS SCENE OVER?: " + answer + "\n END SCENE OVER QUESTION\n")
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

history = [
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
    'content': 'The user is playing the role of Adventurer.',
  },
]

response: ChatResponse = chat(model='dolphin-mixtral:8x7b', messages=[
  {
    'role': 'system',
    'content': 'The player has just entered a room in the dungeon. Remember your system prompts and describe what he finds.',
  },
])

print(response.message.content)

messages += [
  {'role': 'system', 'content': 'The player has just entered a room in the dungeon. Remember your system prompts and describe what he finds.'},
  {'role': 'assistant', 'content': response.message.content},
]

history += [
  {'role': 'system', 'content': 'The player has just entered a room in the dungeon. Remember your system prompts and describe what he finds.'},
  {'role': 'assistant', 'content': response.message.content},
]

while True:
  user_input = input('Input your response: ')
  exit_test = user_input.lower()
  if exit_test == 'quit' or exit_test == 'q' or exit_test == 'exit':
      #print(messages)
      break
  response = chat(
    'dolphin-mixtral:8x7b',
    messages=messages
    + [
      {'role': 'user', 'content': user_input},
      {'role': 'system', 'content': "As the Game Master, respond to the user. Keep your responses brief. Only play as the narrator or NPC, do not assume player responses. Do not repeat yourself."}
    ],
  )

  # Add the response to the messages to maintain the history
  messages += [
    {'role': 'user', 'content': user_input},
    {'role': 'assistant', 'content': response.message.content},
  ]
  history += [
    {'role': 'user', 'content': user_input},
    {'role': 'assistant', 'content': response.message.content},
  ]
  print(response.message.content + '\n')
  if is_scene_over(messages):
      response = chat(
        'dolphin-mixtral:8x7b',
        messages=messages
        + [
          {'role': 'system', 'content': "The player will now leave this room of the dungeon. Briefly describe the scene of the player leaving."},
        ],
      )
      print(response.message.content)
      break

update_player.check_penis_size(history)