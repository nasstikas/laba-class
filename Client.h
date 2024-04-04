#ifndef CLIENT_H
#define CLIENT_H
#include "Person.h"
#include "Manicure.h"
#include <iostream>
using namespace std;

class Client : public Person, public Manicure {
private:
	string day;
	int time;
public:
	Client() {
		time = 0;
		day = "Monday";
	}
	Client(string& name, int phone_number, int age, string& email, string& type, int price, string& day, int time)
		:Person(name, phone_number, age, email), Manicure(type, price) {
		this->day = day;
		this->time = time;
	}
	
	string getDay() {
		return day;
	}
	void setDay(string& day) {
		this->day = day;
	}
	int getTime() {
		return time;
	}
	void setTime(int time) {
		this->time = time;
	}
	friend ostream& operator << (ostream& os, Client& client) {

		os << "Name:" << client.getName() << endl;
		os << "Phone number: " << client.getPhone() << endl;
		os << "Age: " << client.getAge() << endl;
		os << "Email: " << client.getEmail() << endl;
		os << "Manicure type: " << client.getType() << endl;
		os << "Execution time: " << client.getEx_Time() << endl;
		os << "Price: " << client.getPrice() << endl;
		os << "Day of appointment: " << client.getDay() << endl;
		os << "Time of appointment: " << client.getTime() << endl;

		return os;
	}
};

#endif //CLIENT_H

