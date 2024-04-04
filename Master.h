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
	Master(string& name, int phone_number, int age, string& email, double salary,  int experience, string& type, int price, int efficiency)
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

};
#endif //MASTER_H
