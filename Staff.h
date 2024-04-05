#ifndef STAFF_H
#define STAFF_H
#include "worker.h"

class Staff : public Worker {
private:
	string position;
public:
	Staff() {
		position = "administrator";
	}
	Staff(string& name, int phone_number, int age, string& email, double salary, int experience, string& position)
		:Worker(name, phone_number, age, email, salary, experience) {
		this->position = position;
	}
	string getPosition() {
		return position;
	}
	void setPosition(string& position) {
		this->position = position;
	}
	friend ostream& operator << (ostream& os, Staff& staff) {

		os << "Name:" << staff.getName() << endl;
		os << "Phone number: " << staff.getPhone() << endl;
		os << "Age: " << staff.getAge() << endl;
		os << "Email: " << staff.getEmail() << endl;
		os << "Salary: " << staff.getSalary() << endl;
		os << "Experience: " << staff.getExperience() << endl;
		os << "Position: " << staff.getPosition() << endl;
		return os;
	}
};
#endif //STAFF_H