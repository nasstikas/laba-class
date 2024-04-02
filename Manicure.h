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
	Manicure(string& type, int& ex_time, int& price) {
		this->type = type;
		this->ex_time = ex_time;
		this->price = price;
	}
};

#endif //MANICURE_H