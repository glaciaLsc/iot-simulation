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
        print('Queue size:', i.getQueueSize())
        print('Bandwidth:', i.getBandwidth())
        print('Data sensitivity:', i.getDataSensitivity())
        print('Node health:', i.getStatus())
        print('Node security:', i.getMode())
        print()
        
# Construct IoT devices (name, power, consumption rate, bandwidth, hasIdentifiables,
# hasPasswords,hasBiometrics, hasTelemetry, hasMiscellaneous, security status, security mode)
device1 = Node('Laptop_1', 100, 2, 20.45, True, True, False, True, True, nodeStatus.VULNERABLE, nodeMode.PASSIVE)
device2 = Node('Cell_phone_1', 98, 4, 13.30, False, True, False, True, False, nodeStatus.REPAIRED, nodeMode.PASSIVE)

# Initialize BAN with previously-constructed IoT devices
ban = [device1, device2]

# Construct network
network = Network(ban, True)

displayNetwork(network)