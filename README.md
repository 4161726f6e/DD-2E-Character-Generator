# D&D 2E Character Generator

Dependency: ReportLab is required for PDF printing. 

2E_character_generator.py is a Python script which creates a playable D&D Second Edition character. Character creation rules are based off of the D&D 2E Player's Handbook.

Usage: python 2E_character_generator.py -c <class> -r <race> -l <level> -n <number> -o <output>
       -o pdf: Print to PDF (default)    con: Print to console

Calling 2E_character_generator.py with no arguments will generate 1 random level 1 character.

Specify the desired character class with -c, the desired race with -r, the desired level with -l. The maximum level is 20.
  Example: 2E_character_generator.py -c Fighter -r Dwarf -l 12

Additionally, you can specify how many characters to create with -n and specify whether the created character information should be printed to PDF or to the terminal console. If -o is not used, the default is to print a PDF character sheet for each character.

Character names are randomly chosen from male_names.txt and femaile_names.txt. These can be edited to fit your campaign, just keep one name per line. Gender is randomly assigned (binary is assumed).

Wizard and Priest spells are randomly chosen according to class restrictions from the files priest_spells.csv and wizard_spells.csv.

Class-specific data generation is handled through priest.py, rogue.py, warrior.py, and wizard.py. Non-weapon proficiencies are selected through nonWeaponProfs.py.

Allowed Races:
  Human
  Elf
  Half-Elf
  Dwarf
  Halfling
  Gnome
  Half-Orc

Allowed Classes:
  Fighter
  Ranger
  Paladin
  Wizard (Randomized Specialization)
  Mage
  Illusionist
  Priest (Randomized Mythos)
  Cleric
  Druid
  Thief
  Bard

Allowed Demihuman Multiclass:
  Fighter/Thief
  Fighter/Cleric
  Fighter/Druid
  Fighter/Mage
  Fighter/Illusionist
  Fighter/Mage/Cleric
  Fighter/Mage/Druid
  Fighter/Mage/Thief
  Cleric/Illusionist
  Cleric/Mage
  Cleric/Thief
  Cleric/Ranger
  Illusionist/Thief
  Mage/Thief
  Druid/Mage

Race/Class Combinations:
  Half-Orcs are allowed to be:
    Fighter
    Wizard
    Mage
    Illusionist
    Priest
    Cleric
    Thief
    Fighter/Thief
    Fighter/Cleric
    Fighter/Mage
    
  See 2E rules for other race/class restrictions

