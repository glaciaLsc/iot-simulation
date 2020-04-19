import node
import entity

class Network:
    # Constructor
    def __init__(self, ban):
        self.ban = ban
        
    # Methods
    def setBan(self, ban):
        self.ban = ban
    def addNode(self, node):
        self.ban.add(node)
    def addEntity(self, entity):
        self.ban.add(entity)
        
    # Accessors
    def getBan(self):
        return self.ban