#######################################
# AD&D 2nd Edition                    #
# Random Character Generator:         #
#  Rogue                             #
#                                     #
# Adds Rogue abilities to randomly   #
#  generated character                #
#######################################

import random

#--------------------------------------
# Return the amount of experience
#  points a character has based on
#  level
#--------------------------------------
def getRogue_XP(my_level):
    rogue_table = [0,1250,2500,5000,10000,20000,40000,70000,110000,\
        160000,220000,440000,660000,880000,1100000,1320000,1540000,\
        1760000,1980000,2200000]

    my_xp = rogue_table[my_level - 1]

    return my_xp

#--------------------------------------
# Assign and return the base thieving 
#   skills for a rogue
#--------------------------------------
def base_TS():
    baseScores = [15,10,5,10,5,15,60,0]

    return baseScores

#--------------------------------------
# Modify base thief abilities by race
#  and return result
#--------------------------------------
def raceAdjust_TS(my_race):
    my_tscores = base_TS()

    if my_race == 'Dwarf':
        my_tscores[1] += 10
        my_tscores[2] += 15
        my_tscores[6] -= 10
        my_tscores[7] -= 5
    elif my_race == 'Elf':
        my_tscores[0] += 5
        my_tscores[1] -= 5
        my_tscores[3] += 5
        my_tscores[4] += 10
        my_tscores[5] += 5
    elif my_race == 'Gnome':
        my_tscores[1] += 5
        my_tscores[2] += 10
        my_tscores[3] += 5
        my_tscores[4] += 5
        my_tscores[5] += 10
        my_tscores[6] -= 15
    elif my_race == 'Half-Elf':
        my_tscores[0] += 10
        my_tscores[4] += 5
    elif my_race == 'Halfling':
        my_tscores[0] += 5
        my_tscores[1] += 5
        my_tscores[2] += 5
        my_tscores[3] += 10
        my_tscores[4] += 15
        my_tscores[5] += 5
        my_tscores[6] -= 15
        my_tscores[7] -= 5

    return my_tscores

#--------------------------------------
# Modify thief abilities by DEX score
#  and return result
#--------------------------------------
def DEX_Adjust_TS(my_tscores, DEX):
    if DEX == 9:
        my_tscores[0] -= 15
        my_tscores[1] -= 10
        my_tscores[2] -= 10
        my_tscores[3] -= 20
        my_tscores[4] -= 10
    elif DEX == 10:
        my_tscores[0] -= 10
        my_tscores[1] -= 5
        my_tscores[2] -= 10
        my_tscores[3] -= 15
        my_tscores[4] -= 5
    elif DEX == 11:
        my_tscores[0] -= 5
        my_tscores[2] -= 5
        my_tscores[3] -= 10
    elif DEX == 12:
        my_tscores[3] -= 5
    elif DEX == 16:
        my_tscores[1] += 5
    elif DEX == 17:
        my_tscores[0] += 5
        my_tscores[1] += 10
        my_tscores[3] += 5
        my_tscores[4] += 5
    elif DEX == 18:
        my_tscores[0] += 10
        my_tscores[1] += 15
        my_tscores[2] += 5
        my_tscores[3] += 10
        my_tscores[4] += 10
    elif DEX == 19:
        my_tscores[0] += 15
        my_tscores[1] += 20
        my_tscores[2] += 10
        my_tscores[3] += 15
        my_tscores[4] += 15

    return my_tscores

#--------------------------------------
# Modify thief abilities by armor type
#  and return result
#--------------------------------------
def armor_Adjust_TS(my_tscores, my_armor):
    if my_armor == 'No Armor':
        my_tscores[0] += 5
        my_tscores[3] += 10
        my_tscores[4] += 5
        my_tscores[6] += 10
    elif my_armor == 'Padded Armor' or my_armor == 'Studded Leather' \
        or my_armor == 'Hide Armor':
        my_tscores[0] -= 30
        my_tscores[1] -= 10
        my_tscores[2] -= 10
        my_tscores[3] -= 20
        my_tscores[4] -= 20
        my_tscores[5] -= 10
        my_tscores[6] -= 30
    elif my_armor == 'Ring Mail' or my_armor == 'Chain Mail':
        my_tscores[0] -= 25
        my_tscores[1] -= 10
        my_tscores[2] -= 10
        my_tscores[3] -= 15
        my_tscores[4] -= 15
        my_tscores[5] -= 5
        my_tscores[6] -= 25

    return my_tscores

#--------------------------------------
# Return the thief skill scores
#  taking into account race, DEX, and
#  armor modifiers, then randomly
#  apply discretionary points based
#  on character level
#--------------------------------------
def Thief_Skills(my_race, my_level, my_armor, DEX):
    my_skills = raceAdjust_TS(my_race)
    my_skills = DEX_Adjust_TS(my_skills, DEX)
    my_skills = armor_Adjust_TS(my_skills, my_armor)

    # Apply 1st level 60 discrectionary points
    #  randomly amongst skills, no more than 30
    #  to any single skill
    points = 60
    while points > 0:
        increase = random.randint(1,30)
        if increase <= points:
            skill = random.randint(0,7)
            while my_skills[skill] > 80:
                skill = random.randint(0,7)
            my_skills[skill] += increase
            points -= increase

    # For every level above 1, gain 30 discretionary
    #  points and randomly assign to skills, no more
    #  than 15 points at a time to a single skill,
    #  with no skill rising above 95/100
    if my_level > 1:
        points = 30 * (my_level - 1)
        while points > 0:
            increase = 1
            if increase <= points:
                skill = random.randint(0,7)
                if my_skills[skill] + increase < 95:
                    my_skills[skill] += increase
                    points -= increase
                elif my_skills[0] + increase < 95:
                    my_skills[0] += increase
                    points -= increase
                elif my_skills[1] + increase < 95:
                    my_skills[1] += increase
                    points -= increase
                elif my_skills[2] + increase < 95:
                    my_skills[2] += increase
                    points -= increase
                elif my_skills[3] + increase < 95:
                    my_skills[3] += increase
                    points -= increase
                elif my_skills[4] + increase < 95:
                    my_skills[4] += increase
                    points -= increase
                elif my_skills[5] + increase < 95:
                    my_skills[5] += increase
                    points -= increase
                elif my_skills[6] + increase < 95:
                    my_skills[6] += increase
                    points -= increase
                elif my_skills[7] + increase < 95:
                    my_skills[7] += increase
                    points -= increase
                else:
                    points = 0

    return my_skills

#--------------------------------------
# Return a thief's backstab multipler
#--------------------------------------
def backStab(my_level):
    if my_level < 5:
        backstab = 2
    elif my_level < 9:
        backstab = 3
    elif my_level < 13:
        backstab = 4
    else:
        backstab = 5

    return backstab

#--------------------------------------
# Return the number of followers
#  a Thief has by type after
#  reaching 10th level
#--------------------------------------
def getT_Followers(my_class, my_level):

    if my_class != 'Thief' or my_level < 10:
        return 'None'
    
    followers_num = random.randint(4,24)
    followers_roll = random.randint(1,100)

    if followers_roll < 4:
        level = random.randint(1,4)
        followers = str(followers_num) + " - Dwarf Fighter/Thief, level " + str(level)
    elif followers_roll < 9:
        level = random.randint(1,6)
        followers = str(followers_num) + " - Dwarf Thief, level " + str(level)
    elif followers_roll < 14:
        level = random.randint(1,6)
        followers = str(followers_num) + " - Elf Thief, level " + str(level)
    elif followers_roll < 16:
        level = random.randint(1,4)
        followers = str(followers_num) + " - Elf Fighter/Thief, level " + str(level)
    elif followers_roll < 19:
        level = random.randint(1,4)
        followers = str(followers_num) + " - Elf Mage/Thief, level " + str(level)
    elif followers_roll < 25:
        level = random.randint(1,6)
        followers = str(followers_num) + " - Gnome Thief, level " + str(level)
    elif followers_roll < 28:
        level = random.randint(1,4)
        followers = str(followers_num) + " - Gnome Fighter/Thief, level " + str(level)
    elif followers_roll < 31:
        level = random.randint(1,4)
        followers = str(followers_num) + " - Gnome Illusionist/Thief, level " + str(level)
    elif followers_roll < 36:
        level = random.randint(1,6)
        followers = str(followers_num) + " - Half-Elf Thief, level " + str(level)
    elif followers_roll < 39:
        level = random.randint(1,4)
        followers = str(followers_num) + " - Half-Elf Fighter/Thief, level " + str(level)
    elif followers_roll < 42:
        level = random.randint(1,3)
        followers = str(followers_num) + " - Half-Elf Fighter/Mage/Thief, level " + str(level)
    elif followers_roll < 47:
        level = random.randint(1,8)
        followers = str(followers_num) + " - Halfling Thief, level " + str(level)
    elif followers_roll < 51:
        level = random.randint(1,6)
        followers = str(followers_num) + " - Halfling Fighter/Thief, level " + str(level)
    elif followers_roll < 99:
        level = random.randint(1,8)
        followers = str(followers_num) + " - Human Thief, level " + str(level)
    elif followers_roll == 99:
        level1 = random.randint(1,8)
        level2 = random.randint(1,4)
        followers = str(followers_num) + " - Human dual-class Thief/Fighter, level " + str(level1) + \
            "/" + str(level2)
    else:
        followers = str(followers_num) + " - DM\'s Option"

    return followers

#--------------------------------------
# Return the casting level and number
#  of wizard spells a Bard has
#  based on level
#--------------------------------------
def Bard_Spells(my_level):
    bard_spell_table = [[0,0,0,0,0,0],[1,0,0,0,0,0],[2,0,0,0,0,0],[2,1,0,0,0,0],[3,1,0,0,0,0],\
        [3,2,0,0,0,0],[3,2,1,0,0,0],[3,3,1,0,0,0],[3,3,2,0,0,0],[3,3,2,1,0,0],[3,3,3,1,0,0],\
        [3,3,3,2,0,0],[3,3,3,2,1,0],[3,3,3,3,1,0],[3,3,3,3,2,0],[4,3,3,3,2,1],[4,4,3,3,3,1,],\
        [4,4,4,3,3,2],[4,4,4,4,3,2],[4,4,4,4,4,3]]
    
    return bard_spell_table[my_level - 1]

#--------------------------------------
# Return the bard thief skill scores
#  taking into account race, DEX, and
#  armor modifiers, then randomly
#  apply discretionary points based
#  on character level
#--------------------------------------
def bard_skills(my_race, my_level, my_armor, DEX):
    my_skills = raceAdjust_TS(my_race)
    my_skills = DEX_Adjust_TS(my_skills, DEX)
    my_skills = armor_Adjust_TS(my_skills, my_armor)

    # Bards do not have access to all thief skills
    my_skills.pop(1)
    my_skills.pop(1)
    my_skills.pop(1)
    my_skills.pop(1)

    # Adjust from the base score difference between Bard and Thief
    my_skills[0] -= 5
    my_skills[1] += 5
    my_skills[2] -= 10
    my_skills[3] += 5

    # Apply 1st level 20 discrectionary points
    #  randomly amongst skills
    points = 20
    while points > 0:
        increase = random.randint(1,10)
        if increase <= points:
            skill = random.randint(0,3)
            while my_skills[skill] > 80:
                skill = random.randint(0,3)
            my_skills[skill] += increase
            points -= increase

    # For every level above 1, gain 15 discretionary
    #  points and randomly assign to skills,
    #  with no skill rising above 95/100
    if my_level > 1:
        points = 15 * (my_level - 1)
        while points > 0:
            increase = 1
            if increase <= points:
                skill = random.randint(0,3)
                if my_skills[skill] + increase < 95:
                    my_skills[skill] += increase
                    points -= increase
                elif my_skills[0] + increase < 95:
                    my_skills[0] += increase
                    points -= increase
                elif my_skills[1] + increase < 95:
                    my_skills[1] += increase
                    points -= increase
                elif my_skills[2] + increase < 95:
                    my_skills[2] += increase
                    points -= increase
                elif my_skills[3] + increase < 95:
                    my_skills[3] += increase
                    points -= increase
                else:
                    points = 0

    return my_skills