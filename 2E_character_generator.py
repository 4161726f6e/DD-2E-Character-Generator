#######################################
# AD&D 2nd Edition                    #
# Random Character Generator          #
#                                     #
# Creates random AD&D 2e characters   #
#  according to allowed class per     #
#  race. Multiclass is available.     #
#  Dual-class is not implemented.     #
#######################################

import random, sys, getopt, os
from wizard import *
from warrior import *
from priest import *
from rogue import *
from nonWeaponProfs import *

charRace = ['Human', 'Half-Elf', 'Elf', 'Dwarf', 'Half-Orc', 'Halfling', 'Gnome']
charClass = ['Fighter','Ranger','Wizard','Cleric','Druid','Thief','Bard','Paladin','Fighter/Thief',\
    'Fighter/Cleric','Fighter/Mage','Mage/Thief','Fighter/Illusionist','Cleric/Illusionist','Cleric/Thief',\
    'Illusionist/Thief','Fighter/Druid','Cleric/Ranger','Cleric/Mage','Druid/Mage','Fighter/Mage/Cleric',\
    'Fighter/Mage/Druid','Fighter/Mage/Thief','Priest','Mage','Illusionist']
scores = [0,0,0,0,0,0]

#--------------------------------------
# Roll the digital dice and return
#   ability scores
#--------------------------------------
def roll(scores):
    scores[0] = random.randint(3,18)
    scores[1] = random.randint(3,18)
    scores[2] = random.randint(3,18)
    scores[3] = random.randint(3,18)
    scores[4] = random.randint(3,18)
    scores[5] = random.randint(3,18)

    average = sum(scores) / len(scores)

    if average < 8:
        roll(scores)

    #print(scores)
    return scores

#--------------------------------------
# If character is a Fighter, Paladin, 
#  or Ranger and not a Halfling, 
#  and has STR of 18, roll for 
#  exceptional strength
#--------------------------------------
def rollSTR(my_strength, my_race, my_class):
    xSTR = 0
    if my_strength > 18:
        my_strength = 18

    if my_strength == 18:
        if my_race != 'Halfling':
            if my_class == 'Fighter' or my_class == 'Paladin' \
                or my_class == 'Ranger':
                xSTR = random.randint(1,100)
    
    return xSTR, my_strength

#--------------------------------------
# Eliminate racial options based on
#   min/max requirements
#
# Randomly select race from available
#  options
#--------------------------------------
def racial(scores):
    if scores[0] < 8:
        if 'Dwarf' in charRace:
            charRace.remove('Dwarf')
    if scores[2] < 11:
        if 'Dwarf' in charRace:
            charRace.remove('Dwarf')

    if scores[1] < 6:
        if 'Elf' in charRace:
            charRace.remove('Elf')
        if 'Half-Elf' in charRace:
            charRace.remove('Half-Elf')
    if scores[2] < 7:
        if 'Elf' in charRace:
            charRace.remove('Elf')
    if scores[3] < 8:
        if 'Elf' in charRace:
            charRace.remove('Elf')
    if scores[5] < 8:
        if 'Elf' in charRace:
            charRace.remove('Elf')

    if scores[0] < 6:
        if 'Gnome' in charRace:
            charRace.remove('Gnome')
        if 'Half-Orc' in charRace:
            charRace.remove('Half-Orc')
    if scores[2] < 8:
        if 'Gnome' in charRace:
            charRace.remove('Gnome')
    if scores[3] < 6:
        if 'Gnome' in charRace:
            charRace.remove('Gnome')
        if 'Halfling' in charRace:
            charRace.remove('Halfling')

    if scores[2] < 6:
        if 'Half-Elf' in charRace:
            charRace.remove('Half-Elf')
    if scores[3] < 4:
        if 'Half-Elf' in charRace:
            charRace.remove('Half-Elf')

    if scores[2] < 10:
        if 'Halfling' in charRace:
            charRace.remove('Halfling')
    if scores[0] < 7:
        if 'Halfling' in charRace:
            charRace.remove('Halfling')
    if scores[1] < 7:
        if 'Halfling' in charRace:
            charRace.remove('Halfling')

    if scores[2] < 13:
        if 'Half-Orc' in charRace:
            charRace.remove('Half-Orc')

    if scores[1] > 17:
        if 'Dwarf' in charRace:
            charRace.remove('Dwarf')
    if scores[5] > 17:
        if 'Dwarf' in charRace:
            charRace.remove('Dwarf')
    if scores[4] > 17:
        if 'Halfling' in charRace:
            charRace.remove('Halfling')
    if scores[3] > 17:
        if 'Half-Orc' in charRace:
            charRace.remove('Half-Orc')
    if scores[4] > 14:
        if 'Half-Orc' in charRace:
            charRace.remove('Half-Orc')
    if scores[1] > 17:
        if 'Half-Orc' in charRace:
            charRace.remove('Half-Orc')
    if scores[5] > 12:
        if 'Half-Orc' in charRace:
            charRace.remove('Half-Orc')

    #select and return character race
    my_race = random.choice(charRace)

    return my_race

#--------------------------------------
# Apply racial ability adjustments
#  to ability scores and return
#--------------------------------------
def raceAdjust(scores, my_race):
    if my_race == 'Dwarf':
        scores[2] += 1
        scores[5] -= 1
    elif my_race == 'Elf':
        scores[1] += 1
        scores[2] -= 1
    elif my_race == 'Gnome':
        scores[3] += 1
        scores[4] -= 1
    elif my_race == 'Halfling':
        scores[1] += 1
        scores[0] -= 1
    elif my_race == 'Half-Orc':
        scores[0] += 1
        scores[2] += 1
        scores[5] -= 2

    return scores

#--------------------------------------
# Select class after racial 
#  restrictions and minimums are
#  applied
#
# Human classes are selected randomly
#  while all others are selected based
#  upon highest ability score with
#  respect to prime score of a class
#--------------------------------------
def classSelector(scores, my_race):
    if my_race == 'Dwarf':
        toRemove = [1,2,4,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25]
        for i in sorted(toRemove, reverse = True):
            del charClass[i]
    elif my_race == 'Elf':
        toRemove = [4,6,7,9,12,13,14,15,16,17,18,19,20,21,22]
        for i in sorted(toRemove, reverse = True):
            del charClass[i]
    elif my_race == 'Gnome':
        toRemove = [1,2,4,6,7,10,11,16,17,18,19,20,21,22,24]
        for i in sorted(toRemove, reverse = True):
            del charClass[i]
    elif my_race == 'Halfling':
        toRemove = [1,2,4,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25]
        for i in sorted(toRemove, reverse = True):
            del charClass[i]
    elif my_race == 'Half-Orc':
        toRemove = [1,4,6,7,11,12,13,14,15,16,17,18,19,20,21,22]
        for i in sorted(toRemove, reverse = True):
            del charClass[i]
    elif my_race == 'Half-Elf':
        toRemove = [7,12,13,14,15]
        for i in sorted(toRemove, reverse = True):
            del charClass[i]
    else:   # You are Human
        toRemove = [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
        for i in sorted(toRemove, reverse = True):
            del charClass[i]

    if scores[0] < 9:
        if 'Fighter' in charClass:
            charClass.remove('Fighter')
        if 'Fighter/Thief' in charClass:
            charClass.remove('Fighter/Thief')
        if 'Fighter/Mage' in charClass:
            charClass.remove('Fighter/Mage')
        if 'Fighter/Cleric' in charClass:
            charClass.remove('Fighter/Cleric')
        if 'Fighter/Illusionist' in charClass:
            charClass.remove('Fighter/Illusionist')
        if 'Fighter/Druid' in charClass:
            charClass.remove('Fighter/Druid')
        if 'Fighter/Mage/Cleric' in charClass:
            charClass.remove('Fighter/Mage/Cleric')
        if 'Fighter/Mage/Druid' in charClass:
            charClass.remove('Fighter/Mage/Druid')
        if 'Fighter/Mage/Thief' in charClass:
            charClass.remove('Fighter/Mage/Thief')
    if scores[3] < 9:
        if 'Wizard' in charClass:
            charClass.remove('Wizard')
        if 'Mage' in charClass:
            charClass.remove('Mage')
        if 'Mage/Thief' in charClass:
            charClass.remove('Mage/Thief')
        if 'Illusionist' in charClass:
            charClass.remove('Illusionist')
    if scores[1] < 9:
        if 'Thief' in charClass:
            charClass.remove('Thief')
    if scores[4] < 9:
        if 'Cleric' in charClass:
            charClass.remove('Cleric')
        if 'Priest' in charClass:
            charClass.remove('Priest')
        if 'Cleric/Ranger' in charClass:
            charClass.remove('Cleric/Ranger')
        if 'Cleric/Mage' in charClass:
            charClass.remove('Cleric/Mage')
        if 'Druid/Mage' in charClass:
            charClass.remove('Druid/Mage')
        if 'Cleric/Thief' in charClass:
            charClass.remove('Cleric/Thief')
        if 'Cleric/Illusionist' in charClass:
            charClass.remove('Cleric/Illusionist')
    if scores[1] < 12 or scores[3] < 13 or scores[5] < 15:
        if 'Bard' in charClass:
            charClass.remove('Bard')
    if scores[4] < 12 or scores[5] < 15:
        if 'Druid' in charClass:
            charClass.remove('Druid')
    if scores[0] < 13 or scores[1] < 13 or scores[2] < 14 or scores[4] < 14:
        if 'Ranger' in charClass:
            charClass.remove('Ranger')
    if scores[0] < 12 or scores[2] < 9 or scores[4] < 13 or scores[5] < 17:
        if 'Paladin' in charClass:
            charClass.remove('Paladin')

    # Select class based upon value of highest score if not human
    #   Otherwise, random choice
    score_max = max(range(len(scores)), key=scores.__getitem__)

    if len(charClass) == 0:
        my_class = 'Villager' # No available classes         
    elif my_race != 'Human':
        if score_max == 0:
            if 'Fighter' in charClass:
                my_class = 'Fighter'
            else: my_class = random.choice(charClass)
        elif score_max == 1:
            if 'Thief' in charClass:
                my_class = 'Thief'
            else: my_class = random.choice(charClass)
        elif score_max == 3:
            if 'Mage' in charClass:
                my_class = 'Mage'
            else: my_class = random.choice(charClass)
        elif score_max == 4:
            if 'Cleric' in charClass:
                coin_toss = random.randint(1,2)
                if coin_toss == 2:  # Randomly create a priest of a certain mythos
                    my_class = 'Priest'
                else: my_class = 'Cleric'
            else: my_class = random.choice(charClass)
        else: my_class = random.choice(charClass)
    else: my_class = random.choice(charClass)

    # Gnomes can only be Illusionists if they are Wizards
    if my_race == 'Gnome':
        if my_class == 'Wizard' or my_class == 'Mage':
            my_class == 'Illusionist'

    return my_class

#--------------------------------------
# Iterate through random character
#  creation for a specified class
#--------------------------------------
def certainClass(my_class, my_race, scores, cRequest, rand_bool):
    if rand_bool == 0:  # Certain race/class combo requested
        if my_race == 'Dwarf':
            toRemove = [1,2,4,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25]
            for i in sorted(toRemove, reverse = True):
                del charClass[i]
        elif my_race == 'Elf':
            toRemove = [4,6,7,9,12,13,14,15,16,17,18,19,20,21,22]
            for i in sorted(toRemove, reverse = True):
                del charClass[i]
        elif my_race == 'Gnome':
            toRemove = [1,2,4,6,7,10,11,16,17,18,19,20,21,22,24]
            for i in sorted(toRemove, reverse = True):
                del charClass[i]
        elif my_race == 'Halfling':
            toRemove = [1,2,4,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25]
            for i in sorted(toRemove, reverse = True):
                del charClass[i]
        elif my_race == 'Half-Orc':
            toRemove = [1,4,6,7,11,12,13,14,15,16,17,18,19,20,21,22]
            for i in sorted(toRemove, reverse = True):
                del charClass[i]
        elif my_race == 'Half-Elf':
            toRemove = [7,12,13,14,15]
            for i in sorted(toRemove, reverse = True):
                del charClass[i]
        else:
            toRemove = [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
            for i in sorted(toRemove, reverse = True):
                del charClass[i]
        if cRequest not in charClass:
            return 'Villager', my_race, scores

    while my_class != cRequest:
        resetRC()
        scores = roll(scores)
        my_race = racial(scores)
        scores = raceAdjust(scores, my_race)
        my_class = classSelector(scores, my_race)
   
    return my_class, my_race, scores

#--------------------------------------
# Iterate through random character
#  creation for a specified race
#--------------------------------------
def certainRace(my_race, scores, rRequest):
    while my_race != rRequest:
        resetRC()
        scores = roll(scores)
        my_race = racial(scores)
    
    return my_race, scores

#--------------------------------------
# Reset race and class lists
#--------------------------------------
def resetRC():
    global charRace, charClass
    charRace = ['Human', 'Half-Elf', 'Elf', 'Dwarf', 'Half-Orc', 'Halfling', 'Gnome']
    charClass = ['Fighter','Ranger','Wizard','Cleric','Druid','Thief','Bard','Paladin','Fighter/Thief',\
    'Fighter/Cleric','Fighter/Mage','Mage/Thief','Fighter/Illusionist','Cleric/Illusionist','Cleric/Thief',\
    'Illusionist/Thief','Fighter/Druid','Cleric/Ranger','Cleric/Mage','Druid/Mage','Fighter/Mage/Cleric',\
    'Fighter/Mage/Druid','Fighter/Mage/Thief','Priest','Mage','Illusionist']

#--------------------------------------
# Determine character height
#--------------------------------------
def getHeight(my_race, my_gender):
    if my_race == 'Dwarf':
        if my_gender == 'Male':
            base = 43
        else: base = 41
        modifier = random.randint(1,10)
    elif my_race == 'Elf':
        if my_gender == 'Male':
            base = 55
        else: base = 50
        modifier = random.randint(1,10)
    elif my_race == 'Gnome':
        if my_gender == 'Male':
            base = 38
        else: base = 36
        modifier = random.randint(1,6)
    elif my_race == 'Half-Elf':
        if my_gender == 'Male':
            base = 60
        else: base = 58
        modifier = random.randint(2,12)
    elif my_race == 'Halfling':
        if my_gender == 'Male':
            base = 32
        else: base = 30
        modifier = random.randint(2,16)
    elif my_race == 'Half-Orc':
        if my_gender == 'Male':
            base = 65
        else: base = 64
        modifier = random.randint(2,16)
    else:   # my_race == 'Human':
        if my_gender == 'Male':
            base = 60
        else: base = 59
        modifier = random.randint(2,20)
    height = base + modifier

    return height

#--------------------------------------
# Determine character weight
#--------------------------------------
def getWeight(my_race, my_gender):
    if my_race == 'Dwarf':
        if my_gender == 'Male':
            base = 130
        else: base = 105
        modifier = random.randint(4,40)
    elif my_race == 'Elf':
        if my_gender == 'Male':
            base = 90
        else: base = 70
        modifier = random.randint(3,30)
    elif my_race == 'Gnome':
        if my_gender == 'Male':
            base = 72
        else: base = 68
        modifier = random.randint(5,20)
    elif my_race == 'Half-Elf':
        if my_gender == 'Male':
            base = 110
        else: base = 85
        modifier = random.randint(3,36)
    elif my_race == 'Halfling':
        if my_gender == 'Male':
            base = 52
        else: base = 48
        modifier = random.randint(5,20)
    elif my_race == 'Half-Orc':
        if my_gender == 'Male':
            base = 160
        else: base = 120
        modifier = random.randint(6,72)
    else:   # my_race == 'Human':
        if my_gender == 'Male':
            base = 140
        else: base = 100
        modifier = random.randint(6,60)
    weight = base + modifier

    return weight

#--------------------------------------
# Determine character age
#--------------------------------------
def getAge(my_race, my_level):
    if my_race == 'Dwarf':
        base = 40 + my_level
        modifier = random.randint(5,30)
    elif my_race == 'Elf':
        base = 100 + my_level
        modifier = random.randint(5,30)
    elif my_race == 'Gnome':
        base = 60 + my_level
        modifier = random.randint(3,36)
    elif my_race == 'Half-Elf':
        base = 15 + my_level
        modifier = random.randint(1,6)
    elif my_race == 'Halfling':
        base = 20 + my_level
        modifier = random.randint(3,12)
    elif my_race == 'Half-Orc':
        base = 30 + my_level
        modifier = random.randint(2,12)
    else:   # my_race == 'Human':
        base = 15 + my_level
        modifier = random.randint(1,4)
    age = base + modifier

    return age

#--------------------------------------
# Randomly assign gender
#  assuming binary world
#--------------------------------------
def gender():
    gender = ['Male', 'Female']
    my_gender = random.choice(gender)

    return my_gender

#--------------------------------------
# Randomly assign name from a file
#  based on gender, assuming binary
#--------------------------------------
def genName(my_gender):
    if my_gender == 'Male':
        names = open('male_names.txt').readlines()
    else:
        names = open('female_names.txt').readlines()
    my_name = str.rstrip(random.choice(names))

    return my_name

#--------------------------------------
# Choose an alignment
# 
# Random selection within race/class
#  restrictions
#--------------------------------------
def genAL(my_class, my_race):
    if my_race == 'Half-Orc':
        AL = ['CG', 'CN', 'CE']
    elif my_class == 'Paladin':
        AL = ['LG']
    elif my_class == 'Ranger':
        AL = ['LG', 'LN', 'NG', 'TN', 'CG']
    elif my_class == 'Bard':
        AL = ['LN', 'TN', 'CN']
    else:
        AL = ['LG', 'LN', 'LE', 'NG', 'TN', 'NE', 'CG', 'CN', 'CE']
    
    my_AL = random.choice(AL)
    
    return my_AL

#--------------------------------------
# Roll Hit Points
#--------------------------------------
def rollHP(my_class, my_level):
    my_hp = 0
    if my_class == 'Fighter' or my_class == 'Paladin' or my_class == 'Ranger'\
        or my_class == 'Fighter/Thief' or my_class == 'Fighter/Cleric' or my_class == 'Fighter/Mage'\
        or my_class == 'Fighter/Illusionist' or my_class == 'Cleric/Ranger' or my_class == 'Druid/Ranger'\
        or my_class == 'Fighter/Mage/Cleric' or my_class == 'Fighter/Mage/Druid' or my_class == 'Fighter/Mage/Thief':
        for x in range(my_level):
            die = random.randint(1,10)
            my_hp = my_hp + die
    elif my_class == 'Cleric' or my_class == 'Druid' or my_class == 'Cleric/Illusionist' or my_class == 'Cleric/Mage'\
        or my_class == 'Cleric/Druid' or my_class == 'Cleric/Thief':
        for x in range(my_level):
            die = random.randint(1,8)
            my_hp = my_hp + die
    elif my_class == 'Thief' or my_class == 'Bard' or my_class == 'Mage/Thief' or my_class == 'Illusionist/Thief':
        for x in range(my_level):
            die = random.randint(1,6)
            my_hp = my_hp + die
    else:  # You must be a Wizard or Mage
        for x in range(my_level):
            die = random.randint(1,4)
            my_hp = my_hp + die

    return my_hp

#--------------------------------------
# Calculate Character THAC0
#--------------------------------------
def getTHAC0(my_class, my_level):
    thac0_table = [['Priest',20,20,20,18,18,18,16,16,16,14,14,14,12,12,12,\
        10,10,10,8,8],['Rogue',20,20,19,19,18,18,17,17,16,16,15,15,14,14,13,\
            13,12,12,11,11],['Warrior',20,19,18,17,16,15,14,13,12,11,10,9,8,7,\
                6,5,4,3,2,1],['Wizard',20,20,20,19,19,19,18,18,18,17,17,17,16,16,\
                    16,15,15,15,14,14,14]]
    
    if my_class == 'Fighter' or my_class == 'Paladin' or my_class == 'Ranger'\
        or my_class == 'Fighter/Thief' or my_class == 'Fighter/Cleric' or my_class == 'Fighter/Mage'\
        or my_class == 'Fighter/Illusionist' or my_class == 'Cleric/Ranger' or my_class == 'Druid/Ranger'\
        or my_class == 'Fighter/Mage/Cleric' or my_class == 'Fighter/Mage/Druid' or my_class == 'Fighter/Mage/Thief':
        thac0 = thac0_table[2][my_level]
    elif my_class == 'Cleric' or my_class == 'Druid' or my_class == 'Cleric/Illusionist' or my_class == 'Cleric/Mage'\
        or my_class == 'Cleric/Druid' or my_class == 'Cleric/Thief':
        thac0 = thac0_table[0][my_level]
    elif my_class == 'Thief' or my_class == 'Bard' or my_class == 'Mage/Thief' or my_class == 'Illusionist/Thief':
        thac0 = thac0_table[1][my_level]
    else:
        thac0 = thac0_table[3][my_level]

    return thac0

#--------------------------------------
# Calculate Saving Throws
#--------------------------------------
def getST(my_class, my_level, my_race, con):
    st = [0,0,0,0,0]

    st_ppdm_table = [['Priest',10,10,10,9,9,9,7,7,7,6,6,6,5,5,5,4,4,4,2,2],\
        ['Rogue',13,13,13,13,12,12,12,12,11,11,11,11,10,10,10,10,9,9,9,9],\
            ['Warrior',14,14,13,13,11,11,10,10,8,8,7,7,5,5,4,4,3,3,3,3],\
                ['Wizard',14,14,14,14,14,13,13,13,13,13,11,11,11,11,11,10,10,10,10,10]]
    st_rsw_table = [['Priest',14,14,14,13,13,13,11,11,11,10,10,10,9,9,9,8,8,8,6,6],\
        ['Rogue',14,14,14,14,12,12,12,12,10,10,10,10,8,8,8,8,6,6,6,6],\
            ['Warrior',16,16,15,15,13,13,12,12,10,10,9,9,7,7,6,6,5,5,5,5],\
                ['Wizard',11,11,11,11,11,9,9,9,9,9,7,7,7,7,7,5,5,5,5,5,]]
    st_pp_table = [['Priest',13,13,13,12,12,12,10,10,10,9,9,9,8,8,8,7,7,7,5,5],\
        ['Rogue',12,12,12,12,11,11,11,11,10,10,10,10,9,9,9,9,8,8,8,8],\
            ['Warrior',15,15,14,14,12,12,11,11,9,9,8,8,6,6,5,5,4,4,4,4],\
                ['Wizard',13,13,13,13,13,11,11,11,11,11,9,9,9,9,9,7,7,7,7,7]]
    st_bw_table = [['Priest',16,16,16,15,15,15,13,13,13,12,12,12,11,11,11,10,10,10,8,8],\
        ['Rogue',16,16,16,16,15,15,15,15,14,14,14,14,13,13,13,13,12,12,12,12],\
            ['Warrior',17,17,16,16,13,13,12,12,9,9,8,8,5,5,4,4,4,4,4,4],\
                ['Wizard',15,15,15,15,15,13,13,13,13,13,11,11,11,11,11,9,9,9,9,9]]
    st_spell_table = [['Priest',15,15,15,14,14,14,12,12,12,11,11,11,10,10,10,9,9,9,7,7],\
        ['Rogue',15,15,15,15,13,13,13,13,11,11,11,11,9,9,9,9,7,7,7,7],\
            ['Warrior',17,17,16,16,14,14,13,13,11,11,10,10,8,8,7,7,6,6,6,6],\
                ['Wizard',12,12,12,12,12,10,10,10,10,10,8,8,8,8,8,6,6,6,6,6]]

    if my_class == 'Fighter' or my_class == 'Paladin' or my_class == 'Ranger'\
        or my_class == 'Fighter/Thief' or my_class == 'Fighter/Cleric' or my_class == 'Fighter/Mage'\
        or my_class == 'Fighter/Illusionist' or my_class == 'Cleric/Ranger' or my_class == 'Druid/Ranger'\
        or my_class == 'Fighter/Mage/Cleric' or my_class == 'Fighter/Mage/Druid' or my_class == 'Fighter/Mage/Thief':
        st[0] = st_ppdm_table[2][my_level]
        st[1] = st_rsw_table[2][my_level]
        st[2] = st_pp_table[2][my_level]
        st[3] = st_bw_table[2][my_level]
        st[4] = st_spell_table[2][my_level]
    elif my_class == 'Cleric' or my_class == 'Druid' or my_class == 'Cleric/Illusionist' or my_class == 'Cleric/Mage'\
        or my_class == 'Cleric/Druid' or my_class == 'Cleric/Thief':
        st[0] = st_ppdm_table[0][my_level]
        st[1] = st_rsw_table[0][my_level]
        st[2] = st_pp_table[0][my_level]
        st[3] = st_bw_table[0][my_level]
        st[4] = st_spell_table[0][my_level]
    elif my_class == 'Thief' or my_class == 'Bard' or my_class == 'Mage/Thief' or my_class == 'Illusionist/Thief':
        st[0] = st_ppdm_table[1][my_level]
        st[1] = st_rsw_table[1][my_level]
        st[2] = st_pp_table[1][my_level]
        st[3] = st_bw_table[1][my_level]
        st[4] = st_spell_table[1][my_level]
    else:
        st[0] = st_ppdm_table[3][my_level]
        st[1] = st_rsw_table[3][my_level]
        st[2] = st_pp_table[3][my_level]
        st[3] = st_bw_table[3][my_level]
        st[4] = st_spell_table[3][my_level]

    # Paladin saving throw bonus
    if my_class == 'Paladin':
        st[0] = st[0] - 2
        st[1] = st[1] - 2
        st[2] = st[2] - 2
        st[3] = st[3] - 2
        st[4] = st[4] - 2
    
    # Racial saving throw adjustments
    if my_race != 'Human':
        if my_race == 'Dwarf' or my_race == 'Gnome' or my_race == 'Halfling':
            if con < 7:
                st[1] = st[1] - 1
                st[4] = st[4] - 1
            elif con < 11:
                st[1] = st[1] - 2
                st[4] = st[4] - 2
            elif con < 14:
                st[1] = st[1] - 3
                st[4] = st[4] - 3
            elif con < 18:
                st[1] = st[1] - 4
                st[4] = st[4] - 4
            else:
                st[1] = st[1] - 5
                st[4] = st[4] - 5

    return st

#--------------------------------------
# Find STR Attributes
#--------------------------------------
def findSTR(_str, xSTR):
    my_str = _str
    str_att = [0,0,0,0,0,0]
    str_table = [['Hit Prob',-5,-3,-3,-2,-2,-1,-1,0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,3],\
        ['Dmg Adj',-4,-2,-1,-1,-1,0,0,0,0,0,0,0,0,0,0,1,1,2,3,3,4,5,6],\
            ['Weight Allow',1,1,5,10,10,20,20,35,35,40,40,45,45,55,55,70,85,110,135,160,185,235,335],\
                ['Max Press',3,5,10,25,25,55,55,90,90,115,115,140,140,170,170,195,220,255,280,305,330,380,480],\
                    ['Open Doors',1,1,2,3,3,4,4,5,5,6,6,7,7,8,8,9,10,11,12,13,14,15,16],\
                        ['BB LG',0,0,0,0,0,0,0,1,1,2,2,4,4,7,7,10,13,16,20,25,30,35,40]]

    # Using STR score as list index; adjust if xSTR > 0
    if xSTR > 0:
        if xSTR > 99:
            my_str = 23
        elif xSTR > 90:
            my_str = 22
        elif xSTR > 75:
            my_str = 21
        elif xSTR > 50:
            my_str = 20
        else:
            my_str = 19

    str_att[0] = str_table[0][my_str]
    str_att[1] = str_table[1][my_str]
    str_att[2] = str_table[2][my_str]
    str_att[3] = str_table[3][my_str]
    str_att[4] = str_table[4][my_str]
    str_att[5] = str_table[5][my_str]

    return str_att

#--------------------------------------
# Find DEX Attributes
#--------------------------------------
def findDEX(dex):
    dex_att = [0,0,0]
    dex_table = [['Rct Adj',-6,-4,-3,-2,-1,0,0,0,0,0,0,0,0,0,0,1,2,2,3],\
        ['Missle Adj',-6,-4,-3,-2,-1,0,0,0,0,0,0,0,0,0,0,1,2,2,3],\
            ['Def Adj',5,5,4,3,2,1,0,0,0,0,0,0,0,0,-1,-2,-3,-4,-4]]

    dex_att[0] = dex_table[0][dex]
    dex_att[1] = dex_table[1][dex]
    dex_att[2] = dex_table[2][dex]

    return dex_att

#--------------------------------------
# Find CON Attributes
#
# Skipping Poison Save and Regen
#  as these won't normally affect
#--------------------------------------
def findCON(con, my_class):
    con_att = [0,0,0]
    con_table = [['HP Adj',-3,-2,-2,-1,-1,-1,0,0,0,0,0,0,0,0,1,2,2,2,2],\
        ['Sys Shk',25,30,35,40,45,50,55,60,65,70,75,80,85,88,90,95,97,99,99],\
            ['Res Srv',30,35,40,45,50,55,60,65,70,75,80,85,90,92,94,96,98,100,100]]

    con_att[0] = con_table[0][con]
    # Warriors recieve additional HP bonus with high CON
    if my_class == 'Fighter' or my_class == 'Paladin' or my_class == 'Ranger':
        if con == 17:
            con_att[0] += 1
        elif con == 18:
            con_att[0] += 2
        elif con == 19:
            con_att[0] += 3
    con_att[1] = con_table[1][con]
    con_att[2] = con_table[2][con]

    return con_att

#--------------------------------------
# Find INT Attributes
#--------------------------------------
def findINT(my_int):
    int_att = [0,0,0,0,0,0]
    int_table = [['Num Lang',0,1,1,1,1,1,1,1,2,2,2,3,3,4,4,5,6,7,8,9],\
        ['Spell Lvl',0,0,0,0,0,0,0,0,4,5,5,6,6,7,7,8,8,9,9],\
            ['Chance Lrn Spl',0,0,0,0,0,0,0,0,35,40,45,50,55,60,65,70,75,85,95],\
                ['Max Spl/Lvl',0,0,0,0,0,0,0,0,6,7,7,7,9,9,11,11,14,18,'All'],\
                    ['Ill Imnty',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'1st-level']]

    int_att[0] = int_table[0][my_int]
    int_att[1] = int_table[1][my_int]
    int_att[2] = int_table[2][my_int]
    int_att[3] = int_table[3][my_int]
    int_att[4] = int_table[4][my_int]

    return int_att

#--------------------------------------
# Find WIS Attributes
#--------------------------------------
def findWIS(my_wis):
    wis_att = [0,0,0,0,0,0]
    wis_table = [['Mag Def Adj',-6,-4,-3,-2,-1,-1,-1,0,0,0,0,0,0,0,1,2,3,4],\
        ['Bonus Spl',0,0,0,0,0,0,0,0,0,0,0,0,'1-1st','2-1st','1-2nd 2-1st','2-2nd 2-1st',\
            '1-3rd 2-2nd 2-1st','1-4th 1-3rd 2-2nd 2-1st'],\
                ['Chance Spl Fail',80,60,50,45,40,35,30,25,20,15,10,5,0,0,0,0,0,0]]

    wis_att[0] = wis_table[0][my_wis]
    wis_att[1] = wis_table[1][my_wis]
    wis_att[2] = wis_table[2][my_wis]

    return wis_att

#--------------------------------------
# Find CHA Attributes
#--------------------------------------
def findCHA(my_cha):
    cha_att = [0,0,0,0,0,0]
    cha_table = [['Max # Hench',0,1,1,1,2,2,3,3,4,4,4,5,5,6,7,8,10,15],\
        ['Loyal Base',-8,-7,-6,-5,-4,-3,-2,-1,0,0,0,0,0,1,3,4,6,8],\
            ['Reac Adj',-7,-6,-5,-4,-3,-2,-1,0,0,0,0,0,1,2,3,5,6,7]]

    cha_att[0] = cha_table[0][my_cha]
    cha_att[1] = cha_table[1][my_cha]
    cha_att[2] = cha_table[2][my_cha]

    return cha_att

#--------------------------------------
# Find and return the number of
#  nonweapon proficiency slots the
#  character has
#--------------------------------------
def nonwProf(my_class, my_level):
    if my_class == 'Thief' or my_class == 'Bard':
        x = int(my_level / 4)
        nwprofs = x * 3 + 3
    elif my_class == 'Fighter' or my_class == 'Paladin' or my_class == 'Ranger' or my_class == 'Fighter/Thief':
        x = int(my_level / 3)
        nwprofs = x * 3 + 3
    else:
        x = int(my_level / 3)
        nwprofs = x * 4 + 4
    
    return nwprofs

#--------------------------------------
# Find and return the number of
#  weapon proficiency slots the
#  character has
#--------------------------------------
def wProf(my_class, my_level):
    if my_class == 'Thief' or my_class == 'Bard' or my_class == 'Cleric' or my_class == 'Druid'\
        or my_class == 'Mage/Thief' or my_class == 'Cleric/Illusionist' or my_class == 'Cleric/Thief'\
        or my_class == 'Illusionist/Thief' or my_class == 'Cleric/Mage' or my_class == 'Druid/Mage'\
        or my_class == 'Priest':
        x = int(my_level / 4)
        wprofs = x * 2 + 2
    elif my_class == 'Fighter' or my_class == 'Paladin' or my_class == 'Ranger' or my_class == 'Fighter/Thief'\
        or my_class == 'Fighter/Cleric' or my_class == 'Fighter/Mage' or my_class == 'Fighter/Illusionist'\
        or my_class == 'Fighter/Druid' or my_class == 'Cleric/Ranger' or my_class == 'Fighter/Mage/Cleric'\
        or my_class == 'Fighter/Mage/Druid' or my_class == 'Fighter/Mage/Thief':
        x = int(my_level / 3)
        wprofs = x * 4 + 4
    else:
        x = int(my_level / 6)
        wprofs = x * 1 + 1
    
    return wprofs

#--------------------------------------
# Randomly select weapon profs for
#  priests of a certain mythos
#--------------------------------------
def P_selectWP(my_weapons, wprofs):
    my_wprofs = []
    if wprofs > len(my_weapons):
        wprofs = len(my_weapons)
    while wprofs > 0:
        prof_pick = random.randint(0,len(my_weapons)-1)
        while my_weapons[prof_pick] in my_wprofs: # Don't pick already picked weapon
            prof_pick = random.randint(0,len(my_weapons)-1)
        my_wprofs.append(my_weapons[prof_pick])
        wprofs -= 1

    return my_wprofs

#--------------------------------------
# Randomly select weapon profs
#--------------------------------------
def selectWP(my_class, wprofs):
    my_wprofs = []
    all_weapons = ['Battle axe','Blowgun','Composite long bow','Composite short bow','Long bow','Short bow','Club',\
        'Hand crossbow','Heavy crossbow','Light crossbow','Dagger','Dart','Flail','Mace','Pick','Hand/Throwing axe',\
        'Harpoon','Javelin','Knife','Morning star','Awl pike','Bardiche','Bec de corbin','Bill-guisarme','Fauchard',\
        'Fauchard-fork','Glaive','Glaive-guisarme','Guisarme','Guisarme-voulge','Halberd','Hook fauchard','Lucern hammer',\
        'Military fork','Partisan','Ranseur','Spetum','Voulge','Quarterstaff','Scourge','Sickle','Sling','Spear','Staff sling',\
        '1-handed bastard sword','2-handed bastard sword','Broad sword','Khopesh','Long sword','Scimitar','Short sword',\
        '2-handed sword','Trident','Warhammer','Whip']
    cleric_weapons = ['Club','Flail','Mace','Morning star','Quarterstaff','Staff sling','Sling','Warhammer']
    wizard_weapons = ['Dagger','Quarterstaff','Staff sling','Dart','Knife','Sling']
    druid_weapons = ['Club','Sickle','Dart','Spear','Dagger','Scimitar','Quarterstaff','Sling','Staff sling']
    thief_weapons = ['Club','Dagger','Dart','Hand crossbow','Knife','Whip','Short bow','Sling','Quarterstaff',\
        'Staff sling','Broad sword','Long sword','Short sword']

    if my_class == 'Fighter':   # Fighter weapon specialization
        my_wprofs = F_selectWP(all_weapons, wprofs)
    elif my_class == 'Paladin' or my_class == 'Ranger' or my_class == 'Bard' or my_class == 'Fighter/Thief'\
        or my_class == 'Fighter/Mage' or my_class == 'Fighter/Illusionist' or my_class == 'Fighter/Mage/Thief':
        # Pick from all weapons list
        #  until all currently available WP slots are full
        while wprofs > 0:
            prof_pick = random.randint(0,54)    # 55 possible weapons, pick 1
            while all_weapons[prof_pick] in my_wprofs: # Don't pick already picked weapon
                prof_pick = random.randint(0,54)
            my_wprofs.append(all_weapons[prof_pick])
            wprofs -= 1
    elif my_class == 'Cleric' or my_class == 'Fighter/Cleric' or my_class == 'Fighter/Mage/Cleric'\
        or my_class == 'Cleric/Ranger' or my_class == 'Cleric/Thief' or my_class == 'Cleric/Illusionist'\
        or my_class == 'Cleric/Mage':
        # Pick from cleric weapons list
        #  until all currently available WP slots are full
        if wprofs > 8:  # High-level characters may have more slots than weapons
                wprofs = 8
        while wprofs > 0:
            prof_pick = random.randint(0,7)    # 8 possible weapons, pick 1
            while cleric_weapons[prof_pick] in my_wprofs: # Don't pick already picked weapon
                prof_pick = random.randint(0,7)
            my_wprofs.append(cleric_weapons[prof_pick])
            wprofs -= 1
    elif my_class == 'Wizard' or my_class == 'Mage' or my_class == 'Illusionist':
        # Pick from Wizard weapons list
        #  until all currently available WP slots are full
        while wprofs > 0:
            prof_pick = random.randint(0,5)    # 6 possible weapons, pick 1
            while wizard_weapons[prof_pick] in my_wprofs: # Don't pick already picked weapon
                prof_pick = random.randint(0,5)
            my_wprofs.append(wizard_weapons[prof_pick])
            wprofs -= 1
    elif my_class == 'Druid' or my_class == 'Druid/Mage' or my_class == 'Fighter/Druid' or my_class == 'Fighter/Mage/Druid':
        # Pick from Druid weapons list
        #  until all currently available WP slots are full
        if wprofs > 9:      # Druids can accumulate more WP slots than allowed weapons to select
            wprofs = 9
        while wprofs > 0:
            prof_pick = random.randint(0,8)    # 9 possible weapons, pick 1
            while druid_weapons[prof_pick] in my_wprofs: # Don't pick already picked weapon
                prof_pick = random.randint(0,8)
            my_wprofs.append(druid_weapons[prof_pick])
            wprofs -= 1
    elif my_class == 'Thief' or my_class == 'Mage/Thief' or my_class == 'Illusionist/Thief':
        # Pick from Thief weapons list
        #  until all currently available WP slots are full
        while wprofs > 0:
            prof_pick = random.randint(0,12)    # 13 possible weapons, pick 1
            while thief_weapons[prof_pick] in my_wprofs: # Don't pick already picked weapon
                prof_pick = random.randint(0,12)
            my_wprofs.append(thief_weapons[prof_pick])
            wprofs -= 1

    return my_wprofs

#--------------------------------------
# Determine Armor Class
#--------------------------------------
def getAC(armor): 
    if armor == 'Leather Armor' or armor == 'Padded Armor':
        AC = 8
    elif armor == 'Studded Leather' or armor == 'Ring Mail':
        AC = 7
    elif armor == 'Brigandine' or armor == 'Scale Mail' or armor == 'Hide Armor':
        AC = 6
    elif armor == 'Chain Mail':
        AC = 5
    elif armor == 'Splint Mail' or armor == 'Banded Mail' or armor == 'Bronze Plate Mail':
        AC = 4
    elif armor == 'Plate Mail':
        AC = 3
    elif armor == 'Field Plate':
        AC = 2
    elif armor == 'Full Plate':
        AC = 1
    else:
        AC = 10
    
    return AC

#--------------------------------------
# Randomly select armor
#--------------------------------------
def chooseArmor(my_class):
    armor_list = ['Leather Armor','Padded Armor','Studded Leather','Ring Mail',\
        'Brigandine','Scale Mail','Hide Armor','Chain Mail','Splint Mail','Banded Mail',\
            'Bronze Plate Mail','Plate Mail','Field Plate','Full Plate']
    
    if my_class == 'Fighter' or my_class == 'Paladin' or my_class == 'Cleric' or my_class == 'Fighter/Cleric'\
        or my_class == 'Priest':
        my_armor = random.choice(armor_list)
    elif my_class == 'Bard':
        allowed = [0,1,2,3,6,7]
        allowed_list = [armor_list[i] for i in allowed]
        my_armor = random.choice(allowed_list)
    elif my_class == 'Thief' or my_class == 'Ranger' or my_class == 'Cleric/Ranger' or my_class == 'Fighter/Thief'\
        or my_class == 'Cleric/Thief':
        allowed = [0,1,2]
        allowed_list = [armor_list[i] for i in allowed]
        my_armor = random.choice(allowed_list)
    elif my_class == 'Druid' or my_class == 'Fighter/Druid':
        allowed = [0,1,6]
        allowed_list = [armor_list[i] for i in allowed]
        my_armor = random.choice(allowed_list)
    else:
        my_armor = 'No Armor'

    return my_armor

#--------------------------------------
# Generate random character
#--------------------------------------
def genChar(my_level):
    scores = [0,0,0,0,0,0,0]
    scores = roll(scores)
    my_race = racial(scores)
    scores = raceAdjust(scores, my_race)
    my_class = classSelector(scores, my_race)
    xSTR, scores[0] = rollSTR(scores[0], my_race, my_class)
    my_gender = gender()
    my_name = genName(my_gender)
    my_AL = genAL(my_class, my_race)
    my_hp = rollHP(my_class, my_level)
    thac0 = getTHAC0(my_class, my_level)
    my_st = getST(my_class, my_level, my_race, scores[2])

    return scores, my_race, my_class, my_gender, my_name, my_AL, my_hp, xSTR, thac0, my_st

#--------------------------------------
# Returns special abilities associated
#  with the character race
#--------------------------------------
def specialRace(my_race):
    if my_race == 'Dwarf':
        special = ['Infravision: 60\'','Detect Grade/Slope: 83%','Detect New Construction: 83%',\
            'Detect Shift/Slide Room: 66%','Detect Stonework Traps: 50%','Determine Depth: 50%',\
            'Chance of Magic Item Malfunction: 20%','+1 to hit Orcs, Half-Orcs, Goblins, and Hobgoblins']
    elif my_race == 'Elf':
        special = ['Infravision: 60\'','Resistance to Charm/Sleep: 90%',\
            'Detect Secret Doors: 1 in 6 or 2 in 6 if searching','Sneaking: opponets have -4 penalty to suprise']
    elif my_race == 'Half-Elf':
        special = ['Infravision: 60\'','Resistance to Charm/Sleep: 30%',\
            'Detect Secret Doors: 1 in 6 or 2 in 6 if searching']
    elif my_race == 'Halfling':
        special = ['Infravision: 60\'','+1 to hit with thrown weapons and slings',\
            'Sneaking: opponets have -4 penalty to suprise']
    elif my_race == 'Gnome':
        special = ['Infravision: 60\'','Detect Grade/Slope: 83%','Detect Unsafe Walls/Ceiling/Floor: 70%',\
            'Determine Depth: 66%','Detect Direction Underground: 50%',\
            'Chance of Magic Item Malfunction: 20%','+1 to hit Kobolds and Goblins']
    elif my_race == 'Half-Orc':
        special = ['Infravision: 60\'','Detect Grade/Slope: 83%','Detect New Construction: 83%',\
            'Detect Shift/Slide Room: 66%','Detect Stonework Traps: 50%','Determine Depth: 50%',\
            '+2 to saving throws against disease and to resist','    the effect of poison and bad smells']
    else: # only human
        special = ['None']

    return special

#--------------------------------------
# Print out character race
#--------------------------------------
def printRace(my_race):
    print('Race = ' + my_race)

#--------------------------------------
# Print out character class
#--------------------------------------
def printClass(my_class):
    print('Class = ' + my_class)

#--------------------------------------
# Print out character ability scores
#--------------------------------------
def printScores(scores, xSTR, my_class):
    # Find ability score attributes
    str_att = findSTR(scores[0], xSTR)
    dex_att = findDEX(scores[1])
    con_att = findCON(scores[2], my_class)
    int_att = findINT(scores[3])
    wis_att = findWIS(scores[4])
    cha_att = findCHA(scores[5])

    # Print strength modifier if exceptional
    if xSTR != 0:   # Exceptional STR
        print('STR | '+str(scores[0]) + '/' + str(xSTR) + ' | Hit Prob: ' + str(str_att[0])\
            +' | Dmg Adj: ' + str(str_att[1]) + ' | Wgt Allow: ' + str(str_att[2]) + ' | Max Press: ' + str(str_att[3])\
                +' | Op Drs: ' + str(str_att[4])+ ' | BB/LG: ' + str(str_att[5])+ '%')
    else:
        print('STR | '+str(scores[0])+ ' | Hit Prob: ' + str(str_att[0])\
            +' | Dmg Adj: ' + str(str_att[1]) + ' | Wgt Allow: ' + str(str_att[2]) + ' | Max Press: ' + str(str_att[3])\
                +' | Op Drs: ' + str(str_att[4])+ ' | BB/LG: ' + str(str_att[5])+ '%')
    print('DEX | '+str(scores[1])+ ' | Rctn Adj: ' + str(dex_att[0])\
            +' | Missle Att Adj: ' + str(dex_att[1]) + ' | Def Adj: ' + str(dex_att[2]))
    print('CON | '+str(scores[2])+ ' | HP Adj: ' + str(con_att[0])\
            +' | Sys Shock: ' + str(con_att[1]) + '% | Res Survival: ' + str(con_att[2])+'%')
    print('INT | '+str(scores[3])+ ' | # Lang: ' + str(int_att[0])\
            +' | Spell Lvl: ' + str(int_att[1]) + 'th | Chance Lrn Spl: ' + str(int_att[2])+'% | Max # Spl/Lvl ' + \
                str(int_att[3]) + ' | Ill Imnty: ' + str(int_att[4]))
    print('WIS | '+str(scores[4])+ ' | Mag Def Adj: ' + str(wis_att[0])\
            +' | Bonus Spells: ' + str(wis_att[1]) + ' | Chance Spl Fail: ' + str(wis_att[2])+'%')
    print('CHA | '+str(scores[5])+ ' | Max # Hench: ' + str(cha_att[0])\
            +' | Loyalty Base: ' + str(cha_att[1]) + ' | React Adj: ' + str(cha_att[2]))

#--------------------------------------
# Gather and return class-specific 
#   character data
#--------------------------------------
def classData(my_class, my_level, my_race, scores, my_armor):
    if my_class == 'Wizard':
        my_xp = getWizard_XP(my_level)
        spellsByLevel = Wizard_Spells(my_level)
        school = Wizard_Specialist(my_race, scores)
        return my_xp, spellsByLevel, school
    elif my_class == 'Mage':
        my_xp = getWizard_XP(my_level)
        spellsByLevel = Wizard_Spells(my_level)
        school = ['Mage','General','None']
        return my_xp, spellsByLevel, school
    elif my_class == 'Illusionist':
        my_xp = getWizard_XP(my_level)
        spellsByLevel = Wizard_Spells(my_level)
        school = ['Illusionist','Illusion','Necromancy, Invocation/Evocation, and Abjuration']
        return my_xp, spellsByLevel, school
    elif my_class == 'Cleric':
        my_xp = getPriest_XP(my_class, my_level)
        spellsByLevel = Priest_Spells(my_level, scores[4])
        my_Gspheres, my_Mspheres = getSpheres(my_class)
        return my_xp, spellsByLevel, my_Gspheres, my_Mspheres
    elif my_class == 'Priest': # priest of a certain mythos
        my_xp = getPriest_XP(my_class, my_level)
        spellsByLevel = Priest_Spells(my_level, scores[4])
        my_deity, my_Gspheres, my_Mspheres, my_Gpower, my_weapons = getMythos()
        return my_xp, spellsByLevel, my_deity, my_Gspheres, my_Mspheres, my_Gpower, my_weapons
    elif my_class == 'Druid':
        my_xp = getPriest_XP(my_class, my_level)
        spellsByLevel = Priest_Spells(my_level, scores[4])
        my_Gspheres, my_Mspheres = getSpheres(my_class)
        return my_xp, spellsByLevel, my_Gspheres, my_Mspheres
    elif my_class == 'Fighter':
        my_xp = getWarrior_XP(my_class, my_level)
        S_Att_R = getS_Att_R(my_level, my_class)
        Att_R = getAtt_R(my_level)
        followers = getF_Followers(my_level, my_class)
        return my_xp, S_Att_R, Att_R, followers
    elif my_class == 'Paladin':
        my_xp = getWarrior_XP(my_class, my_level)
        Att_R = getAtt_R(my_level)
        sLevel, spellsByLevel = Paladin_Spells(my_level)
        my_Gspheres, my_Mspheres = getSpheres(my_class)
        return my_xp, Att_R, sLevel, spellsByLevel, my_Gspheres, my_Mspheres
    elif my_class == 'Ranger':
        my_xp = getWarrior_XP(my_class, my_level)
        Att_R = getAtt_R(my_level)
        thief_skills, casting_lvl, priest_spells = Ranger_Abilities(my_level)
        my_Gspheres, my_Mspheres = getSpheres(my_class)
        followers = getR_Followers(my_level, my_class)
        return my_xp, Att_R, thief_skills, casting_lvl, priest_spells, my_Gspheres, my_Mspheres, followers
    elif my_class == 'Thief':
        my_xp = getRogue_XP(my_level)
        my_thief_skills = Thief_Skills(my_race, my_level, my_armor, scores[1])
        backstab = backStab(my_level)
        followers = getT_Followers(my_class, my_level)
        return my_xp, my_thief_skills, backstab, followers
    else: # my_class == 'Bard'
        my_xp = getRogue_XP(my_level)
        my_thief_skills = bard_skills(my_race, my_level, my_armor, scores[1])
        spellsByLevel = Bard_Spells(my_level)
        return my_xp, my_thief_skills, spellsByLevel

#--------------------------------------
# Print class-specific 
#   character data
#--------------------------------------
def printClassData(my_class, my_level, my_race, scores, my_armor):
    if my_race != 'Human':
        specialR = specialRace(my_race)
        print('\n------------------------\n' + str(my_race) + ' Abilities:\n')
        for i in range(0,len(specialR)):
            print(specialR[i])      
    
    if 'Fighter' in my_class:
        print('\n------------------------\nFighter Class:\n')
        my_xp, S_Att_R, Att_R, followers = classData('Fighter', my_level, my_race, scores, my_armor)
        print('\nExperience Points: ' + str(my_xp))
        print('\nSpecialist Attacks/Round:\tMelee\tLight X-bow\tHeavy X-bow\tThrown Dagger\tThrown Dart\tOther Missiles(not bow)')
        print('                         \t' + str(S_Att_R[0]) + '\t' + str(S_Att_R[1]) + '\t\t' + str(S_Att_R[2])\
            + '\t\t' + str(S_Att_R[3]) + '\t\t' + str(S_Att_R[4]) + '\t\t' + str(S_Att_R[5]))
        print('\nNon-Specialist Attacks/Round: ' + str(Att_R))
        print('\nFollowers: ' + str(followers))
    if my_class == 'Paladin':
        print('\n------------------------\nPaladin Class:\n')
        my_xp, Att_R, sLevel, spellsByLevel, my_Gspheres, my_Mspheres = classData(my_class, my_level, my_race, scores, my_armor)
        print('\nExperience Points: ' + str(my_xp))
        print('\nAttacks/Round: ' + str(Att_R))
        print('\nPriest Spells:\tCasting Level\t1st\t2nd\t3rd\t4th')
        print('              \t' + str(sLevel) + '\t\t' + str(spellsByLevel[0]) + '\t' + str(spellsByLevel[1]) + '\t' + str(spellsByLevel[2])\
            + '\t' + str(spellsByLevel[3]))
    if 'Ranger' in my_class:
        print('\n------------------------\nRanger Class:\n')
        my_xp, Att_R, thief_skills, casting_lvl, priest_spells, my_Gspheres, my_Mspheres, followers = classData('Ranger', my_level, my_race, scores, my_armor)
        print('\nExperience Points: ' + str(my_xp))
        print('\nAttacks/Round: ' + str(Att_R))
        print('\nPriest Spells:\tCasting Level\t1st\t2nd\t3rd')
        print('              \t' + str(casting_lvl) + '\t\t' + str(priest_spells[0]) + '\t' + str(priest_spells[1]) + '\t' + str(priest_spells[2]))
        print('\nHide in Shadows: ' + str(thief_skills[0]))
        print('Move Silently: ' + str(thief_skills[1]))
        print('\nFollowers: ' + str(followers))
    if my_class == 'Wizard' or 'Mage' in my_class:
        print('\n------------------------\nWizard Class:\n')
        my_xp, wspellsByLevel, school = classData('Wizard', my_level, my_race, scores, my_armor)
        print('\nExperience Points: ' + str(my_xp))
        if school[0] != 'Mage':
            print('\nWizard School Specialization: ' + str(school[1]))
            print('Opposition School(s): ' + str(school[2]))
        print('\nWizard Spells:\t1st\t2nd\t3rd\t4th\t5th\t6th\t7th\t8th\t9th')
        print('              \t' + str(wspellsByLevel[0]) + '\t' + str(wspellsByLevel[1]) + '\t' + str(wspellsByLevel[2])\
            + '\t' + str(wspellsByLevel[3]) + '\t' + str(wspellsByLevel[4]) + '\t' + str(wspellsByLevel[5]) + '\t' + str(wspellsByLevel[6])\
            + '\t' + str(wspellsByLevel[7]) + '\t' + str(wspellsByLevel[8]))
    if 'Illusionist' in my_class:
        print('\n------------------------\nWizard Class:\n')
        my_xp, wspellsByLevel, school = classData('Illusionist', my_level, my_race, scores, my_armor)
        print('\nExperience Points: ' + str(my_xp))
        print('\nWizard School Specialization: ' + str(school[1]))
        print('Opposition School(s): ' + str(school[2]))
        print('\nWizard Spells:\t1st\t2nd\t3rd\t4th\t5th\t6th\t7th\t8th\t9th')
        print('              \t' + str(wspellsByLevel[0]) + '\t' + str(wspellsByLevel[1]) + '\t' + str(wspellsByLevel[2])\
            + '\t' + str(wspellsByLevel[3]) + '\t' + str(wspellsByLevel[4]) + '\t' + str(wspellsByLevel[5]) + '\t' + str(wspellsByLevel[6])\
            + '\t' + str(wspellsByLevel[7]) + '\t' + str(wspellsByLevel[8]))
    if 'Cleric' in my_class:
        print('\n------------------------\nCleric Class:\n')
        my_xp, pspellsByLevel, my_Gspheres, my_Mspheres = classData('Cleric', my_level, my_race, scores, my_armor)
        print('\nExperience Points: ' + str(my_xp))
        print('\nGreater Spheres: ' + str(my_Gspheres))
        print('Minor Spheres: ' + str(my_Mspheres))
        print('\nPriest Spells:\t1st\t2nd\t3rd\t4th\t5th\t6th\t7th')
        print('              \t' + str(pspellsByLevel[0]) + '\t' + str(pspellsByLevel[1]) + '\t' + str(pspellsByLevel[2])\
            + '\t' + str(pspellsByLevel[3]) + '\t' + str(pspellsByLevel[4]) + '\t' + str(pspellsByLevel[5]) + '\t' + str(pspellsByLevel[6]))
    if 'Druid' in my_class:
        print('\n------------------------\nDruid Class:\n')
        my_xp, pspellsByLevel, my_Gspheres, my_Mspheres = classData('Druid', my_level, my_race, scores, my_armor)
        print('\nExperience Points: ' + str(my_xp))
        print('\nGreater Spheres: ' + str(my_Gspheres))
        print('Minor Spheres: ' + str(my_Mspheres))
        print('\nPriest Spells:\t1st\t2nd\t3rd\t4th\t5th\t6th\t7th')
        print('              \t' + str(pspellsByLevel[0]) + '\t' + str(pspellsByLevel[1]) + '\t' + str(pspellsByLevel[2])\
            + '\t' + str(pspellsByLevel[3]) + '\t' + str(pspellsByLevel[4]) + '\t' + str(pspellsByLevel[5]) + '\t' + str(pspellsByLevel[6]))
    if my_class == 'Priest':
        print('\n------------------------\nPriest Class:\n')
        my_xp, pspellsByLevel, my_deity, my_Gspheres, my_Mspheres, my_Gpower, my_weapons = classData(my_class, my_level, my_race, scores, my_armor)
        print('\nExperience Points: ' + str(my_xp))
        print('\nDeity: ' + str(my_deity))
        print('\nGranted Power: ' + str(my_Gpower))
        print('\nGreater Spheres: ' + str(my_Gspheres))
        print('Minor Spheres: ' + str(my_Mspheres))
        print('\nPriest Spells:\t1st\t2nd\t3rd\t4th\t5th\t6th\t7th')
        print('              \t' + str(pspellsByLevel[0]) + '\t' + str(pspellsByLevel[1]) + '\t' + str(pspellsByLevel[2])\
            + '\t' + str(pspellsByLevel[3]) + '\t' + str(pspellsByLevel[4]) + '\t' + str(pspellsByLevel[5]) + '\t' + str(pspellsByLevel[6]))
    if 'Thief' in my_class:
        my_xp, my_thief_skills, backstab, followers = classData('Thief', my_level, my_race, scores, my_armor)
        print('\n------------------------\nThief Class:\n')
        print('\nExperience Points: ' + str(my_xp))
        print('\nThief Skills:\tPick Pockets: ' + str(my_thief_skills[0]) + '%\tOpen Locks: ' + str(my_thief_skills[1]) + '%\t\tFind/Remove Traps: '\
            + str(my_thief_skills[2]) + '%\n             \tMove Silently: ' + str(my_thief_skills[3]) + '%\tHide in Shadows: ' + str(my_thief_skills[4])\
            + '%\tDetect Noise: ' + str(my_thief_skills[5]) + '%\n             \tClimb Walls: ' + str(my_thief_skills[6]) + '%\tRead Languiages: '\
            + str(my_thief_skills[7]) + '%')
        print('\nBackstab Multiplier: x' + str(backstab))
        print('\nFollowers: ' + str(followers))
    if my_class == 'Bard':
        print('\n------------------------\nBard Class:\n')
        my_xp, my_thief_skills, wspellsByLevel = classData(my_class, my_level, my_race, scores, my_armor)
        school = ['Mage','General','None']
        print('\nExperience Points: ' + str(my_xp))
        print('\nThief Skills:\tPick Pockets: ' + str(my_thief_skills[0]) + '%\tDetect Noise: ' + str(my_thief_skills[1]) + '%\n             \tClimb Walls: ' + str(my_thief_skills[2]) + '%\tRead Languiages: '\
            + str(my_thief_skills[3]) + '%')
        print('\nWizard Spells:\t1st\t2nd\t3rd\t4th\t5th\t6th')
        print('              \t' + str(wspellsByLevel[0]) + '\t' + str(wspellsByLevel[1]) + '\t' + str(wspellsByLevel[2])\
            + '\t' + str(wspellsByLevel[3]) + '\t' + str(wspellsByLevel[4]) + '\t' + str(wspellsByLevel[5]))
    
    # Print Weapon Proficiencies
    my_w_prof = wProf(my_class, my_level)

    if my_class == 'Priest':
        my_wprofs = P_selectWP(my_weapons, my_w_prof)
    else:
        my_wprofs = selectWP(my_class, my_w_prof)

    print('\nWeapon Proficiencies:')
    for i in range (0, len(my_wprofs)):
        print(my_wprofs[i]) 

    # Print Nonweapon Proficiencies
    my_nonw_prof = nonwProf(my_class, my_level)
    my_nwprofs = selectNWP(my_class, my_nonw_prof)
    print('\nNonweapon Proficiency:\t| Ability Check + Modifier')
    for i in range (1, len(my_nwprofs)):
        print(my_nwprofs[i][0] + '\t\t' + my_nwprofs[i][2] + ' ' + str(my_nwprofs[i][3]))

    print('\n------------------------\nGear:\n')

    print('Armor = ' + my_armor)
    print('\n')

    if 'Mage' in my_class or 'Illusionist' in my_class or my_class == 'Wizard':
        my_spells = getWizardSpells(my_class, school, wspellsByLevel)
        printWizardSpells(my_class, my_spells)
    elif my_class == 'Bard':
        my_spells = getWizardSpells(my_class, school, wspellsByLevel)
        printWizardSpells(my_class, my_spells)
    
    if 'Cleric' in my_class or 'Druid' in my_class or my_class == 'Priest':
        my_spells = getPriestSpells(pspellsByLevel, my_Gspheres, my_Mspheres, my_class)
        printPriestSpells(my_class, my_spells)
    elif my_class == 'Ranger':
        my_spells = getPriestSpells(priest_spells, my_Gspheres, my_Mspheres, my_class)
        printPriestSpells(my_class, my_spells)
    elif my_class == 'Paladin':
        my_spells = getPriestSpells(spellsByLevel, my_Gspheres, my_Mspheres, my_class)
        printPriestSpells(my_class, my_spells)

#--------------------------------------
# Create character and print to PDF
#--------------------------------------
def printSheet(my_race, my_class, my_level):
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    
    xSTR, scores[0] = rollSTR(scores[0], my_race, my_class)
    my_gender = gender()
    my_height = getHeight(my_race, my_gender)
    my_weight = getWeight(my_race, my_gender)
    my_age = getAge(my_race, my_level)
    my_name = genName(my_gender)
    my_AL = genAL(my_class, my_race)
    my_hp = rollHP(my_class, my_level)
    thac0 = getTHAC0(my_class, my_level)
    my_st = getST(my_class, my_level, my_race, scores[2])
    my_armor = chooseArmor(my_class)
    my_AC = getAC(my_armor)

    # Find ability score attributes
    str_att = findSTR(scores[0], xSTR)
    dex_att = findDEX(scores[1])
    con_att = findCON(scores[2], my_class)
    int_att = findINT(scores[3])
    wis_att = findWIS(scores[4])
    cha_att = findCHA(scores[5])
            
    my_w_prof = wProf(my_class, my_level)

    if my_class == 'Priest':
        my_xp, pspellsByLevel, my_deity, my_Gspheres, my_Mspheres, my_Gpower, my_weapons = classData(my_class, my_level, my_race, scores, my_armor)

    if my_class == 'Priest':
        my_wprofs = P_selectWP(my_weapons, my_w_prof)
    else:
        my_wprofs = selectWP(my_class, my_w_prof)

    my_nonw_prof = nonwProf(my_class, my_level)
    my_nwprofs = selectNWP(my_class, my_nonw_prof)

    # Print character sheets to a directory
    my_dir = '2E_Character_Sheets'
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, my_dir)
    try:
        os.makedirs(path, exist_ok= True)
    except OSError as error:
        print("Directory '%s' can not be created.\n" % my_dir)

    name2 = os.path.join(path, my_name)
    canvas = canvas.Canvas(name2 + ".pdf", pagesize=A4)
    canvas.setLineWidth(.3)
    canvas.setFont('Helvetica', 12)

    canvas.drawString(30,750,'Name: ' + my_name)
    canvas.drawString(30,735,'Race: ' + my_race)
    canvas.drawString(30,720,'Class: ' + my_class)
    canvas.drawString(30,705,'Level: ' + str(my_level))
    canvas.drawString(500,750,'Alignment: ' + my_AL)
    canvas.drawString(500,735,'Gender: ' + my_gender)
    canvas.drawString(310,705,'Height: ' + str(my_height) + ' inches | Weight: ' + str(my_weight) + ' lbs | Age: ' + str(my_age) + ' years')

    canvas.line(30,690,580,690)

    canvas.drawString(30,675,'Ability Scores')
    canvas.drawString(30,645,'STR: ')
    canvas.drawString(65,645,str(scores[0]))
    canvas.drawString(30,630,'DEX: ')
    canvas.drawString(65,630,str(scores[1]))
    canvas.drawString(30,615,'CON: ')
    canvas.drawString(65,615,str(scores[2]))
    canvas.drawString(30,600,'INT: ')
    canvas.drawString(65,600,str(scores[3]))
    canvas.drawString(30,585,'WIS: ')
    canvas.drawString(65,585,str(scores[4]))
    canvas.drawString(30,570,'CHA: ')
    canvas.drawString(65,570,str(scores[5]))
    canvas.line(85,655,85,570)
    canvas.setFont('Helvetica', 8)
    canvas.drawString(90,645,'Hit Prob: ' + str(str_att[0]))
    canvas.drawString(90,630,'Rctn Adj: ' + str(dex_att[0]))
    canvas.drawString(90,615,'HP Adj: ' + str(con_att[0]))
    canvas.drawString(90,600,'# Lang: ' + str(int_att[0]))
    canvas.drawString(90,585,'Mag Def Adj: ' + str(wis_att[0]))
    canvas.drawString(90,570,'Max # Hench: ' + str(cha_att[0]))
    canvas.line(155,655,155,570)
    canvas.drawString(160,645,'Dmg Adj: ' + str(str_att[1]))
    canvas.drawString(160,630,'Missle Att Adj: ' + str(dex_att[1]))
    canvas.drawString(160,615,'Sys Shock: ' + str(con_att[1])+ '%')
    canvas.drawString(160,600,'Spell Lvl: ' + str(int_att[1]))
    canvas.drawString(160,585,'Bonus Spells: ' + str(wis_att[1]))
    canvas.drawString(160,570,'Loyalty Base: ' + str(cha_att[1]))
    canvas.line(225,655,225,600)
    canvas.line(225,580,225,570)
    canvas.drawString(230,645,'Wgt Allow: ' + str(str_att[2]))
    canvas.drawString(230,630,'Def Adj: ' + str(dex_att[2]))
    canvas.drawString(230,615,'Res Survival: ' + str(con_att[2])+ '%')
    canvas.drawString(230,600,'Chance Lrn Spl: ' + str(int_att[2]) + '%')
    canvas.drawString(230,570,'React Adj: ' + str(cha_att[2]))
    canvas.line(310,655,310,570)
    canvas.drawString(315,645,'Max Press: ' + str(str_att[3]))
    canvas.drawString(315,600,'Max # Spl/Lvl: ' + str(int_att[3]))
    canvas.drawString(315,585,'Chance Spl Fail: ' + str(wis_att[2]) + '%')
    canvas.line(400,655,400,570)
    canvas.drawString(405,645,'Op Drs: ' + str(str_att[4]))
    canvas.drawString(405,600,'Ill Imnty: ' + str(int_att[4]))
    canvas.line(460,655,460,570)
    canvas.drawString(465,645,'BB/LG: ' + str(str_att[5]) + '%')

    canvas.setFont('Helvetica', 12)
    canvas.line(30,560,580,560)
    canvas.drawString(30,545,'Saving Throws')
    canvas.setFont('Helvetica', 8)
    canvas.drawString(30,530,'Paralyzation, Poison, or Death Magic: ' + str(my_st[0]))
    canvas.drawString(30,520,'Rod, Staff, or Wand: ' + str(my_st[1]))
    canvas.drawString(30,510,'Petrification or Polymorph: ' + str(my_st[2]))
    canvas.drawString(30,500,'Breath Weapon: ' + str(my_st[3]))
    canvas.drawString(30,490,'Spell: ' + str(my_st[4]))
    canvas.line(30,480,225,480)

    canvas.setFont('Helvetica', 12)
    canvas.drawString(30,465,'Combat')
    canvas.drawString(30,445,'Hit Points: ' + str(my_hp))
    canvas.drawString(30,390,'Base THAC0: ' + str(thac0))
    if my_class == 'Fighter':
        canvas.drawString(30,375,'Melee THAC0: ' + str(thac0 - 1) + ' (Specialist)')
    else:
        canvas.drawString(30,375,'Melee THAC0: ' + str(thac0))
    canvas.drawString(30,360,'Missile THAC0: ' + str(thac0 - dex_att[1]))
    canvas.line(30,355,225,355)
    canvas.drawString(30,340,'Armor')
    canvas.drawString(30,325,'Natural armor class: ' + str(10 + dex_att[2]))
    canvas.drawString(30,310,'Armor - ' + my_armor + ': AC ' + str(my_AC + dex_att[2]))
    canvas.line(225,560,225,295)

    canvas.drawString(230,545,'Weapon Proficiencies')
    canvas.setFont('Helvetica', 8)
    x = 530
    y = 0
    z = 530
    for i in range (0, len(my_wprofs)):
        if y == 23:
            canvas.drawString(340,z,my_wprofs[i])
            z -= 10
        else:
            canvas.drawString(230,x,my_wprofs[i])
            x -= 10
            y += 1
    
    canvas.setFont('Helvetica', 12)
    canvas.drawString(420,545,'Non-Weapon Proficiencies')
    canvas.setFont('Helvetica', 8)

    x = 530
    for i in range (1, len(my_nwprofs)):
        canvas.drawString(420,x,my_nwprofs[i][0])
        canvas.drawString(500,x,str(my_nwprofs[i][2]))
        canvas.drawString(520,x,str(my_nwprofs[i][3]))
        x -= 10

    canvas.setFont('Helvetica', 12)
    canvas.line(30,295,580,295)

    if my_race != 'Human':
        canvas.line(380,295,380,140)
        specialR = specialRace(my_race)
        canvas.drawString(390,280,str(my_race)+' Abilities')
        canvas.setFont('Helvetica', 8)
        y = 250
        for i in range(0,len(specialR)):
            canvas.drawString(390,y,specialR[i])
            y -= 15
    
    canvas.setFont('Helvetica', 12)

    if my_class == 'Fighter':
        canvas.drawString(30,280,'Fighter Class')
        my_xp, S_Att_R, Att_R, followers = classData('Fighter', my_level, my_race, scores, my_armor)
        canvas.drawString(30,250,'Experience Points: ' + str(my_xp))
        canvas.drawString(30,220,'Specialist Attacks/Round:')
        canvas.setFont('Helvetica', 8)
        canvas.drawString(40,205,'Melee')
        canvas.drawString(70,205,'Light X-bow')
        canvas.drawString(120,205,'Heavy X-bow')
        canvas.drawString(180,205,'Thrown Dagger')
        canvas.drawString(240,205,'Thrown Dart')
        canvas.drawString(300,205,'Other Thrown')
        canvas.drawString(40,190,str(S_Att_R[0]))
        canvas.drawString(70,190,str(S_Att_R[1]))
        canvas.drawString(120,190,str(S_Att_R[2]))
        canvas.drawString(180,190,str(S_Att_R[3]))
        canvas.drawString(240,190,str(S_Att_R[4]))
        canvas.drawString(300,190,str(S_Att_R[5]))
        canvas.setFont('Helvetica', 12)
        canvas.drawString(30,170,'Non-Specialist Attacks/Round: ' + str(Att_R))
        canvas.drawString(30,140,'Followers:')
        canvas.setFont('Helvetica', 8)
        canvas.drawString(40,125,'Leader:')
        canvas.drawString(80,125,str(followers[0]))
        canvas.drawString(40,105,'Troops:')
        canvas.drawString(80,105,str(followers[1]))
        canvas.drawString(40,80,'Elite:')
        canvas.drawString(80,80,str(followers[2]))        
    elif my_class == 'Paladin':
        canvas.drawString(30,280,'Paladin Class')
        my_xp, Att_R, sLevel, spellsByLevel, my_Gspheres, my_Mspheres = classData(my_class, my_level, my_race, scores, my_armor)
        canvas.drawString(30,250,'Experience Points: ' + str(my_xp))
        canvas.drawString(30,220,'Attacks/Round: ' + str(Att_R))
        canvas.drawString(30,190,'Priest Spells:')
        canvas.setFont('Helvetica', 8)
        canvas.drawString(120,190,'Casting Level')
        canvas.drawString(180,190,'1st')
        canvas.drawString(200,190,'2nd')
        canvas.drawString(220,190,'3rd')
        canvas.drawString(240,190,'4th')
        canvas.drawString(120,175,str(sLevel))
        canvas.drawString(180,175,str(spellsByLevel[0]))
        canvas.drawString(200,175,str(spellsByLevel[1]))
        canvas.drawString(220,175,str(spellsByLevel[2]))
        canvas.drawString(240,175,str(spellsByLevel[3]))
        canvas.setFont('Helvetica', 12)
    elif my_class == 'Ranger':
        my_xp, Att_R, thief_skills, casting_lvl, priest_spells, my_Gspheres, my_Mspheres, followers = classData('Ranger', my_level, my_race, scores, my_armor)
        canvas.drawString(30,280,'Ranger Class')
        canvas.drawString(30,250,'Experience Points: ' + str(my_xp))
        canvas.drawString(30,220,'Attacks/Round: ' + str(Att_R))
        canvas.drawString(30,190,'Priest Spells:')
        canvas.setFont('Helvetica', 8)
        canvas.drawString(120,190,'Casting Level')
        canvas.drawString(180,190,'1st')
        canvas.drawString(200,190,'2nd')
        canvas.drawString(220,190,'3rd')
        canvas.drawString(120,175,str(casting_lvl))
        canvas.drawString(180,175,str(priest_spells[0]))
        canvas.drawString(200,175,str(priest_spells[1]))
        canvas.drawString(220,175,str(priest_spells[2]))
        canvas.setFont('Helvetica', 12)
        canvas.drawString(30,155,'Priest Spheres:')
        canvas.setFont('Helvetica', 8)
        canvas.drawString(120,155,'Plant, Animal')
        canvas.setFont('Helvetica', 12)
        canvas.drawString(30,130,'Rogue Skills:')
        canvas.setFont('Helvetica', 8)
        canvas.drawString(120,130,'Hide in Shadows:')
        canvas.drawString(190,130,str(thief_skills[0]))
        canvas.drawString(120,115,'Move Silently:')
        canvas.drawString(190,115,str(thief_skills[1]))

        canvas.setFont('Helvetica', 12)
        canvas.drawString(30,100,'Followers:')
        canvas.setFont('Helvetica', 8)
        y = 100
        z = 100
        for i in range (0, len(followers)):
            if y <= 40:
                canvas.drawString(220,z,followers[i])
                z -= 10 
            canvas.drawString(120,y,followers[i])
            y -= 10
    elif my_class == 'Mage':
        my_xp, wspellsByLevel, school = classData('Mage', my_level, my_race, scores, my_armor)
        canvas.drawString(30,280,'Mage Class')
        canvas.drawString(30,250,'Experience Points: ' + str(my_xp))
        canvas.drawString(30,220,'Wizard Spells:')
        canvas.setFont('Helvetica', 8)
        canvas.drawString(120,220,'1st')
        canvas.drawString(140,220,'2nd')
        canvas.drawString(160,220,'3rd')
        canvas.drawString(180,220,'4th')
        canvas.drawString(200,220,'5th')
        canvas.drawString(220,220,'6th')
        canvas.drawString(240,220,'7th')
        canvas.drawString(260,220,'8th')
        canvas.drawString(280,220,'9th')
        canvas.drawString(120,205,str(wspellsByLevel[0]))
        canvas.drawString(140,205,str(wspellsByLevel[1]))
        canvas.drawString(160,205,str(wspellsByLevel[2]))
        canvas.drawString(180,205,str(wspellsByLevel[3]))
        canvas.drawString(200,205,str(wspellsByLevel[4]))
        canvas.drawString(220,205,str(wspellsByLevel[5]))
        canvas.drawString(240,205,str(wspellsByLevel[6]))
        canvas.drawString(260,205,str(wspellsByLevel[7]))
        canvas.drawString(280,205,str(wspellsByLevel[8]))
    elif my_class == 'Wizard':
        my_xp, wspellsByLevel, school = classData('Wizard', my_level, my_race, scores, my_armor)
        canvas.drawString(30,280,'Wizard Class')
        canvas.drawString(30,250,'Experience Points: ' + str(my_xp))
        canvas.drawString(30,220,'Wizard Spells:')
        canvas.setFont('Helvetica', 8)
        canvas.drawString(120,220,'1st')
        canvas.drawString(140,220,'2nd')
        canvas.drawString(160,220,'3rd')
        canvas.drawString(180,220,'4th')
        canvas.drawString(200,220,'5th')
        canvas.drawString(220,220,'6th')
        canvas.drawString(240,220,'7th')
        canvas.drawString(260,220,'8th')
        canvas.drawString(280,220,'9th')
        canvas.drawString(120,205,str(wspellsByLevel[0]))
        canvas.drawString(140,205,str(wspellsByLevel[1]))
        canvas.drawString(160,205,str(wspellsByLevel[2]))
        canvas.drawString(180,205,str(wspellsByLevel[3]))
        canvas.drawString(200,205,str(wspellsByLevel[4]))
        canvas.drawString(220,205,str(wspellsByLevel[5]))
        canvas.drawString(240,205,str(wspellsByLevel[6]))
        canvas.drawString(260,205,str(wspellsByLevel[7]))
        canvas.drawString(280,205,str(wspellsByLevel[8]))
        canvas.setFont('Helvetica', 12)
        canvas.drawString(30,180,'Wizard School Specialization: ' + str(school[1]))
        canvas.drawString(30,160,'Opposition School(s): ' + str(school[2]))
    elif my_class == 'Illusionist':
        my_xp, wspellsByLevel, school = classData('Illusionist', my_level, my_race, scores, my_armor)
        canvas.drawString(30,280,'Wizard Class')
        canvas.drawString(30,250,'Experience Points: ' + str(my_xp))
        canvas.drawString(30,220,'Wizard Spells:')
        canvas.setFont('Helvetica', 8)
        canvas.drawString(120,220,'1st')
        canvas.drawString(140,220,'2nd')
        canvas.drawString(160,220,'3rd')
        canvas.drawString(180,220,'4th')
        canvas.drawString(200,220,'5th')
        canvas.drawString(220,220,'6th')
        canvas.drawString(240,220,'7th')
        canvas.drawString(260,220,'8th')
        canvas.drawString(280,220,'9th')
        canvas.drawString(120,205,str(wspellsByLevel[0]))
        canvas.drawString(140,205,str(wspellsByLevel[1]))
        canvas.drawString(160,205,str(wspellsByLevel[2]))
        canvas.drawString(180,205,str(wspellsByLevel[3]))
        canvas.drawString(200,205,str(wspellsByLevel[4]))
        canvas.drawString(220,205,str(wspellsByLevel[5]))
        canvas.drawString(240,205,str(wspellsByLevel[6]))
        canvas.drawString(260,205,str(wspellsByLevel[7]))
        canvas.drawString(280,205,str(wspellsByLevel[8]))
        canvas.setFont('Helvetica', 12)
        canvas.drawString(30,180,'Wizard School Specialization: ' + str(school[1]))
        canvas.drawString(30,160,'Opposition School(s): ' + str(school[2]))
    elif my_class == 'Cleric':
        my_xp, pspellsByLevel, my_Gspheres, my_Mspheres = classData('Cleric', my_level, my_race, scores, my_armor)
        canvas.drawString(30,280,'Cleric Class')
        canvas.drawString(30,250,'Experience Points: ' + str(my_xp))
        canvas.drawString(30,220,'Priest Spells:')
        canvas.setFont('Helvetica', 8)
        canvas.drawString(120,220,'1st')
        canvas.drawString(140,220,'2nd')
        canvas.drawString(160,220,'3rd')
        canvas.drawString(180,220,'4th')
        canvas.drawString(200,220,'5th')
        canvas.drawString(220,220,'6th')
        canvas.drawString(240,220,'7th')
        canvas.drawString(120,205,str(pspellsByLevel[0]))
        canvas.drawString(140,205,str(pspellsByLevel[1]))
        canvas.drawString(160,205,str(pspellsByLevel[2]))
        canvas.drawString(180,205,str(pspellsByLevel[3]))
        canvas.drawString(200,205,str(pspellsByLevel[4]))
        canvas.drawString(220,205,str(pspellsByLevel[5]))
        canvas.drawString(240,205,str(pspellsByLevel[6]))
        canvas.setFont('Helvetica', 12)
        canvas.drawString(30,180,'Greater Spheres:')
        canvas.setFont('Helvetica', 8)
        x1 = 140
        items = 0
        x2 = 140
        x3 = 140
        x4 = 140
        for i in range (0, len(my_Gspheres)):
            if items >= 9:
                canvas.drawString(x4,135,my_Gspheres[i])
                x4 += 60
            elif items >= 6:
                canvas.drawString(x3,150,my_Gspheres[i])
                x3 += 60
                items += 1
            elif items >= 3:
                canvas.drawString(x2,165,my_Gspheres[i])
                x2 += 60
                items += 1
            else:
                canvas.drawString(x1,180,my_Gspheres[i])
                x1 += 60
                items += 1
        canvas.setFont('Helvetica', 12)
        canvas.drawString(30,120,'Minor Spheres:')
        canvas.setFont('Helvetica', 8)
        x = 140
        for i in range (0, len(my_Mspheres)):
            canvas.drawString(x,120,my_Mspheres[i])
            x += 60
    elif my_class == 'Druid':
        my_xp, pspellsByLevel, my_Gspheres, my_Mspheres = classData('Druid', my_level, my_race, scores, my_armor)
        canvas.drawString(30,280,'Druid Class')
        canvas.drawString(30,250,'Experience Points: ' + str(my_xp))
        canvas.drawString(30,220,'Priest Spells:')
        canvas.setFont('Helvetica', 8)
        canvas.drawString(120,220,'1st')
        canvas.drawString(140,220,'2nd')
        canvas.drawString(160,220,'3rd')
        canvas.drawString(180,220,'4th')
        canvas.drawString(200,220,'5th')
        canvas.drawString(220,220,'6th')
        canvas.drawString(240,220,'7th')
        canvas.drawString(120,205,str(pspellsByLevel[0]))
        canvas.drawString(140,205,str(pspellsByLevel[1]))
        canvas.drawString(160,205,str(pspellsByLevel[2]))
        canvas.drawString(180,205,str(pspellsByLevel[3]))
        canvas.drawString(200,205,str(pspellsByLevel[4]))
        canvas.drawString(220,205,str(pspellsByLevel[5]))
        canvas.drawString(240,205,str(pspellsByLevel[6]))
        canvas.setFont('Helvetica', 12)
        canvas.drawString(30,180,'Greater Spheres:')
        canvas.setFont('Helvetica', 8)
        x1 = 140
        items = 0
        x2 = 140
        x3 = 140
        x4 = 140
        for i in range (0, len(my_Gspheres)):
            if items >= 9:
                canvas.drawString(x4,135,my_Gspheres[i])
                x4 += 60
            elif items >= 6:
                canvas.drawString(x3,150,my_Gspheres[i])
                x3 += 60
                items += 1
            elif items >= 3:
                canvas.drawString(x2,165,my_Gspheres[i])
                x2 += 60
                items += 1
            else:
                canvas.drawString(x1,180,my_Gspheres[i])
                x1 += 60
                items += 1
        canvas.setFont('Helvetica', 12)
        canvas.drawString(30,120,'Minor Spheres:')
        canvas.setFont('Helvetica', 8)
        x = 140
        for i in range (0, len(my_Mspheres)):
            canvas.drawString(x,120,my_Mspheres[i])
            x += 60
    elif my_class == 'Priest':
        my_xp, pspellsByLevel, my_deity, my_Gspheres, my_Mspheres, my_Gpower, my_weapons = classData(my_class, my_level, my_race, scores, my_armor)
        canvas.drawString(30,280,'Priest Class')
        canvas.drawString(30,250,'Experience Points: ' + str(my_xp))
        canvas.drawString(30,220,'Priest Spells:')
        canvas.setFont('Helvetica', 8)
        canvas.drawString(120,220,'1st')
        canvas.drawString(140,220,'2nd')
        canvas.drawString(160,220,'3rd')
        canvas.drawString(180,220,'4th')
        canvas.drawString(200,220,'5th')
        canvas.drawString(220,220,'6th')
        canvas.drawString(240,220,'7th')
        canvas.drawString(120,205,str(pspellsByLevel[0]))
        canvas.drawString(140,205,str(pspellsByLevel[1]))
        canvas.drawString(160,205,str(pspellsByLevel[2]))
        canvas.drawString(180,205,str(pspellsByLevel[3]))
        canvas.drawString(200,205,str(pspellsByLevel[4]))
        canvas.drawString(220,205,str(pspellsByLevel[5]))
        canvas.drawString(240,205,str(pspellsByLevel[6]))
        canvas.setFont('Helvetica', 12)
        canvas.drawString(30,180,'Greater Spheres:')
        canvas.setFont('Helvetica', 8)
        x1 = 140
        items = 0
        x2 = 140
        x3 = 140
        for i in range (0, len(my_Gspheres)):
            if items >= 6:
                canvas.drawString(x3,150,my_Gspheres[i])
                x3 += 60
            elif items >= 3:
                canvas.drawString(x2,165,my_Gspheres[i])
                x2 += 60
                items += 1
            else:
                canvas.drawString(x1,180,my_Gspheres[i])
                x1 += 60
                items += 1
        canvas.setFont('Helvetica', 12)
        canvas.drawString(30,120,'Minor Spheres:')
        canvas.setFont('Helvetica', 8)
        x1 = 140
        for i in range (0, len(my_Mspheres)):
            canvas.drawString(x1,120,my_Mspheres[i])
            x1 += 60

        canvas.setFont('Helvetica', 12)
        canvas.drawString(30,90,'Deity: ' + str(my_deity))
        canvas.drawString(30,70,'Granted Power: ' + str(my_Gpower))
    elif my_class == 'Thief':
        my_xp, thief_skills, backstab, followers = classData('Thief', my_level, my_race, scores, my_armor)
        canvas.drawString(30,280,'Thief Class')
        canvas.drawString(30,250,'Experience Points: ' + str(my_xp))
        canvas.drawString(30,220,'Thief Skills:')
        canvas.setFont('Helvetica', 8)
        canvas.drawString(50,205,'Pick Pockets:')
        canvas.drawString(160,205,'Open Locks:')
        canvas.drawString(50,190,'Find/Remove Traps:')
        canvas.drawString(160,190,'Move Silently:')
        canvas.drawString(50,175,'Hide in Shadows:')
        canvas.drawString(160,175,'Detect Noise:')
        canvas.drawString(50,160,'Climb Walls:')
        canvas.drawString(160,160,'Read Languages:')
        canvas.drawString(130,205,str(thief_skills[0]) + '%')
        canvas.drawString(230,205,str(thief_skills[1]) + '%')
        canvas.drawString(130,190,str(thief_skills[2]) + '%')
        canvas.drawString(230,190,str(thief_skills[3]) + '%')
        canvas.drawString(130,175,str(thief_skills[4]) + '%')
        canvas.drawString(230,175,str(thief_skills[5]) + '%')
        canvas.drawString(130,160,str(thief_skills[6]) + '%')
        canvas.drawString(230,160,str(thief_skills[7]) + '%')
        canvas.setFont('Helvetica', 12)
        canvas.drawString(30,135,'Backstab Multiplier: x' + str(backstab))
        canvas.drawString(30,110,'Followers: ' + str(followers))
    elif my_class == 'Bard':
        my_xp, thief_skills, wspellsByLevel = classData(my_class, my_level, my_race, scores, my_armor)
        school = ['Mage','General','None']
        canvas.drawString(30,280,'Bard Class')
        canvas.drawString(30,250,'Experience Points: ' + str(my_xp))
        canvas.drawString(30,220,'Thief Skills:')
        canvas.setFont('Helvetica', 8)
        canvas.drawString(100,220,'Pick Pockets:')
        canvas.drawString(190,220,'Detect Noise:')
        canvas.drawString(100,205,'Climb Walls:')
        canvas.drawString(190,205,'Read Languages:')
        canvas.drawString(160,220,str(thief_skills[0]) + '%')
        canvas.drawString(260,220,str(thief_skills[1]) + '%')
        canvas.drawString(160,205,str(thief_skills[2]) + '%')
        canvas.drawString(260,205,str(thief_skills[3]) + '%')
        canvas.setFont('Helvetica', 12)
        canvas.drawString(30,180,'Wizard Spells:')
        canvas.setFont('Helvetica', 8)
        canvas.drawString(120,180,'1st')
        canvas.drawString(140,180,'2nd')
        canvas.drawString(160,180,'3rd')
        canvas.drawString(180,180,'4th')
        canvas.drawString(200,180,'5th')
        canvas.drawString(220,180,'6th')
        canvas.drawString(120,165,str(wspellsByLevel[0]))
        canvas.drawString(140,165,str(wspellsByLevel[1]))
        canvas.drawString(160,165,str(wspellsByLevel[2]))
        canvas.drawString(180,165,str(wspellsByLevel[3]))
        canvas.drawString(200,165,str(wspellsByLevel[4]))
        canvas.drawString(220,165,str(wspellsByLevel[5]))
    else:
        # Multi-class Character
        canvas.showPage()
        canvas.setFont('Helvetica', 12)
        canvas.drawString(30,750,'Multi-class Characteristics')
        canvas.line(30,740,580,740)

        if 'Fighter' in my_class:
            canvas.drawString(30,720,'Fighter Class')
            my_xp, S_Att_R, Att_R, followers = classData('Fighter', my_level, my_race, scores, my_armor)
            canvas.drawString(30,690,'Experience Points: ' + str(my_xp))
            canvas.drawString(30,660,'Specialist Attacks/Round:')
            canvas.setFont('Helvetica', 8)
            canvas.drawString(180,660,'Melee')
            canvas.drawString(215,660,'Light X-bow')
            canvas.drawString(285,660,'Heavy X-bow')
            canvas.drawString(355,660,'Thrown Dagger')
            canvas.drawString(425,660,'Thrown Dart')
            canvas.drawString(495,660,'Other Missiles(not bow)')
            canvas.drawString(180,645,str(S_Att_R[0]))
            canvas.drawString(215,645,str(S_Att_R[1]))
            canvas.drawString(285,645,str(S_Att_R[2]))
            canvas.drawString(355,645,str(S_Att_R[3]))
            canvas.drawString(425,645,str(S_Att_R[4]))
            canvas.drawString(495,645,str(S_Att_R[5]))
            canvas.setFont('Helvetica', 12)
            canvas.drawString(30,625,'Non-Specialist Attacks/Round: ' + str(Att_R))
            canvas.drawString(30,595,'Followers:')
            canvas.setFont('Helvetica', 8)
            canvas.drawString(40,580,'Leader:')
            canvas.drawString(130,580,str(followers[0]))
            canvas.drawString(40,560,'Troops (0th-level):')
            canvas.drawString(130,560,str(followers[1]))
            canvas.drawString(40,540,'Elite Units:')
            canvas.drawString(130,540,str(followers[2]))
            canvas.setFont('Helvetica', 12)
            canvas.line(30,530,580,530)
        
        if 'Mage' in my_class:
            my_xp, wspellsByLevel, school = classData('Wizard', my_level, my_race, scores, my_armor)
            canvas.drawString(30,500,'Wizard Class')
            canvas.drawString(30,470,'Experience Points: ' + str(my_xp))
            canvas.drawString(30,440,'Wizard Spells:')
            canvas.setFont('Helvetica', 8)
            canvas.drawString(120,440,'1st')
            canvas.drawString(140,440,'2nd')
            canvas.drawString(160,440,'3rd')
            canvas.drawString(180,440,'4th')
            canvas.drawString(200,440,'5th')
            canvas.drawString(220,440,'6th')
            canvas.drawString(240,440,'7th')
            canvas.drawString(260,440,'8th')
            canvas.drawString(280,440,'9th')
            canvas.drawString(120,425,str(wspellsByLevel[0]))
            canvas.drawString(140,425,str(wspellsByLevel[1]))
            canvas.drawString(160,425,str(wspellsByLevel[2]))
            canvas.drawString(180,425,str(wspellsByLevel[3]))
            canvas.drawString(200,425,str(wspellsByLevel[4]))
            canvas.drawString(220,425,str(wspellsByLevel[5]))
            canvas.drawString(240,425,str(wspellsByLevel[6]))
            canvas.drawString(260,425,str(wspellsByLevel[7]))
            canvas.drawString(280,425,str(wspellsByLevel[8]))
            canvas.setFont('Helvetica', 12)
            canvas.line(30,370,580,370)
        
        if 'Illusionist' in my_class:
            my_xp, wspellsByLevel, school = classData('Wizard', my_level, my_race, scores, my_armor)
            canvas.drawString(30,500,'Wizard Class')
            canvas.drawString(30,470,'Experience Points: ' + str(my_xp))
            canvas.drawString(30,440,'Wizard Spells:')
            canvas.setFont('Helvetica', 8)
            canvas.drawString(120,440,'1st')
            canvas.drawString(140,440,'2nd')
            canvas.drawString(160,440,'3rd')
            canvas.drawString(180,440,'4th')
            canvas.drawString(200,440,'5th')
            canvas.drawString(220,440,'6th')
            canvas.drawString(240,440,'7th')
            canvas.drawString(260,440,'8th')
            canvas.drawString(280,440,'9th')
            canvas.drawString(120,425,str(wspellsByLevel[0]))
            canvas.drawString(140,425,str(wspellsByLevel[1]))
            canvas.drawString(160,425,str(wspellsByLevel[2]))
            canvas.drawString(180,425,str(wspellsByLevel[3]))
            canvas.drawString(200,425,str(wspellsByLevel[4]))
            canvas.drawString(220,425,str(wspellsByLevel[5]))
            canvas.drawString(240,425,str(wspellsByLevel[6]))
            canvas.drawString(260,425,str(wspellsByLevel[7]))
            canvas.drawString(280,425,str(wspellsByLevel[8]))
            canvas.setFont('Helvetica', 12)
            canvas.drawString(30,400,'Wizard School Specialization: ' + str(school[1]))
            canvas.drawString(30,380,'Opposition School(s): ' + str(school[2]))
            canvas.line(30,370,580,370)

        if 'Cleric' in my_class:
            my_xp, pspellsByLevel, my_Gspheres, my_Mspheres = classData('Cleric', my_level, my_race, scores, my_armor)
            canvas.drawString(30,340,'Cleric Class')
            canvas.drawString(30,310,'Experience Points: ' + str(my_xp))
            canvas.drawString(30,280,'Priest Spells:')
            canvas.setFont('Helvetica', 8)
            canvas.drawString(120,280,'1st')
            canvas.drawString(140,280,'2nd')
            canvas.drawString(160,280,'3rd')
            canvas.drawString(180,280,'4th')
            canvas.drawString(200,280,'5th')
            canvas.drawString(220,280,'6th')
            canvas.drawString(240,280,'7th')
            canvas.drawString(120,265,str(pspellsByLevel[0]))
            canvas.drawString(140,265,str(pspellsByLevel[1]))
            canvas.drawString(160,265,str(pspellsByLevel[2]))
            canvas.drawString(180,265,str(pspellsByLevel[3]))
            canvas.drawString(200,265,str(pspellsByLevel[4]))
            canvas.drawString(220,265,str(pspellsByLevel[5]))
            canvas.drawString(240,265,str(pspellsByLevel[6]))
            canvas.setFont('Helvetica', 12)
            canvas.drawString(30,240,'Greater Spheres:')
            canvas.setFont('Helvetica', 8)
            x1 = 140
            items = 0
            x2 = 140
            x3 = 140
            x4 = 140
            for i in range (0, len(my_Gspheres)):
                if items >= 9:
                    canvas.drawString(x4,195,my_Gspheres[i])
                    x4 += 60
                elif items >= 6:
                    canvas.drawString(x3,210,my_Gspheres[i])
                    x3 += 60
                    items += 1
                elif items >= 3:
                    canvas.drawString(x2,225,my_Gspheres[i])
                    x2 += 60
                    items += 1
                else:
                    canvas.drawString(x1,240,my_Gspheres[i])
                    x1 += 60
                    items += 1
            canvas.setFont('Helvetica', 12)
            canvas.drawString(30,180,'Minor Spheres:')
            canvas.setFont('Helvetica', 8)
            x = 140
            for i in range (0, len(my_Mspheres)):
                canvas.drawString(x,180,my_Mspheres[i])
                x += 60
            canvas.setFont('Helvetica', 12)
            canvas.line(30,170,580,170)

        if 'Druid' in my_class:
            my_xp, pspellsByLevel, my_Gspheres, my_Mspheres = classData('Cleric', my_level, my_race, scores, my_armor)
            canvas.drawString(30,340,'Cleric Class')
            canvas.drawString(30,310,'Experience Points: ' + str(my_xp))
            canvas.drawString(30,280,'Priest Spells:')
            canvas.setFont('Helvetica', 8)
            canvas.drawString(120,280,'1st')
            canvas.drawString(140,280,'2nd')
            canvas.drawString(160,280,'3rd')
            canvas.drawString(180,280,'4th')
            canvas.drawString(200,280,'5th')
            canvas.drawString(220,280,'6th')
            canvas.drawString(240,280,'7th')
            canvas.drawString(120,265,str(pspellsByLevel[0]))
            canvas.drawString(140,265,str(pspellsByLevel[1]))
            canvas.drawString(160,265,str(pspellsByLevel[2]))
            canvas.drawString(180,265,str(pspellsByLevel[3]))
            canvas.drawString(200,265,str(pspellsByLevel[4]))
            canvas.drawString(220,265,str(pspellsByLevel[5]))
            canvas.drawString(240,265,str(pspellsByLevel[6]))
            canvas.setFont('Helvetica', 12)
            canvas.drawString(30,240,'Greater Spheres:')
            canvas.setFont('Helvetica', 8)
            x1 = 140
            items = 0
            x2 = 140
            x3 = 140
            x4 = 140
            for i in range (0, len(my_Gspheres)):
                if items >= 9:
                    canvas.drawString(x4,195,my_Gspheres[i])
                    x4 += 60
                elif items >= 6:
                    canvas.drawString(x3,210,my_Gspheres[i])
                    x3 += 60
                    items += 1
                elif items >= 3:
                    canvas.drawString(x2,225,my_Gspheres[i])
                    x2 += 60
                    items += 1
                else:
                    canvas.drawString(x1,240,my_Gspheres[i])
                    x1 += 60
                    items += 1
            canvas.setFont('Helvetica', 12)
            canvas.drawString(30,180,'Minor Spheres:')
            canvas.setFont('Helvetica', 8)
            x = 140
            for i in range (0, len(my_Mspheres)):
                canvas.drawString(x,180,my_Mspheres[i])
                x += 60
            canvas.setFont('Helvetica', 12)
            canvas.line(30,170,580,170)

        if 'Thief' in my_class:
            my_xp, thief_skills, backstab, followers = classData('Thief', my_level, my_race, scores, my_armor)
            canvas.drawString(30,140,'Thief Class')
            canvas.drawString(30,120,'Experience Points: ' + str(my_xp))
            canvas.drawString(30,100,'Thief Skills:')
            canvas.setFont('Helvetica', 8)
            canvas.drawString(100,90,'Pick Pockets:')
            canvas.drawString(210,90,'Open Locks:')
            canvas.drawString(100,75,'Find/Remove Traps:')
            canvas.drawString(210,75,'Move Silently:')
            canvas.drawString(100,60,'Hide in Shadows:')
            canvas.drawString(210,60,'Detect Noise:')
            canvas.drawString(100,45,'Climb Walls:')
            canvas.drawString(210,45,'Read Languages:')
            canvas.drawString(180,90,str(thief_skills[0]) + '%')
            canvas.drawString(280,90,str(thief_skills[1]) + '%')
            canvas.drawString(180,75,str(thief_skills[2]) + '%')
            canvas.drawString(280,75,str(thief_skills[3]) + '%')
            canvas.drawString(180,60,str(thief_skills[4]) + '%')
            canvas.drawString(280,60,str(thief_skills[5]) + '%')
            canvas.drawString(180,45,str(thief_skills[6]) + '%')
            canvas.drawString(280,45,str(thief_skills[7]) + '%')
            canvas.setFont('Helvetica', 12)
            canvas.drawString(30,30,'Backstab Multiplier: x' + str(backstab))
            canvas.drawString(30,15,'Followers: ' + str(followers))

    if 'Mage' in my_class or 'Illusionist' in my_class or my_class == 'Wizard' or my_class == 'Bard':
        my_spells = getWizardSpells(my_class, school, wspellsByLevel)
        csvWizardSpells(my_spells,my_name)
    
    if 'Cleric' in my_class or 'Druid' in my_class or my_class == 'Priest':
        my_spells = getPriestSpells(pspellsByLevel, my_Gspheres, my_Mspheres, my_class)
        csvPriestSpells(my_spells,my_name)
    elif my_class == 'Ranger':
        my_spells = getPriestSpells(priest_spells, my_Gspheres, my_Mspheres, my_class)
        csvPriestSpells(my_spells,my_name)
    elif my_class == 'Paladin':
        my_spells = getPriestSpells(spellsByLevel, my_Gspheres, my_Mspheres, my_class)
        csvPriestSpells(my_spells,my_name)

    canvas.save()

#######################################
#######################################
def main(argv):

    number = 1
    cRequest = 'F'
    rRequest = 'F'
    lRequest = 1
    my_class = ''
    my_race = ''
    pdf = 'pdf'

    try:
        opts, args = getopt.getopt(argv,"hc:r:l:n:o:")
    except getopt.GetoptError:
        print('2E_character_generator.py -c <class> -r <race> -l <level> -n <number> -o <output>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('2E_character_generator.py -c <class> -r <race> -l <level> -n <number> -o <pdf or con>')
            print('\n\t-o pdf: Print to PDF (default)    con: Print to console')
            print('\n\tClasses are Fighter, Ranger, Wizard, Mage, Priest, Cleric, Druid, Thief, Bard, Paladin,')
            print('\tFighter/Thief, Fighter/Cleric, Fighter/Druid, Fighter/Mage, Fighter/Illusionist,')
            print('\tFighter/Mage/Cleric, Fighter/Mage/Druid, Fighter/Mage/Thief,')
            print('\tCleric/Illusionist, Cleric/Thief, Cleric/Ranger, Cleric/Mage,')
            print('\tIllusionist/Thief, Mage/Thief, or Druid/Mage')
            print('\n\tRaces are Human, Half-Elf, Elf, Dwarf, Half-Orc, Halfling, Gnome')
            print('\n\n\tHalf-Orcs are allowed to be:')
            print('\tFighter, Wizard, Mage, Illusionist, Priest, Cleric,')
            print('\tThief, Fighter/Thief, Fighter/Cleric, Fighter/Mage')
            print('\n\tSee AD&D 2e rules for race/class restrictions\n')
            print('\tDefault setting is to generate 1 random level 1 character\n')
            sys.exit()
        if opt in ("-c"):
            cRequest = arg
        if opt in ("-r"):
            rRequest = arg
        if opt in ("-l"):
            try:
                lRequest = int(arg)
            except ValueError:
                print(arg + ' is not a valid level option. Run 2e_chargen.py -h for help.')
                sys.exit()
        if opt in ("-n"):
            number = int(arg)
        if opt in ("-o"):
            pdf = arg
            if arg != 'pdf' and arg != 'con':
                print(arg + ' is not a valid output option. Run 2e_chargen.py -h for help.')
                sys.exit()

    # Generate requested number of characters
    # Default is 1
    for x in range(0, number):

        # Roll for ability scores
        global scores
        scores = roll(scores)

        # Set character level to request if valid (1-20)
        #  otherwise accept default
        if not 1 <= lRequest < 21:
            print('Character level can only be 1-20')
            sys.exit()


        my_level = lRequest

        # Roll selected class and race if requested
        if cRequest != 'F' and rRequest != 'F':
            if cRequest not in charClass or rRequest not in charRace:
                print(rRequest + ' ' + cRequest + ' is not a valid option. Run 2e_chargen.py -h for help.')
                sys.exit()
            else:
                my_race, scores = certainRace(my_race, scores, rRequest)
                scores = raceAdjust(scores, my_race)
                my_class, my_race, scores = certainClass(cRequest, my_race, scores, cRequest, 0)
            if my_class == 'Villager':
                print(rRequest + ' ' + cRequest + ' is not a valid option. Run 2e_chargen.py -h for help.')
                sys.exit()
        else:
            # Select race randomly unless requested
            if rRequest == 'F':
                my_race = racial(scores)
            elif rRequest in charRace:
                my_race, scores = certainRace(my_race, scores, rRequest)
            else:
                print('Race ' + rRequest + ' is not a valid option. Run 2e_chargen.py -h for help.')
                sys.exit()

            # Select class randomly unless requested
            if cRequest == 'F':
                scores = raceAdjust(scores, my_race)
                my_class = classSelector(scores, my_race)
            elif cRequest in charClass:
                my_class, my_race, scores = certainClass(my_class, my_race, scores, cRequest, 1)
            else:
                print('Class ' + cRequest + ' is not a valid option. Run 2e_chargen.py -h for help.')
                sys.exit()

        if pdf == 'pdf':
            # Print to PDF
            printSheet(my_race, my_class, my_level)
        else:
            # Print to console
            xSTR, scores[0] = rollSTR(scores[0], my_race, my_class)
            my_gender = gender()
            my_height = getHeight(my_race, my_gender)
            my_weight = getWeight(my_race, my_gender)
            my_age = getAge(my_race, my_level)
            my_name = genName(my_gender)
            my_AL = genAL(my_class, my_race)
            my_hp = rollHP(my_class, my_level)
            thac0 = getTHAC0(my_class, my_level)
            my_st = getST(my_class, my_level, my_race, scores[2])
            my_armor = chooseArmor(my_class)
            my_AC = getAC(my_armor)

            # Print name of character
            print('------------------------')
            print(my_name)

            # Print alignment, race, class. and level
            print('\nAlignment: ' + my_AL + ' Gender: ' + my_gender + '  Race: ' + my_race + '  Class: ' + my_class + '  Level: ' + str(my_level))

            # Print height, weight, and age
            print('Height: ' + str(my_height) + ' inches  Weight: ' + str(my_weight) + ' lbs.  Age: ' + str(my_age) + ' years')

            # Print HP and THAC0
            print('\nHP = ' + str(my_hp) + '\tTHAC0 = ' + str(thac0) + '\tAC = ' + str(my_AC) + '\n')


            #print(scores)

            # Print ability scores
            print('_________')
            printScores(scores, xSTR, my_class)
            print('_________')
            
            # Print Saving Throws
            print('\nSaving Throws:')
            print('Paralyzation, Poison, or Death Magic: ' + str(my_st[0]))
            print('Rod, Staff, or Wand: ' + str(my_st[1]))
            print('Petrification or Polymorph: ' + str(my_st[2]))
            print('Breath Weapon: ' + str(my_st[3]))
            print('Spell: ' + str(my_st[4]))

            # Print class-specific data
            printClassData(my_class, my_level, my_race, scores, my_armor)

            print('=======================================\n\n')

        # Reset race and class lists for next iteration
        resetRC()
        my_class = ''
        my_race = ''


#======================================

if __name__ == "__main__":
    main(sys.argv[1:])