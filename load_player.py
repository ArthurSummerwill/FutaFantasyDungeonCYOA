# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 20:23:22 2025

@author: Arthur Summerwill
"""

import pandas as pd

def read_player_profile(fileName='player_profile.json'):
    profile = pd.read_json(fileName)
    return profile

def player_description(fileName='player_profile.json'):
    profile = read_player_profile(fileName)
    
    player = ""
    name = "The player character's name is " + profile['Player']['Name'] + "."
    gender = "The player is " + profile['Player']['Gender'] + "."
    description = profile['Player']["Physical Description"]
    cock = ("The player's cock is " + str(profile['Player']["Cock size"]) + 
            " inches and is " + profile['Player']["Circumcision"] + ".")
    orgasm_count = ("Prior to this encounter, the player has had " + 
                    str(profile['Player']["Orgasms"]) + " orgasms.\n")
    
    #Create player profile
    player = (name + '\n' + gender + '\n' + description + '\n' + cock + '\n' + orgasm_count)
    
    #This will only be included if the player is suffering from any status effects
    n_statuses = len(profile['Player']["Statuses"])
    if n_statuses > 0:
        status_list = list(profile['Player']["Statuses"])
        statuses = "The player is currently under the effect of the following:\n"
        for status in status_list:
            statuses = statuses + status + '\n'
        player = player + statuses
    
    #This will only be included if there have been prior encounters
    n_prior_encounters = profile['Player']["Encounters Completed"]
    if n_prior_encounters > 0:
        prior_encounters = ("Prior to this scene, the player has encountered " + 
                            str(n_prior_encounters) + " other encounters." +
                            "The summary of these encounters is:\n")
        encounter_history = list(profile['Player']["Encounter History"])
        for encounter in encounter_history:
            prior_encounters = prior_encounters + encounter + "\n"
        player = player + prior_encounters + '\n'
        
    return player
