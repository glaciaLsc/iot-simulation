from enum import Enum
import node

class nodeNature(Enum):
    BENEVOLENT = 0
    SELFISH = 1
    MALICIOUS = 2
    
class Entity:
    # Constructor
    def __init__(self, name, nature, utility):
        self.name = name
        self.nature = nature
        self.utility = utility
        
    # Methods
    def setName(self, name):
        self.name = name
    def setNature(self, nature):
        self.nature = nature
    def setUtility(self, utility):
        self.utility = utility
        
    # Accessors
    def getName(self):
        return self.name
    def getNature(self):
        return self.nature
    def getUtility(self):
        return self.utility