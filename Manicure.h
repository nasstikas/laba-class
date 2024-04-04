#ifndef MANICURE_H
#define MANICURE_H
#include <iostream>
using namespace std;

class Manicure {
private:
	string type;
	int ex_time;
	int price;
public:
	string getType() {
		return type;
	}
	void setType(string& type) {
		this->type = type;
		if (type == "French") {
			price = 1500;
			ex_time = 180;
		}
		else if (type == "Plain color") {
			price = 1000;
			ex_time = 90;
		}
		else if (type == "Stamping") {
			price = 1150;
			ex_time = 120;
		}
		else {
			price = 1300;
			ex_time = 150;
		}
	}
	int getEx_Time() {
		return ex_time;
	}
	void setEx_Time(int ex_time) {
		this->ex_time = ex_time;
	}
	int getPrice() {
		return price;
	}
	void setPrice(int price) {
		this->price = price;
	}
	Manicure() {
		type = "Plain color";
		ex_time = 90;
		price = 1000;
	}
	Manicure(string& type, int price) {
		this->type = type;
		if (type == "French") {
			ex_time = 180;
		}
		else if (type == "Plain color") {
			ex_time = 90;
		}
		else if (type == "Stamping") {
			ex_time = 120;
		}
		else {
			ex_time = 150;
		}
		this->price = price;
	}
};

#endif //MANICURE_H
