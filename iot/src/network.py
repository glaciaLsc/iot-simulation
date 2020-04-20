import node
from node import Node
import entity
from entity import Entity
from entity import nodeNature

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
    def addNode(self, node):
        self.ban.add(node)
    def addEntity(self, entity):
        self.ban.add(entity)
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
                
    def runLoop(self, threshold):
        while (self.numberOfKnownNodes > 0):
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
                            if (i.getPower() <= 0):
                                #print('Total number of communications before death:', i.getCommunications())
                                self.numberOfKnownNodes -= 1
                                self.ban.remove(i)
            print('Total achieved network utility:', self.overallBenefit)
                                
    # Accessors
    def getBan(self):
        return self.ban