import network
from network import Network
from network import node
from node import Node
from node import nodeMode
from node import entity
from entity import Entity
from entity import nodeNature
        
# Construct IoT devices (name, consumption rate, hasIdentifiables,
# hasPasswords,hasBiometrics, hasTelemetry, hasMiscellaneous, security mode)
# As well as unidentified Entities(name, nature, utility)
device1 = Node('Laptop_1', 2, True, True, False, True, True)
device2 = Node('MP3_Player_1', 4, False, False, False, True, True)

# Initialize BAN with previously-constructed IoT devices
ban = [device1, device2]

# Construct network
network = Network(ban)
# Display network
network.display()

# Run simulation of communication within BAN-- lasts until all known Benevolent
# nodes are depleted of power.
#@param: Arbitrary threshold
network.runSimulation(100, 0.5000)