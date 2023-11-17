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


if __name__ == "__main__":
    pytest.main()
