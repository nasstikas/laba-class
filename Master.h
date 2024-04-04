#ifndef MASTER_H
#define MASTER_H
#include "Worker.h"
#include "Manicure.h"
#include <iostream>
using namespace std;

class Master : public Worker, public Manicure {
private:
	int cost;
	int efficiency;
public:
	Master() {
		cost = 0;
		efficiency = 0;
	}
	Master(string& name, int phone_number, int age, string& email, double salary, int experience, string& type, int price, int efficiency)
		:Worker(name, phone_number, age, email, salary, experience), Manicure(type, price) {
		this->efficiency = efficiency;
		if (experience >= 5) {
			cost = 1000 + price;
		}
		else {
			cost = 500 + price;
		}
	}
	int getCost() {
		return cost;
	}
	int getEfficiency() {
		return efficiency;
	}
	void setCost(int cost) {
		this->cost = cost;
	}
	void setEfficiency(int efficiency) {
		this->efficiency = efficiency;
	}
	friend ostream& operator << (ostream& os, Master& master) {

		os << "Name:" << master.getName() << endl;
		os << "Phone number: " << master.getPhone() << endl;
		os << "Age: " << master.getAge() << endl;
		os << "Email: " << master.getEmail() << endl;
		os << "Salary: " << master.getSalary() << endl;
		os << "Experience: " << master.getExperience() << endl;
		os << "Manicure type: " << master.getType() << endl;
		os << "Execution time: " << master.getEx_Time() << endl;
		os << "Price: " << master.getPrice() << endl;
		os << "Efficiency: " << master.getEfficiency() << endl;
		os << "Cost: " << master.getCost() << endl;
		return os;
	}

};
#endif //MASTER_H
