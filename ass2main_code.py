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