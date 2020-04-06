import network
from network import Network
from network import node
from node import Node
from node import nodeMode
from node import entity
from entity import Entity

def displayNetwork(network):
    for i in network.ban:
        print(i.getName())
        print('------------------------')
        
        print('Power:', i.getPower())
        print('Energy consumption rate:', i.getEnergyConsumption())
        print('Data sensitivity:', i.getDataSensitivity())
        print('Node security policy:', i.getMode())
        print()
        
# Construct IoT devices (name, power, consumption rate, hasIdentifiables,
# hasPasswords,hasBiometrics, hasTelemetry, hasMiscellaneous, security mode)
device1 = Node('Laptop_1', 100, 2, True, True, False, True, True, nodeMode.PASSIVE)
device2 = Node('Cell_phone_1', 98, 4, False, True, False, True, False, nodeMode.PASSIVE)

# Initialize BAN with previously-constructed IoT devices
ban = [device1, device2]

# Construct network
network = Network(ban, True)

displayNetwork(network)