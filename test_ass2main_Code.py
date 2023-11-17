'''
File: ass2main_code.py
Description: This file is about the UML diagram, Alchemist who has a laboratory and drinks potions. There are numerous types of reagents and potions.
Author: Bhavya Gupta
StudentID: 110395898
EmailID: gupby004@mymail.unisa.edu.au
This is my own work as defined by the University's Academic Misconduct Policy.
'''

import pytest
from ass2main_code import * 

"""
Testing the methods of the herb class.
"""
def testHerbClass():
    herb = Herb("Cadantine", 1.5)
    assert herb.getName() == "Cadantine"
    assert herb.getPotency() == 1.5
    assert herb.isGrimy() is True

def testHerbCreation():
    herb = Herb("Cadantine", 1.5)
    herb.refine()
    assert herb.isGrimy() is False
    assert herb.getPotency() == 1.5 * 2.5

"""
Testing the methods of the catalyst class.
"""    
def testCatalyst():
    catalyst = Catalyst("Eye of Newt", 4.3, 1.0)
    assert catalyst.getName() == "Eye of Newt"
    assert catalyst.getPotency() == 4.3
    assert catalyst.getQuality() == 1.0

def testCatalystRefine():
    catalyst = Catalyst("Eye of Newt", 4.3, 7.5)
    catalyst.refine()
    assert catalyst.getQuality() == 8.6

def testCatalystCannotFutherRefine():
    catalyst = Catalyst("Eye of Newt", 4.3, 9.0)
    catalyst.refine()
    assert catalyst.getQuality() == 10.0

"""
Testing SuperPotion class and calculateBoost method.
"""  
def testSuperPotion():
    herb = Herb("Arbuck", 2.6)
    catalyst = Catalyst("Eye of Newt", 4.3, 1.0)
    super_potion = SuperPotion("Super Attack", "attack", herb, catalyst)
    assert super_potion.getName() == "Super Attack"
    assert super_potion.getStat() == "attack"
    assert super_potion.getBoost() == 0.0
    assert super_potion.getHerb() == herb
    assert super_potion.getCatalyst() == catalyst

def testSuperPotionCalculateBoost():
    herb = Herb("Arbuck", 2.6)
    catalyst = Catalyst("Eye of Newt", 4.3, 1.0)
    super_potion = SuperPotion("Super Attack", "attack", herb, catalyst)
    boost = super_potion.calculateBoost(herb, catalyst, None)
    assert boost == round(herb.getPotency() + (catalyst.getPotency() * catalyst.getQuality()) * 1.5, 2)

"""
Testing ExtremePotion class and calculateBoost method.
""" 
def testExtremePotion():
    reagent = Herb("Arbuck", 2.6)
    super_potion = SuperPotion("Super Attack", "attack", Herb("Irit", 1.0), Catalyst("Eye of Newt", 4.3, 1.0))
    extreme_potion = ExtremePotion("Extreme Attack", "attack", reagent, super_potion)
    assert extreme_potion.getName() == "Extreme Attack"
    assert extreme_potion.getStat() == "attack"
    assert extreme_potion.getBoost() == 0.0
    assert extreme_potion.getReagent() == reagent
    assert extreme_potion.getSuperPotion() == super_potion

def testExtremePotionCalculateBoost():
    reagent = Herb("Arbuck", 2.6)
    super_potion = SuperPotion("Super Attack", "attack", Herb("Irit", 1.0), Catalyst("Eye of Newt", 4.3, 1.0))
    extreme_potion = ExtremePotion("Extreme Attack", "attack", reagent, super_potion)
    boost = extreme_potion.calculateBoost(reagent, super_potion)
    assert boost == round((reagent.getPotency() * super_potion.getBoost()) * 3.0, 2)




if __name__ == "__main__":
    pytest.main()
