#ifndef WORKER_H
#define WORKER_H
#include "Person.h"
#include <iostream>
using namespace std;

class Worker : public Person {
private:
	double salary;
	int tax_rate;
	int experience;
public:
	Worker() {
		salary = 0;
		tax_rate = 0;
		experience = 0;
	}
	Worker(string& name, int phone_number, int age, string& email, double salary, int experience)
		:Person(name, phone_number, age, email) {
		this->salary = salary;
		if (salary > 1000) {
			tax_rate = 13;
		}
		else {
			tax_rate = 10;
		}
		this->experience = experience;

	}
	double getSalary() {
		return salary;
	}
	void setSalary(double salary) {
		this->salary = salary;
	}
	int getTaxRate() {
		return tax_rate;
	}
	void setTaxRate(int tax_rate) {
		this->tax_rate = tax_rate;
	}
	double getNETsalary() {
		return salary * (100 - tax_rate) * 0.01;
	}
	int getExperience() {
		return experience;
	}
	void setExperience(int experience) {
		this->experience = experience;
	}
};
#endif //WORKER_H