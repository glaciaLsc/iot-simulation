#include <iostream>
#include <string>
#include <vector>
#include "cloud.h"

void print(std::vector<Node> ban)
{
	std::cout << "\n";
	for (int i=0; i < ban.size(); i++)
	{
		std::cout << ban.at(i).getName() << std::endl;
		std::cout << "------------" << std::endl;

		std::cout << "Power: " << ban.at(i).getPower() << std::endl;
		std::cout << "Consumption: " << ban.at(i).getConsumptionRate() << std::endl;
		std::cout << "Connection: " << ban.at(i).getConnection() << std::endl;
		std::cout << "Health: " << ban.at(i).getStatus() << std::endl;
		std::cout << "Security mode: " << ban.at(i).getMode() << std::endl;
		std::cout << "\n";
	}
}

int main()
{
	// Construct IoT devices (power, consumption, connection, status, security)
	Node device1("Laptop 1", 100, 2, true, vulnerable, passive);
	Node device2("Cell phone 1", 98, 4, true, repaired, passive);
	
	// Initialize BAN
	std::vector<Node> ban;
	
	// Add nodes to BAN
	ban.push_back(device1);
	ban.push_back(device2);

	// Construct cloud
	Cloud cloud(ban);
	
	// Print network
	print(ban);

	return 0;
}
