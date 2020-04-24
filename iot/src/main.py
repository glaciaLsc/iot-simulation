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
device1 = Node('Laptop_1', 2, True, True, True, True, True)
device2 = Node('Cell_Phone_1', 3, False, True, True, True, True)
device3 = Node('MP3_Player_1', 4, False, False, False, True, True)
device4 = Node('Pager_1', 5, False, False, False, False, False)
# Open file for writing results
output = open("../outputs/results_highbenevolent_highthreshold.txt", "a+")

totalBenefit = 0
for i in range(10000):
    # Initialize BAN with previously-constructed IoT devices
    ban = [device1, device2, device3, device4]
    # Construct network
    network = Network(ban)
    
    # Run simulation of communication within BAN-- lasts until all known Benevolent
    # nodes are depleted of power.
    #@param: Number of random entities, Arbitrary threshold
    network.runSimulation(ban.__len__()*100, 0.5000)
    #print(network.getOverallBenefit())
    
    # Log results
    totalBenefit += network.getOverallBenefit()
    # Append results to file
    output.write(str(network.getOverallBenefit()) + '\n')

# Append final average to file    
output.write('\n' + "Average benefit: " + str(totalBenefit / i))