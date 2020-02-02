from enum import Enum
from scipy.stats.mstats_basic import mode

class nodeStatus(Enum):
    COMPROMISED = 0
    VULNERABLE = 1
    REPAIRED = 2
    
class nodeMode(Enum):
    PASSIVE = 0
    SECURE = 1

class Node:
    # Constructor
    def __init__(self, name, power, energyConsumption, bandwidth, status, mode):
        self.name = name
        self.power = power
        self.energyConsumption = energyConsumption
        self.bandwidth = bandwidth
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
    def getStatus(self):
        return self.status
    def getMode(self):
        return self.mode
