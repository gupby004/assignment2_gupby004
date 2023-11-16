from abc import ABC, abstractmethod


class Reagent(ABC):
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        pass

    def getName(self):
        return self.__name

    def getPotency(self):
        return self.__potency

    def setPotency(self, new_potency):
        self.__potency = new_potency


class Herb(Reagent):
    def __init__(self, name, potency):
        super().__init__(name, potency)
        self.__grimy = True

    def refine(self):
        if self.__grimy:
            self.__grimy = False
            super().setPotency(self.getPotency() * 2.5)
            print(f"{self.getName()} has been refined. New potency: {self.getPotency():.2f}")

    def isGrimy(self):
        return self.__grimy    
    

class Catalyst(Reagent):
    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        if self.__quality < 8.9:
            self.__quality += 1.1
            print(f"{self.getName()} has been refined. New quality: {self.getQuality():.2f}")
        else:
            self.__quality = 10.0
            print(f"{self.getName()} cannot be refined any further. Quality set to 10.00")

    def getQuality(self):
        return self.__quality    
    

class Potion(ABC):
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat
        self.__boost = round(boost, 2)

    @abstractmethod
    def calculateBoost(self, reagent1=None, reagent2=None, super_potion=None):
        pass

    def getName(self):
        return self.__name

    def getStat(self):
        return self.__stat

    def getBoost(self):
        return self.__boost

    def setBoost(self, newBoost):
        self.__boost = round(newBoost, 2)


class SuperPotion(Potion):
    def __init__(self, name, stat, herb, catalyst):
        super().__init__(name, stat, 0.0)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self, herb, catalyst):
        if herb is not None and catalyst is not None:
            return round(Herb.getPotency() + (Catalyst.getPotency() * Catalyst.getQuality()) * 1.5, 2)
        else:
            return 0.0

    def getHerb(self):
        return self.__herb

    def getCatalyst(self):
        return self.__catalyst


class ExtremePotion(Potion):
    def __init__(self, name, stat, reagent, super_potion):
        super().__init__(name, stat, 0.0)
        self.__reagent = reagent
        self.__super_potion = super_potion

    def calculateBoost(self, reagent, super_potion):
        if reagent is not None and super_potion is not None:
            return round((Reagent.getPotency() * SuperPotion.getBoost()) * 3.0, 2)
        else:
            return 0.0

    def getReagent(self):
        return self.__reagent

    def getSuperPotion(self):
        return self.__super_potion        
