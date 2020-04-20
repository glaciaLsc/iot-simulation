from enum import Enum
import entity
from entity import nodeNature
import randomfrom random import randint

class nodeMode(Enum):
    PASSIVE = 0
    SECURE = 1

class Node:
    # Constructor
    def __init__(self, name, energyConsumption, hasIdentifiables, 
                 hasPasswords, hasBiometrics, hasTelemetry, hasMiscellaneous):
        self.name = name
        # Starting power
        self.power = 100
        self.energyConsumption = energyConsumption
        # Define energy rating by dividing power percentage by consumption per authentication
        self.energyRating = self.power / energyConsumption
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
        # Node mode set to PASSIVE by default
        self.mode = nodeMode.PASSIVE
        # Bayesian probabilities
        self.M = .3333
        self.S = .3333
        self.B = .3333
        # Number of successful communications
        self.communications = 0
    
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
    def setMode(self, threshold):
        score = self.energyRating * self.dataSensitivity
        #print(self.name, 'Threshold:', threshold)
        #print(self.name, 'Score:', score)
        if (score >= threshold):
            self.mode = nodeMode.SECURE
            #print(self.name, 'set to SECURE')
        else:
            self.mode = nodeMode.PASSIVE
            #print(self.name, 'set to PASSIVE')
    
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
        #print('Current Bayesian probability values (M,S,B):', self.M, self.S, self.B)
        # Passive security policy
        if (self.mode == nodeMode.PASSIVE):
            # Malicious + Selfish + Benevolent     
            allow = (self.M*(entity.getUtility() - self.dataSensitivity - (self.energyRating/100))
                     + self.S*(entity.getUtility() - (self.energyRating / 100)) 
                     + self.B*(entity.getUtility()))
            #print('Estimated Allow benefit:', allow)
            block = 0
            #print('Estimated Blocking benefit:', block)
            # Subtract power according to consumption rate + policy chosen
            self.power -= self.energyConsumption / 100.00
            # Compare benefit of blocking to utility of communicating
            if (allow > block):
                #print('Choosing to forward packets.')
                # Update total number of successful communications
                self.communications += 1
                return True
            else:
                #print('Choosing to block packets.')
                return False
        # Active security policy
        elif (self.mode == nodeMode.SECURE):
            # Evaluation accuracy set at 95%
            seed = randint(1, 100)
            if (seed < 95):
                if (entity.getNature() == nodeNature.MALICIOUS):
                    self.M = self.approachUpperLimit(self.M, .25, 1.0000)
                    self.S = self.approachLowerLimit(self.S, -.125, 0.0000)
                    self.B = self.approachLowerLimit(self.B, -.125, 0.0000)
                elif (entity.getNature() == nodeNature.SELFISH):
                    self.S = self.approachUpperLimit(self.S, .1, 1.0000)
                    self.M = self.approachLowerLimit(self.M, -.05, 0.0000)
                    self.B = self.approachLowerLimit(self.B, -.05, 0.0000)
                elif (entity.getNature() == nodeNature.BENEVOLENT):
                    self.B = self.approachUpperLimit(self.B, .1, 1.0000)
                    self.M = self.approachLowerLimit(self.M, -.05, 0.0000)
                    self.S = self.approachLowerLimit(self.S, -.05, 0.0000)
            else:
                seed = randint(0, 2)
                if (seed == 0):
                    self.M = self.approachUpperLimit(self.M, .25, 1.0000)
                    self.S = self.approachLowerLimit(self.S, -.125, 0.0000)
                    self.B = self.approachLowerLimit(self.B, -.125, 0.0000)
                elif (seed == 1):
                    self.S = self.approachUpperLimit(self.S, .1, 1.0000)
                    self.M = self.approachLowerLimit(self.M, -.05, 0.0000)
                    self.B = self.approachLowerLimit(self.B, -.05, 0.0000)
                elif (seed == 2):
                    self.B = self.approachUpperLimit(self.B, .1, 1.0000)
                    self.M = self.approachLowerLimit(self.M, -.05, 0.0000)
                    self.S = self.approachLowerLimit(self.S, -.05, 0.0000)
                    
            #print('Adjusted Bayesian probability values (M,S,B):', self.M, self.S, self.B)
            allow = (self.M*(entity.getUtility() - self.dataSensitivity - (self.energyRating/100))
                     + self.S*(entity.getUtility() - (self.energyRating / 100)) 
                     + self.B*(entity.getUtility()))
            #print('Estimated Allow benefit:', allow)
            block = 0
            #print('Estimated Blocking benefit:', block)
            # Subtract power according to consumption rate + policy chosen
            self.power -= (self.energyConsumption*2 / 100.00)
            # Compare benefit of blocking to utility of communicating
            if (allow > block):
                #print('Choosing to forward packet(s).')
                # Update total number of successful communications
                self.communications += 1
                return True
            else:
                #print('Choosing to block packet(s).')
                return False
                    
    # Mathematical functions for operating on integers with limited ranges.
    # The inclusion of these functions is due to the fact that probabilities
    # cannot exceed 1 or descend below 0.
    def approachUpperLimit(self, n, margin, limit):
        n += margin
        if (n > limit):
            return limit
        else:
            return n
    def approachLowerLimit(self, n, margin, limit):
        n += margin
        if (n < limit):
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
    def getCommunications(self):
        return self.communications