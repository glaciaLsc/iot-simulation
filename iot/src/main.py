import network
from network import Network
from network import node
from node import Node
from node import nodeStatus
from node import nodeMode

def displayNetwork(network):
    for i in network.ban:
        print(i.getName())
        print('------------------------')
        
        print('Power:', i.getPower())
        print('Energy consumption rate:', i.getEnergyConsumption())
        print('Bandwidth:', i.getBandwidth())
        print('Node health:', i.getStatus())
        print('Node security:', i.getMode())
        
# Construct IoT devices (name, power, consumption rate, bandwidth, security status, security mode)
device1 = Node('Laptop_1', 100, 2, 20.45, nodeStatus.VULNERABLE, nodeMode.PASSIVE)
device2 = Node('Cell_phone_1', 98, 4, 13.30, nodeStatus.REPAIRED, nodeMode.PASSIVE)

# Initialize BAN with previously-constructed IoT devices
ban = [device1, device2]

# Construct network
network = Network(ban, True)

displayNetwork(network)