#######################################
# AD&D 2nd Edition                    #
# Random Character Generator:         #
#  Non-Weapon Proficiencies           #
#                                     #
# Adds NWPs to randomly               #
#  generated character                #
#######################################

import random

#--------------------------------------
# Search a 2D list for a value
#--------------------------------------
def in_List(my_list, value):
    for row in my_list:
        if value in row:
            return True
    return False

#--------------------------------------
# Randomly select nonweapon profs
#--------------------------------------
def selectNWP(my_class, nwprofs):
    my_nwprofs = []
    general_nwp = [['Agriculture',1,'INT','+0'],['Animal Handling',1,'WIS','-1'],\
        ['Animal Training',1,'WIS','+0'],['Artistic Ability',1,'WIS','+0'],['Blacksmithing',1,'STR','+0'],\
        ['Brewing',1,'INT','+0'],['Carpentry',1,'STR','+0'],['Cobbling',1,'DEX','+0'],['Cooking',1,'INT','+0'],\
        ['Dancing',1,'DEX','+0'],['Direction Sense',1,'WIS','+1'],['Etiquette',1,'CHA','+0'],['Fire-building',1,'WIS','-1'],\
        ['Fishing',1,'WIS','-1'],['Heraldry',1,'INT','+0'],['Languages, Modern',1,'INT','+0'],['Leatherworking',1,'INT','+0'],\
        ['Mining',2,'WIS','-3'],['Pottery',1,'DEX','-2'],['Riding, Airborne',2,'WIS','-2'],['Riding, Land-based',1,'WIS','+3'],\
        ['Rope Use',1,'DEX','+0'],['Seamanship',1,'DEX','+1'],['Seamstress/Tailor',1,'DEX','-1'],['Singing',1,'CHA','+0'],\
        ['Stonemasonry',1,'STR','-2'],['Swimming',1,'STR','+0'],['Weather Sense',1,'WIS','-1'],['Weaving',1,'INT','-1']]
    priest_nwp = [['Ancient History',1,'INT',-1],['Astrology',2,'INT',0],['Engineering',2,'INT',-3],\
        ['Healing',2,'WIS',-2],['Herbalism',2,'INT',-2],['Languages, Ancient',1,'INT',0],['Local History',1,'CHA',0],\
        ['Musical Instrument',1,'DEX',-1],['Navigation',1,'INT',-2],['Reading/Writing',1,'INT',1],['Religion',1,'WIS',0],\
        ['Spellcraft',1,'INT',-2]]
    rogue_nwp = [['Ancient History',1,'INT',-1],['Appraising',1,'INT',0],['Blind-fighting',2,'N/A','N/A'],\
        ['Disguise',1,'CHA',-1],['Forgery',1,'DEX',-1],['Gaming',1,'CHA',0],['Gem Cutting',2,'DEX',-2],['Juggling',1,'DEX',-1],\
        ['Jumping',1,'STR',0],['Local History',1,'CHA',0],['Musical Instrument',1,'DEX',-1],['Reading Lips',2,'INT',-2],\
        ['Set Snares',1,'DEX',-1],['Tightrope Walking',1,'DEX',0],['Tumbling',1,'DEX',0],['Ventriloquism',1,'INT',-2]]
    warrior_nwp = [['Animal Lore',1,'INT','+0'],['Armorer',2,'INT','-1'],['Blind-fighting',2,'N/A','N/A'],\
        ['Bowyer/Fletcher',1,'DEX','-1'],['Charioteering',1,'DEX','+2'],['Endurance',2,'CON','+0'],['Gaming',1,'CHA','+0'],\
        ['Hunting',1,'WIS','-1'],['Mountaineering',1,'N/A','N/A'],['Navigation',1,'INT','-2'],['Running',1,'CON','-6'],\
        ['Set Snares',1,'INT','-1'],['Survival',2,'INT','+0'],['Tracking',2,'WIS','+0'],['Weaponsmithing',3,'INT','-3']]
    wizard_nwp = [['Ancient History',1,'INT',-1],['Astrology',2,'INT',0],['Engineering',2,'INT',-3],['Gem Cutting',2,'DEX',-2],\
        ['Herbalism',2,'INT',-2],['Languages, Ancient',1,'INT',0],['Navigation',1,'INT',-2],['Reading/Writing',1,'INT',1],\
        ['Religion',1,'WIS',0],['Spellcraft',1,'INT',-2]]
    
    if my_class == 'Thief':
        # Pick from Rogue and General NWPs
        #  until all currently available NWP slots are full
        while nwprofs > 0:
            group = random.randint(1,2)
            if group == 1:   # Rogue NWP
                if len(rogue_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(rogue_nwp, 1):
                            prof_pick = random.randint(0,len(rogue_nwp)-1)
                            my_nwprofs.append(rogue_nwp[prof_pick])
                            nwprofs -= rogue_nwp[prof_pick][1]
                            rogue_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(rogue_nwp)-1)
                        while nwprofs - rogue_nwp[prof_pick][1] < 0:
                            if len(rogue_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(rogue_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(rogue_nwp[prof_pick])
                        nwprofs -= rogue_nwp[prof_pick][1]
                        rogue_nwp.pop(prof_pick)
            else:   # General NWP
                if len(general_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(general_nwp, 1):
                            prof_pick = random.randint(0,len(general_nwp)-1)
                            my_nwprofs.append(general_nwp[prof_pick])
                            nwprofs -= general_nwp[prof_pick][1]
                            general_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(general_nwp)-1)
                        while nwprofs - general_nwp[prof_pick][1] < 0:
                            if len(general_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(general_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(general_nwp[prof_pick])
                        nwprofs -= general_nwp[prof_pick][1]
                        general_nwp.pop(prof_pick)
    elif my_class == 'Bard':
        # Pick from Rogue, Warrior, Wizard, and General NWPs
        #  until all currently available NWP slots are full
        while nwprofs > 0:
            group = random.randint(1,4)
            if group == 1:   # Rogue NWP
                if len(rogue_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(rogue_nwp, 1):
                            prof_pick = random.randint(0,len(rogue_nwp)-1)
                            my_nwprofs.append(rogue_nwp[prof_pick])
                            nwprofs -= rogue_nwp[prof_pick][1]
                            rogue_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(rogue_nwp)-1)
                        while nwprofs - rogue_nwp[prof_pick][1] < 0:
                            if len(rogue_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(rogue_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(rogue_nwp[prof_pick])
                        nwprofs -= rogue_nwp[prof_pick][1]
                        rogue_nwp.pop(prof_pick)
            if group == 2:   # Warrior NWP
                if len(warrior_nwp) > 0:    # NWP list is not empty
                    if nwprofs == 1:        # Only 1 NWP slot left
                        if in_List(warrior_nwp, 1):
                            prof_pick = random.randint(0,len(warrior_nwp)-1)
                            my_nwprofs.append(warrior_nwp[prof_pick])
                            nwprofs -= warrior_nwp[prof_pick][1]
                            warrior_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(warrior_nwp)-1)
                        while nwprofs - warrior_nwp[prof_pick][1] < 0:
                            if len(warrior_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(warrior_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(warrior_nwp[prof_pick])
                        nwprofs -= warrior_nwp[prof_pick][1]
                        warrior_nwp.pop(prof_pick)
            if group == 3:   # Wizard NWP
                if len(wizard_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(wizard_nwp, 1):
                            prof_pick = random.randint(0,len(wizard_nwp)-1)
                            my_nwprofs.append(wizard_nwp[prof_pick])
                            nwprofs -= wizard_nwp[prof_pick][1]
                            wizard_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(wizard_nwp)-1)
                        while nwprofs - wizard_nwp[prof_pick][1] < 0:
                            if len(wizard_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(wizard_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(wizard_nwp[prof_pick])
                        nwprofs -= wizard_nwp[prof_pick][1]
                        wizard_nwp.pop(prof_pick)
            else:   # General NWP
                if len(general_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(general_nwp, 1):
                            prof_pick = random.randint(0,len(general_nwp)-1)
                            my_nwprofs.append(general_nwp[prof_pick])
                            nwprofs -= general_nwp[prof_pick][1]
                            general_nwp.pop(prof_pick)
                    elif nwprofs > 1:
                        prof_pick = random.randint(0,len(general_nwp)-1)
                        while nwprofs - general_nwp[prof_pick][1] < 0:
                            if len(general_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(general_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(general_nwp[prof_pick])
                        nwprofs -= general_nwp[prof_pick][1]
                        general_nwp.pop(prof_pick)
    elif my_class == 'Wizard' or my_class == 'Mage' or my_class == 'Illusionist':
        # Pick from Wizard and General NWPs
        #  until all currently available NWP slots are full
        while nwprofs > 0:
            group = random.randint(1,2)
            if group == 1:   # Wizard NWP
                if len(wizard_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(wizard_nwp, 1):
                            prof_pick = random.randint(0,len(wizard_nwp)-1)
                            my_nwprofs.append(wizard_nwp[prof_pick])
                            nwprofs -= wizard_nwp[prof_pick][1]
                            wizard_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(wizard_nwp)-1)
                        while nwprofs - wizard_nwp[prof_pick][1] < 0:
                            if len(wizard_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(wizard_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(wizard_nwp[prof_pick])
                        nwprofs -= wizard_nwp[prof_pick][1]
                        wizard_nwp.pop(prof_pick)
            else:   # General NWP
                if len(general_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(general_nwp, 1):
                            prof_pick = random.randint(0,len(general_nwp)-1)
                            my_nwprofs.append(general_nwp[prof_pick])
                            nwprofs -= general_nwp[prof_pick][1]
                            general_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(general_nwp)-1)
                        while nwprofs - general_nwp[prof_pick][1] < 0:
                            if len(general_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(general_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(general_nwp[prof_pick])
                        nwprofs -= general_nwp[prof_pick][1]
                        general_nwp.pop(prof_pick)
    elif my_class == 'Druid':
        # Pick from Priest, Warrior, and General NWPs
        #  until all currently available NWP slots are full
        while nwprofs > 0:
            group = random.randint(1,3)
            if group == 1:   # Warrior NWP
                if len(warrior_nwp) > 0:    # NWP list is not empty
                    if nwprofs == 1:        # Only 1 NWP slot left
                        if in_List(warrior_nwp, 1):
                            prof_pick = random.randint(0,len(warrior_nwp)-1)
                            my_nwprofs.append(warrior_nwp[prof_pick])
                            nwprofs -= warrior_nwp[prof_pick][1]
                            warrior_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(warrior_nwp)-1)
                        while nwprofs - warrior_nwp[prof_pick][1] < 0:
                            if len(warrior_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(warrior_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(warrior_nwp[prof_pick])
                        nwprofs -= warrior_nwp[prof_pick][1]
                        warrior_nwp.pop(prof_pick)
            elif group == 2:   # Priest NWP
                if len(priest_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(priest_nwp, 1):
                            prof_pick = random.randint(0,len(priest_nwp)-1)
                            my_nwprofs.append(priest_nwp[prof_pick])
                            nwprofs -= priest_nwp[prof_pick][1]
                            priest_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(priest_nwp)-1)
                        while nwprofs - priest_nwp[prof_pick][1] < 0:
                            if len(priest_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(priest_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(priest_nwp[prof_pick])
                        nwprofs -= priest_nwp[prof_pick][1]
                        priest_nwp.pop(prof_pick)
            else:   # General NWP
                if len(general_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(general_nwp, 1):
                            prof_pick = random.randint(0,len(general_nwp)-1)
                            my_nwprofs.append(general_nwp[prof_pick])
                            nwprofs -= general_nwp[prof_pick][1]
                            general_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(general_nwp)-1)
                        while nwprofs - general_nwp[prof_pick][1] < 0:
                            if len(general_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(general_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(general_nwp[prof_pick])
                        nwprofs -= general_nwp[prof_pick][1]
                        general_nwp.pop(prof_pick)
    elif my_class == 'Cleric' or my_class == 'Priest':
        # Pick from Priest and General NWPs
        #  until all currently available NWP slots are full
        while nwprofs > 0:
            group = random.randint(1,2)
            if group == 1:   # Priest NWP
                if len(priest_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(priest_nwp, 1):
                            prof_pick = random.randint(0,len(priest_nwp)-1)
                            my_nwprofs.append(priest_nwp[prof_pick])
                            nwprofs -= priest_nwp[prof_pick][1]
                            priest_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(priest_nwp)-1)
                        while nwprofs - priest_nwp[prof_pick][1] < 0:
                            if len(priest_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(priest_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(priest_nwp[prof_pick])
                        nwprofs -= priest_nwp[prof_pick][1]
                        priest_nwp.pop(prof_pick)
            else:   # General NWP
                if len(general_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(general_nwp, 1):
                            prof_pick = random.randint(0,len(general_nwp)-1)
                            my_nwprofs.append(general_nwp[prof_pick])
                            nwprofs -= general_nwp[prof_pick][1]
                            general_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(general_nwp)-1)
                        while nwprofs - general_nwp[prof_pick][1] < 0:
                            if len(general_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(general_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(general_nwp[prof_pick])
                        nwprofs -= general_nwp[prof_pick][1]
                        general_nwp.pop(prof_pick)
    elif my_class == 'Ranger':
        # Pick from Warrior, Wizard, and General NWPs
        #  until all currently available NWP slots are full
        while nwprofs > 0:
            group = random.randint(1,3)
            if group == 1:   # Warrior NWP
                if len(warrior_nwp) > 0:    # NWP list is not empty
                    if nwprofs == 1:        # Only 1 NWP slot left
                        if in_List(warrior_nwp, 1):
                            prof_pick = random.randint(0,len(warrior_nwp)-1)
                            my_nwprofs.append(warrior_nwp[prof_pick])
                            nwprofs -= warrior_nwp[prof_pick][1]
                            warrior_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(warrior_nwp)-1)
                        while nwprofs - warrior_nwp[prof_pick][1] < 0:
                            if len(warrior_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(warrior_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(warrior_nwp[prof_pick])
                        nwprofs -= warrior_nwp[prof_pick][1]
                        warrior_nwp.pop(prof_pick)
            elif group == 2:   # Wizard NWP
                if len(wizard_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(wizard_nwp, 1):
                            prof_pick = random.randint(0,len(wizard_nwp)-1)
                            my_nwprofs.append(wizard_nwp[prof_pick])
                            nwprofs -= wizard_nwp[prof_pick][1]
                            wizard_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(wizard_nwp)-1)
                        while nwprofs - wizard_nwp[prof_pick][1] < 0:
                            if len(wizard_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(wizard_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(wizard_nwp[prof_pick])
                        nwprofs -= wizard_nwp[prof_pick][1]
                        wizard_nwp.pop(prof_pick)
            else:   # General NWP
                if len(general_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(general_nwp, 1):
                            prof_pick = random.randint(0,len(general_nwp)-1)
                            my_nwprofs.append(general_nwp[prof_pick])
                            nwprofs -= general_nwp[prof_pick][1]
                            general_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(general_nwp)-1)
                        while nwprofs - general_nwp[prof_pick][1] < 0:
                            if len(general_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(general_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(general_nwp[prof_pick])
                        nwprofs -= general_nwp[prof_pick][1]
                        general_nwp.pop(prof_pick)
    elif my_class == 'Paladin':
        # Pick from Warrior, Priest, and General NWPs
        #  until all currently available NWP slots are full
        while nwprofs > 0:
            group = random.randint(1,3)
            if group == 1:   # Warrior NWP
                if len(warrior_nwp) > 0:    # NWP list is not empty
                    if nwprofs == 1:        # Only 1 NWP slot left
                        if in_List(warrior_nwp, 1):
                            prof_pick = random.randint(0,len(warrior_nwp)-1)
                            my_nwprofs.append(warrior_nwp[prof_pick])
                            nwprofs -= warrior_nwp[prof_pick][1]
                            warrior_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(warrior_nwp)-1)
                        while nwprofs - warrior_nwp[prof_pick][1] < 0:
                            if len(warrior_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(warrior_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(warrior_nwp[prof_pick])
                        nwprofs -= warrior_nwp[prof_pick][1]
                        warrior_nwp.pop(prof_pick)
            elif group == 2:   # Priest NWP
                if len(priest_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(priest_nwp, 1):
                            prof_pick = random.randint(0,len(priest_nwp)-1)
                            my_nwprofs.append(priest_nwp[prof_pick])
                            nwprofs -= priest_nwp[prof_pick][1]
                            priest_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(priest_nwp)-1)
                        while nwprofs - priest_nwp[prof_pick][1] < 0:
                            if len(priest_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(priest_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(priest_nwp[prof_pick])
                        nwprofs -= priest_nwp[prof_pick][1]
                        priest_nwp.pop(prof_pick)
            else:   # General NWP
                if len(general_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(general_nwp, 1):
                            prof_pick = random.randint(0,len(general_nwp)-1)
                            my_nwprofs.append(general_nwp[prof_pick])
                            nwprofs -= general_nwp[prof_pick][1]
                            general_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(general_nwp)-1)
                        while nwprofs - general_nwp[prof_pick][1] < 0:
                            if len(general_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(general_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(general_nwp[prof_pick])
                        nwprofs -= general_nwp[prof_pick][1]
                        general_nwp.pop(prof_pick)
    elif my_class == 'Fighter':
        # Pick from Warrior and General NWPs
        #  until all currently available NWP slots are full
        while nwprofs > 0:
            group = random.randint(1,2)
            if group == 1:   # Warrior NWP
                if len(warrior_nwp) > 0:    # NWP list is not empty
                    if nwprofs == 1:        # Only 1 NWP slot left
                        if in_List(warrior_nwp, 1):
                            prof_pick = random.randint(0,len(warrior_nwp)-1)
                            my_nwprofs.append(warrior_nwp[prof_pick])
                            nwprofs -= warrior_nwp[prof_pick][1]
                            warrior_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(warrior_nwp)-1)
                        while nwprofs - warrior_nwp[prof_pick][1] < 0:
                            if len(warrior_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(warrior_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(warrior_nwp[prof_pick])
                        nwprofs -= warrior_nwp[prof_pick][1]
                        warrior_nwp.pop(prof_pick)
            else:   # General NWP
                if len(general_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(general_nwp, 1):
                            prof_pick = random.randint(0,len(general_nwp)-1)
                            my_nwprofs.append(general_nwp[prof_pick])
                            nwprofs -= general_nwp[prof_pick][1]
                            general_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(general_nwp)-1)
                        while nwprofs - general_nwp[prof_pick][1] < 0:
                            if len(general_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(general_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(general_nwp[prof_pick])
                        nwprofs -= general_nwp[prof_pick][1]
                        general_nwp.pop(prof_pick)
    elif my_class == 'Fighter/Thief':
        # Pick from Warrior, Rogue, and General NWPs
        #  until all currently available NWP slots are full
        while nwprofs > 0:
            group = random.randint(1,3)
            if group == 1:   # Warrior NWP
                if len(warrior_nwp) > 0:    # NWP list is not empty
                    if nwprofs == 1:        # Only 1 NWP slot left
                        if in_List(warrior_nwp, 1):
                            prof_pick = random.randint(0,len(warrior_nwp)-1)
                            my_nwprofs.append(warrior_nwp[prof_pick])
                            nwprofs -= warrior_nwp[prof_pick][1]
                            warrior_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(warrior_nwp)-1)
                        while nwprofs - warrior_nwp[prof_pick][1] < 0:
                            if len(warrior_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(warrior_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(warrior_nwp[prof_pick])
                        nwprofs -= warrior_nwp[prof_pick][1]
                        warrior_nwp.pop(prof_pick)
            elif group == 2:   # Rogue NWP
                if len(rogue_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(rogue_nwp, 1):
                            prof_pick = random.randint(0,len(rogue_nwp)-1)
                            my_nwprofs.append(rogue_nwp[prof_pick])
                            nwprofs -= rogue_nwp[prof_pick][1]
                            rogue_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(rogue_nwp)-1)
                        while nwprofs - rogue_nwp[prof_pick][1] < 0:
                            if len(rogue_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(rogue_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(rogue_nwp[prof_pick])
                        nwprofs -= rogue_nwp[prof_pick][1]
                        rogue_nwp.pop(prof_pick)
            else:   # General NWP
                if len(general_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(general_nwp, 1):
                            prof_pick = random.randint(0,len(general_nwp)-1)
                            my_nwprofs.append(general_nwp[prof_pick])
                            nwprofs -= general_nwp[prof_pick][1]
                            general_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(general_nwp)-1)
                        while nwprofs - general_nwp[prof_pick][1] < 0:
                            if len(general_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(general_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(general_nwp[prof_pick])
                        nwprofs -= general_nwp[prof_pick][1]
                        general_nwp.pop(prof_pick)
    elif my_class == 'Fighter/Cleric' or my_class == 'Fighter/Druid':
        # Pick from Warrior, Priest, and General NWPs
        #  until all currently available NWP slots are full
        while nwprofs > 0:
            group = random.randint(1,3)
            if group == 1:   # Warrior NWP
                if len(warrior_nwp) > 0:    # NWP list is not empty
                    if nwprofs == 1:        # Only 1 NWP slot left
                        if in_List(warrior_nwp, 1):
                            prof_pick = random.randint(0,len(warrior_nwp)-1)
                            my_nwprofs.append(warrior_nwp[prof_pick])
                            nwprofs -= warrior_nwp[prof_pick][1]
                            warrior_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(warrior_nwp)-1)
                        while nwprofs - warrior_nwp[prof_pick][1] < 0:
                            if len(warrior_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(warrior_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(warrior_nwp[prof_pick])
                        nwprofs -= warrior_nwp[prof_pick][1]
                        warrior_nwp.pop(prof_pick)
            elif group == 2:   # Priest NWP
                if len(priest_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(priest_nwp, 1):
                            prof_pick = random.randint(0,len(priest_nwp)-1)
                            my_nwprofs.append(priest_nwp[prof_pick])
                            nwprofs -= priest_nwp[prof_pick][1]
                            priest_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(priest_nwp)-1)
                        while nwprofs - priest_nwp[prof_pick][1] < 0:
                            if len(priest_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(priest_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(priest_nwp[prof_pick])
                        nwprofs -= priest_nwp[prof_pick][1]
                        priest_nwp.pop(prof_pick)
            else:   # General NWP
                if len(general_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(general_nwp, 1):
                            prof_pick = random.randint(0,len(general_nwp)-1)
                            my_nwprofs.append(general_nwp[prof_pick])
                            nwprofs -= general_nwp[prof_pick][1]
                            general_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(general_nwp)-1)
                        while nwprofs - general_nwp[prof_pick][1] < 0:
                            if len(general_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(general_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(general_nwp[prof_pick])
                        nwprofs -= general_nwp[prof_pick][1]
                        general_nwp.pop(prof_pick)
    elif my_class == 'Fighter/Mage' or my_class == 'Fighter/Illusionist':
        # Pick from Warrior, Wizard, and General NWPs
        #  until all currently available NWP slots are full
        while nwprofs > 0:
            group = random.randint(1,3)
            if group == 1:   # Warrior NWP
                if len(warrior_nwp) > 0:    # NWP list is not empty
                    if nwprofs == 1:        # Only 1 NWP slot left
                        if in_List(warrior_nwp, 1):
                            prof_pick = random.randint(0,len(warrior_nwp)-1)
                            my_nwprofs.append(warrior_nwp[prof_pick])
                            nwprofs -= warrior_nwp[prof_pick][1]
                            warrior_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(warrior_nwp)-1)
                        while nwprofs - warrior_nwp[prof_pick][1] < 0:
                            if len(warrior_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(warrior_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(warrior_nwp[prof_pick])
                        nwprofs -= warrior_nwp[prof_pick][1]
                        warrior_nwp.pop(prof_pick)
            elif group == 2:   # Wizard NWP
                if len(wizard_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(wizard_nwp, 1):
                            prof_pick = random.randint(0,len(wizard_nwp)-1)
                            my_nwprofs.append(wizard_nwp[prof_pick])
                            nwprofs -= wizard_nwp[prof_pick][1]
                            wizard_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(wizard_nwp)-1)
                        while nwprofs - wizard_nwp[prof_pick][1] < 0:
                            if len(wizard_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(wizard_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(wizard_nwp[prof_pick])
                        nwprofs -= wizard_nwp[prof_pick][1]
                        wizard_nwp.pop(prof_pick)
            else:   # General NWP
                if len(general_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(general_nwp, 1):
                            prof_pick = random.randint(0,len(general_nwp)-1)
                            my_nwprofs.append(general_nwp[prof_pick])
                            nwprofs -= general_nwp[prof_pick][1]
                            general_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(general_nwp)-1)
                        while nwprofs - general_nwp[prof_pick][1] < 0:
                            if len(general_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(general_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(general_nwp[prof_pick])
                        nwprofs -= general_nwp[prof_pick][1]
                        general_nwp.pop(prof_pick)
    elif my_class == 'Mage/Thief' or my_class == 'Illusionist/Thief':
        # Pick from Rogue, Wizard, and General NWPs
        #  until all currently available NWP slots are full
        while nwprofs > 0:
            group = random.randint(1,3)
            if group == 1:   # Rogue NWP
                if len(rogue_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(rogue_nwp, 1):
                            prof_pick = random.randint(0,len(rogue_nwp)-1)
                            my_nwprofs.append(rogue_nwp[prof_pick])
                            nwprofs -= rogue_nwp[prof_pick][1]
                            rogue_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(rogue_nwp)-1)
                        while nwprofs - rogue_nwp[prof_pick][1] < 0:
                            if len(rogue_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(rogue_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(rogue_nwp[prof_pick])
                        nwprofs -= rogue_nwp[prof_pick][1]
                        rogue_nwp.pop(prof_pick)
            elif group == 2:   # Wizard NWP
                if len(wizard_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(wizard_nwp, 1):
                            prof_pick = random.randint(0,len(wizard_nwp)-1)
                            my_nwprofs.append(wizard_nwp[prof_pick])
                            nwprofs -= wizard_nwp[prof_pick][1]
                            wizard_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(wizard_nwp)-1)
                        while nwprofs - wizard_nwp[prof_pick][1] < 0:
                            if len(wizard_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(wizard_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(wizard_nwp[prof_pick])
                        nwprofs -= wizard_nwp[prof_pick][1]
                        wizard_nwp.pop(prof_pick)
            else:   # General NWP
                if len(general_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(general_nwp, 1):
                            prof_pick = random.randint(0,len(general_nwp)-1)
                            my_nwprofs.append(general_nwp[prof_pick])
                            nwprofs -= general_nwp[prof_pick][1]
                            general_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(general_nwp)-1)
                        while nwprofs - general_nwp[prof_pick][1] < 0:
                            if len(general_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(general_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(general_nwp[prof_pick])
                        nwprofs -= general_nwp[prof_pick][1]
                        general_nwp.pop(prof_pick)
    elif my_class == 'Cleric/Mage' or my_class == 'Cleric/Illusionist' or my_class == 'Cleric/Ranger':
        # Pick from Priest, Wizard, and General NWPs
        #  until all currently available NWP slots are full
        while nwprofs > 0:
            group = random.randint(1,3)
            if group == 1:   # Priest NWP
                if len(priest_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(priest_nwp, 1):
                            prof_pick = random.randint(0,len(priest_nwp)-1)
                            my_nwprofs.append(priest_nwp[prof_pick])
                            nwprofs -= priest_nwp[prof_pick][1]
                            priest_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(priest_nwp)-1)
                        while nwprofs - priest_nwp[prof_pick][1] < 0:
                            if len(priest_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(priest_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(priest_nwp[prof_pick])
                        nwprofs -= priest_nwp[prof_pick][1]
                        priest_nwp.pop(prof_pick)
            elif group == 2:   # Wizard NWP
                if len(wizard_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(wizard_nwp, 1):
                            prof_pick = random.randint(0,len(wizard_nwp)-1)
                            my_nwprofs.append(wizard_nwp[prof_pick])
                            nwprofs -= wizard_nwp[prof_pick][1]
                            wizard_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(wizard_nwp)-1)
                        while nwprofs - wizard_nwp[prof_pick][1] < 0:
                            if len(wizard_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(wizard_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(wizard_nwp[prof_pick])
                        nwprofs -= wizard_nwp[prof_pick][1]
                        wizard_nwp.pop(prof_pick)
            else:   # General NWP
                if len(general_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(general_nwp, 1):
                            prof_pick = random.randint(0,len(general_nwp)-1)
                            my_nwprofs.append(general_nwp[prof_pick])
                            nwprofs -= general_nwp[prof_pick][1]
                            general_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(general_nwp)-1)
                        while nwprofs - general_nwp[prof_pick][1] < 0:
                            if len(general_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(general_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(general_nwp[prof_pick])
                        nwprofs -= general_nwp[prof_pick][1]
                        general_nwp.pop(prof_pick)
    elif my_class == 'Cleric/Thief':
        # Pick from Priest, Rogue, and General NWPs
        #  until all currently available NWP slots are full
        while nwprofs > 0:
            group = random.randint(1,3)
            if group == 1:   # Priest NWP
                if len(priest_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(priest_nwp, 1):
                            prof_pick = random.randint(0,len(priest_nwp)-1)
                            my_nwprofs.append(priest_nwp[prof_pick])
                            nwprofs -= priest_nwp[prof_pick][1]
                            priest_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(priest_nwp)-1)
                        while nwprofs - priest_nwp[prof_pick][1] < 0:
                            if len(priest_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(priest_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(priest_nwp[prof_pick])
                        nwprofs -= priest_nwp[prof_pick][1]
                        priest_nwp.pop(prof_pick)
            elif group == 2:   # Rogue NWP
                if len(rogue_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(rogue_nwp, 1):
                            prof_pick = random.randint(0,len(rogue_nwp)-1)
                            my_nwprofs.append(rogue_nwp[prof_pick])
                            nwprofs -= rogue_nwp[prof_pick][1]
                            rogue_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(rogue_nwp)-1)
                        while nwprofs - rogue_nwp[prof_pick][1] < 0:
                            if len(rogue_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(rogue_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(rogue_nwp[prof_pick])
                        nwprofs -= rogue_nwp[prof_pick][1]
                        rogue_nwp.pop(prof_pick)
            else:   # General NWP
                if len(general_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(general_nwp, 1):
                            prof_pick = random.randint(0,len(general_nwp)-1)
                            my_nwprofs.append(general_nwp[prof_pick])
                            nwprofs -= general_nwp[prof_pick][1]
                            general_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(general_nwp)-1)
                        while nwprofs - general_nwp[prof_pick][1] < 0:
                            if len(general_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(general_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(general_nwp[prof_pick])
                        nwprofs -= general_nwp[prof_pick][1]
                        general_nwp.pop(prof_pick)
    elif my_class == 'Druid/Mage' or my_class == 'Fighter/Mage/Cleric' or my_class == 'Fighter/Mage/Druid':
        # Pick from Priest, Wizard, Warrior, and General NWPs
        #  until all currently available NWP slots are full
        while nwprofs > 0:
            group = random.randint(1,4)
            if group == 1:   # Priest NWP
                if len(priest_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(priest_nwp, 1):
                            prof_pick = random.randint(0,len(priest_nwp)-1)
                            my_nwprofs.append(priest_nwp[prof_pick])
                            nwprofs -= priest_nwp[prof_pick][1]
                            priest_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(priest_nwp)-1)
                        while nwprofs - priest_nwp[prof_pick][1] < 0:
                            if len(priest_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(priest_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(priest_nwp[prof_pick])
                        nwprofs -= priest_nwp[prof_pick][1]
                        priest_nwp.pop(prof_pick)
            elif group == 2:   # Wizard NWP
                if len(wizard_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(wizard_nwp, 1):
                            prof_pick = random.randint(0,len(wizard_nwp)-1)
                            my_nwprofs.append(wizard_nwp[prof_pick])
                            nwprofs -= wizard_nwp[prof_pick][1]
                            wizard_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(wizard_nwp)-1)
                        while nwprofs - wizard_nwp[prof_pick][1] < 0:
                            if len(wizard_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(wizard_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(wizard_nwp[prof_pick])
                        nwprofs -= wizard_nwp[prof_pick][1]
                        wizard_nwp.pop(prof_pick)
            elif group == 3:   # Warrior NWP
                if len(warrior_nwp) > 0:    # NWP list is not empty
                    if nwprofs == 1:        # Only 1 NWP slot left
                        if in_List(warrior_nwp, 1):
                            prof_pick = random.randint(0,len(warrior_nwp)-1)
                            my_nwprofs.append(warrior_nwp[prof_pick])
                            nwprofs -= warrior_nwp[prof_pick][1]
                            warrior_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(warrior_nwp)-1)
                        while nwprofs - warrior_nwp[prof_pick][1] < 0:
                            if len(warrior_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(warrior_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(warrior_nwp[prof_pick])
                        nwprofs -= warrior_nwp[prof_pick][1]
                        warrior_nwp.pop(prof_pick)
            else:   # General NWP
                if len(general_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(general_nwp, 1):
                            prof_pick = random.randint(0,len(general_nwp)-1)
                            my_nwprofs.append(general_nwp[prof_pick])
                            nwprofs -= general_nwp[prof_pick][1]
                            general_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(general_nwp)-1)
                        while nwprofs - general_nwp[prof_pick][1] < 0:
                            if len(general_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(general_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(general_nwp[prof_pick])
                        nwprofs -= general_nwp[prof_pick][1]
                        general_nwp.pop(prof_pick)
    elif my_class == 'Fighter/Mage/Thief':
        # Pick from Rogue, Wizard, Warrior, and General NWPs
        #  until all currently available NWP slots are full
        while nwprofs > 0:
            group = random.randint(1,4)
            if group == 1:   # Rogue NWP
                if len(rogue_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(rogue_nwp, 1):
                            prof_pick = random.randint(0,len(rogue_nwp)-1)
                            my_nwprofs.append(rogue_nwp[prof_pick])
                            nwprofs -= rogue_nwp[prof_pick][1]
                            rogue_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(rogue_nwp)-1)
                        while nwprofs - rogue_nwp[prof_pick][1] < 0:
                            if len(rogue_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(rogue_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(rogue_nwp[prof_pick])
                        nwprofs -= rogue_nwp[prof_pick][1]
                        rogue_nwp.pop(prof_pick)
            elif group == 2:   # Wizard NWP
                if len(wizard_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(wizard_nwp, 1):
                            prof_pick = random.randint(0,len(wizard_nwp)-1)
                            my_nwprofs.append(wizard_nwp[prof_pick])
                            nwprofs -= wizard_nwp[prof_pick][1]
                            wizard_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(wizard_nwp)-1)
                        while nwprofs - wizard_nwp[prof_pick][1] < 0:
                            if len(wizard_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(wizard_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(wizard_nwp[prof_pick])
                        nwprofs -= wizard_nwp[prof_pick][1]
                        wizard_nwp.pop(prof_pick)
            elif group == 3:   # Warrior NWP
                if len(warrior_nwp) > 0:    # NWP list is not empty
                    if nwprofs == 1:        # Only 1 NWP slot left
                        if in_List(warrior_nwp, 1):
                            prof_pick = random.randint(0,len(warrior_nwp)-1)
                            my_nwprofs.append(warrior_nwp[prof_pick])
                            nwprofs -= warrior_nwp[prof_pick][1]
                            warrior_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(warrior_nwp)-1)
                        while nwprofs - warrior_nwp[prof_pick][1] < 0:
                            if len(warrior_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(warrior_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(warrior_nwp[prof_pick])
                        nwprofs -= warrior_nwp[prof_pick][1]
                        warrior_nwp.pop(prof_pick)
            else:   # General NWP
                if len(general_nwp) > 0:
                    if nwprofs == 1:
                        if in_List(general_nwp, 1):
                            prof_pick = random.randint(0,len(general_nwp)-1)
                            my_nwprofs.append(general_nwp[prof_pick])
                            nwprofs -= general_nwp[prof_pick][1]
                            general_nwp.pop(prof_pick)
                    else:
                        prof_pick = random.randint(0,len(general_nwp)-1)
                        while nwprofs - general_nwp[prof_pick][1] < 0:
                            if len(general_nwp)-1 > 1:
                                prof_pick = random.randint(0,len(general_nwp)-1)
                            else:
                                prof_pick = 0
                        my_nwprofs.append(general_nwp[prof_pick])
                        nwprofs -= general_nwp[prof_pick][1]
                        general_nwp.pop(prof_pick)

    return my_nwprofs