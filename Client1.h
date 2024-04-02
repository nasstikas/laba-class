#ifndef CLIENT1_H
#define CLIENT1_H
#include "Person.h"
#include "Manicure.h"
#include <iostream>

class Client : public Person, public Manicure {
private:
	string day;// в какой день запись
	int time;//во сколько записан на маникюр
public:
	Client() {
		time = 0;
		day = "Monday";
	}
	Client(string& name, int& phone_number, int& age, string& email, string& type, int& ex_time, int& price, string& day, int& time)
		:Person(name, phone_number, age, email), Manicure(type, ex_time, price) {
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
};



#endif //CLIENT1_H