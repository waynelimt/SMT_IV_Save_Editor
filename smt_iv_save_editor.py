#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import sys
print_n = sys.stdout.write

STAT_TXT = ("Str", "Dex", "Mag", "Agi", "Lck")

# Main Character
MC_STAT1 = ["0x122", 2]
MC_MAX_HP = ("0x12C", 2)
MC_MAX_MP = ("0x12E", 2)
MC_STAT2 = ["0x130", 2]
MC_CURR_HP = ("0x13A", 2)
MC_CURR_MP = ("0x13C", 2)
MC_SKILL = ("0x144", 2, 8)
MC_LVL = ("0x186", 2)

# Miscellaneous
MISC_MACCA = ("0x10C", 4)
MISC_APP_PTS = ("0x98F0", 2)

# Demons
DE_NUM_MAX = 24
DE_START = "0x19C"
DE_NEXT_OFFSET = "0x604"
DE_STAT1 = ("0x4", 2)
DE_MAX_HP = ("0xE", 2)
DE_MAX_MP = ("0x10", 2)
DE_STAT2 = ("0x12", 2)
DE_CURR_HP = ("0x2A", 2)
DE_CURR_MP = ("0x2C", 2)
DE_SKILL = ("0x34", 2, 8)
DE_ID = ("0x46", 2, 8)
DE_LVL = ("0x48", 1)

# Skill Information
SKILL_TYPE = ("Fire", "Ice", "Electric", "Force", "Almighty",
              "Dark", "Light", "Ailment", "Healing", "Status",
              "Support", "Physical", "Gun", "Auto", "Dummy")

SKILL_DMG = ("Zero", "Weak", "Medium", "Heavy", "Severe",
             "KO", "Fixed", "Unknown", "Mega")

SKILL_TARGET = ("Single", "Multiple", "Enemies", "Self",
                "Ally", "Allies", "All", "Unknown")

SKILL_IDS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', '10',
             '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d',
             '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a',
             '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37',
             '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44',
             '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '51', '52', '53', '54',
             '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '65', '66',
             '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', '72', '73',
             '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7f', '89', '8a', '8b',
             '8c', '8d', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1',
             'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ae', 'b0',
             'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd',
             'be', 'bf', 'c0', 'c1', 'c2', 'fb', 'fc', 'fd', 'fe', '100', '101', '102', '103',
             '104', '105', '106', '107', '108', '109', '10a', '10b', '10c', '10d', '10e',
             '10f', '110', '111', '112', '113', '12d', '12e', '12f', '130', '131', '132',
             '133', '134', '135', '136', '137', '138', '139', '13a', '13b', '13c', '13d',
             '13e', '13f', '140', '141', '143', '144', '145', '146', '147', '148', '165',
             '167', '184', '185', '186', '187', '188', '189', '18a', '18b', '18c', '18d',
             '18e', '18f', '191', '192', '193', '194', '195', '196', '197', '198', '199',
             '19a', '19b', '19c', '19d', '19e', '19f', '1a0', '1a1', '1a2', '1a3', '1a4',
             '1a5', '1a6', '1a7', '1a8', '1a9', '1aa', '1ab', '1ac', '1ad', '1ae', '1af',
             '1b0', '1b1', '1b2', '1b3', '1b4', '1b5', '1b6', '1b7', '1b8', '1b9', '1ba',
             '1bb', '1bc', '1bd', '1be', '1bf', '1c0', '1c1', '1c2', '1c3', '1c4', '1c5',
             '1c6', '1c7', '1cd', '1ce', '1cf', '1d0', '1d1', '1d2', '1d7', '1db', '1dd',
             '1de', '1df', '1e0', '1e1', '1e2', '1e3', '1e4', '1e5', '1e6', '1e7', '1e8',
             '1e9', '1ea', '1eb', '1ec', '1ed')

ALL_SKILLS = {
    "1": ("Agi", 0, 1, 1, 0, "Weak Fire damage. 1 enemy."),
    "2": ("Agilao", 0, 4, 2, 0, "Medium Fire damage. 1 enemy."),
    "3": ("Agidyne", 0, 10, 3, 0, "Heavy Fire damage. 1 enemy."),
    "4": ("Maragi", 0, 7, 1, 2, "Weak Fire damage. All enemies."),
    "5": ("Maragion", 0, 16, 2, 2, "Medium Fire damage. All enemies."),
    "6": ("Maragidyne", 0, 28, 3, 2, "Heavy Fire damage. All enemies."),
    "7": ("Fire Breath", 0, 17, 1, 1, "1~4 hits weak Fire damage. Multiple enemies."),
    "8": ("Trisagion", 0, 18, 4, 0, "Severe Fire damage. 1 enemy"),
    "9": ("Ragnarok", 0, 31, 2, 1, "1~4 hits medium Fire damage. Muliple enemies."),
    "102": ("Sunny Ray", 0, 1, 1, 2, "Weak Fire damage. 70% Poison. All enemies."),
    "138": ("Inferno of God", 0, 46, 3, 2, "Heavy Fire damage. Pierce enemy Fire Resist/Null/Drain. All enemies."),
    "a": ("Bufu", 1, 1, 1, 0, "Weak Ice damage. 1 enemy."),
    "b": ("Bufula", 1, 4, 2, 0, "Medium Ice damage. 1 enemy."),
    "c": ("Bufudyne", 1, 10, 3, 0, "Heavy Ice damage. 1 enemy."),
    "d": ("Mabufu", 1, 7, 1, 2, "Weak Ice damage. All enemies."),
    "e": ("Mabufula", 1, 16, 2, 2, "Medium Ice damage. All enemies."),
    "f": ("Mabufudyne", 1, 28, 3, 2, "Heavy Ice damage. All enemies."),
    "10": ("Ice Breath", 1, 17, 1, 1, "1~4 hits weak Ice damage. Muliple enemies."),
    "11": ("Glacial Blast", 1, 18, 2, 1, "1~4 hits medium Ice damage. Multiple enemies."),
    "12": ("Cold World", 1, 46, 3, 2, "Heavy Ice damage. 15% KO. All enemies."),
    "4c": ("Breath", 1, 20, 2, 1, "1~5 hits medium Ice damage. Multiple enemies."),
    "134": ("Hailstorm of God", 1, 46, 3, 2, "Heavy Ice damage. Pierce enemy Ice Resist/Null/Drain. All enemies."),
    "13b": ("Refrigerate", 9, 22, 1, 1, "1~8 hits weak Ice damage. Multiple enemies."),
    "13": ("Zio", 2, 1, 1, 0, "Weak Elec damage. 1 enemy."),
    "14": ("Zionga", 2, 4, 2, 0, "Medium Elec damage. 1 enemy."),
    "15": ("Ziodyne", 2, 10, 3, 0, "Heavy Elec damage. 1 enemy."),
    "16": ("Mazio", 2, 7, 1, 2, "Weak Elec damage. All enemies."),
    "17": ("Mazionga", 2, 16, 2, 2, "Medium Elec damage. All enemies."),
    "18": ("Maziodyne", 2, 28, 3, 2, "Heavy Elec damage. All enemies."),
    "19": ("Shock", 2, 17, 1, 1, "1~4 hits weak Elec damage. Muliple enemies."),
    "1a": ("Thunder Reign", 2, 18, 4, 2, "Severe Elec damage. All enemies."),
    "1b": ("Charming Bolt", 2, 41, 3, 2, "Heavy Elec damage. 25% Panic. All enemies."),
    "12e": ("Lightning of God", 2, 46, 3, 2, "Heavy Elec damage. Pierce enemy Elec Resist/Null/Drain. All enemies."),
    "139": ("Plasma Discharge", 2, 18, 1, 1, "1~8 hits weak Elec damage. Multiple enemies."),
    "1c": ("Zan", 3, 1, 1, 0, "Weak Force damage. 1 enemy."),
    "1d": ("Zanma", 3, 4, 2, 0, "Medium Force damage. 1 enemy."),
    "1e": ("Zandyne", 3, 10, 3, 0, "Heavy Force damage. 1 enemy."),
    "1f": ("Mazan", 3, 7, 1, 2, "Weak Force damage. All enemies."),
    "20": ("Mazanma", 3, 16, 2, 2, "Medium Force damage. All enemies."),
    "21": ("Mazandyne", 3, 28, 3, 2, "Heavy Force damage. All enemies."),
    "22": ("Wind Breath", 3, 17, 1, 1, "1~4 hits weak Force damage. Muliple enemies."),
    "23": ("Deadly Wind", 3, 18, 4, 0, "Severe Force damage. 1 enemy."),
    "24": ("Floral Gust", 3, 31, 2, 1, "1~4 hits medium Force damage. Muliple enemies."),
    "132": ("Tornado of God", 3, 46, 3, 2, "Heavy Force damage. Pierce enemy Force Resist/Null/Drain. All enemies."),
    "25": ("Megido", 4, 21, 1, 2, "Weak Almighty damage. All enemies."),
    "26": ("Megidola", 4, 36, 2, 2, "Medium Almighty damage. All enemies."),
    "27": ("Megidolaon", 4, 56, 3, 2, "Heavy Almighty damage. All enemies."),
    "28": ("Great Logos", 4, 66, 4, 2, "Severe Almighty damage. All enemies."),
    "29": ("Antichthon", 4, 76, 4, 2, "Severe Almighty damage. Debilitate. All enemies."),
    "2a": ("Babylon Goblet", 4, 61, 2, 2, "Medium Almighty damage. 25% Panic."),
    "2b": ("Holy Wrath", 4, 41, 2, 2, "50% additional damage VS Chaos."),
    "2c": ("Judgement", 4, 41, 2, 2, "50% additional damage VS Neutral."),
    "2d": ("Sea of Chaos", 4, 41, 1, 2, "50% additional damage VS Law."),
    "2e": ("Life Drain", 4, 1, 1, 0, "Weak Almighty damage. Drain HP. 1 enemy."),
    "2f": ("Spirit Drain", 4, 1, 1, 0, "Weak Almighty damage. Drain MP. 1 enemy."),
    "30": ("Energy Drain", 4, 1, 1, 0, "Weak Almighty damage. Drain HP/MP. 1 enemy."),
    "47": ("Strange Ray", 4, 1, 6, 0, "Almighty attack reduce target MP to 50%."),
    "48": ("Enigmatic Ray", 4, 6, 6, 2, "???"),
    "49": ("Macca Beam", 4, 1, 6, 0, "Almighty attack reduce target Macca to 20%."),
    "4a": ("Wastrel Beam", 4, 6, 6, 0, "Almighty attack reduce target Macca to 50%"),
    "4b": ("Crushing Wave", 4, 6, 6, 0, "Almighty attack reduce target HP to 1."),
    "4d": ("Death's Door", 4, 6, 6, 2, "All Sick enemies' HP reduced to 1."),
    "c2": ("Desperate Hit", 4, 36, 1, 1, "1~5 hits Almighty damage. Multiple enemies."),
    "fd": ("Queen's Feast", 4, 1, 2, 2, "Medium Almighty damage. Drain HP."),
    "100": ("Ameno Murakumo", 4, 1, 2, 2, "Medium Almighty damage. Tarunda."),
    "101": ("Homeland Song", 4, 1, 3, 1, "2~3 hits weak Almighty damage. Multiple enemies."),
    "103": ("Vulnera", 4, 1, 2, 2, "Medium Almighty damage. 50% Bind. All enemies."),
    "105": ("Deceit Chain", 4, 1, 2, 1, "Medium Almighty damage. 50% Bind. All enemies."),
    "106": ("Naughty Wave", 4, 1, 2, 2, "Medium Almighty damage. 10% KO."),
    "109": ("Evil Shine", 4, 1, 3, 2, "Heavy Almighty damage. 70% Panic. All enemies."),
    "10b": ("Morning Star", 4, 1, 6, 2, "Almighty attack reduce target HP by 50%."),
    "10c": ("Chariot", 4, 1, 2, 2, "Medium Almighty damage. Sukunda. All enemies."),
    "10d": ("Shalt Not Resist", 4, 1, 8, 1, "2 hits mega Almighty damage. Rakunda. All enemies."),
    "10e": ("Hexagram", 4, 1, 5, 0, "Almighty attack. 100% KO."),
    "10f": ("Hell's Torment", 4, 1, 6, 2, "Almighty attack reduce target HP by 66%."),
    "131": ("Serpent of Sheol", 4, 41, 4, 2, "Severe Almighty damage. Drain HP/MP."),
    "137": ("Fallen Grace", 4, 40, 6, 0, "666 Almighty damage to 1 enemy."),
    "13a": ("Megidoplasma", 4, 37, 3, 2, "Heavy Almighty damage to all enemies."),
    "13d": ("Punishment", 4, 1, 6, 2, "Hits 333 Almighty damage per enemy resistance. All enemies."),
    "140": ("Curse Thy Enemy", 4, 76, 3, 2, "Heavy Almighty damage. Gurantees weakness. All enemies."),
    "143": ("Damnation", 4, 61, 3, 2, "Heavy Almighty damage. 70% Poison. All enemies."),
    "144": ("Stigmatic Gleam", 4, 71, 3, 2, "Heavy Almighty damage. 25% Brand. All enemies."),
    "146": ("Gaea Rage", 4, 58, 3, 2, "Heavy Almighty damage. 30% Lost. All enemies."),
    "184": ("Assist (1)", 4, 1, 7, 2, "1 hit ??? Almighty damage. All enemies."),
    "185": ("Assist (2)", 4, 1, 7, 2, "2 hits ??? Almighty damage. All enemies."),
    "186": ("Assist (3)", 4, 1, 7, 2, "3 hits ??? Almighty damage. All enemies."),
    "187": ("Assist (4)", 4, 1, 7, 2, "4 hits ??? Almighty damage. All enemies."),
    "188": ("Assist (5)", 4, 1, 7, 2, "5 hits ??? Almighty damage. All enemies."),
    "189": ("Assist (6)", 4, 1, 7, 2, "6 hits ??? Almighty damage. All enemies."),
    "18a": ("Assist (7)", 4, 1, 7, 2, "7 hits ??? Almighty damage. All enemies."),
    "18b": ("Assist (8)", 4, 1, 7, 2, "8 hits ??? Almighty damage. All enemies."),
    "18c": ("Assist (9)", 4, 1, 7, 2, "9 hits ??? Almighty damage. All enemies."),
    "18d": ("Assist Rush (1)", 4, 1, 7, 2, "10 hits ??? Almighty damage. All enemies."),
    "18e": ("Assist Rush (2)", 4, 1, 7, 2, "11 hits ??? Almighty damage. All enemies."),
    "18f": ("Assist Rush (3)", 4, 1, 7, 2, "12 hits ??? Almighty damage. All enemies."),
    "31": ("Mudo", 5, 2, 5, 0, "Dark magic. 30% KO 1 enemy."),
    "32": ("Mudoon", 5, 6, 5, 0, "Dark magic. 55% KO 1 enemy."),
    "33": ("Mamudo", 5, 14, 5, 2, "Dark magic. 30% KO all enemies."),
    "34": ("Mamudoon", 5, 26, 5, 2, "Dark magic. 55% KO all enemies."),
    "35": ("Die for Me!", 5, 41, 5, 2, "Dark magic. 80% KO all enemies."),
    "36": ("Hama", 6, 2, 5, 0, "Light magic. 30% KO 1 enemy."),
    "37": ("Hamaon", 6, 6, 5, 0, "Light magic. 55% KO 1 enemy."),
    "38": ("Mahama", 6, 14, 5, 2, "Light magic. 30% KO all enemies."),
    "39": ("Mahamaon", 6, 26, 5, 2, "Light magic. 55% KO all enemies."),
    "3a": ("Judgement Light", 6, 41, 5, 2, "Light magic. 80% KO all enemies."),
    "3b": ("Dormina", 7, 1, 0, 0, "90% Sleep. 1 enemy."),
    "3c": ("Lullaby", 7, 7, 0, 2, "70% Sleep. All enemies."),
    "3d": ("Poisma", 7, 1, 0, 0, "90% Poison. 1 enemy."),
    "3e": ("Poison Breath", 7, 7, 0, 2, "70% Poison. All enemies."),
    "3f": ("Shibaboo", 7, 1, 0, 0, "50% Bind an enemy."),
    "40": ("Bind Voice", 7, 11, 0, 2, "50% Bind all enemies."),
    "41": ("Pulpina", 7, 1, 0, 0, "90% Panic. 1 enemy."),
    "42": ("Panic Voice", 7, 11, 0, 2, "70% Panic. All enemies."),
    "43": ("Cough", 7, 14, 0, 0, "90% Sick. 1 enemy."),
    "44": ("Pandemic Bomb", 7, 7, 0, 2, "70% Sick. All Enemies."),
    "45": ("Ancient Curse", 7, 36, 0, 2, "80% random ailment. All enemies."),
    "46": ("Shivering Taboo", 7, 36, 0, 2, "70% random ailment. All enemies."),
    "133": ("Lamentation", 7, 41, 0, 2, "45% random ailment. 100% Brand. All enemies."),
    "51": ("Dia", 8, 1, 0, 4, "Heal HP for ally. Low."),
    "52": ("Diarama", 8, 5, 0, 4, "Heal HP for ally. Medium."),
    "53": ("Diarahan", 8, 12, 0, 4, "Heal HP for ally. High."),
    "54": ("Media", 8, 8, 0, 5, "Heal HP for party. Low."),
    "55": ("Mediarama", 8, 18, 0, 5, "Heal HP for party. Medium."),
    "56": ("Mediarahan", 8, 36, 0, 5, "Heal HP for party. High."),
    "57": ("Salvation", 8, 46, 0, 5, "Heal full HP and cure ailments for party."),
    "58": ("Patra", 8, 1, 0, 4, "Cure Sleep/Panic/Bind for ally."),
    "59": ("Me Patra", 8, 11, 0, 5, "Cure Sleep/Panic/Bind for party."),
    "5a": ("Posumudi", 8, 1, 0, 4, "Cure Poison/Sick for ally."),
    "5b": ("Nervundi", 8, 1, 7, 7, "???"),
    "5c": ("Amrita", 8, 16, 0, 4, "Cure all ailments for ally."),
    "5d": ("Recarm", 8, 16, 0, 4, "Revive ally with little starting HP."),
    "5e": ("Samerecarm", 8, 36, 0, 4, "Revive ally with full starting HP."),
    "5f": ("Recarmdra", 8, 1, 0, 5, "User dies. Revive all allies with full HP."),
    "65": ("Tarukaja", 9, 11, 0, 5, "Increase Attack. All allies."),
    "66": ("Sukukaja", 9, 11, 0, 5, "Increase Hit/Evade. All allies."),
    "67": ("Rakukaja", 9, 11, 0, 5, "Increase Defense. All allies."),
    "68": ("Luster Candy", 9, 46, 0, 5, "Increase all stats. All allies."),
    "69": ("Dekaja", 9, 6, 0, 2, "Neutralize -kaja effects. All enemies."),
    "6a": ("Tarunda", 9, 11, 0, 2, "Decrease Attack. All enemies."),
    "6b": ("Sukunda", 9, 11, 0, 2, "Decrease Hit/Evade. All enemies."),
    "6c": ("Rakunda", 9, 11, 0, 2, "Decrease Defense. All enemies."),
    "6d": ("Debilitate", 9, 46, 0, 2, "Decrease all stats. All enemies."),
    "6e": ("Dekunda", 9, 6, 0, 5, "Neutralize -unda effects. All allies."),
    "6f": ("Silent Prayer", 9, 11, 0, 6, "Neutralize stat modifications for all."),
    "70": ("War Cry", 9, 41, 0, 2, "Decrease Attack/Defense. All enemies"),
    "71": ("Fog Breath", 9, 41, 0, 2, "Decrease Attack/Hit/Evade. All enemies"),
    "72": ("Acid Breath", 9, 41, 0, 2, "Decrease Defense/Hit/Evade. All enemies"),
    "73": ("Taunt", 9, 16, 0, 2, "Decrease Defense. Increase Attack. All enemies."),
    "75": ("Panic Caster", 9, 46, 0, 3, "User Panic. Temporary increase in magic damage."),
    "76": ("Tetrakarn", 9, 46, 0, 5, "Reflect Phys/Gun damage once."),
    "77": ("Makarakarn", 9, 46, 0, 5, "Reflect magic damage once."),
    "78": ("Tetraja", 9, 11, 0, 5, "Nullify Light/Dark magic once."),
    "79": ("Charge", 9, 5, 0, 3, "User's next Phys/Gun damage 250%."),
    "7a": ("Concentrate", 9, 7, 0, 3, "User's next magic damage 250%."),
    "7b": ("Blood Ritual", 9, 21, 0, 3, "Luster Candy. Reduce user's HP to 1."),
    "8a": ("Doping", 9, 41, 0, 5, "All allies' HP 133%"),
    "8b": ("Angelic Order", 9, 21, 0, 4, "Bestows Smirk. 1 ally."),
    "fe": ("Orchard Guardian", 9, 1, 0, 3, "Luster Candy."),
    "10a": ("Kingly One", 9, 1, 0, 1, "Return 1 demon to player's stock at random."),
    "110": ("Light Wing (Fire)", 9, 1, 0, 3, "Repel all attacks except Almight/Fire."),
    "111": ("Light Wing (Ice)", 9, 1, 0, 3, "Repel all attacks except Almight/Ice."),
    "112": ("Light Wing (Elec)", 9, 1, 0, 3, "Repel all attacks except Almight/Elec."),
    "113": ("Light Wing (Force)", 9, 1, 0, 3, "Repel all attacks except Almight/Force."),
    "12f": ("Tetracoerce", 9, 31, 0, 2, "Nullifies enemy Tetrakarn effect."),
    "135": ("Makaracoerce", 9, 31, 0, 2, "Nullifies enemy Makarakarn effect."),
    "136": ("Archangel's Law", 9, 46, 0, 4, "Bestows Smirk. 1 ally."),
    "13e": ("I Have Dr. Pepper", 9, 1, 0, 0, "Maximizes user's stats. Minimizes 1 enemy's stats."),
    "145": ("Spirit Focus", 9, 31, 0, 3, "User's next magic damage 300%."),
    "148": ("Dark Energy", 9, 31, 0, 3, "User's next Phys/Gun damage 300%."),
    "7c": ("Sabbatma", 10, 16, 0, 4, "Summon/return 1 ally to stock."),
    "7d": ("Invitation", 10, 41, 0, 4, "Summon/return 1 ally to stock and revive if dead."),
    "7f": ("Bad Company", 10, 11, 0, 5, "Summon highest level allies from stock."),
    "89": ("Trafuri", 10, 1, 0, 5, "Guaranteed escape from random battles."),
    "8c": ("Estoma Sword", 10, 21, 0, 7, "Used in maps. Hit enemies to banish them."),
    "8d": ("Call Ally", 10, 1, 0, 3, "Dummy"),
    "141": ("Guardian's Eye", 10, 251, 0, 5, "Bestows 3 Turn Press icons."),
    "97": ("Lunge", 11, 2, 1, 0, "Weak Phys damage. High Crit. Low Acc. 1 enemy."),
    "98": ("Oni-Kagura", 11, 5, 2, 0, "Medium Phys damage. High Crit. Low Acc. 1 enemy."),
    "99": ("Mortal Jihad", 11, 9, 3, 0, "Heavy Phys damage. High Crit. Low Acc. 1 enemy."),
    "9a": ("Critical Wave", 11, 6, 1, 2, "Weak Phys damage. High Crit. Low Acc. All enemies."),
    "9b": ("Megaton Press", 11, 13, 2, 2, "Medium Phys damage. High Crit. Low Acc. All enemies."),
    "9c": ("Titanomachia", 11, 26, 3, 2, "Heavy Phys damage. High Crit. Low Acc. All enemies."),
    "9d": ("Gram Slice", 11, 1, 1, 0, "Weak Phys damage. 1 enemy."),
    "9e": ("Fatal Sword", 11, 4, 2, 0, "Medium Phys damage. 1 enemy."),
    "9f": ("Berserker God", 11, 8, 3, 0, "Heavy Phys damage. 1 enemy."),
    "a0": ("Heat Wave", 11, 7, 1, 2, "Weak Phys damage. All enemies."),
    "a1": ("Javelin Rain", 11, 17, 2, 2, "Medium Phys damage. All enemies."),
    "a2": ("Hades Blast", 11, 28, 3, 2, "Heavy Phys damage. All enemies."),
    "a3": ("Bouncing Claw", 11, 1, 1, 1, "1~3 hits weak Phys damage. 1 enemy."),
    "a4": ("Damascus Claw", 11, 3, 2, 1, "1~3 hits medium Phys damage. 1 enemy."),
    "a5": ("Nihil Claw", 11, 7, 3, 1, "1~3 hits heavy Phys damage. 1 enemy."),
    "a6": ("Scratch Dance", 11, 5, 1, 1, "1~3 hits weak Phys damage. Multiple enemies."),
    "a7": ("Axel Claw", 11, 11, 2, 1, "1~3 hits medium Phys damage. Multiple enemies."),
    "a8": ("Madness Nails", 11, 22, 3, 1, "1~3 hits heavy Phys damage. Multiple enemies."),
    "a9": ("Fang Breaker", 11, 8, 1, 0, "Weak Phys damage. Tarunda. 1 enemy."),
    "aa": ("Dream Fist", 11, 5, 1, 0, "Weak Phys damage. 70% Sleep. 1 enemy."),
    "ab": ("Purple Smoke", 11, 10, 2, 1, "1~3 hits medium Phys damage. 70% Panic. Multiple enemies."),
    "ac": ("Carol Hit", 11, 11, 1, 0, "Weak Phys damage. 50% Lost. 1 enemy."),
    "ae": ("Tetanus Cut", 11, 7, 2, 0, "Medium Phys damage. 70% Sick. 1 enemy."),
    "b0": ("Blight", 11, 10, 1, 2, "Weak Phys damage. 60% Poison. All enemies."),
    "b1": ("Occult Flash", 11, 26, 2, 2, "Medium Phys damage. 50% KO. All enemies."),
    "b2": ("Binding Claw", 11, 7, 2, 0, "Medium Phys damage. 35% Bind. 1 enemy."),
    "b3": ("Poison Claw", 11, 5, 2, 0, "Medium Phys damage. 70% Poison. 1 enemy."),
    "b4": ("Iron Judgement", 11, 4, 2, 0, "Medium Phys damage. 1 enemy."),
    "fb": ("Labrys Strike", 11, 1, 8, 1, "2~3 hits mega Phys damage. Multiple enemies."),
    "104": ("Conquerer Spirit", 11, 1, 3, 2, "2 hits heavy Phys damage. All enemies."),
    "108": ("Impossible Slash", 11, 1, 2, 2, "2~3 hits medium Phys damage. All enemies."),
    "12d": ("Kannuki-Throw", 11, 31, 1, 1, "1~15 weak hits Phys damage. Multiple enemies."),
    "130": ("Stigma Strike", 11, 16, 3, 0, "Heavy Phys damage. 250% Brand. 1 enemy."),
    "147": ("Deadly Fury", 11, 41, 3, 2, "Heavy Phys damage. 70% Panic. All enemies."),
    "b5": ("Needle Shot", 12, 2, 1, 0, "Weak Gun damage. 1 enemy."),
    "b6": ("Tathlum Shot", 12, 5, 2, 0, "Medium Gun damage. 1 enemy."),
    "b7": ("Grand Tack", 12, 9, 3, 0, "Heavy Gun damage. 1 enemy."),
    "b8": ("Riot Gun", 12, 6, 4, 0, "Severe Gun damage. 1 enemy."),
    "b9": ("Rapid Needle", 12, 13, 1, 2, "Weak Gun damage. All enemies."),
    "ba": ("Blast Arrow", 12, 26, 2, 2, "Medium Gun damage. All enemies."),
    "bb": ("Heaven's Bow", 12, 1, 3, 2, "Heavy Gun damage. All enemies."),
    "bc": ("Dream Needle", 12, 4, 1, 0, "Weak Gun damage. 70% Sleep. 1 enemy."),
    "bd": ("Toxic Sting", 12, 8, 1, 0, "Weak Gun damage. 70% Poison. 1 enemy."),
    "be": ("Stun Needle", 12, 7, 1, 0, "Weak Gun damage. 60% Bind. 1 enemy."),
    "bf": ("Madness Needle", 12, 17, 1, 0, "Weak Gun damage. 70% Panic. 1 enemy."),
    "c0": ("Stun Needles", 12, 28, 2, 1, "1~3 hits medium Gun damage. 60% Bind. Muliple enemies."),
    "c1": ("Myriad Arrows", 12, 26, 1, 1, "2~4 hits weak Gun damage. Multiple enemies."),
    "fc": ("Snake's Fangs", 12, 1, 2, 1, "2~3 hits medium Gun damage. Multiple enemies."),
    "107": ("Blank Bullet", 12, 1, 2, 2, "2 hits medium Gun damage. All enemies."),
    "13c": ("Star Tarantella", 12, 32, 3, 2, "Heavy Gun damage. 70% Panic. All enemies."),
    "13f": ("Masenko-Ha", 12, 1, 3, 2, "Heavy Gun damage. ???. All enemies."),
    "165": ("Dorn Gift", 12, 2, 2, 0, "Medium Gun damage. 1 enemy."),
    "167": ("Barrage", 12, 1, 1, 2, "Weak Gun damage. All enemies."),
    "191": ("Resist Phys", 13, 0, 0, 3, "None"),
    "192": ("Null Phys", 13, 0, 0, 3, "None"),
    "193": ("Repel Phys", 13, 0, 0, 3, "None"),
    "194": ("Drain Phys", 13, 0, 0, 3, "None"),
    "195": ("Resist Gun", 13, 0, 0, 3, "None"),
    "196": ("Null Gun", 13, 0, 0, 3, "None"),
    "197": ("Repel Gun", 13, 0, 0, 3, "None"),
    "198": ("Drain Gun", 13, 0, 0, 3, "None"),
    "199": ("Resist Fire", 13, 0, 0, 3, "None"),
    "19a": ("Null Fire", 13, 0, 0, 3, "None"),
    "19b": ("Repel Fire", 13, 0, 0, 3, "None"),
    "19c": ("Drain Fire", 13, 0, 0, 3, "None"),
    "19d": ("Resist Ice", 13, 0, 0, 3, "None"),
    "19e": ("Null Ice", 13, 0, 0, 3, "None"),
    "19f": ("Repel Ice", 13, 0, 0, 3, "None"),
    "1a0": ("Drain Ice", 13, 0, 0, 3, "None"),
    "1a1": ("Resist Elec", 13, 0, 0, 3, "None"),
    "1a2": ("Null Elec", 13, 0, 0, 3, "None"),
    "1a3": ("Repel Elec", 13, 0, 0, 3, "None"),
    "1a4": ("Drain Elec", 13, 0, 0, 3, "None"),
    "1a5": ("Resist Force", 13, 0, 0, 3, "None"),
    "1a6": ("Null Force", 13, 0, 0, 3, "None"),
    "1a7": ("Repel Force", 13, 0, 0, 3, "None"),
    "1a8": ("Drain Force", 13, 0, 0, 3, "None"),
    "1a9": ("Resist Dark", 13, 0, 0, 3, "None"),
    "1aa": ("Null Dark", 13, 0, 0, 3, "None"),
    "1ab": ("Resist Light", 13, 0, 0, 3, "None"),
    "1ac": ("Null Light", 13, 0, 0, 3, "None"),
    "1ad": ("Null Mind", 13, 0, 0, 3, "None"),
    "1ae": ("Null Nerve", 13, 0, 0, 3, "None"),
    "1af": ("Phys Pleroma", 13, 0, 0, 3, "Phsical attacks 125%."),
    "1b0": ("High Phys Pleroma", 13, 0, 0, 3, "Phsical attacks 150%."),
    "1b1": ("Gun Pleroma", 13, 0, 0, 3, "Gun attacks 125%."),
    "1b2": ("High Gun Pleroma", 13, 0, 0, 3, "Gun attacks 125%."),
    "1b3": ("Fire Pleroma", 13, 0, 0, 3, "Fire attacks 125%."),
    "1b4": ("High Fire Pleroma", 13, 0, 0, 3, "Fire attacks 125%."),
    "1b5": ("Ice Pleroma", 13, 0, 0, 3, "Ice attacks 125%."),
    "1b6": ("High Ice Pleroma", 13, 0, 0, 3, "Ice attacks 125%."),
    "1b7": ("Elec Pleroma", 13, 0, 0, 3, "Elec attacks 125%."),
    "1b8": ("High Elec Pleroma", 13, 0, 0, 3, "Elec attacks 125%."),
    "1b9": ("Force Pleroma", 13, 0, 0, 3, "Force attacks 125%."),
    "1ba": ("High Force Pleroma", 13, 0, 0, 3, "Force attacks 125%."),
    "1bb": ("Heal Pleroma", 13, 0, 0, 3, "Heal effects 125%."),
    "1bc": ("High Heal Pleroma", 13, 0, 0, 3, "Heal effects 125%."),
    "1bd": ("Endure", 13, 0, 0, 3, "Survive a fatal attack with 1 HP."),
    "1be": ("Enduring Soul", 13, 0, 0, 3, "Survive a fatal attack with full HP."),
    "1bf": ("Counter", 13, 0, 0, 3, "Chance to counter Phys/Gun attacks with weak blow."),
    "1c0": ("Retaliate", 13, 0, 0, 3, "Chance to counter Phys/Gun attacks with heavy blow."),
    "1c1": ("Ally Counter", 13, 0, 0, 3, "Chance to counter Phys/Gun attacks for ally with weak blow."),
    "1c2": ("Ally Retaliate", 13, 0, 0, 3, "Chance to counter Phys/Gun attacks for ally with heavy blow."),
    "1c3": ("Life Aid", 13, 0, 0, 3, "Recover moderate HP after battle."),
    "1c4": ("Mana Aid", 13, 0, 0, 3, "Recover moderate MP after battle."),
    "1c5": ("Victory Cry", 13, 0, 0, 3, "Recover full HP/MP after battle."),
    "1c6": ("Spring of Life", 13, 0, 0, 3, "Gain a little HP while walking."),
    "1c7": ("Chakra Walk", 13, 0, 0, 3, "Gain a little MP while walking."),
    "1cd": ("Life Bonus", 13, 0, 0, 3, "HP 110%."),
    "1ce": ("Life Gain", 13, 0, 0, 3, "HP 120%."),
    "1cf": ("Life Surge", 13, 0, 0, 3, "HP 130%."),
    "1d0": ("Mana Bonus", 13, 0, 0, 3, "MP 110%."),
    "1d1": ("Mana Gain", 13, 0, 0, 3, "MP 120%."),
    "1d2": ("Mana Surge", 13, 0, 0, 3, "MP 130%."),
    "1d7": ("Healing Knowhow", 13, 0, 0, 3, "Can use healing items in battle."),
    "1db": ("Attack Knowhow", 13, 0, 0, 3, "Can use attack items in battle."),
    "1dd": ("Light Life Aid", 13, 0, 0, 3, "Recover a little HP after battle."),
    "1de": ("Light Mana Aid", 13, 0, 0, 3, "Recover a little MP after battle."),
    "1df": ("Speed Lesson", 13, 0, 0, 3, "Raises base AG by 10."),
    "1e0": ("Haste Lesson", 13, 0, 0, 3, "Raises base AG by 20."),
    "1e1": ("Awakening", 13, 0, 0, 3, "Raises all base stats by 5."),
    "1e2": ("Hellish Mask", 13, 0, 0, 3, "Resist all ailments."),
    "1e3": ("Hard Worker", 13, 0, 0, 3, "Slightly increases earned EXP from battle."),
    "1e4": ("Workaholic", 13, 0, 0, 3, "Greatly increases earned EXP from battle."),
    "1e5": ("Beastly Reaction", 13, 0, 0, 3, "Slightly increases Hit/Evade."),
    "1e6": ("Draconic Reaction", 13, 0, 0, 3, "Greatly increases Hit/Evade."),
    "1e7": ("Bloody Glee", 13, 0, 0, 3, "Increases Crit chance."),
    "1e8": ("Pierce Physical", 13, 0, 0, 3, "User's Phys attacks pierce enemy Phys Resist/Null/Drain."),
    "1e9": ("Pierce Gun", 13, 0, 0, 3, "User's Gun attacks pierce enemy Gun Resist/Null/Drain."),
    "1ea": ("Pierce Fire", 13, 0, 0, 3, "User's Fire attacks pierce enemy Fire Resist/Null/Drain."),
    "1eb": ("Pierce Ice", 13, 0, 0, 3, "User's Ice attacks pierce enemy Ice Resist/Null/Drain."),
    "1ec": ("Pierce Elec", 13, 0, 0, 3, "User's Elec attacks pierce enemy Elec Resist/Null/Drain."),
    "1ed": ("Pierce Force", 13, 0, 0, 3, "User's Force attacks pierce enemy Force Resist/Null/Drain.")
}

# Demon Information
ALL_DEMONS = {
    "1": ("Reserved", "Godly", "(?)"),
    "2": ("Reserved", "Godly", "(?)"),
    "3": ("Reserved", "Godly", "(?)"),
    "4": ("Reserved", "Godly", "(?)"),
    "5": ("Reserved", "Godly", "(?)"),
    "6": ("???", "???", "(?)"),
    "7": ("Reserved", "Godly", "(?) (Resist: Charm/Daze/Mute) (Attack: Phys x1, Multi-enemies)"),
    "8": ("Reserved", "???", "(?)"),
    "9": ("Reserved", "Godly", "(?) (Attack: Phys x2, Multi-enemies)"),
    "a": ("Satan", "Primal", ""),
    "b": ("Merkabah", "Herald", ""),
    "c": ("Seraph", "Herald", ""),
    "d": ("Reserved", "???", "(?)"),
    "e": ("Metatron", "Herald", ""),
    "f": ("Reserved", "???", "(?)"),
    "10": ("Mastema", "Herald", ""),
    "11": ("Aniel", "Herald", ""),
    "12": ("Sraosha", "Herald", ""),
    "13": ("Reserved", "???", "(?)"),
    "14": ("Azrael", "Herald", ""),
    "15": ("Kazfiel", "Herald", ""),
    "16": ("0", "Herald", "(?)"),
    "17": ("Israfel", "Herald", ""),
    "18": ("Victor", "Herald", ""),
    "19": ("Lailah", "Herald", ""),
    "1a": ("Reserved", "Herald", "(?)"),
    "1b": ("Dummy", "Herald", "(?)"),
    "1c": ("Dummy", "Herald", "(?)"),
    "1d": ("Dummy", "Herald", "(?)"),
    "1c": ("Dummy", "Herald", "(?)"),
    "1e": ("Dummy", "Herald", "(?)"),
    "1f": ("Lakshmi", "Megami", ""),
    "20": ("Norn", "Megami", ""),
    "21": ("Anat", "Megami", ""),
    "22": ("Tlazolteotl", "Megami", ""),
    "23": ("Pallas Athena", "Megami", ""),
    "24": ("Ishtar", "Megami", ""),
    "25": ("Scathach", "Megami", ""),
    "26": ("Reserved", "Megami", "(?)"),
    "27": ("Parvati", "Megami", ""),
    "28": ("Fortuna", "Megami", ""),
    "29": ("Hathor", "Megami", ""),
    "2a": ("Brigid", "Megami", ""),
    "2b": ("Izanami", "Megami", ""),
    "2c": ("Cleopatra", "Megami", ""),
    "2d": ("Reserved", "Megami", "(?)"),
    "2e": ("Reserved", "Megami", "(?)"),
    "2f": ("Garuda", "Avian", ""),
    "30": ("Yatagarasu", "Avian", ""),
    "31": ("Feng Huang", "Avian", ""),
    "32": ("Thunderbird", "Avian", ""),
    "33": ("Vidofnir", "Avian", ""),
    "34": ("Phoenix", "Avian", ""),
    "35": ("Suparna", "Avian", ""),
    "36": ("Hamsa", "Avian", ""),
    "37": ("Reserved", "Avian", "(?) (Attack: Phys x1, All enemies)"),
    "38": ("Reserved", "Avian", "(?) (Attack: Phys x1, All enemies)"),
    "39": ("Reserved", "Avian", "(?) (Attack: Phys x1, All enemies)"),
    "3a": ("Reserved", "Avian", "(?) (Attack: Phys x1, All enemies)"),
    "3b": ("Reserved", "Avian", "(?) (Attack: Phys x1, All enemies)"),
    "3c": ("Yggdrasil", "Tree", ""),
    "3d": ("Haoma", "Tree", ""),
    "3e": ("Kukunochi", "Tree", ""),
    "3f": ("Mayahuel", "Tree", ""),
    "40": ("Narcissus", "Tree", ""),
    "41": ("Daphne", "Tree", ""),
    "42": ("Reserved", "Tree", "(?) (Attack: Phys x1, All enemies)"),
    "43": ("Reserved", "Tree", "(?) (Attack: Phys x1, All enemies)"),
    "44": ("Reserved", "Tree", "(?)"),
    "45": ("Reserved", "Tree", "(?)"),
    "46": ("Reserved", "Tree", "(?)"),
    "47": ("Cherub", "Divine", ""),
    "48": ("Throne", "Divine", ""),
    "49": ("Dominion", "Divine", ""),
    "4a": ("Virtue", "Divine", ""),
    "4b": ("Power", "Divine", ""),
    "4c": ("Principality", "Divine", ""),
    "4d": ("Archangel", "Divine", ""),
    "4e": ("Angel", "Divine", "(Lvl 10)"),
    "4f": ("Reserved", "Divine", "(?)"),
    "50": ("Angel", "Divine", "(Lvl 82)"),
    "51": ("Reserved", "Divine", "(?)"),
    "52": ("Reserved", "Divine", "(?)"),
    "53": ("Reserved", "Divine", "(?)"),
    "54": ("Reserved", "Divine", "(?)"),
    "55": ("Da Peng", "Flight", ""),
    "56": ("Rukh", "Flight", ""),
    "57": ("Reserved", "Flight", "(?) (Attack: Gun x1, 1 enemy)"),
    "58": ("Reserved", "Flight", "(?) (Attack: Gun x1, 1 enemy)"),
    "59": ("Tuofei", "Flight", ""),
    "5a": ("Caladrius", "Flight", ""),
    "5b": ("Gu Huo Niao", "Flight", ""),
    "5c": ("Harpy", "Flight", ""),
    "5d": ("Tangata Manu", "Flight", ""),
    "5e": ("Reserved", "Flight", "(?)"),
    "5f": ("Reserved", "Flight", "(?)"),
    "60": ("Reserved", "Flight", "(?)"),
    "61": ("Reserved", "Flight", "(?)"),
    "62": ("Reserved", "Flight", "(?)"),
    "63": ("Ganesha", "Yoma", ""),
    "64": ("Master Therion", "Yoma", ""),
    "65": ("Xiuhtecuhtli", "Yoma", ""),
    "66": ("Valkyrie", "Yoma", ""),
    "67": ("Shiwanna", "Yoma", ""),
    "68": ("Dis", "Yoma", ""),
    "69": ("Karasu Tengu", "Yoma", ""),
    "6a": ("Koppa Tengu", "Yoma", ""),
    "6b": ("Agathion", "Yoma", ""),
    "6c": ("Vodyanik", "Yoma", ""),
    "6d": ("Centaur", "Yoma", ""),
    "6e": ("Reserved", "Yoma", "(?)"),
    "6f": ("Reserved", "Yoma", "(?)"),
    "70": ("Reserved", "Yoma", "(?)"),
    "71": ("Reserved", "Yoma", "(?)"),
    "72": ("Peri", "Nymph", ""),
    "73": ("Sarasvati", "Nymph", ""),
    "74": ("Reserved", "Nymph", "(?)"),
    "75": ("Senri", "Nymph", ""),
    "76": ("Apsaras", "Nymph", ""),
    "77": ("Kikuri-Hime", "Nymph", ""),
    "78": ("Reserved", "Nymph", "(?)"),
    "79": ("Reserved", "Nymph", "(?)"),
    "7a": ("Reserved", "Nymph", "(?)"),
    "7b": ("Reserved", "Nymph", "(?)"),
    "7c": ("Demiurge", "Vile", ""),
    "7d": ("Seth", "Vile", ""),
    "7e": ("Pales", "Viles", ""),
    "7f": ("Alciel", "Vile", ""),
    "80": ("Taotie", "Vile", ""),
    "81": ("Pachacamac", "Vile", ""),
    "82": ("Reserved", "Vile", "(?)"),
    "83": ("Mishaguji", "Vile", ""),
    "84": ("Baphomet", "Vile", ""),
    "85": ("Reserved", "Vile", "(?)"),
    "86": ("Reserved", "Vile", "(?)"),
    "87": ("Reserved", "Vile", "(?)"),
    "88": ("Reserved", "Vile", "(?)"),
    "89": ("Reserved", "Vile", "(?)"),
    "8a": ("Hresvelgr", "Raptor", ""),
    "8b": ("Huoniao", "Raptor", ""),
    "8c": ("Anzu", "Raptor", ""),
    "8d": ("Gurr", "Raptor", ""),
    "8e": ("Zhen", "Raptor", ""),
    "8f": ("Itsumade", "Raptor", ""),
    "90": ("Moh Shuvuu", "Raptor", ""),
    "91": ("Camazotz", "Raptor", ""),
    "92": ("Fuxi", "Raptor", ""),
    "93": ("Reserved", "Raptor", "(?)"),
    "94": ("Reserved", "Raptor", "(?)"),
    "95": ("Reserved", "Raptor", "(?)"),
    "96": ("Reserved", "Raptor", "(?)"),
    "97": ("Reserved", "Raptor", "(?)"),
    "98": ("Erikonig", "Wood", ""),
    "99": ("Alraune", "Wood", ""),
    "9a": ("Zaccoum", "Wood", ""),
    "9b": ("Skogsra", "Wood", ""),
    "9c": ("Mandrake", "Wood", ""),
    "9d": ("Shan Xiao", "Wood", ""),
    "9e": ("Reserved", "Wood", "(?)"),
    "9f": ("Reserved", "Wood", "(?)"),
    "a0": ("Reserved", "Wood", "(?)"),
    "a1": ("Reserved", "Wood", "(?)"),
    "a2": ("Reserved", "Wood", "(?)"),
    "a3": ("Reserved", "Deity", "(?) (Resist: Charm/Daze/Mute) (Attack: Phys x1~2, 1 enemy)"),
    "a4": ("Reserved", "Deity", "(?) (Attack: Phys x1~3, 1 enemy)"),
    "a5": ("Hachiman", "Deity", ""),
    "a6": ("Apsu", "Deity", ""),
    "a7": ("Baal", "Deity", ""),
    "a8": ("Odin", "Deity", ""),
    "a9": ("Ometeotl", "Deity", ""),
    "aa": ("Lord Nandou", "Deity", ""),
    "ab": ("Prometheus", "Deity", ""),
    "ac": ("Inti", "Deity", ""),
    "ad": ("Thoth", "Deity", ""),
    "ae": ("Krishna", "Deity", ""),
    "af": ("Mahamayuri", "Deity", ""),
    "b0": ("Osiris", "Deity", ""),
    "b1": ("Maitreya", "Deity", ""),
    "b2": ("Reserved", "Deity", "(?)"),
    "b3": ("Reserved", "Deity", "(?)"),
    "b4": ("Amaterasu", "Amatsu", ""),
    "b5": ("Take-Mikazuchi", "Amatsu", ""),
    "b6": ("Reserved", "Amatsu", "(?) (Weak: Sick)"),
    "b7": ("Reserved", "Amatsu", "(?)"),
    "b8": ("Ame no Uzume", "Amatsu", ""),
    "b9": ("Reserved", "Amatsu", "(?)"),
    "ba": ("Reserved", "Kunitsu", "(?)"),
    "bb": ("Reserved", "Famed", "(?)"),
    "bc": ("Reserved", "Human", "(?)"),
    "bd": ("Reserved", "Human", "(?)"),
    "be": ("Barong", "Avatar", ""),
    "bf": ("Anubis", "Avatar", ""),
    "c0": ("Ukano Mitama", "Avatar", ""),
    "c1": ("Chimera", "Avatar", ""),
    "c2": ("Kaiming Shou", "Avatar", ""),
    "c3": ("Makami", "Avatar", ""),
    "c4": ("Kamapua'a", "Avatar", ""),
    "c5": ("Shiisa", "Avatar", ""),
    "c6": ("Reserved", "Avatar", "(?)"),
    "c7": ("Reserved", "Avatar", "(?)"),
    "c8": ("Reserved", "Avatar", "(?)"),
    "c9": ("Reserved", "Avatar", "(?)"),
    "ca": ("Reserved", "Avatar", "(?)"),
    "cb": ("Sphinx", "Holy", ""),
    "cc": ("Sleipnir", "Holy", ""),
    "cd": ("Baihu", "Holy", ""),
    "ce": ("Airavata", "Holy", ""),
    "cf": ("Chironnupu", "Holy", ""),
    "d0": ("Qing Niuguai", "Holy", ""),
    "d1": ("Pabilsag", "Holy", ""),
    "d2": ("Apis", "Holy", ""),
    "d3": ("Heqet", "Holy", ""),
    "d4": ("Reserved", "Holy", "(?)"),
    "d5": ("Reserved", "Holy", "(?)"),
    "d6": ("Reserved", "Holy", "(?)"),
    "d7": ("Reserved", "Holy", "(?)"),
    "d8": ("Reserved", "Holy", "(?)"),
    "d9": ("Heimdall", "Genma", ""),
    "da": ("Hanuman", "Genma", ""),
    "db": ("Jarilo", "Genma", ""),
    "dc": ("Kresnik", "Genma", ""),
    "dd": ("Cu Chulainn", "Genma", ""),
    "de": ("Kurama Tengu", "Genma", ""),
    "df": ("Tlaloc", "Genma", ""),
    "e0": ("Frost Ace", "Genma", ""),
    "e1": ("Nata Taishi", "Genma", ""),
    "e2": ("Tam Lin", "Genma", ""),
    "e3": ("Ictinike", "Genma", ""),
    "e4": ("Baldur", "Genma", ""),
    "e5": ("Reserved", "Genma", "(?)"),
    "e6": ("Reserved", "Genma", "(?)"),
    "e7": ("Reserved", "Genma", "(?)"),
    "e8": ("Reserved", "Genma", "(?)"),
    "e9": ("Demonee-ho", "Fairy", ""),
    "ea": ("Titania", "Fairy", ""),
    "eb": ("Oberon", "Fairy", ""),
    "ec": ("Vivian", "Fairy", ""),
    "ed": ("Spriggan", "Fairy", ""),
    "ee": ("Nadja", "Fairy", ""),
    "ef": ("Lorelei", "Fairy", ""),
    "f0": ("Kelpie", "Fairy", ""),
    "f1": ("Silky", "Fairy", ""),
    "f2": ("High Pixie", "Fairy", ""),
    "f3": ("Setanta", "Fairy", ""),
    "f4": ("Pyro Jack", "Fairy", ""),
    "f5": ("Jack Frost", "Fairy", ""),
    "f6": ("Goblin", "Fairy", ""),
    "f7": ("Reserved", "Fairy", "(?)"),
    "f8": ("Pixie", "Fairy", ""),
    "f9": ("Napaea", "Fairy", ""),
    "fa": ("Reserved", "???", "(?)"),
    "fb": ("Reserved", "Fairy", "(?)"),
    "fc": ("Reserved", "Fairy", "(?)"),
    "fd": ("Reserved", "Fairy", "(?)"),
    "fe": ("Cerberus", "Beast", ""),
    "ff": ("Ammut", "Beast", ""),
    "100": ("Orthus", "Beast", ""),
    "101": ("Dormath", "Beast", ""),
    "102": ("Hsing-Hsing", "Beast", ""),
    "103": ("Nekomata", "Beast", ""),
    "104": ("Reserved", "Beast", "(?)"),
    "105": ("Inugami", "Beast", ""),
    "106": ("Kabuso", "Beast", ""),
    "107": ("Kaso", "Beast", ""),
    "108": ("Stonka", "Beast", ""),
    "109": ("Gryphon", "Beast", ""),
    "10a": ("Hairy Jack", "Beast", ""),
    "10b": ("Reserved", "Beast", "(?)"),
    "10c": ("Reserved", "???", "(?)"),
    "10d": ("Reserved", "Beast", "(?)"),
    "10e": ("Reserved", "Beast", "(?)"),
    "10f": ("Gogmagog", "Jirae", ""),
    "110": ("Tlaltecuhtli", "Jirae", ""),
    "111": ("Titan", "Jirae", ""),
    "112": ("Tsuchigumo", "Jirae", ""),
    "113": ("Kwancha", "Jirae", ""),
    "114": ("Sudama", "Jirae", ""),
    "115": ("Hua Po", "Jirae", ""),
    "116": ("Knocker", "Jirae", ""),
    "117": ("Dwarf", "Jirae", ""),
    "118": ("Reserved", "Jirae", "(?)"),
    "119": ("Reserved", "Jirae", "(?)"),
    "11a": ("Reserved", "Jirae", "(?)"),
    "11b": ("Reserved", "Jirae", "(?)"),
    "11c": ("Reserved", "Jirae", "(?)"),
    "11d": ("Reserved", "Snake", "(?) (Attack: Phys x1~3, 1 enemy)"),
    "11e": ("Pendragon", "Snake", ""),
    "11f": ("Orochi", "Snake", ""),
    "120": ("Ouroboros", "Snake", ""),
    "121": ("Gui Xian", "Snake", ""),
    "122": ("Yurlungur", "Snake", ""),
    "123": ("Vouivre", "Snake", ""),
    "124": ("Nozuchi", "Snake", ""),
    "125": ("Naga", "Snake", ""),
    "126": ("Reserved", "Snake", "(?)"),
    "127": ("Reserved", "Snake", "(?)"),
    "128": ("Reserved", "Snake", "(?)"),
    "129": ("Reserved", "Snake", "(?)"),
    "12a": ("Reserved", "Snake", "(?)"),
    "12b": ("Mot", "Reaper", ""),
    "12c": ("Nergal", "Reaper", ""),
    "12d": ("Guedhe", "Reaper", ""),
    "12e": ("Persephone", "Reaper", ""),
    "12f": ("Orcus", "Reaper", ""),
    "130": ("Hel", "Reaper", ""),
    "131": ("Ixtab", "Reaper", ""),
    "132": ("Cernunnos", "Reaper", ""),
    "133": ("Reserved", "Reaper", "(?)"),
    "134": ("Reserved", "Reaper", "(?)"),
    "135": ("Reserved", "Reaper", "(?)"),
    "136": ("Fenrir", "Wilder", ""),
    "137": ("Taowu", "Wilder", ""),
    "138": ("Cabracan", "Wilder", ""),
    "139": ("Catoblepas", "Wilder", ""),
    "13a": ("Manticore", "Wilder", ""),
    "13b": ("Porewit", "Wilder", ""),
    "13c": ("Peallaidh", "Wilder", ""),
    "13d": ("Nue", "Wilder", ""),
    "13e": ("Raiju", "Wilder", ""),
    "13f": ("Jueyuan", "Wilder", ""),
    "140": ("Chagrin", "Wilder", ""),
    "141": ("Reserved", "Wilder", "(?)"),
    "142": ("Reserved", "Wilder", "(?)"),
    "143": ("Reserved", "Wilder", "(?)"),
    "144": ("Reserved", "Wilder", "(?)"),
    "145": ("Reserved", "Wilder", "(?)"),
    "146": ("Hekatoncheires", "Jaki", ""),
    "147": ("Girimehkala", "Jaki", ""),
    "148": ("Grendel", "Jaki", ""),
    "149": ("Reserved", "Jaki", "(?)"),
    "14a": ("Rakshasa", "Jaki", ""),
    "14b": ("Black Frost", "Jaki", ""),
    "14c": ("Wendigo", "Jaki", ""),
    "14d": ("Ippon-Datara", "Jaki", ""),
    "14e": ("Gremlin", "Jaki", ""),
    "14f": ("Lham Dearg", "Jaki", ""),
    "150": ("Ogre", "Jaki", ""),
    "151": ("Reserved", "Jaki", "(?)"),
    "152": ("Reserved", "Jaki", "(?)"),
    "153": ("Reserved", "Jaki", "(?)"),
    "154": ("Reserved", "Jaki", "(?)"),
    "155": ("Arachne", "Vermin", ""),
    "156": ("Okiku-Mushi", "Vermin", ""),
    "157": ("Ubu", "Vermin", ""),
    "158": ("Mothman", "Vermin", ""),
    "159": ("Myrmecolion", "Vermin", ""),
    "15a": ("Reserved", "Vermin", "(?)"),
    "15b": ("Reserved", "Vermin", "(?)"),
    "15c": ("Reserved", "Vermin", "(?)"),
    "15d": ("Reserved", "Vermin", "(?)"),
    "15e": ("Reserved", "Vermin", "(?)"),
    "15f": ("Shiva", "Fury", ""),
    "160": ("Susano-o", "Fury", ""),
    "161": ("Kartikeya", "Fury", ""),
    "162": ("Beiji-Weng", "Fury", ""),
    "163": ("Wu Kong", "Fury", ""),
    "164": ("Chernobog", "Fury", ""),
    "165": ("Asura", "Fury", ""),
    "166": ("Tonatiuh", "Fury", ""),
    "167": ("Ares", "Fury", ""),
    "168": ("Mitra-Buddha", "Fury", ""),
    "169": ("Reserved", "???", "(?)"),
    "16a": ("Reserved", "Fury", "(?)"),
    "16b": ("Reserved", "Fury", "(?)"),
    "16c": ("Reserved", "Fury", "(?)"),
    "16d": ("Xi Wangmu", "Lady", ""),
    "16e": ("Skadi", "Lady", ""),
    "16f": ("Black Maria", "Lady", ""),
    "170": ("Inanna", "Lady", ""),
    "171": ("Asherah", "Lady", ""),
    "172": ("Diana", "Lady", ""),
    "173": ("Hariti", "Lady", ""),
    "174": ("Sedna", "Lady", ""),
    "175": ("Dzelarhons", "Lady", ""),
    "176": ("Pele", "Lady", ""),
    "177": ("Isis", "Lady", ""),
    "178": ("Reserved", "Lady", "(?)"),
    "179": ("Reserved", "Lady", "(?)"),
    "17a": ("Reserved", "Lady", "(?)"),
    "17b": ("Reserved", "Lady", "(?)"),
    "17c": ("Huang Long", "Dragon", ""),
    "17d": ("Quetzalcoatl", "Dragon", ""),
    "17e": ("Zhu Yin", "Dragon", ""),
    "17f": ("Illuyanka", "Dragon", ""),
    "180": ("Long", "Dragon", ""),
    "181": ("Gucumatz", "Dragon", ""),
    "182": ("Patrimpas", "Dragon", ""),
    "183": ("Makara", "Dragon", ""),
    "184": ("Reserved", "Dragon", "(?) (Attack: Phys x2, 1 enemy)"),
    "185": ("Reserved", "Dragon", "(?)"),
    "186": ("Reserved", "Dragon", "(?)"),
    "187": ("Reserved", "Dragon", "(?)"),
    "188": ("Reserved", "Dragon", "(?)"),
    "189": ("Thor", "Kishin", ""),
    "18a": ("Marishiten", "Kishin", ""),
    "18b": ("Bishamonten", "Kishin", ""),
    "18c": ("Jikokuten", "Kishin", ""),
    "18d": ("Zhong Kui", "Kishin", ""),
    "18e": ("Koumokuten", "Kishin", ""),
    "18f": ("Zouchouten", "Kishin", ""),
    "190": ("Reserved", "Kishin", "(?)"),
    "191": ("Reserved", "Kishin", "(?)"),
    "192": ("Reserved", "Kishin", "(?)"),
    "193": ("Reserved", "Kishin", "(?)"),
    "194": ("Reserved", "Kishin", "(?)"),
    "195": ("Arahabaki", "Kunitsu", ""),
    "196": ("Kushinada-hime", "Kunitsu", ""),
    "197": ("Okuninushi", "Kunitsu", ""),
    "198": ("Take-Minakata", "Kunitsu", ""),
    "199": ("Oumitsunu", "Kunitsu", ""),
    "19a": ("Hitokotonushi", "Kunitsu", ""),
    "19b": ("Sukuna-Hikona", "Kunitsu", ""),
    "19c": ("Reserved", "Kunitsu", "(?)"),
    "19d": ("Reserved", "Kunitsu", "(?)"),
    "19e": ("Samael", "Fallen", ""),
    "19f": ("Murmur", "Fallen", ""),
    "1a0": ("Gemori", "Fallen", ""),
    "1a1": ("Adramelech", "Fallen", ""),
    "1a2": ("Reserved", "Fallen", "(?)"),
    "1a3": ("Decarabia", "Fallen", ""),
    "1a4": ("Nebiros", "Fallen", ""),
    "1a5": ("Ose", "Fallen", ""),
    "1a6": ("Dantalian", "Fallen", ""),
    "1a7": ("Orias", "Fallen", ""),
    "1a8": ("Halphas", "Fallen", ""),
    "1a9": ("Bifrons", "Fallen", ""),
    "1aa": ("Melchom", "Fallen", ""),
    "1ab": ("Azazel->moved to Tyant", "Fallen", "(?)"),
    "1ac": ("Shax", "Fallen", ""),
    "1ad": ("Barbatos", "Fallen", ""),
    "1ae": ("Botis", "Fallen", ""),
    "1af": ("Reserved", "Fallen", "(?)"),
    "1b0": ("Ongyo-Ki", "Brute", ""),
    "1b1": ("Berserker", "Brute", ""),
    "1b2": ("Sui-Ki", "Brute", ""),
    "1b3": ("Fuu-Ki", "Brute", ""),
    "1b4": ("Kin-Ki", "Brute", ""),
    "1b5": ("Yomotsu Ikusa", "Brute", ""),
    "1b6": ("Yamawaro", "Brute", ""),
    "1b7": ("Momunofu", "Brute", ""),
    "1b8": ("Azumi", "Brute", ""),
    "1b9": ("Oni", "Brute", ""),
    "1ba": ("Reserved", "Brute", "(?)"),
    "1bb": ("Yaksha", "Brute", ""),
    "1bc": ("Bilwis", "Brute", ""),
    "1bd": ("Reserved", "Brute", "(?)"),
    "1be": ("Reserved", "Brute", "(?)"),
    "1bf": ("Reserved", "Brute", "(?)"),
    "1c0": ("Rangda", "Femme", ""),
    "1c1": ("Dakini", "Femme", ""),
    "1c2": ("Atropos", "Femme", ""),
    "1c3": ("Lachesis", "Femme", ""),
    "1c4": ("Clotho", "Femme", ""),
    "1c5": ("Yuki Jyorou", "Femme", ""),
    "1c6": ("Shikome", "Femme", ""),
    "1c7": ("Strix", "Femme", ""),
    "1c8": ("Leanan Sidhe", "Femme", ""),
    "1c9": ("Mermaid", "Femme", ""),
    "1ca": ("Taraka", "Femme", ""),
    "1cb": ("Kali", "Femme", ""),
    "1cc": ("Medusa", "Femme", ""),
    "1cd": ("Reserved", "Femme", "(?)"),
    "1ce": ("Maya", "Night", ""),
    "1cf": ("Reserved", "Night", "(?)"),
    "1d0": ("Reserved", "Night", "(?)"),
    "1d1": ("Queen Mab", "Night", ""),
    "1d2": ("Wild Hunt", "Night", ""),
    "1d3": ("Succubus", "Night", ""),
    "1d4": ("Kaiwan", "Night", ""),
    "1d5": ("Incubus", "Night", ""),
    "1d6": ("Kikimora", "Night", ""),
    "1d7": ("Lilim", "Night", ""),
    "1d8": ("Sandman", "Night", ""),
    "1d9": ("Fomorian", "Night", ""),
    "1da": ("Mokoi", "Night", ""),
    "1db": ("Reserved", "Night", "(?)"),
    "1dc": ("Reserved", "Night", "(?)"),
    "1dd": ("Reserved", "Night", "(?)"),
    "1de": ("Reserved", "Night", "(?)"),
    "1df": ("Reserved", "Night", "(?)"),
    "1e0": ("Lucifer", "Tyrant", ""),
    "1e1": ("Mara", "Tyrant", ""),
    "1e2": ("Chi You", "Tyrant", ""),
    "1e3": ("Surt", "Tyrant", ""),
    "1e4": ("Tzitzimitl", "Tyrant", ""),
    "1e5": ("Beelzebub", "Tyrant", ""),
    "1e6": ("Abaddon", "Tyrant", ""),
    "1e7": ("Loki", "Tyrant", ""),
    "1e8": ("Belial", "Tyrant", ""),
    "1e9": ("Astaroth", "Tyrant", "(?) (Dummied out leftover from SMTIV)"),
    "1ea": ("Balor", "Tyrant", ""),
    "1eb": ("King Frost", "Tyrant", ""),
    "1ec": ("Samyaza", "Tyrant", ""),
    "1ed": ("Horkos", "Tyrant", ""),
    "1ee": ("Mithras", "Tyrant", ""),
    "1ef": ("Morax", "Tyrant", ""),
    "1f0": ("Azazel", "Tyrant", ""),
    "1f1": ("Mephisto", "Tyrant", ""),
    "1f2": ("Lucifuge", "Tyrant", ""),
    "1f3": ("Reserved", "Tyrant", "(?)"),
    "1f4": ("Reserved", "Tyrant", "(?)"),
    "1f5": ("Fafnir", "Drake", ""),
    "1f6": ("Ym", "Drake", ""),
    "1f7": ("Nidhoggr", "Drake", ""),
    "1f8": ("Tiamat", "Drake", ""),
    "1f9": ("Mushussu", "Drake", ""),
    "1fa": ("Kingu", "Drake", ""),
    "1fb": ("Basilisk", "Drake", ""),
    "1fc": ("Bai Suzhen", "Drake", ""),
    "1fd": ("Toubyou", "Drake", ""),
    "1fe": ("Zhu Tun She", "Drake", ""),
    "1ff": ("Vasuki", "Drake", ""),
    "200": ("Phython", "Drake", ""),
    "201": ("Reserved", "Drake", "(?)"),
    "202": ("Reserved", "Drake", "(?)"),
    "203": ("Reserved", "Drake", "(?)"),
    "204": ("Legion", "Spirit", ""),
    "205": ("Pisaca", "Spirit", ""),
    "206": ("Inferno", "Spirit", ""),
    "207": ("Macabre", "Spirit", ""),
    "208": ("Quicksilver", "Spirit", ""),
    "209": ("Poltergeist", "Spirit", ""),
    "20a": ("Wicker Man", "Spirit", ""),
    "20b": ("Dybbuk", "Spirit", ""),
    "20c": ("Garrote", "Spirit", ""),
    "20d": ("Reserved", "Spirit", "(?)"),
    "20e": ("Reserved", "Spirit", "(?)"),
    "20f": ("Reserved", "Spirit", "(?)"),
    "210": ("Reserved", "Spirit", "(?)"),
    "211": ("Reserved", "Foul", "(?)"),
    "212": ("Reserved", "Foul", "(?)"),
    "213": ("Mad Gasser", "Foul", ""),
    "214": ("Reserved", "Foul", ""),
    "215": ("Night Stalker", "Foul", ""),
    "216": ("Hooligan", "Foul", ""),
    "217": ("Jack the Ripper", "Foul", ""),
    "218": ("Slime", "Foul", ""),
    "219": ("Tattooed Man", "Foul", ""),
    "21a": ("Reserved", "Foul", "(?)"),
    "21b": ("Reserved", "Foul", "(?)"),
    "21c": ("Reserved", "Foul", "(?)"),
    "21d": ("Reserved", "Foul", "(?)"),
    "21e": ("Vetala", "Ghost", ""),
    "21f": ("Kudlak", "Ghost", ""),
    "220": ("Ghoul", "Ghost", ""),
    "221": ("Enku", "Ghost", ""),
    "222": ("Churel", "Ghost", ""),
    "223": ("Mou-Ryo", "Ghost", ""),
    "224": ("Obariyon", "Ghost", ""),
    "225": ("Preta", "Ghost", ""),
    "226": ("Strigoii", "Ghost", ""),
    "227": ("Dullahan", "Ghost", "(?) (Dummied out leftover from SMTIV)"),
    "228": ("Reserved", "Ghost", "(?)"),
    "229": ("Reserved", "Ghost", "(?)"),
    "22a": ("Reserved", "Ghost", "(?)"),
    "22b": ("Reserved", "Ghost", "(?)"),
    "22c": ("Saki Mitama", "Mitama", "(Enemy-only)"),
    "22d": ("Kushi Mitama", "Mitama", "(Enemy-only)"),
    "22e": ("Nigi Mitama", "Mitama", "(Enemy-only)"),
    "22f": ("Ara Mitama", "Mitama", "(Enemy-only)"),
    "230": ("Reserved", "Mitama", "(?)"),
    "231": ("Reserved", "Mitama", "(?)"),
    "232": ("Reserved", "Mitama", "(?)"),
    "233": ("Reserved", "Mitama", "(?)"),
    "234": ("Reserved", "Mitama", "(?)"),
    "235": ("Salamander", "Element", ""),
    "236": ("Undine", "Element", ""),
    "237": ("Sylph", "Element", ""),
    "238": ("Gnome", "Element", ""),
    "239": ("Flaemis", "Element", ""),
    "23a": ("Aquans", "Element", ""),
    "23b": ("Aeros", "Element", ""),
    "23c": ("Erthys", "Element", ""),
    "23d": ("Reserved", "Element", "(?)"),
    "23e": ("Reserved", "Element", "(?)"),
    "23f": ("Reserved", "Element", "(?)"),
    "240": ("Reserved", "Element", "(?)"),
    "241": ("Reserved", "Element", "(?)"),
    "242": ("Mother Harlot", "Fiend", ""),
    "243": ("Trumpeter", "Fiend", ""),
    "244": ("Pale Rider", "Fiend", ""),
    "245": ("Black Rider", "Fiend", ""),
    "246": ("Red Rider", "Fiend", ""),
    "247": ("White Rider", "Fiend", ""),
    "248": ("Reserved", "Fiend", "(?)"),
    "249": ("Matador", "Fiend", ""),
    "24a": ("David", "Fiend", ""),
    "24b": ("Reserved", "Fiend", "(?)"),
    "24c": ("Reserved", "???", "(?)"),
    "24d": ("Reserved", "Fiend", "(?)"),
    "24e": ("Reserved", "Fiend", "(?)"),
    "24f": ("Reserved", "Fiend", "(?)"),
    "250": ("Kangiten", "Enigma", ""),
    "251": ("Kama", "Enigma", ""),
    "252": ("Kinmamon", "Enigma", ""),
    "253": ("Futotama", "Enigma", ""),
    "254": ("Kanbari", "Enigma", ""),
    "255": ("Reserved", "Enigma", "(?)"),
    "256": ("Reserved", "Enigma", "(?)"),
    "257": ("Reserved", "Enigma", "(?)"),
    "258": ("Reserved", "Enigma", "(?)"),
    "259": ("Reserved", "Enigma", "(?)"),
    "25a": ("Hare of Inaba", "Food", ""),
    "25b": ("Kuda", "Food", ""),
    "25c": ("Chupacabra", "Food", ""),
    "25d": ("Mamedanuki", "Food", ""),
    "25e": ("Katakirauwa", "Food", ""),
    "25f": ("Onmoraki", "Food", ""),
    "260": ("Reserved", "Food", "(?)"),
    "261": ("Reserved", "Food", "(?)"),
    "262": ("Reserved", "Food", "(?)"),
    "263": ("Reserved", "Food", "(?)"),
    "264": ("Reserved", "Food", "(?)"),
    "265": ("Moved to Diff Race: Masakado", "Zealot", "(?) (Entire portrait is solid white)"),
    "266": ("Tezcatlipoca", "Zealot", ""),
    "267": ("Attis", "Zealot", ""),
    "268": ("Aramisaki", "Zealot", ""),
    "269": ("Dionysus", "Zealot", ""),
    "26a": ("Ogun", "Zealot", ""),
    "26b": ("Reserved", "Zealot", "(?)"),
    "26c": ("Reserved", "Zealot", "(?)"),
    "26d": ("Reserved", "Zealot", "(?)"),
    "26e": ("Reserved", "Zealot", "(?)"),
    "26f": ("Reserved", "Zealot", "(?)"),
    "270": ("Alilat", "Entity", ""),
    "271": ("Reserved", "Entity", "(?)"),
    "272": ("Reserved", "Entity", "(?)"),
    "273": ("Reserved", "Entity", "(?)"),
    "274": ("Reserved", "Entity", "(?)"),
    "275": ("Reserved", "Entity", "(?)"),
    "276": ("Huang Di", "Famed", ""),
    "277": ("Tokisada", "Famed", ""),
    "278": ("Rama", "Famed", ""),
    "279": ("Kanseiteikun", "Famed", ""),
    "27a": ("Siegfried", "Famed", ""),
    "27b": ("Hagen", "Famed", ""),
    "27c": ("Jeanne d'Arc", "Famed", ""),
    "27d": ("Lanling Wang", "Famed", ""),
    "27e": ("Yoshitsune", "Famed", ""),
    "27f": ("Tenkai", "Famed", ""),
    "280": ("Reserved", "Famed", "(?)"),
    "281": ("Reserved", "Famed", "(?)"),
    "282": ("DLC Stock", "Famed", "(?) (Resist: Charm/Daze/Mute)"),
    "283": ("Reserved", "Famed", "(?)"),
    "284": ("Ashura-kai Man", "Human", "(Enemy-only)"),
    "285": ("Ashura-kai Woman", "Human", "(Enemy-only)"),
    "286": ("Reserved", "Human", "(?)"),
    "287": ("Reserved", "Human", "(?)"),
    "288": ("Reserved", "Human", "(?)"),
    "289": ("Reserved", "Human", "(?)"),
    "28a": ("Reserved", "Human", "(?)"),
    "28b": ("Reserved", "Human", "(?)"),
    "28c": ("Reserved", "Human", "(?)"),
    "28d": ("Gaea Man", "Human", "(Enemy-only)"),
    "28e": ("Gaea Woman", "Human", "(Enemy-only)"),
    "28f": ("Reserved", "Human", "(?)"),
    "290": ("Reserved", "Human", "(?)"),
    "291": ("Samurai Zombie", "Undead", "(Male) (Enemy-only, unused leftover from SMTIV)"),
    "292": ("Samurai Zombie", "Undead", "(Female) (Enemy-only, unused leftover from SMTIV)"),
    "293": ("Zombie", "Undead", "(Enemy-only, unused leftover from SMTIV)"),
    "294": ("Alice", "Undead", ""),
    "295": ("Reserved", "Undead", "(?) (Resist: Gun, Weak: Fire/Light, Null: Dark)"),
    "296": ("Zombie Cop", "Undead", ""),
    "297": ("Deleted", "Undead", "(?) (Resist: Gun, Weak: Fire/Light, Null: Dark)"),
    "298": ("Deleted", "Undead", "(?)"),
    "299": ("Patriot", "Undead", ""),
    "29a": ("Corpse", "Undead", ""),
    "29b": ("Reserved", "Cyber", "(?)"),
    "29c": ("Reserved", "Cyber", "(?)"),
    "29d": ("Flynn", "Human", "(YHVH Fight, Bonds Flynn?)"),
    "29e": ("Flynn", "Human", "(YHVH Fight, Massacre Flynn?)"),
    "29f": ("Walter", "Human", "(YHVH Fight)"),
    "2a0": ("Jonathan", "Human", "(YHVH Fight)"),
    "2a1": ("Isabeau", "Human", "(YHVH Fight)"),
    "2a2": ("Satan", "Primal", "(YHVH Fight)"),
    "2a3": ("Timothy", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a4": ("Nozomi", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a5": ("Navarre", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a6": ("Portable Cannon", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a7": ("Nozomi", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a8": ("Orb of the Gates", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a9": ("Giant Horde", "Horde", "(Unused)"),
    "2aa": ("Innocent Horde", "Horde", "(Enemy-only)"),
    "2ab": ("Oni Horde", "Horde", "(Enemy-only)"),
    "2ac": ("Dragon Horde", "Horde", "(Enemy-only)"),
    "2ad": ("Dead Horde", "Horde", "(Enemy-only)"),
    "2ae": ("Wildfire Horde", "Horde", "(Unused leftover from SMTIV)"),
    "2af": ("Demon Horde", "Horde", "(Unused leftover from SMTIV)"),
    "2b0": ("Azteca Force", "Horde", "(Enemy-only)"),
    "2b1": ("Jaki Horde", "Horde", "(Enemy-only)"),
    "2b2": ("Greek Force", "Horde", "(Enemy-only)"),
    "2b3": ("Angel Army", "Horde", "(Enemy-only)"),
    "2b4": ("Defiant Horde", "Horde", "(Enemy-only)"),
    "2b5": ("Freezing Horde", "Horde", "(Enemy-only)"),
    "2b6": ("Gale Horde", "Horde", "(Unused)"),
    "2b7": ("Fallen Horde", "Horde", "(Enemy-only)"),
    "2b8": ("Demon Army", "Horde", "(Enemy-only)"),
    "2b9": ("Not Used", "Horde", ""),
    "2ba": ("Thunder Horde", "Horde", "(Enemy-only)"),
    "2bb": ("Blazing Horde", "Horde", "(Enemy-only)"),
    "2bc": ("Indian Horde", "Horde", "(Enemy-only)"),
    "2bd": ("Not Used", "Horde", ""),
    "2be": ("Not Used", "Horde", ""),
    "2bf": ("Inferno Horde", "Horde", "(Enemy-only)"),
    "2c0": ("Blizzard Horde", "Horde", "(Enemy-only)"),
    "2c1": ("Tengu Horde", "Horde", "(Enemy-only)"),
    "2c2": ("Jack Union", "Horde", "(Enemy-only)"),
    "2c3": ("Frosts", "Horde", "(Unused leftover from SMTIV)"),
    "2c4": ("Norse Force", "Horde", "(Enemy-only)"),
    "2c5": ("Not Used", "Horde", ""),
    "2c6": ("Pirate Horde", "Horde", "(Unused leftover from SMTIV)"),
    "2c7": ("A. Demon Army", "Horde", "(Enemy-only)"),
    "2c8": ("A. Angel Army", "Horde", "(Enemy-only)"),
    "2c9": ("A. Angel Horde", "Horde", "(Enemy-only)"),
    "2ca": ("Herald Army", "Horde", "(Enemy-only)"),
    "2cb": ("Seraph Army", "Horde", "(Enemy-only)"),
    "2cc": ("Metatron Army", "Horde", "(Enemy-only)"),
    "2cd": ("Angel Army", "Horde", "(Enemy-only)"),
    "2ce": ("Not Used", "Horde", ""),
    "2cf": ("Not Used", "Horde", ""),
    "2d0": ("Not Used", "Horde", ""),
    "2d1": ("Not Used", "Horde", ""),
    "2d2": ("Not Used", "Horde", ""),
    "2d3": ("Itsumade Horde", "Horde", "(Enemy-only)"),
    "2d4": ("Not Used", "Horde", ""),
    "2d5": ("Strix Horde", "Horde", "(Enemy-only)"),
    "2d6": ("Demonstrators", "Horde", "(Enemy-only)"),
    "2d7": ("Obsessed Horde", "Horde", "(Enemy-only)"),
    "2d8": ("Greedy Horde", "Horde", "(Enemy-only)"),
    "2d9": ("Maruo Faction", "Horde", "(Enemy-only)"),
    "2da": ("Zaccoum Horde", "Horde", "(Enemy-only)"),
    "2db": ("Corpse Army", "Horde", "(Enemy-only)"),
    "2dc": ("Yomi Army", "Horde", "(Enemy-only)"),
    "2dd": ("Rakshasa", "Horde", "(?) (Unfinished hoarde, appropriate resist/attack)"),
    "2de": ("Ares", "Horde", "(?) (Unfinished hoarde, appropriate resist/attack)"),
    "2df": ("Long", "Horde", "(?) (Unfinished hoarde, appropriate resist/attack)"),
    "2e0": ("Black Frost", "Jaki", "(Boss version)"),
    "2e1": ("Tlaltecuhtli", "Jirae", "(Boss version)"),
    "2e2": ("Prometheus", "Deity", "(Boss version)"),
    "2e3": ("Dormarth", "Beast", "(Boss version)"),
    "2e4": ("Loki", "Tyrant", "(Boss version)"),
    "2e5": ("Lanling Wang", "Famed", "(Boss version)"),
    "2e6": ("Girimehkala", "Jaki", "(Boss version)"),
    "2e7": ("Aramisaki", "Zealot", "(Boss version)"),
    "2e8": ("Ashura-kai Man", "Human", "(Boss version)"),
    "2e9": ("Shax", "Fallen", "(Boss version)"),
    "2ea": ("Futotama", "Enigma", "(Boss version)"),
    "2eb": ("Arahabaki", "Kunitsu", "(Boss version)"),
    "2ec": ("Mara", "Tyrant", "(Boss version)"),
    "2ed": ("Hagen", "Famed", "(Boss version)"),
    "2ee": ("Ongyo-Ki", "Brute", "(Boss version)"),
    "2ef": ("Izanami", "Megami", "(Boss version)"),
    "2f0": ("Maruo", "Human", "(Enemy-only)"),
    "2f1": ("Zhen", "Raptor", "(Boss version)"),
    "2f2": ("Tamagami", "Ghost", "(Enemy-only)"),
    "2f3": ("Okuninushi", "Kunitsu", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f4": ("Kanseiteikun", "Famed", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f5": ("Manticore", "Wilder", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f6": ("Abaddon", "Tyrant", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f7": ("Demonee-ho", "Fairy", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f8": ("Taowu", "Wilder", "(?)  (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f9": ("Prisoner Yokota", "Human", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "2fa": ("Fusou Fujio", "Human", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "2fb": ("Hiro Jingu", "Human", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "2fc": ("G.H. Hills", "Human", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "2fd": ("Take-Mikazuchi", "Amatsu", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2fe": ("Dionysus", "Zealot", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2ff": ("Silky", "Fairy", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "300": ("Lorelei", "Fairy", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "301": ("Persephone", "Reaper", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "302": ("Tiamat", "Drake", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "303": ("Astaroth", "Tyrant", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "304": ("Anzu", "Raptor", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "305": ("Astaroth", "Tyrant", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "306": ("Cernunnos", "Reaper", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "307": ("Grendel", "Jaki", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "308": ("Dormarth", "Beast", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "309": ("Marishiten", "Kishin", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "30a": ("Throne", "Divine", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "30b": ("Dominion", "Divine", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "30c": ("Power", "Divine", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "30d": ("Kazfiel", "Herald", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "30e": ("Hunter Man", "Human", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "30f": ("Hunter Woman", "Human", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "310": ("Thor", "Kishin", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "311": ("Morax", "Tyrant", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "312": ("Chimera", "Avatar", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "313": ("Tokisada", "Famed", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "314": ("Gaston", "Human", "(Plain spear) (Partner)"),
    "315": ("Gaston", "Human", "(Gungnir) (Partner)"),
    "316": ("Toki", "Human", "(Unmasked) (Partner)"),
    "317": ("Isabeau", "Human", "(Partner)"),
    "318": ("Asahi", "Human", "(Partner)"),
    "319": ("Navarre", "Ghost", "(Partner)"),
    "31a": ("Nozomi", "Human", "(Partner)"),
    "31b": ("Gaston", "Human", "(Spear of Michael) (Partner)"),
    "31c": ("Hallelujah", "Human", "(Partner)"),
    "31d": ("Hallelujah", "Hybrid", "(Partner)"),
    "31e": ("Toki", "Human", "(Masked) (Partner)"),
    "31f": ("Flynn", "Samurai", "(Aniel fight ally)"),
    "320": ("Lucifer's Minions", "Horde", "(Enemy-only)"),
    "321": ("Katakirauwa", "Food", "(Tutorial version)"),
    "322": ("Lucifer's Minions", "Horde", "(Enemy-only)"),
    "323": ("Angel", "Divine", "(Boss version)"),
    "324": ("Aniel", "Herald", "(Boss version)"),
    "325": ("King Frost", "Tyrant", "(Boss version)"),
    "326": ("Sukuna-Hikona", "Kunitsu", "(Boss version)"),
    "327": ("Shesha", "Snake", "(Encounter 1)"),
    "328": ("Minotaur", "Beast", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "329": ("Medusa", "Femme", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "32a": ("Titan", "Jirae", "(Boss version)"),
    "32b": ("Medusa", "Femme", "(Boss version)"),
    "32c": ("Shesha", "Snake", "(Encounter 2)"),
    "32d": ("Gaea Woman", "Human", "(Boss version)"),
    "32e": ("Zhong Kui", "Kishin", "(Boss version)"),
    "32f": ("Toki", "Human", "(Masked, boss version)"),
    "330": ("Odin", "Deity", "(Boss version, encounter 1)"),
    "331": ("Not Used", "Horde", ""),
    "332": ("Gaea Man", "Human", "(Boss version)"),
    "333": ("Quetzalcoatl", "Dragon", "(Boss version)"),
    "334": ("Jikokuten", "Kishin", "(Boss version)"),
    "335": ("Koumokuten", "Kishin", "(Boss version)"),
    "336": ("Zouchouten", "Kishin", "(Boss version)"),
    "337": ("Bishamonten", "Kishin", "(Boss version)"),
    "338": ("Marishiten", "Kishin", "(Boss version)"),
    "339": ("Inanna Remnant", "Lady", "(Enemy-only)"),
    "33a": ("Maitreya", "Deity", "(Boss version)"),
    "33b": ("Shesha", "Snake", "(Encounter 3)"),
    "33c": ("Krishna", "Deity", "(Boss version)"),
    "33d": ("Not Used", "Archaic", "(?) (Null: Light/Dark)"),
    "33e": ("Not Used", "Archaic", "(?) (Null: Light/Dark)"),
    "33f": ("Not Used", "Archaic", "(?) (Null: Light/Dark)"),
    "340": ("Not Used", "Archaic", "(?) (Null: Light/Dark)"),
    "341": ("Gaea Man", "Human", "(Boss version)"),
    "342": ("Gaea Woman", "Human", "(Boss version)"),
    "343": ("Adramelech", "Fallen", "(Boss version)"),
    "344": ("Angel Army", "Horde", "(Boss version)"),
    "345": ("Azrael", "Herald", "(Boss version)"),
    "346": ("Belial", "Tyrant", "(Boss version)"),
    "347": ("Lucifuge", "Tyrant", "(Boss version)"),
    "348": ("Samyaza", "Tyrant", "(Boss version)"),
    "349": ("Lucifer", "Tyrant", "(Boss version)"),
    "34a": ("Merkabah", "Herald", "(Boss version)"),
    "34b": ("Not Used", "Drake", "(?) (Repel: Phys, Resist: Gun, Weak: Ice/Elec)"),
    "34c": ("Not Used", "Vile", "(?) (Null: Ice/Dark, Resist: Light, Weak: Fire)"),
    "34d": ("Not Used", "Horde", "(?) (Resist: Dark, Weak: Fire/Force/Light) (Attack: Phys x3~4, 1 enemy)"),
    "34e": ("Odin", "Deity", "(Boss version, encounter 2)"),
    "34f": ("Baal", "Deity", "(Boss version)"),
    "350": ("Apsu", "Deity", "(Boss version)"),
    "351": ("Seth", "Vile", "(Boss version)"),
    "352": ("Inanna", "Lady", "(Boss version)"),
    "353": ("Mitra-Buddha", "Fury", "(Boss version)"),
    "354": ("Dagda", "Deity", "(Enemy-only)"),
    "355": ("Vishnu-Flynn", "Deity", "(1st form) (Enemy-only)"),
    "356": ("Metatron", "Herald", "(Boss version)"),
    "357": ("Metatron Army", "Horde", "(Boss version)"),
    "358": ("Not Used", "Human", "(?) (Null: Light/Dark)"),
    "359": ("Not Used", "Megami", "(?) (Repel: Gun, Null: Dark, Resist: Phys/Light)"),
    "35a": ("Satan", "Primal", "(Boss version)"),
    "35b": ("YHVH", "Godly", "(1st form) (Enemy-only)"),
    "35c": ("YHVH", "Godly", "(2nd form) (Enemy-only)"),
    "35d": ("Vishnu-Flynn", "Deity", "(2nd form) (Enemy-only)"),
    "35e": ("Angel Army", "Horde", "(Boss version)"),
    "35f": ("Rukh", "Flight", "(Boss version)"),
    "360": ("Navarre", "Ghost", "(Boss version)"),
    "361": ("Nozomi", "Human", "(Boss version)"),
    "362": ("Hallelujah", "Hybrid", "(Boss version)"),
    "363": ("Gaston", "Human", "(Boss version)"),
    "364": ("Toki", "Human", "(Unmasked, boss version)"),
    "365": ("Isabeau", "Human", "(Boss version)"),
    "366": ("Human Army", "Horde", "(Wave 1) (Enemy-only)"),
    "367": ("Human Army", "Horde", "(Wave 2) (Enemy-only)"),
    "368": ("Human Army", "Horde", "(Wave 3) (Enemy-only)"),
    "369": ("Human Army", "Horde", "(Wave 4) (Enemy-only)"),
    "36a": ("Human Army", "Horde", "(Wave 5) (Enemy-only)"),
    "36b": ("A. Lucifer", "Tyrant", ""),
    "36c": ("A. Beelzebub", "Tyrant", ""),
    "36d": ("A. Lucifuge", "Tyrant", ""),
    "36e": ("A. Merkabah", "Herald", ""),
    "36f": ("A. Aniel", "Herald", ""),
    "370": ("A. Azrael", "Herald", ""),
    "371": ("Pachacamac", "Vile", "(Boss version)"),
    "372": ("Mushussu", "Drake", "(Boss version)"),
    "373": ("Gemori", "Fallen", "(Boss version)"),
    "374": ("Murmur", "Fallen", "(Boss version)"),
    "375": ("Master Therion", "Yoma", "(Boss version)"),
    "376": ("Dominion", "Divine", "(Boss version)"),
    "377": ("Throne", "Divine", "(Boss version)"),
    "378": ("Abaddon", "Tyrant", "(Boss version)"),
    "379": ("Barbatos", "Fallen", "(Boss version)"),
    "37a": ("Fafnir", "Drake", "(Boss version)"),
    "37b": ("Pales", "Vile", "(Boss version)"),
    "37c": ("Michizane", "Famed", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "37d": ("Yamato Takeru", "Famed", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "37e": ("Merkabah", "Tyrant", "(?) (Tyrant? No idea what this was supposed to be.)"),
    "37f": ("Belial", "Tyrant", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "380": ("Karasu Tengu", "Yoma", "(?) (Boss version, appropriate resist/attack)"),
    "381": ("Koppa Tengu", "Yoma", "(?) (Boss version, appropriate resist/attack)"),
    "382": ("Ose", "Fallen", "(?) (Boss version, appropriate resist/attack)"),
    "383": ("Kaiwan", "Night", "(?) (Boss version, appropriate resist/attack)"),
    "384": ("A. Nebiros", "Fallen", ""),
    "385": ("A. Adramelech", "Fallen", ""),
    "386": ("A. Barbatos", "Fallen", ""),
    "387": ("A. Murmur", "Fallen", ""),
    "388": ("A. Dantalian", "Fallen", ""),
    "389": ("A. Belial", "Tyrant", ""),
    "38a": ("A. Alciel", "Vile", ""),
    "38b": ("A. Cherub", "Divine", ""),
    "38c": ("A. Throne", "Divine", ""),
    "38d": ("A. Dominion", "Divine", ""),
    "38e": ("A. Virtue", "Divine", ""),
    "38f": ("A. Power", "Divine", ""),
    "390": ("A. Angel", "Divine", ""),
    "391": ("Chimera", "Avatar", "(Twisted Tokyo version)"),
    "392": ("Legion", "Spirit", "(Twisted Tokyo version)"),
    "393": ("Inferno", "Spirit", "(Twisted Tokyo version)"),
    "394": ("Hitokotonuchi", "Kunitsu", "(Twisted Tokyo version)"),
    "395": ("Corpse", "Undead", "(Twisted Tokyo version)"),
    "396": ("Slime", "Foul", "(Twisted Tokyo version)"),
    "397": ("Attis", "Zealot", "(Twisted Tokyo version)"),
    "398": ("Kaiming Shou", "Avatar", "(Twisted Tokyo version)"),
    "399": ("Itsumade", "Raptor", "(Twisted Tokyo version)"),
    "39a": ("Vetala", "Ghost", "(Twisted Tokyo version)"),
    "39b": ("Chernobog", "Fury", "(Twisted Tokyo version)"),
    "39c": ("Yatagarasu", "Avian", "(Twisted Tokyo version)"),
    "39d": ("Orthrus", "Beast", "(Twisted Tokyo version)"),
    "39e": ("Black Maria", "Lady", "(Twisted Tokyo version)"),
    "39f": ("Tlazolteotl", "Megami", "(Twisted Tokyo version)"),
    "3a0": ("Kanbari", "Enigma", "(Twisted Tokyo version)"),
    "3a1": ("Peallaidh", "Wilder", "(Twisted Tokyo version)"),
    "3a2": ("Ogun", "Zealot", "(Twisted Tokyo version)"),
    "3a3": ("Ometeotl", "Deity", "(Twisted Tokyo version)"),
    "3a4": ("Ukano Mitama", "Avatar", "(Twisted Tokyo version)"),
    "3a5": ("Centaur", "Yoma", "(Twisted Tokyo version)"),
    "3a6": ("Yggdrasil", "Tree", "(Twisted Tokyo version)"),
    "3a7": ("Skadi", "Lady", "(Twisted Tokyo version)"),
    "3a8": ("Taotie", "Vile", "(Twisted Tokyo version)"),
    "3a9": ("Kingu", "Drake", "(Twisted Tokyo version)"),
    "3aa": ("Azazel", "Tyrant", "(Twisted Tokyo version)"),
    "3ab": ("Hachiman", "Deity", "(Twisted Tokyo version)"),
    "3ac": ("Kartikeya", "Fury", "(Twisted Tokyo version)"),
    "3ad": ("Tezcatilipoca", "Zealot", "(Twisted Tokyo version)"),
    "3ae": ("Girimehkala", "Jaki", "(Twisted Tokyo version)"),
    "3af": ("Nergal", "Reaper", "(Twisted Tokyo version)"),
    "3b0": ("Botis", "Fallen", "(Twisted Tokyo version)"),
    "3b1": ("Kangiten", "Enigma", "(Twisted Tokyo version)"),
    "3b2": ("Surt", "Tyrant", "(Twisted Tokyo version)"),
    "3b3": ("Python", "Drake", "(Twisted Tokyo version)"),
    "3b4": ("", "Mot", "(Twisted Tokyo version)"),
    "3b5": ("Vasuki", "Drake", "(Twisted Tokyo version)"),
    "3b6": ("Samael", "Fallen", "(Twisted Tokyo version)"),
    "3b7": ("Itsumade Horde", "Horde", "(Twisted Tokyo version)"),
    "3b8": ("Wildfire Horde", "Horde", "(Twisted Tokyo version)"),
    "3b9": ("Pirate Horde", "Horde", "(Twisted Tokyo version)"),
    "3ba": ("Yomi Army", "Horde", "(Twisted Tokyo version)"),
    "3bb": ("Frosts", "Horde", "(Twisted Tokyo version)"),
    "3bc": ("Defiant Horde", "Horde", "(Twisted Tokyo version)"),
    "3bd": ("Demon Horde", "Horde", "(Twisted Tokyo version)"),
    "3be": ("Formorian", "Night", "(Tir Na Nog version)"),
    "3bf": ("Dormarth", "Beast", "(Tir Na Nog version)"),
    "3c0": ("Setanta", "Fairy", "(Tir Na Nog version)"),
    "3c1": ("Wicker Man", "Spirit", "(Tir Na Nog version)"),
    "3c2": ("Skadi", "Lady", "(Tir Na Nog version)"),
    "3c3": ("Scathach", "Megami", "(Tir Na Nog version)"),
    "3c4": ("Brigid", "Megami", "(Tir Na Nog version)"),
    "3c5": ("Balor", "Tyrant", "(Tir Na Nog version)"),
    "3c6": ("Cu Chulainn", "Genma", "(Tir Na Nog version)"),
    "3c7": ("Queen Mab", "Night", "(Tir Na Nog version)"),
    "3c8": ("Cernunnos", "Reaper", "(Tir Na Nog version)"),
    "3c9": ("Formorian", "Night", "(Tir Na Nog version)"),
    "3ca": ("Dormarth", "Beast", "(Tir Na Nog version)"),
    "3cb": ("Setanta", "Fairy", "(Tir Na Nog version)"),
    "3cc": ("Wicker Man", "Spirit", "(Tir Na Nog version)"),
    "3cd": ("Skadi", "Lady", "(Tir Na Nog version)"),
    "3ce": ("Scathach", "Megami", "(Tir Na Nog version)"),
    "3cf": ("Brigid", "Megami", "(Tir Na Nog version)"),
    "3d0": ("Balor", "Tyrant", "(Tir Na Nog version)"),
    "3d1": ("Cu Chulainn", "Genma", "(Tir Na Nog version)"),
    "3d2": ("Queen Mab", "Night", "(Tir Na Nog version)"),
    "3d3": ("Cernunnos", "Reaper", "(Tir Na Nog version)"),
    "3d4": ("Formorian", "Night", "(Tir Na Nog version)"),
    "3d5": ("Mother Harlot", "Fiend", "(Boss version)"),
    "3d6": ("Trumpeter", "Fiend", "(Boss version)"),
    "3d7": ("Pale Rider", "Fiend", "(Boss version)"),
    "3d8": ("Black Rider", "Fiend", "(Boss version)"),
    "3d9": ("Red Rider", "Fiend", "(Boss version)"),
    "3da": ("White Rider", "Fiend", "(Boss version)"),
    "3db": ("Not Used", "Fiend", "(?) (Entire portrait is solid white) (Null: Dark, Resist: Light) (Probably used to be Chemtrail)"),
    "3dc": ("Matador", "Fiend", "(Boss version)"),
    "3dd": ("David", "Fiend", "(Boss version)"),
    "3de": ("Not Used", "Tree", "(?)"),
    "3df": ("Lucifer", "Tyrant", "(?) (Unused leftover from SMTIV, guest ally version?)"),
    "3e0": ("Lucifer", "Tyrant", "(?) (Unused leftover from SMTIV, guest ally version?)"),
    "3e1": ("Merkabah", "Herald", "(?) (Unused leftover from SMTIV, guest ally version?)"),
    "3e2": ("Merkabah", "Herald", "(?) (Unused leftover from SMTIV, guest ally version?)"),
    "3e3": ("Adramelech", "Fallen", "(Shesha fight ally)"),
    "3e4": ("Archangel", "Divine", "(Shesha fight ally)"),
    "3e5": ("Principality", "Divine", "(Boss version)"),
    "3e6": ("Ose", "Fallen", "(Boss version)"),
    "3e7": ("Fortuna", "Megami", "(Boss version)"),
    "3e8": ("Not Used", "Tree", "(?)"),
    "3e9": ("Ippon-Datara", "Jaki", "(?) (Unused SMTIV Training Battle leftover)"),
    "3ea": ("Horkos", "Tyrant", "(Godslayer Training version)"),
    "3eb": ("Dionysus", "Zealot", "(Godslayer Training version)"),
    "3ec": ("Anubis", "Avatar", "(Godslayer Training version)"),
    "3ed": ("Demonee-ho", "Fairy", "(Godslayer Training version)"),
    "3ee": ("Jack Frost", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "3ef": ("Raiju", "Wilder", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f0": ("Toubyou", "Drake", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f1": ("Pyro Jack", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f2": ("Jack Frost", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f3": ("Jack the Ripper", "Foul", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f4": ("Demonee-ho", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f5": ("Demonstrators", "Horde", ""),
    "3f6": ("Lanling Wang", "Famed", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f7": ("Pyro Jack", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f8": ("Asahi", "Human", ""),
    "3f9": ("Navarre", "Ghost", ""),
    "3fa": ("Nozomi", "Human", ""),
    "3fb": ("Parvati", "Megami", "(Asahi's?)"),
    "3fc": ("Stonka", "Beast", ""),
    "3fd": ("Navarre", "Ghost", ""),
    "3fe": ("Mushussu", "Drake", ""),
    "3ff": ("Sarasvati", "Nymph", "(Asahi's?)"),
    "400": ("Navarre", "Ghost", ""),
    "401": ("Master Therion", "Yoma", "(Godslayer Training version)"),
    "402": ("Aramisaki", "Zealot", "(Godslayer Training version)"),
    "403": ("Ometeotl", "Deity", "(Godslayer Training version)"),
    "404": ("Huoniao", "Raptor", "(Godslayer Training version)"),
    "405": ("Long", "Dragon", "(Godslayer Training version)"),
    "406": ("Ym", "Drake", "(Godslayer Training version)"),
    "407": ("Gaston", "Samurai", ""),
    "408": ("", "Surt", "(Godslayer Training version)"),
    "409": ("Hachiman", "Deity", "(Godslayer Training version)"),
    "40a": ("Vasuki", "Drake", "(Godslayer Training version)"),
    "40b": ("Yaksha", "Brute", "(Godslayer Training version)"),
    "40c": ("Mara", "Tyrant", "(Godslayer Training version)"),
    "40d": ("Botis", "Fallen", "(Godslayer Training version)"),
    "40e": ("Oberon", "Fairy", "(Godslayer Training version)"),
    "40f": ("Cherub", "Divine", "(Godslayer Training version)"),
    "410": ("Zhong Kui", "Kishin", "(?) (Unused SMTIV Training Battle leftover)"),
    "411": ("Nata Taishi", "Genma", "(?) (Unused SMTIV Training Battle leftover)"),
    "412": ("Samyaza", "Tyrant", "(?) (Unused SMTIV Training Battle leftover)"),
    "413": ("Dakini", "Femme", "(?) (Unused SMTIV Training Battle leftover)"),
    "414": ("Nadja", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "415": ("Kushinada-hime", "Kunitsu", "(?) (Unused SMTIV Training Battle leftover)"),
    "416": ("Principality", "Divine", "(?) (Unused SMTIV Training Battle leftover)"),
    "417": ("Power", "Divine", "(?) (Unused SMTIV Training Battle leftover)"),
    "418": ("Momunofu", "Brute", "(?) (Unused SMTIV Training Battle leftover)"),
    "419": ("Okuninushi", "Kunitsu", "(?) (Unused SMTIV Training Battle leftover)"),
    "41a": ("Mad Gasser", "Foul", "(?) (Unused SMTIV Training Battle leftover)"),
    "41b": ("Krishna", "Tyrant", "(Test demon?)"),
    "41c": ("Odin", "King", ""),
    "41d": ("Maitreya", "Cyber", ""),
    "41e": ("Chironnupu", "Archaic", ""),
    "41f": ("Shesha 1st Form", "Archaic", ""),
    "420": ("Inanna Remnant", "Archaic", ""),
    "421": ("Shesha 2nd Form", "Archaic", ""),
    "422": ("Krishna", "Herald", "(Actually Gaston with Gungnir)"),
    "423": ("Merkabah", "Tree", "(Cutscene-related stuff below. Character sprites that appear briefly during battles have to be saved as demons, I guess.)"),
    "424": ("Lucifer", "Tree", ""),
    "425": ("Inanna", "Tree", ""),
    "426": ("Mitra-Buddha", "Tree", "(Portrait shows Inanna, but sprite shows Mitra-Buddha)"),
    "427": ("Dagda", "Tree", "(Portrait shows Mitra-Buddha, sprite shows Dagda)"),
    "428": ("Vishnu-Flynn 1", "Tree", "(Portrait is Dagda, sprite is Vishnu-Flynn)"),
    "429": ("YHVH 1", "Tree", "(Portrait is Vishnu-Flynn, sprite is...Frost Ace)"),
    "42a": ("YHVH 2", "Tree", ""),
    "42b": ("Vishnu-Flynn 2", "Tree", ""),
    "42c": ("Nanashi", "Tree", "(No art, not even a question mark)"),
    "42d": ("Binding Field", "Tree", "(Sprite is the purple field surrounding Flynn when he's crucified)"),
    "42e": ("Crucified Flynn", "Tree", ""),
    "42f": ("Danu", "Tree", ""),
    "430": ("St. Germain Hole", "Tree", ""),
    "431": ("Pillar of Light", "Tree", ""),
    "432": ("Lucifer", "Tree", "(2nd Form Normal) (Sprite is Asahi as your Goddess. Seems like they replaced stuff from SMTIV without actually changing the names.)"),
    "433": ("Michael", "Tree", "(Giant) (Goddess Navarre)"),
    "434": ("Gabriel", "Tree", "(Giant) (Goddess Nozomi)"),
    "435": ("Raphael", "Tree", "(Giant) (Goddess Gaston)"),
    "436": ("Uriel", "Tree", "(Giant) (Goddess Hallelujah)"),
    "437": ("Masakado", "Tree", "(Giant) (Goddess Toki)"),
    "438": ("Charon", "Tree", "(Event) (Goddess Isabeau)"),
    "439": ("Asterius", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43a": ("Aeshma", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43b": ("Ancient of Days", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43c": ("Sanat", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43d": ("Lucifer Hikaru", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43e": ("Silhouette Lucif", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43f": ("Trial Cyber", "Tree", "(?)"),
    "440": ("Trial Cyber", "Tree", "(?)"),
    "441": ("Trial Cyber", "Tree", "(?)"),
    "442": ("Trial Cyber", "Tree", "(?)"),
    "443": ("Trial Cyber", "Tree", "(?)"),
    "444": ("Trial Cyber", "Tree", "(?)"),
    "445": ("Trial Cyber", "Tree", "(?)"),
    "446": ("Trial Cyber", "Tree", "(?)"),
    "447": ("Trial Cyber", "Tree", "(?)"),
    "448": ("Trial Cyber", "Tree", "(?)"),
    "449": ("Mii", "Tree", ""),
    "44a": ("Kei", "Tree", ""),
    "44b": ("Warp Hole", "Tree", ""),
    "44c": ("Trial Cyber", "Tree", "(?)"),
    "44d": ("Egyptian Horde", "Horde", "(Enemy-only)"),
    "44e": ("Demonic Samurai", "???", "(Enemy-only)"),
    "44f": ("Demonic Hope", "???", "(Enemy-only)"),
    "450": ("Demonic Hugo", "???", "(Enemy-only)"),
    "451": ("A. Law Horde", "Horde", "(Enemy-only)"),
    "452": ("A. Chaos Horde", "Horde", "(Enemy-only)"),
    "453": ("En no Ozuno", "Fiend", "(Enemy-only)"),
    "454": ("Cleopatra", "Megami", "(Boss version)"),
    "455": ("Mephisto", "Tyrant", "(Boss version)"),
    "456": ("Stephen", "Meta", "(Sitting) (Enemy-only)"),
    "457": ("Stephen", "Meta", "(Standing) (Enemy-only)"),
    "458": ("A. Neutral Horde", "Horde", "(Enemy-only)"),
    "459": ("Ara Mitama", "Mitama", "(Enemy-only)"),
    "45a": ("Nigi Mitama", "Mitama", "(Enemy-only)"),
    "45b": ("Kushi Mitama", "Mitama", "(Enemy-only)"),
    "45c": ("Saki Mitama", "Mitama", "(Enemy-only)"),
    "45d": ("Dormarth", "Beast", "(Tir Na Nog version)"),
    "45e": ("Setanta", "Fairy", "(Tir Na Nog version)"),
    "45f": ("Wicker Man", "Spirit", "(Tir Na Nog version)"),
    "460": ("Skadi", "Lady", "(Tir Na Nog version)"),
    "461": ("Scathach", "Megami", "(Tir Na Nog version)"),
    "462": ("Brigid", "Megami", "(Tir Na Nog version)"),
    "463": ("Balor", "Tyrant", "(Tir Na Nog version)"),
    "464": ("Cu Chulainn", "Genma", "(Tir Na Nog version)"),
    "465": ("Queen Mab", "Night", "(Tir Na Nog version)"),
    "466": ("Cernunnos", "Reaper", "(Tir Na Nog version)"),
    "467": ("Formorian", "Night", "(Tir Na Nog version)"),
    "468": ("Dormarth", "Beast", "(Tir Na Nog version)"),
    "469": ("Setanta", "Fairy", "(Tir Na Nog version)"),
    "46a": ("Wicker Man", "Spirit", "(Tir Na Nog version)"),
    "46b": ("Skadi", "Lady", "(Tir Na Nog version)"),
    "46c": ("Scathach", "Megami", "(Tir Na Nog version)"),
    "46d": ("Brigid", "Megami", "(Tir Na Nog version)"),
    "46e": ("Balor", "Tyrant", "(Tir Na Nog version)"),
    "46f": ("Cu Chulainn", "Genma", "(Tir Na Nog version)"),
    "470": ("Queen Mab", "Night", "(Tir Na Nog version)"),
    "471": ("Cernunnos", "Reaper", "(Tir Na Nog version)"),
    "472": ("Formorian", "Night", "(Tir Na Nog version)"),
    "473": ("Dormarth", "Beast", "(Tir Na Nog version)"),
    "474": ("Setanta", "Fairy", "(Tir Na Nog version)"),
    "475": ("Wicker Man", "Spirit", "(Tir Na Nog version)"),
    "476": ("Skadi", "Lady", "(Tir Na Nog version)"),
    "477": ("Scathach", "Megami", "(Tir Na Nog version)"),
    "478": ("Brigid", "Megami", "(Tir Na Nog version)"),
    "479": ("Balor", "Tyrant", "(Tir Na Nog version)"),
    "47a": ("Cu Chulainn", "Genma", "(Tir Na Nog version)"),
    "47b": ("Queen Mab", "Night", "(Tir Na Nog version)"),
    "47c": ("Cernunnos", "Reaper", "(Tir Na Nog version)"),
    "47d": ("Trial Cyber", "Tree", "(?)"),
    "47e": ("Trial:Single:Sword", "Tree", "(These are all Mitamas with different attack animations for testing purposes)"),
    "47f": ("Trial:Single:Scimitar", "Tree", ""),
    "480": ("Trial:Single:Spear", "Tree", ""),
    "481": ("Trial:Single:Blunt", "Tree", ""),
    "482": ("Trial:Single:Fist", "Tree", ""),
    "483": ("Trial:Single:Scratch", "Tree", ""),
    "484": ("Trial:Single:Bite", "Tree", ""),
    "485": ("Trial:Single:Gun", "Tree", ""),
    "486": ("Trial:Single:Heavy", "Tree", ""),
    "487": ("Trial:Single:Rifle", "Tree", ""),
    "488": ("Trial:Single:Machinga", "Tree", ""),
    "489": ("Trial:Single:Sword", "Tree", ""),
    "48a": ("Trial:Single:Scimitar", "Tree", ""),
    "48b": ("Trial:Single:Spear", "Tree", ""),
    "48c": ("Trial:Single:Blunt", "Tree", ""),
    "48d": ("Trial:Single:Fist", "Tree", ""),
    "48e": ("Trial:Single:Scratch", "Tree", ""),
    "48f": ("Trial:Single:Bite", "Tree", ""),
    "490": ("Trial:Single:Gun", "Tree", ""),
    "491": ("Trial:Single:Heavy", "Tree", ""),
    "492": ("Trial:Single:Rifle", "Tree", ""),
    "493": ("Erthys", "Element", "(Diamond Realm version)"),
    "494": ("Aeros", "Element", "(Diamond Realm version)"),
    "495": ("Aquans", "Element", "(Diamond Realm version)"),
    "496": ("Flaemis", "Element", "(Diamond Realm version)"),
    "497": ("Demonic Citizens", "???", "(Enemy-only)"),
    "498": ("Demonic Citizens", "???", "(Enemy-only)"),
    "499": ("Demonic Citizens", "???", "(Enemy-only)"),
    "49a": ("Demonic Citizens", "???", "(Enemy-only)"),
    "49b": ("Demonic Horde", "Horde", "(Enemy-only)"),
    "49c": ("Demonic Horde", "Horde", "(Enemy-only)"),
    "49d": ("The Hero", "Human", ""),
    "49e": ("Aleph", "Replicant", ""),
    "49f": ("Demi-fiend", "Chaos", ""),
    "4a0": ("Flynn", "Human", "(Stephen Fight)"),
}

class mytestapp(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.minsize(400, 100)
        self.title("Shin Megami Tensei IV Save Editor")
        self.bind(sequence="<Escape>", func=lambda x: self.quit())
        self.resizable(width="False", height="False")
        self.grid()

        self.initVars()
        self.processList()
        self.createWidgets()
        # x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        # y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        # self.geometry("+%d+%d" % (x, y))
        # self.initialSetup()


    def initVars(self):
        self.saveFilePath = None
        self.saveFileDir = None
        self.saveFileName = None
        self.save_bytes = None
        self.mcValues = {}
        self.mcSelSkill = {}
        self.mcNewSkill = {}
        self.miscValues = {}
        self.deValues = {}
        self.deSelSkill = {}
        self.deNewSkill = {}
        self.demonList = []
        self.vcmd = (self.register(self.validate_int), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.deSkillTB = []


    def processList(self):
        skillIDNameList = []
        # max_width = 0
        for val in SKILL_IDS:
            if val in ALL_SKILLS:
                # tmp_str = val + " - " + ALL_SKILLS[val][0]
                # if len(tmp_str) > max_width:
                #     max_width = len(tmp_str)
                skillIDNameList.append(val + " - " + ALL_SKILLS[val][0])
            else:
                skillIDNameList.append(val + " - None")
        self.skillIDNameList = skillIDNameList
        # self.skillIDNameWidth = max_width


    def createWidgets(self):
        # Menu bar
        menubar = tk.Menu(self)
        submenu1 = tk.Menu(menubar, tearoff=0)
        submenu1.add_command(label="Open Save File", underline=0, command=self.openFileChooser)
        submenu1.add_command(label="Save Changes", underline=0, command=self.saveChanges)
        submenu1.add_separator()
        submenu1.add_command(label="Exit", underline=0, command=self.exitApp)
        menubar.add_cascade(label="File", underline=0, menu=submenu1)
        menubar.add_separator()
        # submenu2 = tk.Menu(menubar, tearoff=0)
        # submenu2.add_command(label="Compare difference(s)", command=self.>Diff)
        # menubar.add_cascade(label="Compare", menu=submenu2)
        menubar.add_command(label="About", command=self.aboutCreator)
        self.config(menu=menubar)

        # Main content frame
        mainFrame = tk.Frame(self)
        mainFrame.grid(column=0, row=0, padx=10, pady=10, sticky="EW")
        self.mainFrame = mainFrame

        # Frame for folder paths
        folderpathFrame = tk.Frame(mainFrame)
        folderpathFrame.grid(column=0, row=1, sticky="EW")
        folderpathFrame.grid_columnconfigure(1, weight=1)
        tk.Label(folderpathFrame, text="Save file: ").grid(column=0, row=1, sticky="W")
        self.saveFilePathTxt = tk.StringVar()
        tk.Entry(
            folderpathFrame, textvariable=self.saveFilePathTxt, state='readonly', width=80
        ).grid(column=1, row=1, sticky="EW", padx="5 0")

        # Frame for tab buttons
        tabButtonsFrame = tk.Frame(mainFrame)
        tabButtonsFrame.grid(column=0, row=2, pady="20 0", sticky="EW")
        self.tab1Button = tk.Button(
            tabButtonsFrame, text="Main Character", relief="sunken", state="disabled",
            command=lambda: self.changeTab(self.tab1Frame, self.tab1Button)
        )
        self.tab1Button.grid(column=0, row=0, sticky="W")
        self.tab2Button = tk.Button(
            tabButtonsFrame, text="Demons",
            command=lambda: self.changeTab(self.tab2Frame, self.tab2Button)
        )
        self.tab2Button.grid(column=1, row=0, sticky="W")
        self.tab3Button = tk.Button(
            tabButtonsFrame, text="Miscellaneous",
            command=lambda: self.changeTab(self.tab3Frame, self.tab3Button)
        )
        self.tab3Button.grid(column=2, row=0, sticky="W")

        # Frame for tab frames
        tabFramesFrame = tk.Frame(mainFrame)
        tabFramesFrame.grid(column=0, row=3, sticky="EW")
        tabFramesFrame.columnconfigure(0, weight=1)

        # Frame for 1st tab
        tab1Frame = tk.Frame(tabFramesFrame, bd="2", relief="sunken", padx="10", pady="10")
        self.tab1Frame = tab1Frame
        tab1Frame.grid(column=0, row=0, sticky="EW")
        self.mcValues["level"] = tk.StringVar()
        self.mcValues["max_hp"] = tk.StringVar()
        self.mcValues["max_mp"] = tk.StringVar()
        self.mcValues["curr_hp"] = tk.StringVar()
        self.mcValues["curr_mp"] = tk.StringVar()
        self.mcValues["stats"] = []
        self.mcValues["skills"] = []
        for x in range(0, len(STAT_TXT)):
            self.mcValues["stats"].append(tk.StringVar())
        for x in range(0, DE_SKILL[2]):
            self.mcValues["skills"].append(tk.StringVar())

        # Top inner frame for 1st tab
        tab1TopFrame = tk.Frame(tab1Frame)
        tab1TopFrame.grid(column=0, row=0, columnspan=2, sticky="NW")


        # Top left inner frame for 1st tab
        tab1TopLFrame = tk.Frame(tab1TopFrame)
        tab1TopLFrame.grid(column=0, row=0, sticky="NW")
        tk.Label(
            tab1TopLFrame, text="Skills: ", font=("Helvetica", 15, "bold")
        ).grid(column=0, row=0, sticky="W", pady="0 10")
        eval_link = lambda p: (lambda _: self.showMCSelSkill(p, self.mcValues["skills"][p-1].get()))
        for x in range(1, 9):
            tk.Label(tab1TopLFrame, text="Slot %d: " % x).grid(column=0, row=x, sticky="W")
            tmp_handle = tk.Entry(
                tab1TopLFrame, textvariable=self.mcValues["skills"][x-1], state="readonly"
            )
            tmp_handle.grid(column=1, row=x, sticky="EW", padx="5 0")
            tmp_handle.bind(
                "<Button-1>", eval_link(x)
            )

        # Top right inner frame for 1st tab
        tab1TopRFrame = tk.Frame(tab1TopFrame)
        tab1TopRFrame.grid(column=1, row=0, sticky="NW", padx="70 0")
        tk.Label(
            tab1TopRFrame, text="Stats: ", font=("Helvetica", 15, "bold")
        ).grid(column=0, row=0, columnspan=2, sticky="W", pady="0 10")
        # Level
        tk.Label(tab1TopRFrame, text="Level: ").grid(column=0, row=1, sticky="W")
        tk.Entry(
            tab1TopRFrame, textvariable=self.mcValues["level"], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=1, sticky="EW", padx="5 0")
        # HP Max
        tk.Label(tab1TopRFrame, text="Max HP: ").grid(column=0, row=2, sticky="W")
        tk.Entry(
            tab1TopRFrame, textvariable=self.mcValues["max_hp"], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=2, sticky="EW", padx="5 0")
        # MP Max
        tk.Label(tab1TopRFrame, text="Max MP: ").grid(column=0, row=3, sticky="W")
        tk.Entry(
            tab1TopRFrame, textvariable=self.mcValues["max_mp"], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=3, sticky="EW", padx="5 0")
        tk.Label(tab1TopRFrame, text="Current HP: ").grid(column=0, row=4, sticky="W")
        tk.Entry(
            tab1TopRFrame, textvariable=self.mcValues["curr_hp"], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=4, sticky="EW", padx="5 0")
        tk.Label(tab1TopRFrame, text="Current MP: ").grid(column=0, row=5, sticky="W")
        tk.Entry(
            tab1TopRFrame, textvariable=self.mcValues["curr_mp"], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=5, sticky="EW", padx="5 0")
        tk.Label(tab1TopRFrame, text="Strength: ").grid(column=0, row=6, sticky="W")
        tk.Entry(
            tab1TopRFrame, textvariable=self.mcValues["stats"][0], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=6, sticky="EW", padx="5 0")
        tk.Label(tab1TopRFrame, text="Dexterity: ").grid(column=0, row=7, sticky="W")
        tk.Entry(
            tab1TopRFrame, textvariable=self.mcValues["stats"][1], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=7, sticky="EW", padx="5 0")
        tk.Label(tab1TopRFrame, text="Magic: ").grid(column=0, row=8, sticky="W")
        tk.Entry(
            tab1TopRFrame, textvariable=self.mcValues["stats"][2], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=8, sticky="EW", padx="5 0")
        tk.Label(tab1TopRFrame, text="Agility: ").grid(column=0, row=9, sticky="W")
        tk.Entry(
            tab1TopRFrame, textvariable=self.mcValues["stats"][3], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=9, sticky="EW", padx="5 0")
        tk.Label(tab1TopRFrame, text="Luck: ").grid(column=0, row=10, sticky="W")
        tk.Entry(
            tab1TopRFrame, textvariable=self.mcValues["stats"][4], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=10, sticky="EW", padx="5 0")

        # Middle inner frame for 1st tab
        tab1MidFrame = tk.Frame(tab1Frame)
        tab1MidFrame.grid(column=0, row=1, columnspan=2, sticky="NW")

        # Frame (skill info) for middle inner frame for 1st tab
        tab1MidInfoFrame = tk.Frame(tab1MidFrame, bd="2", relief="sunken", padx="5", pady="5")
        tab1MidInfoFrame.grid(column=0, row=0, sticky="NEW", pady="20 0")
        self.mcSelSkill["slot_no"] = tk.IntVar()
        self.mcSelSkill["id"] = tk.StringVar()
        self.mcSelSkill["name"] = tk.StringVar()
        self.mcSelSkill["type"] = tk.StringVar()
        self.mcSelSkill["mp"] = tk.IntVar()
        self.mcSelSkill["dmg"] = tk.StringVar()
        self.mcSelSkill["target"] = tk.StringVar()

        tk.Label(
            tab1MidInfoFrame, text="Selected Skill Info:", font=("Helvetica", 11, "underline")
        ).grid(column=0, row=0, columnspan=2, sticky="W", pady="0 10")

        tk.Label(tab1MidInfoFrame, text="Selected Slot: ").grid(column=0, row=1, sticky="W")
        tk.Entry(
            tab1MidInfoFrame, textvariable=self.mcSelSkill["slot_no"], state="readonly"
        ).grid(column=1, row=1, sticky="EW", padx="5 0")
        tk.Label(tab1MidInfoFrame, text="Skill ID: ").grid(column=0, row=2, sticky="W")
        tk.Entry(
            tab1MidInfoFrame, textvariable=self.mcSelSkill["id"], state="readonly"
        ).grid(column=1, row=2, sticky="EW", padx="5 0")
        tk.Label(tab1MidInfoFrame, text="Skill Name: ").grid(column=0, row=3, sticky="W")
        tk.Entry(
            tab1MidInfoFrame, textvariable=self.mcSelSkill["name"], state="readonly"
        ).grid(column=1, row=3, sticky="EW", padx="5 0")
        tk.Label(tab1MidInfoFrame, text="Skill Desc: ").grid(column=0, row=4, sticky="W")
        desc_text = tk.Text(
            tab1MidInfoFrame, height=5, width=30, state="disabled"
        )
        self.mcSelSkill["desc"] = desc_text
        desc_text.grid(column=1, row=4, sticky="EW", padx="5 0")

        tk.Label(tab1MidInfoFrame, text="Skill Type: ").grid(column=0, row=5, sticky="W")
        tk.Entry(
            tab1MidInfoFrame, textvariable=self.mcSelSkill["type"], state="readonly"
        ).grid(column=1, row=5, sticky="EW", padx="5 0")
        tk.Label(tab1MidInfoFrame, text="Skill MP: ").grid(column=0, row=6, sticky="W")
        tk.Entry(
            tab1MidInfoFrame, textvariable=self.mcSelSkill["mp"], state="readonly"
        ).grid(column=1, row=6, sticky="EW", padx="5 0")
        tk.Label(tab1MidInfoFrame, text="Skill Damage: ").grid(column=0, row=7, sticky="W")
        tk.Entry(
            tab1MidInfoFrame, textvariable=self.mcSelSkill["dmg"], state="readonly"
        ).grid(column=1, row=7, sticky="EW", padx="5 0")
        tk.Label(tab1MidInfoFrame, text="Skill Target: ").grid(column=0, row=8, sticky="W")
        tk.Entry(
            tab1MidInfoFrame, textvariable=self.mcSelSkill["target"], state="readonly"
        ).grid(column=1, row=8, sticky="EW", padx="5 0")

        mcChngSkillBtn = tk.Button(
            tab1MidInfoFrame, text="Change Skill", command=lambda: self.mcNewSkillVisible(mcChngSkillBtn)
        )
        mcChngSkillBtn.grid(column=0, row=10, columnspan=2, sticky="EW", pady="10 0")

        # Frame (replace skill) for middle inner frame for 1st tab
        tab1MidNewFrame = tk.Frame(tab1MidFrame, bd="2", relief="sunken", padx="5", pady="5")
        self.tab1MidNewFrame = tab1MidNewFrame
        tab1MidNewFrame.grid(column=1, row=0, columnspan=2, sticky="N", padx="20 0", pady="20 0")
        self.mcNewSkill["desc"] = tk.StringVar()
        self.mcNewSkill["type"] = tk.StringVar()
        self.mcNewSkill["mp"] = tk.IntVar()
        self.mcNewSkill["dmg"] = tk.StringVar()
        self.mcNewSkill["target"] = tk.StringVar()

        tk.Label(
            tab1MidNewFrame, text="New Skill Info:", font=("Helvetica", 11, "underline")
        ).grid(column=0, row=0, columnspan=2, sticky="W", pady="0 10")

        tk.Label(tab1MidNewFrame, text="Skill: ").grid(column=0, row=2, sticky="W")
        mcSkillListFrame = tk.Frame(tab1MidNewFrame, bd="2", relief="sunken")
        mcSkillListFrame.grid(column=1, row=2, padx="5 0", sticky="EW")
        mcSkillListFrame.columnconfigure(0, weight=1)
        mcSkillScrollbar = tk.Scrollbar(mcSkillListFrame)
        mcSkillScrollbar.grid(column=1, row=0, sticky="NS")
        mcSkillListBox = tk.Listbox(
            mcSkillListFrame, yscrollcommand=mcSkillScrollbar.set, height=5,# width=self.skillIDNameWidth
            exportselection=0
        )
        self.mcSkillListBox = mcSkillListBox
        mcSkillListBox.insert(tk.END, *self.skillIDNameList)
        mcSkillListBox.grid(column=0, row=0, sticky="EW")
        mcSkillListBox.bind("<<ListboxSelect>>", self.showMCNewSkill)
        mcSkillScrollbar.config(command=mcSkillListBox.yview)

        tk.Label(tab1MidNewFrame, text="Skill Desc: ").grid(column=0, row=3, sticky="W")
        desc_text = tk.Text(
            tab1MidNewFrame, height=5, width=30, state="disabled"
        )
        self.mcNewSkill["desc"] = desc_text
        desc_text.grid(column=1, row=3, sticky="EW", padx="5 0")

        tk.Label(tab1MidNewFrame, text="Skill Type: ").grid(column=0, row=4, sticky="W")
        tk.Entry(
            tab1MidNewFrame, textvariable=self.mcNewSkill["type"], state="readonly"
        ).grid(column=1, row=4, sticky="EW", padx="5 0")
        tk.Label(tab1MidNewFrame, text="Skill MP: ").grid(column=0, row=5, sticky="W")
        tk.Entry(
            tab1MidNewFrame, textvariable=self.mcNewSkill["mp"], state="readonly"
        ).grid(column=1, row=5, sticky="EW", padx="5 0")
        tk.Label(tab1MidNewFrame, text="Skill Damage: ").grid(column=0, row=6, sticky="W")
        tk.Entry(
            tab1MidNewFrame, textvariable=self.mcNewSkill["dmg"], state="readonly"
        ).grid(column=1, row=6, sticky="EW", padx="5 0")
        tk.Label(tab1MidNewFrame, text="Skill Target: ").grid(column=0, row=7, sticky="W")
        tk.Entry(
            tab1MidNewFrame, textvariable=self.mcNewSkill["target"], state="readonly"
        ).grid(column=1, row=7, sticky="EW", padx="5 0")

        tk.Button(
            tab1MidNewFrame, text="Replace", command=self.updateMCSkill
        ).grid(column=0, row=10, columnspan=2, sticky="EW", pady="10 0")

        # Bottom inner frame for 1st tab
        tab1BtmFrame = tk.Frame(tab1Frame, bd="2", relief="sunken")
        tab1BtmFrame.grid(column=0, row=2, columnspan=2, sticky="EW", pady="20 0")
        tab1BtmFrame.columnconfigure(0, weight=1)
        tk.Button(
            tab1BtmFrame, text="Apply", command=self.applyMCChanges
        ).grid(column=0, row=0, sticky="EW")

        # Frame for 2nd tab
        tab2Frame = tk.Frame(tabFramesFrame, bd="2", relief="sunken", padx="10", pady="10")
        self.tab2Frame = tab2Frame
        tab2Frame.grid(column=0, row=0, sticky="EW")

        # Top inner frame for 2nd tab
        tab2TopFrame = tk.Frame(tab2Frame)
        tab2TopFrame.grid(column=0, row=0, sticky="NW")

        # Top left inner frame for 2nd tab
        tab2TopLFrame = tk.Frame(tab2TopFrame)
        tab2TopLFrame.grid(column=0, row=0, sticky="NW")
        self.deValues["race"] = tk.StringVar()

        tk.Label(
            tab2TopLFrame, text="Demons: ", font=("Helvetica", 15, "bold")
        ).grid(column=0, row=0, columnspan=2, sticky="W", pady="0 10")
        # Demon List
        tk.Label(tab2TopLFrame, text="Demon: ").grid(column=0, row=1, sticky="W")
        demonListFrame = tk.Frame(tab2TopLFrame, bd="2", relief="sunken")
        demonListFrame.grid(column=1, row=1, padx="5 0", sticky="EW")
        demonListFrame.columnconfigure(0, weight=1)
        demonScrollbar = tk.Scrollbar(demonListFrame)
        demonScrollbar.grid(column=1, row=0, sticky="NS")
        demonListBox = tk.Listbox(
            demonListFrame, yscrollcommand=demonScrollbar.set, height=5, font=("Consolas", 10),
            width=40, exportselection=0
        )
        self.demonListBox = demonListBox
        demonListBox.grid(column=0, row=0, sticky="EW")
        demonListBox.bind("<<ListboxSelect>>", self.showDemonValues)
        demonScrollbar.config(command=demonListBox.yview)
        # Demon Race
        tk.Label(tab2TopLFrame, text="Race: ").grid(column=0, row=2, sticky="W")
        tk.Entry(
            tab2TopLFrame, textvariable=self.deValues["race"], state="readonly"
        ).grid(column=1, row=2, sticky="EW", padx="5 0")
        # # Demon Description (if any)
        # tk.Label(tab2TopLFrame, text="Desc: ").grid(column=0, row=3, sticky="W")
        # de_desc_text = tk.Text(
        #     tab2TopLFrame, height=5, width=30, state="disabled"
        # )
        # de_desc_text.grid(column=1, row=4, sticky="EW", padx="5 0")
        # self.deValues["desc"] = de_desc_text


        # Top middle inner frame for 2nd tab
        tab2TopMFrame = tk.Frame(tab2TopFrame)
        tab2TopMFrame.grid(column=1, row=0, sticky="NW", padx="70 0", )
        self.deValues["level"] = tk.StringVar()
        self.deValues["max_hp"] = tk.StringVar()
        self.deValues["max_mp"] = tk.StringVar()
        self.deValues["curr_hp"] = tk.StringVar()
        self.deValues["curr_mp"] = tk.StringVar()
        self.deValues["stats"] = []
        self.deValues["skills"] = []
        for x in range(0, len(STAT_TXT)):
            self.deValues["stats"].append(tk.StringVar())
        for x in range(0, DE_SKILL[2]):
            self.deValues["skills"].append(tk.StringVar())

        tk.Label(
            tab2TopMFrame, text="Stats: ", font=("Helvetica", 15, "bold")
        ).grid(column=0, row=0, columnspan=2, sticky="W", pady="0 10")
        # Level
        tk.Label(tab2TopMFrame, text="Level: ").grid(column=0, row=1, sticky="W")
        tk.Entry(
            tab2TopMFrame, textvariable=self.deValues["level"], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=1, sticky="EW", padx="5 0")
        # HP Max
        tk.Label(tab2TopMFrame, text="Max HP: ").grid(column=0, row=2, sticky="W")
        tk.Entry(
            tab2TopMFrame, textvariable=self.deValues["max_hp"], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=2, sticky="EW", padx="5 0")
        # MP Max
        tk.Label(tab2TopMFrame, text="Max MP: ").grid(column=0, row=3, sticky="W")
        tk.Entry(
            tab2TopMFrame, textvariable=self.deValues["max_mp"], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=3, sticky="EW", padx="5 0")
        tk.Label(tab2TopMFrame, text="Current HP: ").grid(column=0, row=4, sticky="W")
        tk.Entry(
            tab2TopMFrame, textvariable=self.deValues["curr_hp"], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=4, sticky="EW", padx="5 0")
        tk.Label(tab2TopMFrame, text="Current MP: ").grid(column=0, row=5, sticky="W")
        tk.Entry(
            tab2TopMFrame, textvariable=self.deValues["curr_mp"], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=5, sticky="EW", padx="5 0")
        tk.Label(tab2TopMFrame, text="Strength: ").grid(column=0, row=6, sticky="W")
        tk.Entry(
            tab2TopMFrame, textvariable=self.deValues["stats"][0], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=6, sticky="EW", padx="5 0")
        tk.Label(tab2TopMFrame, text="Dexterity: ").grid(column=0, row=7, sticky="W")
        tk.Entry(
            tab2TopMFrame, textvariable=self.deValues["stats"][1], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=7, sticky="EW", padx="5 0")
        tk.Label(tab2TopMFrame, text="Magic: ").grid(column=0, row=8, sticky="W")
        tk.Entry(
            tab2TopMFrame, textvariable=self.deValues["stats"][2], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=8, sticky="EW", padx="5 0")
        tk.Label(tab2TopMFrame, text="Agility: ").grid(column=0, row=9, sticky="W")
        tk.Entry(
            tab2TopMFrame, textvariable=self.deValues["stats"][3], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=9, sticky="EW", padx="5 0")
        tk.Label(tab2TopMFrame, text="Luck: ").grid(column=0, row=10, sticky="W")
        tk.Entry(
            tab2TopMFrame, textvariable=self.deValues["stats"][4], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=10, sticky="EW", padx="5 0")

        # Top right inner frame for 2nd tab
        tab2TopRFrame = tk.Frame(tab2TopFrame)
        tab2TopRFrame.grid(column=2, row=0, sticky="NW", padx="70 0")
        tk.Label(
            tab2TopRFrame, text="Skills: ", font=("Helvetica", 15, "bold")
        ).grid(column=0, row=0, sticky="W", pady="0 10")
        eval_link = lambda p: (lambda _: self.showDeSelSkill(p, self.deValues["skills"][p-1].get()))
        for x in range(1, 9):
            tk.Label(tab2TopRFrame, text="Slot %d: " % x).grid(column=0, row=x, sticky="W")
            tmp_handle = tk.Entry(
                tab2TopRFrame, textvariable=self.deValues["skills"][x-1], state="readonly"
            )
            tmp_handle.grid(column=1, row=x, sticky="EW", padx="5 0")
            tmp_handle.bind("<Button-1>", eval_link(x))
            self.deSkillTB.append(tmp_handle)

        deSkillManualBtn = tk.Button(
            tab2TopRFrame, text="Manual Edit", command=lambda: self.deSkillManualEdit(deSkillManualBtn)
        )
        deSkillManualBtn.grid(column=0, row=9, columnspan=2, sticky="EW", pady="10 0")
        self.deSkillManual = False

        # Middle inner frame for 2nd tab
        tab2MidFrame = tk.Frame(tab2Frame)
        tab2MidFrame.grid(column=0, row=1, columnspan=2, sticky="NW")

        # Frame (skill info) for middle inner frame for 2nd tab
        tab2MidInfoFrame = tk.Frame(tab2MidFrame, bd="2", relief="sunken", padx="5", pady="5")
        tab2MidInfoFrame.grid(column=0, row=0, sticky="NEW", pady="20 0")
        self.deSelSkill["slot_no"] = tk.IntVar()
        self.deSelSkill["id"] = tk.StringVar()
        self.deSelSkill["name"] = tk.StringVar()
        self.deSelSkill["type"] = tk.StringVar()
        self.deSelSkill["mp"] = tk.IntVar()
        self.deSelSkill["dmg"] = tk.StringVar()
        self.deSelSkill["target"] = tk.StringVar()

        tk.Label(
            tab2MidInfoFrame, text="Selected Skill Info:", font=("Helvetica", 11, "underline")
        ).grid(column=0, row=0, columnspan=2, sticky="W", pady="0 10")

        tk.Label(tab2MidInfoFrame, text="Selected Slot: ").grid(column=0, row=1, sticky="W")
        tk.Entry(
            tab2MidInfoFrame, textvariable=self.deSelSkill["slot_no"], state="readonly"
        ).grid(column=1, row=1, sticky="EW", padx="5 0")
        tk.Label(tab2MidInfoFrame, text="Skill ID: ").grid(column=0, row=2, sticky="W")
        tk.Entry(
            tab2MidInfoFrame, textvariable=self.deSelSkill["id"], state="readonly"
        ).grid(column=1, row=2, sticky="EW", padx="5 0")
        tk.Label(tab2MidInfoFrame, text="Skill Name: ").grid(column=0, row=3, sticky="W")
        tk.Entry(
            tab2MidInfoFrame, textvariable=self.deSelSkill["name"], state="readonly"
        ).grid(column=1, row=3, sticky="EW", padx="5 0")
        tk.Label(tab2MidInfoFrame, text="Skill Desc: ").grid(column=0, row=4, sticky="W")
        desc_text = tk.Text(
            tab2MidInfoFrame, height=5, width=30, state="disabled"
        )
        self.deSelSkill["desc"] = desc_text
        desc_text.grid(column=1, row=4, sticky="EW", padx="5 0")

        tk.Label(tab2MidInfoFrame, text="Skill Type: ").grid(column=0, row=5, sticky="W")
        tk.Entry(
            tab2MidInfoFrame, textvariable=self.deSelSkill["type"], state="readonly"
        ).grid(column=1, row=5, sticky="EW", padx="5 0")
        tk.Label(tab2MidInfoFrame, text="Skill MP: ").grid(column=0, row=6, sticky="W")
        tk.Entry(
            tab2MidInfoFrame, textvariable=self.deSelSkill["mp"], state="readonly"
        ).grid(column=1, row=6, sticky="EW", padx="5 0")
        tk.Label(tab2MidInfoFrame, text="Skill Damage: ").grid(column=0, row=7, sticky="W")
        tk.Entry(
            tab2MidInfoFrame, textvariable=self.deSelSkill["dmg"], state="readonly"
        ).grid(column=1, row=7, sticky="EW", padx="5 0")
        tk.Label(tab2MidInfoFrame, text="Skill Target: ").grid(column=0, row=8, sticky="W")
        tk.Entry(
            tab2MidInfoFrame, textvariable=self.deSelSkill["target"], state="readonly"
        ).grid(column=1, row=8, sticky="EW", padx="5 0")

        deChngSkillBtn = tk.Button(
            tab2MidInfoFrame, text="Change Skill", command=lambda: self.deNewSkillVisible(deChngSkillBtn)
        )
        deChngSkillBtn.grid(column=0, row=10, columnspan=2, sticky="EW", pady="10 0")

        # Frame (replace skill) for middle inner frame for 2nd tab
        tab2MidNewFrame = tk.Frame(tab2MidFrame, bd="2", relief="sunken", padx="5", pady="5")
        self.tab2MidNewFrame = tab2MidNewFrame
        tab2MidNewFrame.grid(column=1, row=0, columnspan=2, sticky="N", padx="20 0", pady="20 0")
        self.deNewSkill["desc"] = tk.StringVar()
        self.deNewSkill["type"] = tk.StringVar()
        self.deNewSkill["mp"] = tk.IntVar()
        self.deNewSkill["dmg"] = tk.StringVar()
        self.deNewSkill["target"] = tk.StringVar()

        tk.Label(
            tab2MidNewFrame, text="New Skill Info:", font=("Helvetica", 11, "underline")
        ).grid(column=0, row=0, columnspan=2, sticky="W", pady="0 10")

        tk.Label(tab2MidNewFrame, text="Skill: ").grid(column=0, row=2, sticky="W")
        deSkillListFrame = tk.Frame(tab2MidNewFrame, bd="2", relief="sunken")
        deSkillListFrame.grid(column=1, row=2, padx="5 0", sticky="EW")
        deSkillListFrame.columnconfigure(0, weight=1)
        deSkillScrollbar = tk.Scrollbar(deSkillListFrame)
        deSkillScrollbar.grid(column=1, row=0, sticky="NS")
        deSkillListBox = tk.Listbox(
            deSkillListFrame, yscrollcommand=deSkillScrollbar.set, height=5,# width=self.skillIDNameWidth
            exportselection=0
        )
        self.deSkillListBox = deSkillListBox
        deSkillListBox.insert(tk.END, *self.skillIDNameList)
        deSkillListBox.grid(column=0, row=0, sticky="EW")
        deSkillListBox.bind("<<ListboxSelect>>", self.showDeNewSkill)
        deSkillScrollbar.config(command=deSkillListBox.yview)

        tk.Label(tab2MidNewFrame, text="Skill Desc: ").grid(column=0, row=3, sticky="W")
        desc_text = tk.Text(
            tab2MidNewFrame,
            height=5, width=30, state="disabled"
        )
        self.deNewSkill["desc"] = desc_text
        desc_text.grid(column=1, row=3, sticky="EW", padx="5 0")

        tk.Label(tab2MidNewFrame, text="Skill Type: ").grid(column=0, row=4, sticky="W")
        tk.Entry(
            tab2MidNewFrame, textvariable=self.deNewSkill["type"], state="readonly"
        ).grid(column=1, row=4, sticky="EW", padx="5 0")
        tk.Label(tab2MidNewFrame, text="Skill MP: ").grid(column=0, row=5, sticky="W")
        tk.Entry(
            tab2MidNewFrame, textvariable=self.deNewSkill["mp"], state="readonly"
        ).grid(column=1, row=5, sticky="EW", padx="5 0")
        tk.Label(tab2MidNewFrame, text="Skill Damage: ").grid(column=0, row=6, sticky="W")
        tk.Entry(
            tab2MidNewFrame, textvariable=self.deNewSkill["dmg"], state="readonly"
        ).grid(column=1, row=6, sticky="EW", padx="5 0")
        tk.Label(tab2MidNewFrame, text="Skill Target: ").grid(column=0, row=7, sticky="W")
        tk.Entry(
            tab2MidNewFrame, textvariable=self.deNewSkill["target"], state="readonly"
        ).grid(column=1, row=7, sticky="EW", padx="5 0")

        tk.Button(
            tab2MidNewFrame, text="Replace", command=self.updateDeSkill
        ).grid(column=0, row=10, columnspan=2, sticky="EW", pady="10 0")

        # Bottom inner frame for 2nd tab
        tab2BtmFrame = tk.Frame(tab2Frame, bd="2", relief="sunken")
        tab2BtmFrame.grid(column=0, row=2, columnspan=2, sticky="EW", pady="20 0")
        tab2BtmFrame.columnconfigure(0, weight=1)
        tk.Button(
            tab2BtmFrame, text="Apply Changes (for selected demon)", command=self.applyDeChanges
        ).grid(column=0, row=0, sticky="EW")

        # Frame for 3rd tab
        tab3Frame = tk.Frame(tabFramesFrame, bd="2", relief="sunken", padx="10", pady="10")
        self.tab3Frame = tab3Frame
        tab3Frame.grid(column=0, row=0, sticky="EW")
        self.miscValues["macca"] = tk.StringVar()
        self.miscValues["app_pts"] = tk.StringVar()

        tk.Label(
            tab3Frame, text="Miscellaneous: ", font=("Helvetica", 15, "bold")
        ).grid(column=0, row=0, columnspan=2, sticky="W", pady="0 10")
        # Macca
        tk.Label(tab3Frame, text="Macca: ").grid(column=0, row=1, sticky="W")
        tk.Entry(
            tab3Frame, textvariable=self.miscValues["macca"], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=1, sticky="EW", padx="5 0")
        # App Points
        tk.Label(tab3Frame, text="App Points: ").grid(column=0, row=2, sticky="W")
        tk.Entry(
            tab3Frame, textvariable=self.miscValues["app_pts"], validate="key", validatecommand=self.vcmd
        ).grid(column=1, row=2, sticky="EW", padx="5 0")
        tk.Button(
            tab3Frame, text="Apply", command=self.applyMiscChanges
        ).grid(column=0, row=3, columnspan=2, pady="10 0")

        # Hide Replace Skill frame for first & second tab
        self.tab1MidNewFrame.grid_remove()
        self.tab2MidNewFrame.grid_remove()
        self.mcNewSkillShown = False
        self.deNewSkillShown = False

        # Hide the other tabs, only show first tab
        self.tabShown = self.tab1Frame
        self.tabButton = self.tab1Button
        self.tab3Frame.grid_remove()
        self.tab2Frame.grid_remove()


    def deSkillManualEdit(self, button):
        if self.deSkillManual:
            button.config(text="Manual Edit")
            for tb in self.deSkillTB:
                tb.config(state="readonly")
            self.deSkillManual = False
        else:
            button.config(text="End Manual Edit")
            for tb in self.deSkillTB:
                tb.config(state="normal")
            self.deSkillManual = True
            self.showMessage(1, "Warning", "Do not add zero-padding to the Skill ID!" +
                                "\nSkill IDs must also be lower case!" +
                                "\nE.g. Not '01C5', should be '1c5'." +
                                "\n\nIf you are unsure, end 'Manual Edit'" +
                                "\nand use 'Change Skill' instead!")


    def showDeSelSkill(self, slot_no, skill_id):
        if self.save_bytes:
            # print(slot_no, skill_id, ALL_SKILLS[skill_id])
            self.deSelSkill["slot_no"].set(slot_no)
            self.deSelSkill["id"].set(skill_id)
            self.deSelSkill["desc"].config(state="normal")
            self.deSelSkill["desc"].delete("0.0", tk.END)
            if skill_id in ALL_SKILLS:
                skill_info = ALL_SKILLS[skill_id]
                self.deSelSkill["name"].set(skill_info[0])
                self.deSelSkill["desc"].insert("0.0", skill_info[5])
                self.deSelSkill["type"].set(SKILL_TYPE[skill_info[1]])
                self.deSelSkill["mp"].set(skill_info[2])
                self.deSelSkill["dmg"].set(SKILL_DMG[skill_info[3]])
                self.deSelSkill["target"].set(SKILL_TARGET[skill_info[4]])
            else:
                self.deSelSkill["name"].set("")
                self.deSelSkill["type"].set("")
                self.deSelSkill["mp"].set(0)
                self.deSelSkill["dmg"].set("")
                self.deSelSkill["target"].set("")
            self.deSelSkill["desc"].config(state="disabled")


    def showDemonValues(self, evt):
        selection = self.demonListBox.curselection()
        if selection:
            demon_values = self.demonList[selection[0]]
            demon_id = demon_values["id"]
            # self.deValues["desc"].config(state="normal")
            # self.deValues["desc"].delete("0.0", tk.END)
            # print(format(demon_values["start_add"], "x"), demon_values["id"])
            if demon_id in ALL_DEMONS:
                self.deValues["race"].set(ALL_DEMONS[demon_id][1])
                # self.deValues["desc"].insert("0.0", ALL_DEMONS[demon_id][2])
                self.deValues["level"].set(demon_values["level"])
                self.deValues["max_hp"].set(demon_values["max_hp"])
                self.deValues["max_mp"].set(demon_values["max_mp"])
                self.deValues["curr_hp"].set(demon_values["curr_hp"])
                self.deValues["curr_mp"].set(demon_values["curr_mp"])
                for x in range(0, len(STAT_TXT)):
                    self.deValues["stats"][x].set(demon_values["stats"][x])
                for x in range(0, DE_SKILL[2]):
                    self.deValues["skills"][x].set(demon_values["skills"][x])
            else:
                self.deValues["race"].set("")
                self.deValues["level"].set("")
                self.deValues["max_hp"].set("")
                self.deValues["max_mp"].set("")
                self.deValues["curr_hp"].set("")
                self.deValues["curr_mp"].set("")
                for x in range(0, len(STAT_TXT)):
                    self.deValues["stats"][x].set("")
                for x in range(0, DE_SKILL[2]):
                    self.deValues["skills"][x].set("")
            # self.deValues["desc"].config(state="disabled")


    def showMCNewSkill(self, evt):
        selection = self.mcSkillListBox.curselection()
        if selection:
            skill_id = SKILL_IDS[selection[0]]
            self.mcNewSkill["desc"].config(state="normal")
            if skill_id in ALL_SKILLS:
                skill_info = ALL_SKILLS[skill_id]
                self.mcNewSkill["desc"].delete("0.0", tk.END)
                self.mcNewSkill["desc"].insert("0.0", skill_info[5])
                self.mcNewSkill["type"].set(SKILL_TYPE[skill_info[1]])
                self.mcNewSkill["mp"].set(skill_info[2])
                self.mcNewSkill["dmg"].set(SKILL_DMG[skill_info[3]])
                self.mcNewSkill["target"].set(SKILL_TARGET[skill_info[4]])
            else:
                self.mcNewSkill["desc"].delete("0.0", tk.END)
                self.mcNewSkill["type"].set("")
                self.mcNewSkill["mp"].set(0)
                self.mcNewSkill["dmg"].set("")
                self.mcNewSkill["target"].set("")
            self.mcNewSkill["desc"].config(state="disabled")


    def showDeNewSkill(self, evt):
        selection = self.deSkillListBox.curselection()
        if selection:
            skill_id = SKILL_IDS[selection[0]]
            self.deNewSkill["desc"].config(state="normal")
            if skill_id in ALL_SKILLS:
                skill_info = ALL_SKILLS[skill_id]
                self.deNewSkill["desc"].delete("0.0", tk.END)
                self.deNewSkill["desc"].insert("0.0", skill_info[5])
                self.deNewSkill["type"].set(SKILL_TYPE[skill_info[1]])
                self.deNewSkill["mp"].set(skill_info[2])
                self.deNewSkill["dmg"].set(SKILL_DMG[skill_info[3]])
                self.deNewSkill["target"].set(SKILL_TARGET[skill_info[4]])
            else:
                self.deNewSkill["desc"].delete("0.0", tk.END)
                self.deNewSkill["type"].set("")
                self.deNewSkill["mp"].set(0)
                self.deNewSkill["dmg"].set("")
                self.deNewSkill["target"].set("")
            self.deNewSkill["desc"].config(state="disabled")


    def mcNewSkillVisible(self, button):
        if self.mcNewSkillShown:
            self.tab1MidNewFrame.grid_remove()
            self.mcNewSkillShown = False
            button.config(text="Change Skill")
        else:
            self.tab1MidNewFrame.grid()
            self.mcNewSkillShown = True
            button.config(text="End Skill Change")


    def deNewSkillVisible(self, button):
        if self.deNewSkillShown:
            self.tab2MidNewFrame.grid_remove()
            self.deNewSkillShown = False
            button.config(text="Change Skill")
        else:
            self.tab2MidNewFrame.grid()
            self.deNewSkillShown = True
            button.config(text="End Skill Change")


    def updateMCSkill(self):
        if self.save_bytes:
            slot_index = self.mcSelSkill["slot_no"].get() - 1
            if -1 < slot_index < 8:
                selection = self.mcSkillListBox.curselection()
                if selection:
                    skill_id = SKILL_IDS[selection[0]]
                    self.mcValues["skills"][slot_index].set(skill_id)
                    self.showMCSelSkill(slot_index+1, skill_id)


    def updateDeSkill(self):
        if self.save_bytes:
            slot_index = self.deSelSkill["slot_no"].get() - 1
            if -1 < slot_index < 8:
                selection = self.deSkillListBox.curselection()
                if selection:
                    skill_id = SKILL_IDS[selection[0]]
                    self.deValues["skills"][slot_index].set(skill_id)
                    self.showDeSelSkill(slot_index+1, skill_id)


    def validate_int(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if action == "0":
            return True
        try:
            int(value_if_allowed)
            return True
        except ValueError:
            return False


    def changeTab(self, tab_to_show, tab_button):
        if self.tabShown is tab_to_show:
            return
        self.tabShown.grid_remove()
        tab_to_show.grid()
        self.tabButton.config(state="normal", relief="raised")
        tab_button.config(state="disabled", relief="sunken")
        self.tabButton = tab_button
        self.tabShown = tab_to_show


    def showMCSelSkill(self, slot_no, skill_id):
        if self.save_bytes:
            self.mcSelSkill["slot_no"].set(slot_no)
            self.mcSelSkill["id"].set(skill_id)
            self.mcSelSkill["desc"].config(state="normal")
            self.mcSelSkill["desc"].delete("0.0", tk.END)
            if skill_id in ALL_SKILLS:
                skill_info = ALL_SKILLS[skill_id]
                self.mcSelSkill["name"].set(skill_info[0])
                self.mcSelSkill["desc"].insert("0.0", skill_info[5])
                self.mcSelSkill["type"].set(SKILL_TYPE[skill_info[1]])
                self.mcSelSkill["mp"].set(skill_info[2])
                self.mcSelSkill["dmg"].set(SKILL_DMG[skill_info[3]])
                self.mcSelSkill["target"].set(SKILL_TARGET[skill_info[4]])
            else:
                self.mcSelSkill["name"].set("")
                self.mcSelSkill["type"].set("")
                self.mcSelSkill["mp"].set(0)
                self.mcSelSkill["dmg"].set("")
                self.mcSelSkill["target"].set("")
            self.mcSelSkill["desc"].config(state="disabled")


    def clearMCSelSkillInfo(self):
        self.mcSelSkill["slot_no"].set(0)
        self.mcSelSkill["id"].set("")
        self.mcSelSkill["name"].set("")
        self.mcSelSkill["type"].set("")
        self.mcSelSkill["mp"].set(0)
        self.mcSelSkill["dmg"].set("")
        self.mcSelSkill["target"].set("")
        self.mcSelSkill["desc"].config(state="normal")
        self.mcSelSkill["desc"].delete("0.0", tk.END)
        self.mcSelSkill["desc"].config(state="disabled")


    def clearDeStats(self):
        self.deValues["race"].set("")
        # self.deValues["desc"].config(state="normal")
        # self.deValues["desc"].delete("0.0", tk.END)
        # self.deValues["desc"].config(state="disabled")
        self.deValues["level"].set("")
        self.deValues["max_hp"].set("")
        self.deValues["max_mp"].set("")
        self.deValues["curr_hp"].set("")
        self.deValues["curr_mp"].set("")
        for x in range(0, len(STAT_TXT)):
            self.deValues["stats"][x].set("")
        for x in range(0, DE_SKILL[2]):
            self.deValues["skills"][x].set("")


    def clearDeSelSkillInfo(self):
        self.deSelSkill["slot_no"].set(0)
        self.deSelSkill["id"].set("")
        self.deSelSkill["name"].set("")
        self.deSelSkill["type"].set("")
        self.deSelSkill["mp"].set(0)
        self.deSelSkill["dmg"].set("")
        self.deSelSkill["target"].set("")
        self.deSelSkill["desc"].config(state="normal")
        self.deSelSkill["desc"].delete("0.0", tk.END)
        self.deSelSkill["desc"].config(state="disabled")


    def processSaveFile(self):
        with open(self.saveFilePath, 'rb') as fh:
            self.save_bytes = bytearray(fh.read())
        if self.save_bytes is not None:
            # For 1st Tab (Main Character)
            level_int = int(self.getHexStr(self.save_bytes, MC_LVL[0], MC_LVL[1]), 16)
            self.mcValues["level"].set(level_int)
            print("Level: %d" % level_int)
            max_hp_int = int(self.getHexStr(self.save_bytes, MC_MAX_HP[0], MC_MAX_HP[1]), 16)
            self.mcValues["max_hp"].set(max_hp_int)
            print("Max HP: %d" % max_hp_int)
            max_mp_int = int(self.getHexStr(self.save_bytes, MC_MAX_MP[0], MC_MAX_MP[1]), 16)
            self.mcValues["max_mp"].set(max_mp_int)
            print("Max MP: %d" % max_mp_int)
            curr_hp_int = int(self.getHexStr(self.save_bytes, MC_CURR_HP[0], MC_CURR_HP[1]), 16)
            self.mcValues["curr_hp"].set(curr_hp_int)
            print("Current HP: %d" % curr_hp_int)
            curr_mp_int = int(self.getHexStr(self.save_bytes, MC_CURR_MP[0], MC_CURR_MP[1]), 16)
            self.mcValues["curr_mp"].set(curr_mp_int)
            print("Current MP: %d" % curr_mp_int)

            # stat1 = []
            counter = 0
            for idx, val in enumerate(STAT_TXT):
                stat_int = int(self.getHexStr(self.save_bytes, MC_STAT1[0], MC_STAT1[1], counter), 16)
                # stat1.append(stat_int)
                self.mcValues["stats"][idx].set(stat_int)
                print("%s: %d" % (val, stat_int))
                counter += 2
            # print(str(stat1))

            print_str = ""
            # skill = []
            counter = 0
            for x in range(0, MC_SKILL[2]):
                if print_str:
                    print_str += ", "
                skill_id = self.getHexStr(self.save_bytes, MC_SKILL[0], MC_SKILL[1], counter)
                # skill.append(skill_id)
                self.mcValues["skills"][x].set(skill_id)
                print_str += skill_id
                counter += 2
            print("Skills: " + print_str)
            # print(str(skill))

            # For 3rd Tab (Miscellaneous)
            macca = int(self.getHexStr(self.save_bytes, MISC_MACCA[0], MISC_MACCA[1]), 16)
            self.miscValues["macca"].set(macca)
            print("Macca: %d" % macca)
            app_pts = int(self.getHexStr(self.save_bytes, MISC_APP_PTS[0], MISC_APP_PTS[1]), 16)
            self.miscValues["app_pts"].set(app_pts)
            print("App Points: %d" % app_pts)

            # For 2nd Tab (Demons)
            d_start_add = int(DE_START, 16)
            next_demon_offs = int(DE_NEXT_OFFSET, 16)
            self.demonListBox.delete(0, tk.END)
            del self.demonList[:]
            for x in range(0, DE_NUM_MAX):
                d_id_add = d_start_add + int(DE_ID[0], 16)
                demon_id = self.getHexStr(self.save_bytes, d_id_add, DE_ID[1], add_is_dec=True)
                if demon_id in ALL_DEMONS:
                    d_lvl_add = d_start_add + int(DE_LVL[0], 16)
                    d_maxhp_add = d_start_add + int(DE_MAX_HP[0], 16)
                    d_maxmp_add = d_start_add + int(DE_MAX_MP[0], 16)
                    d_currhp_add = d_start_add + int(DE_CURR_HP[0], 16)
                    d_currmp_add = d_start_add + int(DE_CURR_MP[0], 16)
                    d_stats_add = d_start_add + int(DE_STAT1[0], 16)
                    d_skills_add = d_start_add + int(DE_SKILL[0], 16)
                    # Get stats for demon
                    stat1 = []
                    counter = 0
                    for y in range(0, len(STAT_TXT)):
                        stat_int = int(
                            self.getHexStr(self.save_bytes, d_stats_add, DE_STAT1[1], counter, add_is_dec=True), 16
                        )
                        stat1.append(stat_int)
                        counter += 2
                    # Get skills for demon
                    skills = []
                    counter = 0
                    for y in range(0, DE_SKILL[2]):
                        skill_id = self.getHexStr(
                            self.save_bytes, d_skills_add, MC_SKILL[1], counter, add_is_dec=True
                        )
                        skills.append(skill_id)
                        counter += 2

                    d_info = {
                        "start_add": d_start_add,
                        "id": demon_id,
                        "level": int(self.getHexStr(self.save_bytes, d_lvl_add, DE_LVL[1], add_is_dec=True), 16),
                        "max_hp": int(self.getHexStr(self.save_bytes, d_maxhp_add, DE_MAX_HP[1], add_is_dec=True), 16),
                        "max_mp": int(self.getHexStr(self.save_bytes, d_maxmp_add, DE_MAX_HP[1], add_is_dec=True), 16),
                        "curr_hp": int(self.getHexStr(self.save_bytes, d_currhp_add, DE_MAX_HP[1], add_is_dec=True), 16),
                        "curr_mp": int(self.getHexStr(self.save_bytes, d_currmp_add, DE_MAX_HP[1], add_is_dec=True), 16),
                        "stats": stat1,
                        "skills": skills
                    }
                    self.demonList.append(d_info)
                    demon_info = ALL_DEMONS[demon_id]
                    print("Start Address: %x, Demon ID: %s, Name: %s." % (d_start_add, demon_id, demon_info[0]))
                    self.demonListBox.insert(tk.END, "%4s - %s" % (demon_id, demon_info[0]))

                d_start_add += next_demon_offs


    def applyMCChanges(self):
        if self.save_bytes:
            # Level
            tmp_val = format(int(self.mcValues["level"].get()), "x")
            self.writeHexBytes(self.save_bytes, tmp_val, MC_LVL[0], MC_LVL[1])
            # Max HP
            tmp_val = format(int(self.mcValues["max_hp"].get()), "x")
            self.writeHexBytes(self.save_bytes, tmp_val, MC_MAX_HP[0], MC_MAX_HP[1])
            # Max MP
            tmp_val = format(int(self.mcValues["max_mp"].get()), "x")
            self.writeHexBytes(self.save_bytes, tmp_val, MC_MAX_MP[0], MC_MAX_MP[1])
            # Current HP
            tmp_val = format(int(self.mcValues["curr_hp"].get()), "x")
            self.writeHexBytes(self.save_bytes, tmp_val, MC_CURR_HP[0], MC_CURR_HP[1])
            # Current MP
            tmp_val = format(int(self.mcValues["curr_mp"].get()), "x")
            self.writeHexBytes(self.save_bytes, tmp_val, MC_CURR_MP[0], MC_CURR_MP[1])
            # Stats
            counter = 0
            for val in self.mcValues["stats"]:
                tmp_val = format(int(val.get()), "x")
                self.writeHexBytes(self.save_bytes, tmp_val, MC_STAT1[0], MC_STAT1[1], counter)
                counter += 2
            # Skills
            counter = 0
            for val in self.mcValues["skills"]:
                tmp_val = format(int(val.get(), 16), "x")
                self.writeHexBytes(self.save_bytes, tmp_val, MC_SKILL[0], MC_SKILL[1], counter)
                counter += 2


    def applyMiscChanges(self):
        if self.save_bytes:
            # Macca
            tmp_val = format(int(self.miscValues["macca"].get()), "x")
            self.writeHexBytes(self.save_bytes, tmp_val, MISC_MACCA[0], MISC_MACCA[1])
            # App Points
            tmp_val = format(int(self.miscValues["app_pts"].get()), "x")
            self.writeHexBytes(self.save_bytes, tmp_val, MISC_APP_PTS[0], MISC_APP_PTS[1])


    def applyDeChanges(self):
        if self.save_bytes:
            selection = self.demonListBox.curselection()
            if selection:
                demon_values = self.demonList[selection[0]]
                d_start_add = demon_values["start_add"]
                # Level
                tmp_val_int = int(self.deValues["level"].get())
                demon_values["level"] = tmp_val_int
                tmp_val_hex = format(tmp_val_int, "x")
                self.writeHexBytes(
                    self.save_bytes, tmp_val_hex, d_start_add + int(DE_LVL[0], 16),
                    DE_LVL[1], add_is_dec=True
                )
                # Max HP
                tmp_val_int = int(self.deValues["max_hp"].get())
                demon_values["max_hp"] = tmp_val_int
                tmp_val_hex = format(tmp_val_int, "x")
                self.writeHexBytes(
                    self.save_bytes, tmp_val_hex, d_start_add + int(DE_MAX_HP[0], 16),
                    DE_MAX_HP[1], add_is_dec=True
                )
                # Max MP
                tmp_val_int = int(self.deValues["max_mp"].get())
                demon_values["max_mp"] = tmp_val_int
                tmp_val_hex = format(tmp_val_int, "x")
                self.writeHexBytes(
                    self.save_bytes, tmp_val_hex, d_start_add + int(DE_MAX_MP[0], 16),
                    DE_MAX_MP[1], add_is_dec=True
                )
                # Current HP
                tmp_val_int = int(self.deValues["curr_hp"].get())
                demon_values["curr_hp"] = tmp_val_int
                tmp_val_hex = format(tmp_val_int, "x")
                self.writeHexBytes(
                    self.save_bytes, tmp_val_hex, d_start_add + int(DE_CURR_HP[0], 16),
                    DE_CURR_HP[1], add_is_dec=True
                )
                # Current MP
                tmp_val_int = int(self.deValues["curr_mp"].get())
                demon_values["curr_mp"] = tmp_val_int
                tmp_val_hex = format(tmp_val_int, "x")
                self.writeHexBytes(
                    self.save_bytes, tmp_val_hex, d_start_add + int(DE_CURR_MP[0], 16),
                    DE_CURR_MP[1], add_is_dec=True
                )
                # Stats
                d_stat1_add = d_start_add + int(DE_STAT1[0], 16)
                d_stat2_add = d_start_add + int(DE_STAT2[0], 16)
                for idx, val in enumerate(self.deValues["stats"]):
                    tmp_val_int = int(val.get())
                    demon_values["stats"][idx] = tmp_val_int
                    tmp_val_hex = format(tmp_val_int, "x")
                    self.writeHexBytes(self.save_bytes, tmp_val_hex, d_stat1_add, DE_STAT1[1], add_is_dec=True)
                    self.writeHexBytes(self.save_bytes, tmp_val_hex, d_stat2_add, DE_STAT2[1], add_is_dec=True)
                    d_stat1_add += DE_STAT1[1]
                    d_stat2_add += DE_STAT2[1]
                # Skills
                d_skill_add = d_start_add + int(DE_SKILL[0], 16)
                for idx, val in enumerate(self.deValues["skills"]):
                    tmp_val_hex = format(int(val.get(), 16), "x")
                    demon_values["skills"][idx] = tmp_val_hex
                    self.writeHexBytes(self.save_bytes, tmp_val_hex, d_skill_add, DE_SKILL[1], add_is_dec=True)
                    d_skill_add += DE_SKILL[1]





    def writeHexBytes(self, byte_arr, hex_str, start_add, num_bytes, skip_bytes = None, add_is_dec = False):
        hex_str = hex_str.zfill(num_bytes * 2)
        hex_bytes = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
        hex_bytes.reverse()
        if add_is_dec:
            curr_add = start_add
        else:
            curr_add = int(start_add, 16)
        if skip_bytes:
            curr_add += skip_bytes
        for val in hex_bytes:
            # print("old: %d, new: %d" % (byte_arr[curr_add], int(val, 16)))
            byte_arr[curr_add] = int(val, 16)
            curr_add += 1


    def getHexStr(self, byte_arr, start_add, num_bytes, skip_bytes = None, add_is_dec = False):
        hex_str = ""
        if add_is_dec:
            curr_add = start_add
        else:
            curr_add = int(start_add, 16)
        if skip_bytes:
            curr_add += skip_bytes
        while num_bytes > 0:
            hex_str = format(byte_arr[curr_add], '02x') + hex_str
            num_bytes -= 1
            curr_add += 1
        hex_str = hex_str.lstrip("0")
        return hex_str if hex_str else "0"


    def showMessage(self, type = 0, title = None, message = None):
        if not title:
            title = "Test"
        if not message:
            message = "This is a test!"
        if type == 0:
            tk.messagebox.showinfo(title, message)
        elif type == 1:
            tk.messagebox.showwarning(title, message)
        elif type == 2:
            tk.messagebox.showerror(title, message)


    # Menu Functions
    def openFileChooser(self):
        sel_file = filedialog.askopenfilenames(parent=self, initialdir=os.path.dirname(os.path.realpath(sys.argv[0])),
                                               filetypes=(("Save files", "*.sav"), ("All files", "*.*")))
        if sel_file:
            sel_file = sel_file[0]
            # print(sel_file)
            if os.path.isfile(sel_file):
                self.saveFilePathTxt.set(sel_file)
                self.saveFilePath = sel_file
                self.saveFileDir = os.path.dirname(sel_file)
                self.saveFileName = os.path.basename(sel_file)
                # print(self.saveFileName)
                # Reset Info
                self.clearMCSelSkillInfo()
                self.mcSkillListBox.select_clear(0, tk.END)
                self.clearDeStats()
                self.clearDeSelSkillInfo()
                self.deSkillListBox.select_clear(0, tk.END)
                self.processSaveFile()

    def saveChanges(self):
        if self.saveFilePath and os.path.isdir(self.saveFileDir):
            self.applyMCChanges()
            self.applyMiscChanges()
            self.applyDeChanges()
            edited_dir = os.path.join(self.saveFileDir, "Edited")
            if not os.path.isdir(edited_dir):
                os.mkdir(edited_dir)
            with open(os.path.join(edited_dir, self.saveFileName), 'wb') as fh:
                fh.write(self.save_bytes)

    def exitApp(self):
        self.quit()

    def aboutCreator(self):
        tk.messagebox.showinfo("About This", "Made by waynelimt" +
                               "\n\nCredits to:" +
                               "\nSkipperGames (GitHub) - Skill list from his unfinished save editor" +
                               "\nNrubyiglith (GBATemp) - Demon IDs list")


if __name__ == "__main__":
    app = mytestapp(None)
    app.mainloop()
