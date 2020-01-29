#include <vector>
#include "node.h"

class Cloud
{
	public:
		// Methods
		void addNode(Node node);
		void setConnection(bool b);

		// Constructor
		Cloud();
		Cloud(std::vector<Node> nodes);
		
		// Accessors
		std::vector<Node> getBan();
		bool getConnection();
	private:
		// Data
		std::vector<Node> ban;
		bool isUp;
};
