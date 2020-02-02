#include <string>
#include "node.h"

void Node::setName(std::string str)
{
	name = str;
}
void Node::setPower(int n)
{
	power = n;
}
void Node::setConsumptionRate(int n)
{
	consumptionRate = n;
}
void Node::setConnection(bool b)
{
	isConnected = b;
}
void Node::setStatus(enum nodeStatus s)
{
	status = s;
}
void Node::setMode(enum nodeMode m)
{
	mode = m;
}

// Constructor
Node::Node(void)
{
}
Node::Node(std::string str, int n, int n2, bool b, enum nodeStatus s, enum nodeMode m)
{
	name = str;
	power = n;
	consumptionRate = n2;
	isConnected = b;
	status = s;
	mode = m;
}

// Accessors
std::string Node::getName()
{
	return name;
}
int Node::getPower()
{
	return power;
}
int Node::getConsumptionRate()
{
	return consumptionRate;
}
bool Node::getConnection()
{
	return isConnected;
}
enum nodeStatus Node::getStatus()
{
	return status;
}
enum nodeMode Node::getMode()
{
	return mode;
}
