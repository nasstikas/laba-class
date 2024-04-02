#ifndef MASTER_H
#define MASTER_H
#include "Person.h"
#include "Manicure.h"
#include <iostream>

class Master: public Person, public Manicure{
private:
	int cost;
	int experience;
public:
	Master() {
		cost = 0;
		experience = 0;
	}
	Master(string& name, int& phone_number, int& age, string& email, string& type, int& ex_time, int& price, int& cost, int& experience)
		:Person(name, phone_number, age, email), Manicure(type,ex_time,price)  {
		this->experience = experience;
		if (experience > 5) {
			cost = 1000 + price;
		}
		else{
			cost = 500 + price;
		}
	}
	int getCost() {
		return cost;
	}
	int getExperience() {
		return experience;
	}
	void setCost(int cost) {
		this->cost = cost;
	}
	void setExperience(int experience) {
		this->experience = experience;
	}

};
#endif //MASTER_H