#######################################
# AD&D 2nd Edition                    #
# Random Character Generator:         #
#  Priest                             #
#                                     #
# Adds Priest abilities to randomly   #
#  generated character                #
#######################################

import random, re, csv, os

#--------------------------------------
# Return the amount of experience
#  points a character has based on
#  level
#--------------------------------------
def getPriest_XP(my_class, my_level):
    cleric_table = [0,1500,3000,6000,13000,27500,55000,110000,225000,450000,\
        675000,900000,1125000,1350000,1575000,1800000,2025000,2250000,2475000,2700000]
    druid_table = [0,2000,4000,7500,12500,20000,35000,60000,90000,125000,200000,\
        300000,750000,1500000,3000000,3500000,500000,1000000,1500000,2000000]
    
    if my_class == 'Cleric':
        my_xp = cleric_table[my_level - 1]
    else:
        my_xp = druid_table[my_level - 1]

    return my_xp

#--------------------------------------
# Return the casting level and number
#  of priest spells a cleric or druid
#  has based on level and WIS score
#--------------------------------------
def Priest_Spells(my_level, WIS):
    if WIS < 17:
        priest_spell_table = [[1,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,1,0,0,0,0,0],[3,2,0,0,0,0,0],\
        [3,3,1,0,0,0,0],[3,3,2,0,0,0,0],[3,3,2,1,0,0,0],[3,3,3,2,0,0,0],[4,4,3,2,1,0,0],\
        [4,4,3,3,2,0,0],[5,4,4,3,2,0,0],[6,5,5,3,2,0,0],[6,6,6,4,2,0,0],[6,6,6,5,3,0,0],\
        [6,6,6,6,4,0,0],[7,7,7,6,4,0,0],[7,7,7,7,5,0,0],[8,8,8,8,6,0,0],[9,9,8,8,6,0,0],\
        [9,9,9,8,7,0,0]]
    elif WIS < 18:
        priest_spell_table = [[1,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,1,0,0,0,0,0],[3,2,0,0,0,0,0],\
        [3,3,1,0,0,0,0],[3,3,2,0,0,0,0],[3,3,2,1,0,0,0],[3,3,3,2,0,0,0],[4,4,3,2,1,0,0],\
        [4,4,3,3,2,0,0],[5,4,4,3,2,1,0],[6,5,5,3,2,2,0],[6,6,6,4,2,2,0],[6,6,6,5,3,2,0],\
        [6,6,6,6,4,2,0],[7,7,7,6,4,3,0],[7,7,7,7,5,3,0],[8,8,8,8,6,4,0],[9,9,8,8,6,4,0],\
        [9,9,9,8,7,5,0]]
    elif WIS > 17:
        priest_spell_table = [[1,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,1,0,0,0,0,0],[3,2,0,0,0,0,0],\
        [3,3,1,0,0,0,0],[3,3,2,0,0,0,0],[3,3,2,1,0,0,0],[3,3,3,2,0,0,0],[4,4,3,2,1,0,0],\
        [4,4,3,3,2,0,0],[5,4,4,3,2,1,0],[6,5,5,3,2,2,0],[6,6,6,4,2,2,0],[6,6,6,5,3,2,1],\
        [6,6,6,6,4,2,1],[7,7,7,6,4,3,1],[7,7,7,7,5,3,2],[8,8,8,8,6,4,2],[9,9,8,8,6,4,2],\
        [9,9,9,8,7,5,2]]
    
    return priest_spell_table[my_level - 1]

#--------------------------------------
# Randomly generate a specific mythos 
#  for the cleric, including deity, 
#  spheres, weapons allowed, and
#  granted powers
#--------------------------------------
def getMythos():
    deity = ['Agriculture','Blacksmith','Death','Disease','Earth','Healing','Hunt','Lightning',\
        'Love','Nature','Oceans','Peace','Strength','Thunder','War','Wind']
    weapons = [['Bill-guisarme','Flail','Sickle'],['Warhammer'],['Sickle'],['Scourge','Whip'],\
        ['Pick'],['Quarterstaff'],['Composite long bow','Composite short bow','Long bow',\
        'Short bow','Javelin','Sling','Spear'],['Dart','Javelin','Spear'],['Composite long bow',\
        'Composite short bow','Long bow','Short bow'],['Club','Scimitar','Sickle'],['Harpoon',\
        'Spear','Trident'],['Quarterstaff'],['Lucerne hammer','Warhammer'],['Club','Mace','Warhammer'],\
        ['Battle axe','Mace','Morning star','1-handed bastard sword','2-handed bastard sword','Broad sword',\
        'Long sword','Short sword','2-handed sword','Spear'],['Blowgun','Dart']]
    greater_spheres = [['Plant','Sun','Weather','All'],['Creation','Protection','All'],['Necromantic',\
        'Summoning','Combat','All'],['Healing','Charm','All'],['Elemental','Guardian','Protection','All'],\
        ['Healing','Necromantic','Divination','All'],['Animal','Divination','All'],['Elemental','Weather',\
        'Combat','All'],['Healing','Charm','Protection','Necromantic','All'],['Animal','Creation','Plant',\
        'Sun','Weather','All'],['Elemental','Weather','Combat','All'],['Charm','Healing','Sun','Divination',\
        'All'],['Combat','Healing','Protection','All'],['Weather','Combat','Elemental','Guardian','All'],\
        ['Combat','Protection','Summoning','All'],['Elemental','Weather','Animal','All']]
    minor_spheres = [['Healing','Creation'],['Guardian','Elemental','Combat'],['Astral'],['Necromantic','Plant'],\
        ['Creation','Divination'],['Protection','Sun'],['Sun','Combat'],['Protection','Guardian'],['Astral',\
        'Animal'],['Healing'],['Creation','Healing','Summoning'],['Protection','Animal','Plant'],['Sun','Weather'],\
        ['Astral'],['Charm','Divination'],['Healing','Sun']]
    granted_powers = ['Plant Growth (per 4th level Wizard Spell)','Enchant Weapon (per 4th level Wizard Spell)',\
        'Enervation (per 4th level Wizard Spell)','Contagion (per 4th level Wizard Spell)',\
        'Stoneskin (per 4th level Wizard Spell)','Soothing Word, able to remove fear and influence hostile reactions',\
        'Wizard Eye (per 4th level Wizard Spell)','Chain Lightning (per 6th level Wizard Spell)',\
        'Charm or Fascination, which could act as a suggestion spell',\
        'Create Shelter (per 4th level Wizard Spell \"Leomund\'s Secure Shelter\")','Lower or Raise Water (per 6th level Wizard Spell)',\
        'Soothing Word, able to remove fear and influence hostile reactions', 'Wall of Force (per 5th level Wizard Spell)',\
        'Thunderclap, similar to 4th level Wizard spell \"Shout\"','Incite Berserker Rage, adding a +2 bonus to attack and damage rolls',\
        'Cone of Cold (per 5th level Wizard Spell)']

    index = random.randint(0,15)
    my_deity = deity[index]
    my_weapons = weapons[index]
    my_Gspheres = greater_spheres[index]
    my_Mspheres = minor_spheres[index]
    my_Gpower = granted_powers[index]

    return my_deity, my_Gspheres, my_Mspheres, my_Gpower, my_weapons

#--------------------------------------
# Return the spheres of a Cleric,
#  Druid, Paladin, or Ranger
#--------------------------------------
def getSpheres(my_class):
    if my_class == 'Cleric':
        my_Gspheres = ['All','Astral','Charm','Combat','Creation','Divination',\
            'Guardian','Healing','Necromantic','Protection','Summoning','Sun']
        my_Mspheres = ['Elemental']
    elif my_class == 'Druid':
        my_Gspheres = ['All','Animal','Elemental','Healing','Plant','Weather']
        my_Mspheres = ['Divination']
    elif my_class == 'Paladin':
        my_Gspheres = ['Combat','Divination','Healing','Protection']
        my_Mspheres = ['Combat','Divination','Healing','Protection']
    elif my_class == 'Ranger':
        my_Gspheres = ['Plant','Animal']
        my_Mspheres = ['Plant','Animal']
    else:
        my_Gspheres = ['None']
        my_Mspheres = ['None']

    return my_Gspheres, my_Mspheres

#--------------------------------------
# Randomly select spells for a priest
# Select Priest spells
# If Cleric, choose from a given set of spheres
# If Druid or Priest of certain Mythos, select based on their spheres
#   Major sphere access = all spells available, limited by character level
#   Minor sphere access = 1st - 3rd level spells, limited by character level
#--------------------------------------
def getPriestSpells(spellsByLevel, my_Gspheres, my_Mspheres, my_class):
    # Read random spells from PH, stored in priest_spells.csv, put in list
    with open("priest_spells.csv") as f:
        reader = csv.reader(f, delimiter=",")
        spells = list(reader)
    # Randomly select spells from list, minding max number of spells allowed
    #   to memorize, by level, according to sphere access, and store to new list
    my_spells = []
    count = spellsByLevel[0]
    limit = count
    while count > 0: # 1st level spells
        spell_pick = random.randint(1,24)    # 24 possible 1st level spells, pick 1 within spheres  
        if re.sub(r' \([^)]*\)', '', spells[spell_pick][3]) in my_Gspheres or \
            re.sub(r' \([^)]*\)', '', spells[spell_pick][3]) in my_Mspheres:
            if spells[spell_pick] in my_spells: # Don't pick already picked spell
                limit -= 1
                if limit < 0:
                    count = 0
            else:
                my_spells.append(spells[spell_pick])
                count -= 1           
    count = spellsByLevel[1]
    limit = count
    while count > 0: # 2nd level spells
        spell_pick = random.randint(25,52)    # 28 possible 2nd level spells, pick 1 within spheres
        if re.sub(r' \([^)]*\)', '', spells[spell_pick][3]) in my_Gspheres or \
            re.sub(r' \([^)]*\)', '', spells[spell_pick][3]) in my_Mspheres:
            if spells[spell_pick] in my_spells: # Don't pick already picked spell
                limit -= 1
                if limit < 0:
                    count = 0
            else:
                my_spells.append(spells[spell_pick])
                count -= 1 
    count = spellsByLevel[2]
    limit = count
    while count > 0: # 3rd level spells
        spell_pick = random.randint(53,82)    # 30 possible 3rd level spells, pick 1 within spheres
        if re.sub(r' \([^)]*\)', '', spells[spell_pick][3]) in my_Gspheres or \
            re.sub(r' \([^)]*\)', '', spells[spell_pick][3]) in my_Mspheres:
            if spells[spell_pick] in my_spells: # Don't pick already picked spell
                limit -= 1
                if limit < 0:
                    count = 0
            else:
                my_spells.append(spells[spell_pick])
                count -= 1 
    if my_class != 'Ranger':
        count = spellsByLevel[3]
        limit = count
        while count > 0: # 4th level spells
            spell_pick = random.randint(83,107)    # 25 possible 4th level spells, pick 1 within spheres
            if re.sub(r' \([^)]*\)', '', spells[spell_pick][3]) in my_Gspheres:
                if spells[spell_pick] in my_spells: # Don't pick already picked spell
                    limit -= 1
                    if limit < 0:
                        count = 0
                else:
                    my_spells.append(spells[spell_pick])
                    count -= 1                
        if my_class != 'Paladin':
            count = spellsByLevel[4]
            limit = count
            while count > 0: # 5th level spells
                spell_pick = random.randint(108,130)    # 23 possible 5th level spells, pick 1 within spheres
                if re.sub(r' \([^)]*\)', '', spells[spell_pick][3]) in my_Gspheres:
                    if spells[spell_pick] in my_spells: # Don't pick already picked spell
                        limit -= 1
                        if limit < 0:
                            count = 0
                    else:
                        my_spells.append(spells[spell_pick])
                        count -= 1 
            count = spellsByLevel[5]
            limit = count
            while count > 0: # 6th level spells
                spell_pick = random.randint(131,152)    # 22 possible 6th level spells, pick 1 within spheres
                if re.sub(r' \([^)]*\)', '', spells[spell_pick][3]) in my_Gspheres:
                    if spells[spell_pick] in my_spells: # Don't pick already picked spell
                        limit -= 1
                        if limit < 0:
                            count = 0
                    else:
                        my_spells.append(spells[spell_pick])
                        count -= 1 
            count = spellsByLevel[6]
            limit = count
            while count > 0: # 7th level spells
                spell_pick = random.randint(153,174)    # 22 possible 7th level spells, pick 1 within spheres
                if re.sub(r' \([^)]*\)', '', spells[spell_pick][3]) in my_Gspheres:
                    if spells[spell_pick] in my_spells: # Don't pick already picked spell
                        limit -= 1
                        if limit < 0:
                            count = 0
                    else:
                        my_spells.append(spells[spell_pick])
                        count -= 1
                else:
                    limit -= 1
                    if limit < 0:
                        count = 0

    return my_spells

#--------------------------------------
# Print Priest Spells to screen
#--------------------------------------
def printPriestSpells(my_class,my_spells):
    print('\n------------------------\nPriest Spells:\n\n')
    print('1st Level:')
    for i in range(0,len(my_spells)):
        if my_spells[i][0] == '1':
            print('\n\n' + str(my_spells[i][1]))
            print('\n(' + str(my_spells[i][2]) + ')\n')
            print('Sphere: ' + str(my_spells[i][3]))
            print('Range: ' + str(my_spells[i][4]) + '\tComponents: ' + str(my_spells[i][5]))
            print('Duration: ' + str(my_spells[i][6]) + '\tCasting Time: ' +str(my_spells[i][7]))
            print('Area of Effect: ' + str(my_spells[i][8]) + '\tSaving Throw: ' + str(my_spells[i][9]))
            print('\n' + str(my_spells[i][10]))
    print('\n\n2nd Level:')
    for i in range(0,len(my_spells)):
        if my_spells[i][0] == '2':
            print('\n\n' + str(my_spells[i][1]))
            print('\n(' + str(my_spells[i][2]) + ')\n')
            print('Sphere: ' + str(my_spells[i][3]))
            print('Range: ' + str(my_spells[i][4]) + '\tComponents: ' + str(my_spells[i][5]))
            print('Duration: ' + str(my_spells[i][6]) + '\tCasting Time: ' +str(my_spells[i][7]))
            print('Area of Effect: ' + str(my_spells[i][8]) + '\tSaving Throw: ' + str(my_spells[i][9]))
            print('\n' + str(my_spells[i][10]))
    print('\n\n3rd Level:')
    for i in range(0,len(my_spells)):
        if my_spells[i][0] == '3':
            print('\n\n' + str(my_spells[i][1]))
            print('\n(' + str(my_spells[i][2]) + ')\n')
            print('Sphere: ' + str(my_spells[i][3]))
            print('Range: ' + str(my_spells[i][4]) + '\tComponents: ' + str(my_spells[i][5]))
            print('Duration: ' + str(my_spells[i][6]) + '\tCasting Time: ' +str(my_spells[i][7]))
            print('Area of Effect: ' + str(my_spells[i][8]) + '\tSaving Throw: ' + str(my_spells[i][9]))
            print('\n' + str(my_spells[i][10]))
    if my_class != 'Ranger':
        print('\n\n4th Level:')
        for i in range(0,len(my_spells)):
            if my_spells[i][0] == '4':
                print('\n\n' + str(my_spells[i][1]))
                print('\n(' + str(my_spells[i][2]) + ')\n')
                print('Sphere: ' + str(my_spells[i][3]))
                print('Range: ' + str(my_spells[i][4]) + '\tComponents: ' + str(my_spells[i][5]))
                print('Duration: ' + str(my_spells[i][6]) + '\tCasting Time: ' +str(my_spells[i][7]))
                print('Area of Effect: ' + str(my_spells[i][8]) + '\tSaving Throw: ' + str(my_spells[i][9]))
                print('\n' + str(my_spells[i][10]))
        if my_class != 'Paladin':
            print('\n\n5th Level:')
            for i in range(0,len(my_spells)):
                if my_spells[i][0] == '5':
                    print('\n\n' + str(my_spells[i][1]))
                    print('\n(' + str(my_spells[i][2]) + ')\n')
                    print('Sphere: ' + str(my_spells[i][3]))
                    print('Range: ' + str(my_spells[i][4]) + '\tComponents: ' + str(my_spells[i][5]))
                    print('Duration: ' + str(my_spells[i][6]) + '\tCasting Time: ' +str(my_spells[i][7]))
                    print('Area of Effect: ' + str(my_spells[i][8]) + '\tSaving Throw: ' + str(my_spells[i][9]))
                    print('\n' + str(my_spells[i][10]))
            print('\n\n6th Level:')
            for i in range(0,len(my_spells)):
                if my_spells[i][0] == '6':
                    print('\n\n' + str(my_spells[i][1]))
                    print('\n(' + str(my_spells[i][2]) + ')\n')
                    print('Sphere: ' + str(my_spells[i][3]))
                    print('Range: ' + str(my_spells[i][4]) + '\tComponents: ' + str(my_spells[i][5]))
                    print('Duration: ' + str(my_spells[i][6]) + '\tCasting Time: ' +str(my_spells[i][7]))
                    print('Area of Effect: ' + str(my_spells[i][8]) + '\tSaving Throw: ' + str(my_spells[i][9]))
                    print('\n' + str(my_spells[i][10]))
            print('\n\n7th Level:')
            for i in range(0,len(my_spells)):
                if my_spells[i][0] == '7':
                    print('\n\n' + str(my_spells[i][1]))
                    print('\n(' + str(my_spells[i][2]) + ')\n')
                    print('Sphere: ' + str(my_spells[i][3]))
                    print('Range: ' + str(my_spells[i][4]) + '\tComponents: ' + str(my_spells[i][5]))
                    print('Duration: ' + str(my_spells[i][6]) + '\tCasting Time: ' +str(my_spells[i][7]))
                    print('Area of Effect: ' + str(my_spells[i][8]) + '\tSaving Throw: ' + str(my_spells[i][9]))
                    print('\n' + str(my_spells[i][10]))

    print('\n\n')

#--------------------------------------
# Print Priest Spells to CSV
#--------------------------------------
def csvPriestSpells(my_spells,my_name):

    # Print spell list to character sheet directory
    my_dir = '2E_Character_Sheets'
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, my_dir)
    try:
        os.makedirs(path, exist_ok= True)
    except OSError as error:
        print("Directory '%s' can not be created.\n" % my_dir)

    name2 = os.path.join(path, my_name)

    with open(name2 + '_Priest_Spell_List.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Level","Name","School","Sphere","Range","Components","Duration","Casting Time",\
            "Area of Effect","Saving Throw","Description"])
        writer.writerows(my_spells)
