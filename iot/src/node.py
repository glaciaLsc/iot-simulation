from enum import Enum

# Defines type of device in IoT network. Different types of devices can be assumed to contain
# varying levels of sensitive data, which allows for the assigning of different security "weights"
# depending on the device's classification. A less-sensitive device can more aggressively conserve
# battery by neglecting to authenticate network traffic.
class nodeCategory(Enum):
    DESKTOP = 0
    LAPTOP = 1
    SMARTPHONE = 2
    SMARTWATCH= 3
    HOME_ASSISTANT = 4
    HOME_UTILITY = 5
    KITCHEN_APPLIANCE = 6

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
    def __init__(self, name, category, power, energyConsumption, bandwidth, status, mode):
        self.name = name
        self.category= category
        self.power = power
        self.energyConsumption = energyConsumption
        self.bandwidth = bandwidth
        self.status = status
        self.mode = mode
    
    # Methods
    def setName(self, name):
        self.name = name
    def setType(self, category):
        self.category = category
    def setPower(self, power):
        self.power = power
    def setEnergyConsumption(self, energyConsumption):
        self.energyConsumption = energyConsumption
    def setBandwidth(self, bandwidth):
        self.bandwidth = bandwidth
    def setStatus(self, status):
        self.status = status
    def setMode(self, mode):
        self.mode = mode
    
    # Accessors
    def getName(self):
        return self.name
    def getCategory(self):
        return self.category
    def getPower(self):
        return self.power
    def getEnergyConsumption(self):
        return self.energyConsumption
    def getBandwidth(self):
        return self.bandwidth
    def getStatus(self):
        return self.status
    def getMode(self):
        return self.mode