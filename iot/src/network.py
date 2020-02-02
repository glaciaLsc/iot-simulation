import node

class Network:
    # Constructor
    def __init__(self, ban, connection):
        self.ban = ban
        self.connection = connection
        
    # Methods
    def setBan(self, ban):
        self.ban = ban
    def setConnection(self, connection):
        self.connection = connection
    def addNode(self, node):
        self.ban.add(node)
        
    # Accessors
    def getBan(self):
        return self.ban
    def getConnection(self):
        return self.connection