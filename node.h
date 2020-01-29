enum nodeStatus {compromised, vulnerable, repaired};
enum nodeMode {passive, secure};

class Node
{
	public:
		// Methods
		void setName(std::string str);
		void setPower(int n);
		void setConsumptionRate(int n);
		void setConnection(bool b);
		void setStatus(enum nodeStatus s);
		void setMode(enum nodeMode m);

		// Constructor
		Node();
		Node(std::string str, int n, int n2, bool b, enum nodeStatus s, enum nodeMode m);

		// Accessors
		std::string getName();
		int getPower();
		int getConsumptionRate();
		bool getConnection();
		enum nodeStatus getStatus();
		enum nodeMode getMode();
	private:
		// Data
		std::string name;
		int power;
		int consumptionRate;
		bool isConnected;
		enum nodeStatus status;
		enum nodeMode mode;
};
