from enum import Enum
import entity
from entity import nodeNature
import randomfrom random import randint

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
        
        # Define energy rating by dividing power percentage by consumption per authentication
        self.energyRating = power / energyConsumption
        
        # Define data sensitivity according to the types of data stored. This allows for the implementation of
        # a weighted security policy, with data-critical devices maintaining relatively aggressive security activity,
        # and less data-sensitive devices prioritizing energy conservation.
        self.dataSensitivity = 0
        if (hasIdentifiables == True):
            self.dataSensitivity += .3000
        if (hasPasswords == True):
            self.dataSensitivity += .3000
        if (hasBiometrics == True):
            self.dataSensitivity += .2000
        if (hasTelemetry == True):
            self.dataSensitivity += .1000
        if (hasMiscellaneous == True):
            self.dataSensitivity += .1000
            
        self.mode = mode
    
    # Methods
    def setName(self, name):
        self.name = name
    def setPower(self, power):
        self.power = power
    def setEnergyConsumption(self, energyConsumption):
        self.energyConsumption = energyConsumption
    def setEnergyRating(self, power, energyConsumption):
        self.energyRating = power / energyConsumption
    def setDataSensitivity(self, hasIdentifiables, hasPasswords, hasBiometrics, hasTelemetry, hasMiscellaneous):
        sensitivity = 0
        
        if (hasIdentifiables == True):
            sensitivity += .3000
        if (hasPasswords == True):
            sensitivity += .3000
        if (hasBiometrics == True):
            sensitivity += .2000
        if (hasTelemetry == True):
            sensitivity += .1000
        if (hasMiscellaneous == True):
            sensitivity += .1000
            
        self.dataSensitivity = sensitivity
    # Decide on security policy according to energy & data vulnerability
    def setMode(self, energyRating, dataSensitivity, threshold):
        score = energyRating * dataSensitivity
        
        if (score >= threshold):
            self.mode = nodeMode.SECURE
        else:
            self.mode = nodeMode.PASSIVE
    
    # Set Markovian probabilities for an opposing Node to be classified as
    # either Malevolent, Selfish, or Benevolent
    def setProbabilities(self):
        self.M = .3333
        self.S = .3333
        self.B = .3333
    
    # Evaluate node according to security policy. A value of 0 returned
    # indicates that an entity should be blocked. Conversely, a value of
    # 1 returned represents a permissable entity.
    def evaluateEntity(self, entity):
        # Passive security policy
        if (self.mode == nodeMode.PASSIVE):
            # Malicious + Selfish + Benevolent     
            allow = ((entity.Entity.getUtility() - self.dataSensitivity - (self.energyRating/100))
                     + (entity.Entity.getUtility() - (self.energyRating / 100)) 
                     + (entity.Entity.getUtility()))
            block = 0
            # Compare benefit of blocking to utility of communicating
            if (allow > block):
                return True
            else:
                return False
        # Active security policy
        elif (self.mode == nodeMode.ACTIVE):
            # Evaluation accuracy set at 95%
            seed = randint % 100 + 1
            if (seed < 95):
                if (entity.Entity.getNature() == nodeNature.MALICIOUS):
                    self.M = self.approachLimit(self.M, .25, 1.0000)
                    self.S = self.approachLimit(self.S, -.125, 0.0000)
                    self.B = self.approachLimit(self.B, -.125, 0.0000)
                elif (entity.Entity.getNature() == nodeNature.SELFISH):
                    self.S = self.approachLimit(self.S, .25, 1.0000)
                    self.M = self.approachLimit(self.M, -.125, 0.0000)
                    self.B = self.approachLimit(self.B, -.125, 0.0000)
                elif (entity.Entity.getNature() == nodeNature.BENEVOLENT):
                    self.B = self.approachLimit(self.B, .25, 1.0000)
                    self.M = self.approachLimit(self.M, -.125, 0.0000)
                    self.S = self.approachLimit(self.S, -.125, 0.0000)
            else:
                seed = randint % 3
                if (seed == 0):
                    self.M = self.approachLimit(self.M, .25, 1.0000)
                    self.S = self.approachLimit(self.S, -.125, 0.0000)
                    self.B = self.approachLimit(self.B, -.125, 0.0000)
                elif (seed == 1):
                    self.S = self.approachLimit(self.S, .25, 1.0000)
                    self.M = self.approachLimit(self.M, -.125, 0.0000)
                    self.B = self.approachLimit(self.B, -.125, 0.0000)
                elif (seed == 2):
                    self.B = self.approachLimit(self.B, .25, 1.0000)
                    self.M = self.approachLimit(self.M, -.125, 0.0000)
                    self.S = self.approachLimit(self.S, -.125, 0.0000)
            
            allow = (self.M*(entity.Entity.getUtility() - self.dataSensitivity - (self.energyRating/100))
                     + self.S*(entity.Entity.getUtility() - (self.energyRating / 100)) 
                     + self.B*(entity.Entity.getUtility()))
            block = 0
            # Compare benefit of blocking to utility of communicating
            if (allow > block):
                return True
            else:
                return False
                    
    # Mathematical function for operating on integers with limited ranges.
    # The inclusion of this function is due to the fact that probabilities
    # cannot exceed 1 or descend below 0.
    def approachLimit(self, n, margin, limit):
        n += margin
        if (n > limit) or (n < limit):
            return limit
        else:
            return n
    # Accessors
    def getName(self):
        return self.name
    def getPower(self):
        return self.power
    def getEnergyConsumption(self):
        return self.energyConsumption
    def getEnergyRating(self):
        return self.energyRating
    def getDataSensitivity(self):
        return self.dataSensitivity
    def getMode(self):
        return self.mode