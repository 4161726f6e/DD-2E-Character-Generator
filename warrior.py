#######################################
# AD&D 2nd Edition                    #
# Random Character Generator:         #
#  Warrior                            #
#                                     #
# Adds Warrior abilities to randomly  #
#  generated character                #
#######################################

import random

#--------------------------------------
# Return the amount of experience
#  points a character has based on
#  level
#--------------------------------------
def getWarrior_XP(my_class, my_level):
    fighter_table = [0,2000,4000,8000,16000,32000,64000,125000,250000,500000,\
        750000,1000000,1250000,1500000,1750000,2000000,2250000,2500000,2750000,3000000]
    pal_rang_table = [0,2250,4500,9000,18000,36000,75000,150000,300000,600000,\
        900000,1200000,1500000,1800000,2100000,2400000,2700000,3000000,3300000,3600000]
    
    if my_class == 'Fighter':
        my_xp = fighter_table[my_level - 1]
    else:
        my_xp = pal_rang_table[my_level - 1]

    return my_xp

#--------------------------------------
# Return the number of melee attacks
#  per round based on level
#--------------------------------------
def getAtt_R(my_level):
    if my_level < 7:
        my_att = '1/round'
    elif my_level < 13:
        my_att = '3/2 rounds'
    else:
        my_att = '2/round'

    return my_att

#--------------------------------------
# Return the number of specialist
#  attacks per round based on level
#--------------------------------------
def getS_Att_R(my_level, my_class):
    if my_class != 'Fighter':
        return [0,0,0,0,0,0]

    if my_level < 7:
        return ['3/2','1/1','1/2','3/1','4/1','3/2']
    elif my_level < 13:
        return ['2/1','3/2','1/1','4/1','5/1','2/1']
    else:
        return ['5/2','2/1','3/2','5/1','6/1','5/2']

#--------------------------------------
# Randomly select weapon profs and
#  apply specialization to each as
#  long as lots are available
#--------------------------------------
def F_selectWP(all_weapons, wprofs):
    my_wprofs = []
    bows = ['Composite long bow','Composite short bow','Long bow','Short bow']
    while wprofs > 0:
        prof_pick = random.randint(0,54)    # 55 possible weapons, pick 1
        while all_weapons[prof_pick] in my_wprofs: # Don't pick already picked weapon
            prof_pick = random.randint(0,54)
        if all_weapons[prof_pick] in bows:  # a bow was picked
            if wprofs > 2:  # if there are enough slots to specialize in a bow
                my_wprofs.append(all_weapons[prof_pick] + ' + Specialist')
                wprofs -= 3
        elif wprofs > 1:    # if enough slots to specialize in melee or crossbow
                my_wprofs.append(all_weapons[prof_pick] + ' + Specialist')
                wprofs -= 2
        else:   # no specialization
            my_wprofs.append(all_weapons[prof_pick])
            wprofs -= 1

    return my_wprofs

#--------------------------------------
# Return the number of followers
#  a Fighter has by type after
#  reaching 9th level
#--------------------------------------
def getF_Followers(my_level, my_class):
    if my_class != 'Fighter' or my_level < 9:
        return ['None','None','None']
    
    leader_roll = random.randint(1,100)
    troops_roll = random.randint(1,100)
    elite_roll  = random.randint(1,100)

    if leader_roll < 41:
        leader = '5th-level fighter, plate mail, shield, battle axe +2'
    elif leader_roll < 76:
        leader = '6th-level fighter, plate mail, shield +1, spear +1, dagger +1'
    elif leader_roll < 96:
        leader = '6th-level fighter, plate mail +1, shield, spear +1, dagger +1, plus 3rd-level fighter, splint mail, shield, crossbow of distance'
    elif leader_roll < 100:
        leader = '7th-level fighter, plate mail +1, shield +1, broad sword +2, heavy war horse with horseshoes of speed'
    else:
        leader = 'DM\'s Option'

    if troops_roll < 51:
        troops = '20 cavalry with ring mail, shield, 3 javelins, long sword, hand axe; 100 infantry with scale mail, polearm, club'
    elif troops_roll < 76:
        troops = '20 infantry with splint mail, morning star, hand axe; 60 infantry with leather armor, pike, short sword'
    elif troops_roll < 91:
        troops = '40 infantry with chain mail, heavy crossbow, short sword; 20 infantry with chain mail, light crossbow, military fork'
    elif troops_roll < 100:
        troops = '10 cavalry with banded mail, shield, lance, bastard sword, mace; 20 cavalry with scale mail, shield, lance, long sword, mace; 30 cavalry with studded leather armor, shield, lance, long sword'
    else:
        troops = 'DM\'s Option (Barbarians, headhunters, armed peasants, extra-heavy cavalry, etc.)'

    if elite_roll < 11:
        elite = '10 mounted knights; 1st-level fighters with field plate, large shield, lance, broad sword, morning star, and heavy war horse with full barding'
    elif elite_roll < 21:
        elite = '10 1st-level elven fighter/mages with chain mail, long sword, long bow, dagger'
    elif elite_roll < 31:
        elite = '15 wardens: 1st-level rangers with scale mail, shield, long sword, spear, long bow'
    elif elite_roll < 41:
        elite = '20 berserkers: 2nd-level fighters with leather armor, shield, battle axe, broad sword, dagger (berserkers receive +1 bonus to attack and damage rolls)'
    elif elite_roll < 66:
        elite = '20 expert archers: 1st-level fighters with studded leather armor, long bows or crossbows (+2 to hit, or bow specialization)'
    elif elite_roll < 100:
        elite = '30 infantry: 1st-level fighters with plate mail, body shield, spear, short sword'
    else:
        elite = 'DM\'s Option (pegasi cavalry, eagle riders, demihumans, siege train, etc.)'

    return leader, troops, elite

#--------------------------------------
# Return the casting level and number
#  of priest spells a Paladin has
#  based on level
#
#  Paladins can cast up to 4th level
#  priest spells
#--------------------------------------
def Paladin_Spells(my_level):
    level = my_level - 8
    paladin_spell_table = [[1,0,0,0],[2,0,0,0],[2,1,0,0],[2,2,0,0],[2,2,1,0],[3,2,1,0],\
        [3,2,1,1],[3,3,2,1],[3,3,3,1],[3,3,3,1],[3,3,3,2],[3,3,3,3]]
    
    if my_level < 9:
        return 0, [0,0,0,0]
    if my_level > 17:
        return 9, paladin_spell_table[level - 1]
    else:
        return level, paladin_spell_table[level - 1] 

#--------------------------------------
# Return the Ranger's Hide in Shadows 
#  and Move Silently abilities, as well
#  as the casting level and number
#  of priest spells a Ranger has
#  based on level
#
#  Rangers can cast up to 3rd level
#  priest spells
#--------------------------------------
def Ranger_Abilities(my_level):
    ranger_thief_table = [['0%','0%'],['10%','15%'],['15%','21%'],['20%','27%'],['25%','33%'],['31%','40%'],\
        ['37%','47'],['43%','55%'],['49%','62%'],['56%','70%'],['63%','78%'],['70%','86%'],['77%','94%'],\
        ['85%','99%'],['93%','99%'],['99%','99%'],['99%','99%']]
    ranger_spell_table = [[1,0,0],[2,0,0],[2,1,0],[2,2,0],[2,2,1],[3,2,1],[3,2,2],[3,3,2],[3,3,3]]

    if my_level > 16:
        my_level = 16   # max ability
    
    thief_skills = ranger_thief_table[my_level]

    if my_level < 8:
        priest_spells = [0,0,0]
        casting_lvl = 0
    else:
        priest_spells = ranger_spell_table[my_level - 8]
        casting_lvl = my_level - 7

    return thief_skills, casting_lvl, priest_spells

#--------------------------------------
# Return the number of followers
#  a Ranger has by type after
#  reaching 10th level
#--------------------------------------
def getR_Followers(my_level, my_class):
    if my_class != 'Ranger' or my_level < 10:
        return ['None']
    
    number = random.randint(2,12)
    ranger_followers = []
    
    while number > 0:
        followers = random.randint(1,100)
        if followers < 11:
            ranger_followers.append('Bear, black')
        elif followers < 21:
            ranger_followers.append('Bear, brown')
        elif followers < 22:
            if 'Brownie' not in ranger_followers:
                ranger_followers.append('Brownie')
        elif followers < 27:
            ranger_followers.append('Cleric (human)')
        elif followers < 39:
            ranger_followers.append('Dog/wolf')
        elif followers < 41:
            ranger_followers.append('Druid')
        elif followers < 51:
            ranger_followers.append('Falcon')
        elif followers < 54:
            ranger_followers.append('Fighter (elf)')
        elif followers < 56:
            ranger_followers.append('Fighter (gnome)')
        elif followers < 58:
            ranger_followers.append('Fighter (halfling)')
        elif followers < 66:
            ranger_followers.append('Fighter (human)')
        elif followers < 67:
            if 'Fighter/mage (elf)' not in ranger_followers:
                ranger_followers.append('Fighter/mage (elf)')
        elif followers < 73:
            if 'Great cat (tiger, lion, etc.)' not in ranger_followers:
                ranger_followers.append('Great cat (tiger, lion, etc.)')
        elif followers < 74:
            ranger_followers.append('Hippogriff')
        elif followers < 75:
            if 'Pegasus' not in ranger_followers:
                ranger_followers.append('Pegasus')
        elif followers < 76:
            if 'Pixie' not in ranger_followers:
                ranger_followers.append('Pixie')
        elif followers < 81:
            ranger_followers.append('Ranger (half-elf)')
        elif followers < 91:
            ranger_followers.append('Ranger (human)')
        elif followers < 95:
            ranger_followers.append('Raven')
        elif followers < 96:
            if 'Satyr' not in ranger_followers:
                ranger_followers.append('Satyr')
        elif followers < 97:
            ranger_followers.append('Thief (halfling)')
        elif followers < 98:
            ranger_followers.append('Thief (human)')
        elif followers < 99:
            if 'Treant' not in ranger_followers:
                ranger_followers.append('Treant')
        elif followers < 100:
            if 'Werebear/weretiger' not in ranger_followers:
                ranger_followers.append('Werebear/weretiger')
        else:
            ranger_followers.append('Other wilderness creature (chosen by the DM)')

        number -= 1
        
    return ranger_followers