'''
File: ass2main_code.py
Description: This file is about the UML diagram, Alchemist who has a laboratory and drinks potions. There are numerous types of reagents and potions.
Author: Bhavya Gupta
StudentID: 110395898
EmailID: gupby004@mymail.unisa.edu.au
This is my own work as defined by the University's Academic Misconduct Policy.
'''

from abc import ABC, abstractmethod


class Reagent(ABC): 

    """
    Abstract Base Class reagent is forrmed.

    Attributes:
        __name (str): The private name of reagent.
        __potency (float): The private potency value of reagent.

    Methods:
        refine(): Abstract method for refining reagent.
        getName():Recieve name of reagent.
        getPotency(): Recieve potency value of reagent.
        setPotency(new_potency): Setting a new potency value for reagent.
    """

    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):

        """
        Abstract method refining is implememnted.
        """
        pass

    def getName(self):

        """
        To recieve the name of reagent.
        """
        return self.__name

    def getPotency(self):

        """
        To recieve the potency of reagent.
        """
        return self.__potency

    def setPotency(self, new_potency):

        """
        Setting the potency of reagent.
        """
        self.__potency = new_potency


class Herb(Reagent):

    """
    Class herb inherited from reagent.

    Attributes:
        __grimy (bool): Checking herb is grimy or not.

    Methods:
        refine(): Refining the herb.
        isGrimy(): Check herb is grimy or not.
    """
    def __init__(self, name, potency):
        super().__init__(name, potency)
        self.__grimy = True

    def refine(self):

        """
        Refining the herb on the basis of grimy.
        """
        if self.__grimy:
            self.__grimy = False
            super().setPotency(self.getPotency() * 2.5)
            print(f"{self.getName()} has been refined. New potency: {self.getPotency():.2f}")

    def isGrimy(self):

        """
        Checking the herb's grimy.
        """
        return self.__grimy    
    

class Catalyst(Reagent):

    """
    Class Catalyst inherited from reagent.

    Attributes:
        __quality (float): Indicating quality of catalyst.

    Methods:
        refine(): Refining the catalyst.
        getQuality():Reieving quality of catalyst.
    """
    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):

        """
        Refining the catalyst on the basis of quality.
        """
        if self.__quality < 8.9:
            self.__quality += 1.1
            print(f"{self.getName()} has been refined. New quality: {self.getQuality():.2f}")
        else:
            self.__quality = 10.0
            print(f"{self.getName()} cannot be refined any further. Quality set to 10.00")

    def getQuality(self):

        """
        Recieving the quality of the catalyst.
        """
        return self.__quality    
    

class Potion(ABC):

    """
    Abstract Base Case Potion.

    Attributes:
        __name (str): Name of potion.
        __stat (str): Stat of the Potion.
        __boost (float): The amount by which Potion gets boosted.

    Methods:
        calculateBoost(reagent1, reagent2, super_potion): Abstract method to calculate boost.
        getName(): Recieving name of potion.
        getStat(): Recieving the stat of Potion.
        getBoost(): Recieving the amount of boost.
        setBoost(newBoost): Setting the value of boost.
    """
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat
        self.__boost = round(boost, 2)

    @abstractmethod
    def calculateBoost(self, reagent1=None, reagent2=None, super_potion=None):
        
        """
        Abstract method to calculate boost.
        """
        pass

    def getName(self):

        """
        To get the potion's name.
        """
        return self.__name

    def getStat(self):

        """
        To get the stat.
        """
        return self.__stat

    def getBoost(self):

        """
        To get the amount of potion's boost.
        """
        return self.__boost

    def setBoost(self, newBoost):

        """
        Setting the boost.
        """
        self.__boost = round(newBoost, 2)


class SuperPotion(Potion):

    """
    Class super potion which is inherited from Potion.

    Attributes:
        __herb (Herb): The herb reagent used in potion.
        __catalyst (Catalyst): The catalyst reagent used in potion.

    Methods:
        calculateBoost(herb, catalyst, super_potion): Calculate the boost.
        getHerb(): Get the herb used in potion.
        getCatalyst(): Get the catalyst used in potion.
    """
    def __init__(self, name, stat, herb, catalyst):
        super().__init__(name, stat, 0.0)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self, herb, catalyst):

        """
        Calculating the boost.
        """
        if herb is not None and catalyst is not None:
            return round(Herb.getPotency() + (Catalyst.getPotency() * Catalyst.getQuality()) * 1.5, 2)
        else:
            return 0.0

    def getHerb(self):

        """
        To get the herb.
        """
        return self.__herb

    def getCatalyst(self):

        """
        To get the catalyst.
        """
        return self.__catalyst


class ExtremePotion(Potion):

    """
    Class extreme potion inherited from Potion.

    Attributes:
        __reagent (Reagent): Reagent used in potion.
        __super_potion (Potion): Super potion used in the potion.

    Methods:
        calculateBoost(reagent, super_potion): Calculate the boost.
        getReagent(): Getting reagent which is used in potion.
        getSuperPotion(): Getting super potion which is used in the potion.
    """
    def __init__(self, name, stat, reagent, super_potion):
        super().__init__(name, stat, 0.0)
        self.__reagent = reagent
        self.__super_potion = super_potion

    def calculateBoost(self, reagent, super_potion):

        """
        Calculating the boost.
        """
        if reagent is not None and super_potion is not None:
            return round((Reagent.getPotency() * SuperPotion.getBoost()) * 3.0, 2)
        else:
            return 0.0

    def getReagent(self):

        """
        Get the reagent used.
        """
        return self.__reagent

    def getSuperPotion(self):

        """
        Get superPotion used.
        """
        return self.__super_potion        
    

class Laboratory:

    """
    Class Laboratory is created.

    Attributes:
        __potions (list): List to store potions.
        __herbs (list): List to store herbs.
        __catalysts (list): List to store catalysts.

    Methods:
        mixPotion(reagent1, reagent2, potion): Mixing two reagents to create a potion.
        addReagent(reagent): Adding a reagent.
        refineReagents(): Refine all herbs and catalyst.
    """
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mixPotion(self, reagent1, reagent2, potion):

        """
        Mixing two reagents to create a potion.
        """
        boost = Potion.calculateBoost(reagent1, reagent2, None)
        Potion.setBoost(boost)
        self.__potions.append(potion)
        print(f"Created {Potion.getName()} potion with {Potion.getBoost()} boost to {Potion.getStat()}.")

    def addReagent(self, reagent):

        """
        Adding a reagent.
        """
        if isinstance(reagent, Herb):
            self.__herbs.append(reagent)
        elif isinstance(reagent, Catalyst):
            self.__catalysts.append(reagent)
        else:
            print("Invalid reagent type.")

    def refineReagents(self):

        """
        Refining the reagents.
        """
        print("Refining the Reagents:")
        for herb in self.__herbs:
            Herb.refine()
        for catalyst in self.__catalysts:
            Catalyst.refine()

        self.__herbs = []
        self.__catalysts = []        

class Alchemist:

    """
    Class alchemist is formed.

    Attributes:
        __attack (float): Alchemist's attack.
        __strength (float): Alchemist's strength.
        __defense (float): Alchemist's defense.
        __magic (float): Alchemist's magic.
        __ranged (float): Alchemist's ranged.
        laboratory (Laboratory): Achemist owns a laboratory.
        recipes (list): List to store recipes.

    Methods:
        getLaboratory(): Getting laboratory.
        getRecipes(recipe): Getting recipes.
        mixPotion(self, firstElement, secondElement, potionName, stat): Mixing elements to create a potion.
        drinkPotion(potion): Drinking a potion.
        collectReagent(reagent): Collect a reagent.
        refineReagents(): Refining all reagents.
    """
    def __init__(self, attack, strength, defense, magic, ranged):
        self.__attack = attack
        self.__strength = strength
        self.__defense = defense
        self.__magic = magic
        self.__ranged = ranged
        self.laboratory = Laboratory()
        self.recipes = []

    def getLaboratory(self):

        """
        Get laboratory.
        """
        return self.laboratory

    def getRecipes(self, recipe):

        """
        Get Recipes.
        """
        self.recipes.append(recipe)

    def mixPotion(self, firstElement, secondElement, potionName, stat):

        """
        Mixing elements to get a potion.
        """
        if stat == "Super":
            newPotion = SuperPotion(potionName, stat, firstElement, secondElement)
        elif stat == "Extreme":
            newPotion = ExtremePotion(potionName, stat, firstElement, secondElement)
        else:
            print("Invalid potion status.")
            return

        self.laboratory.mixPotion(firstElement, secondElement, newPotion)
        

    def drinkPotion(self, potion):

        """
        Drink potion to check the stat.
        """
        if potion.getStat() == "attack":
            self.__attack += potion.getBoost()
        elif potion.getStat() == "strength":
            self.__strength += potion.getBoost()
        elif potion.getStat() == "defense":
            self.__defense += potion.getBoost()
        elif potion.getStat() == "magic":
            self.__magic += potion.getBoost()
        elif potion.getStat() == "ranged":
            self.__ranged += potion.getBoost()
        else:
            print("Unknown potion status")


    def collectReagent(self, reagent):

        """
        Collecting Reagents.
        """
        self.laboratory.addReagent(reagent)

    def refineReagents(self):

        """
        Refining the reagents.
        """
        self.laboratory.refineReagents()

