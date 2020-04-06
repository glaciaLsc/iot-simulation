from enum import Enum
import entity
class nodeMode(Enum):
    PASSIVE = 0
    SECURE = 1

class Node:
    # Constructor
    def __init__(self, name, power, energyConsumption, hasIdentifiables, 
                 hasPasswords, hasBiometrics, hasTelemetry, hasMiscellaneous, mode):
        self.name = name
        self.power = power
        self.energyConsumption = energyConsumption
        
        # Define data sensitivity according to the types of data stored. This allows for the implementation of
        # a weighted security policy, with data-critical devices maintaining relatively aggressive security activity,
        # and less data-sensitive devices prioritizing energy conservation.
        self.dataSensitivity = 0
        if (hasIdentifiables == True):
            self.dataSensitivity += 5
        if (hasPasswords == True):
            self.dataSensitivity += 4
        if (hasBiometrics == True):
            self.dataSensitivity += 3
        if (hasTelemetry == True):
            self.dataSensitivity += 2
        if (hasMiscellaneous == True):
            self.dataSensitivity += 1
            
        self.mode = mode
    
    # Methods
    def setName(self, name):
        self.name = name
    def setPower(self, power):
        self.power = power
    def setEnergyConsumption(self, energyConsumption):
        self.energyConsumption = energyConsumption
    def setDataSensitivity(self, hasIdentifiables, hasPasswords, hasBiometrics, hasTelemetry, hasMiscellaneous):
        sensitivity = 0
        
        if (hasIdentifiables == True):
            sensitivity += 5
        if (hasPasswords == True):
            sensitivity += 4
        if (hasBiometrics == True):
            sensitivity += 3
        if (hasTelemetry == True):
            sensitivity += 2
        if (hasMiscellaneous == True):
            sensitivity += 1
            
        self.dataSensitivity = sensitivity
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
    def getDataSensitivity(self):
        return self.dataSensitivity
    def getMode(self):
        return self.mode