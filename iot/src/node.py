from enum import Enum
import entity

class nodeCounterpartEvaluation(Enum):
    BENENEVOLENT = 0
    SELFISH = 1
    MALICIOUS = 2
    UNKNOWN = 3
    
class nodeMode(Enum):
    PASSIVE = 0
    SECURE = 1

class Node:
    # Constructor
    def __init__(self, name, power, energyConsumption, mode):
        self.name = name
        self.power = power
        self.energyConsumption = energyConsumption
        self.mode = mode
    
    # Methods
    def setName(self, name):
        self.name = name
    def setPower(self, power):
        self.power = power
    def setEnergyConsumption(self, energyConsumption):
        self.energyConsumption = energyConsumption
    def setMode(self, mode):
        self.mode = mode
        
    #def evaluateEntity(self, entity):
    
    # Accessors
    def getName(self):
        return self.name
    def getPower(self):
        return self.power
    def getEnergyConsumption(self):
        return self.energyConsumption
    def getMode(self):
        return self.mode