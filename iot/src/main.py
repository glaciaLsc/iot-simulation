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
device1 = Node('Laptop_1', 1, True, True, False, True, True)
entity1 = Entity('CISCO Router', nodeNature.MALICIOUS, 0.3)

# Initialize BAN with previously-constructed IoT devices
ban = [device1]

# Construct network
network = Network(ban)
# Display network
network.display()

# Run simulation of communication within BAN-- lasts until all known Benevolent
# nodes are depleted of power.
#@param: Arbitrary threshold
network.runLoop(0.2500)