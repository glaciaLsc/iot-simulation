#include <string>
#include <vector>
#include "cloud.h"

void Cloud::addNode(Node node)
{
	ban.push_back(node);
}
void Cloud::setConnection(bool b)
{
	isUp = b;
}

// Constructor
Cloud::Cloud(void)
{
}
Cloud::Cloud(std::vector<Node> nodes)
{
	ban = nodes;
}

// Accessors
std::vector<Node> Cloud::getBan()
{
	return ban;
}
bool Cloud::getConnection()
{
	return isUp;
}
