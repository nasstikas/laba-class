#include <iostream>
#include "Person.h"
#include "Master.h"
#include "Worker.h"
#include "Client.h"
#include "Manicure.h"
using namespace std;
int main()
{
	string name1("Anastasia");
	string email("no email");
	string type("French");
	string a;
	//cin >> a;

	Master Anastasia(name1, 999, 19, email, 20000, 4, type, 1300, 3);
	
	
	//Anastasia.setName(a);
	cout << "name: " << Anastasia.getName() << endl;
	cout << "phone number: " << Anastasia.getPhone() << endl;
	cout << "age: " << Anastasia.getAge() << endl;
	cout << "email: " << Anastasia.getEmail() << endl;
	cout << "salary: " << Anastasia.getSalary() << endl;
	cout << "tax rate: " << Anastasia.getTaxRate() << endl;
	cout << "experience: " << Anastasia.getExperience() << endl;
	cout << "cost: " << Anastasia.getCost() << endl;
	cout << "type: " << Anastasia.getType() << endl;
	cout << "execution time: " << Anastasia.getEx_Time() << endl;
	cout << "price: " << Anastasia.getPrice() << endl;
	cout << "efficiency: " << Anastasia.getEfficiency() << endl;

	string name2("Ulyana");
	string day("Friday");
	Client Ulyana;
	//Client Ulyana(name2, 555, 18, email, type, 0, 0, day, 17);
	Ulyana.setType(type);
	cout << Ulyana.getType() << " " << Ulyana.getPrice() << " " << Ulyana.getEx_Time() << endl;
}