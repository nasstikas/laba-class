#ifndef PERSON_H
#define PERSON_H
#include <iostream>
using namespace std;

class Person {
private:
	string name;
	int phone_number;
	int age;
	string email;
public:
	string getEmail() {
		return email;
	}
	string getName() {
		return name;
	}
	int getAge() {
		return age;
	}
	int getPhone() {
		return phone_number;
	}
	void setName(string& name) {
		this->name = name;
	}
	void setPhone(int phone) {
		this->phone_number = phone;
	}
	void setEmail(string& email) {
		this->email = email;
	}
	void setAge(int age) {
		this->age = age;
	}
	Person() {
		name = string("No name");
		email = string("example@qmail.com");
		age = 0;
		phone_number = 0;
	}
	Person(string& name, int phone_number, int age, string& email) {
		this->name = name;
		this->phone_number = phone_number;
		this->email = email;
		this->age = age;
	}
};
#endif //PERSON_H

