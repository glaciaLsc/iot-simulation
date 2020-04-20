import node
from node import Node
import entity
from entity import Entity
from entity import nodeNature
import random
from random import randint

class Network:
    # Constructor
    def __init__(self, ban):
        self.ban = ban
        self.numberOfKnownNodes = 0
        for i in ban:
            if (i.__class__.__name__ == 'Node'):
                self.numberOfKnownNodes += 1
        # Overall benefit contributed to network over lifetime of communication
        self.overallBenefit = 0
        
    # Methods
    def setBan(self, ban):
        self.ban = ban
        self.numberOfKnownNodes = 0
        for i in ban:
            if (i.__class__.__name__ == 'Node'):
                self.numberOfKnownNodes += 1
        self.overallBenefit = 0
    def addNode(self, node):
        self.ban.append(node)
    def addEntity(self, entity):
        self.ban.append(entity)
    def display(self):
        for i in self.ban:
            if (i.__class__.__name__ == 'Node'):
                print('Device class:', i.__class__.__name__)
                print('Device name:', i.getName())
                print('------------------------')
        
                print('Power:', i.getPower())
                print('Energy consumption rate:', i.getEnergyConsumption())
                print('Energy rating:', i.getEnergyRating())
                print('Data sensitivity:', i.getDataSensitivity())
                print('Node security policy:', i.getMode())
                print()
            elif (i.__class__.__name__ == 'Entity'):
                print('Device class:', i.__class__.__name__)
                print('Device name:', i.getName())
                print('------------------------')
            
                print('Nature:', i.getNature())
                print('Estimated utility:', i.getUtility())
                print()
                
    def runSimulation(self, numRandomEntities, threshold):
        while (self.numberOfKnownNodes > 0):
            # Create random unknown entities
            for i in range(numRandomEntities):
                rnature = random.randint(1, 99)
                rutility = random.randint(0, 10)
                if (rnature <= 75):
                    e = Entity('e', nodeNature.BENEVOLENT, rutility)
                elif (rnature > 75 <= 87):
                    e = Entity('e', nodeNature.MALICIOUS, rutility)
                elif (rnature > 87 <= 99):
                    e = Entity('e', nodeNature.SELFISH, rutility)
                self.addEntity(e)
            
            # Loop through network & simulate interactions
            for i in self.ban:
                if  (i.__class__.__name__ == 'Node'):
                    i.setMode(threshold)
                    for j in self.ban:
                        if (j.__class__.__name__ == 'Entity'):
                            # Have node evaluate entity
                            if (i.evaluateEntity(j) == True):
                                # Derive actual benefit to network
                                if (j.getNature() == nodeNature.MALICIOUS):
                                    self.overallBenefit += j.getUtility() - i.getDataSensitivity() - (i.getEnergyRating()/100.00)
                                elif (j.getNature() == nodeNature.SELFISH):
                                    self.overallBenefit += j.getUtility() - (i.getEnergyRating()/100.00)
                                elif (j.getNature() == nodeNature.BENEVOLENT):
                                    self.overallBenefit += j.getUtility()
                            # If power is depleted, remove node from network
                            if (i.getPower() <= 0):
                                break
                    #print('Total number of communications before death:', i.getCommunications())
                    self.numberOfKnownNodes -= 1
                    self.ban.remove(i)
                
        #print('Total achieved network utility:', self.overallBenefit)
                                
    # Accessors
    def getBan(self):
        return self.ban
    def getNumberOfKnownNodes(self):
        return self.numberOfKnownNodes
    def getOverallBenefit(self):
        return self.overallBenefit