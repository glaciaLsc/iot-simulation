from enum import Enum

# Defines health of node
class nodeStatus(Enum):
    COMPROMISED = 0
    VULNERABLE = 1
    REPAIRED = 2
  
# Defines whether device is in passive or active security mode 
class nodeMode(Enum):
    PASSIVE = 0
    SECURE = 1

class Node:
    # Constructor
    def __init__(self, name, power, energyConsumption, bandwidth, hasIdentifiables, 
                 hasPasswords, hasBiometrics, hasTelemetry, hasMiscellaneous, status, mode):
        self.name = name
        self.power = power
        self.energyConsumption = energyConsumption
        self.bandwidth = bandwidth
        
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
            
        self.status = status
        self.mode = mode
    
    # Methods
    def setName(self, name):
        self.name = name
    def setPower(self, power):
        self.power = power
    def setEnergyConsumption(self, energyConsumption):
        self.energyConsumption = energyConsumption
    def setBandwidth(self, bandwidth):
        self.bandwidth = bandwidth
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
    def setStatus(self, status):
        self.status = status
    def setMode(self, mode):
        self.mode = mode
    
    # Accessors
    def getName(self):
        return self.name
    def getPower(self):
        return self.power
    def getEnergyConsumption(self):
        return self.energyConsumption
    def getBandwidth(self):
        return self.bandwidth
    def getDataSensitivity(self):
        return self.dataSensitivity
    def getStatus(self):
        return self.status
    def getMode(self):
        return self.mode