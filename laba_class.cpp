#include <iostream>
#include "Person.h"
#include "Master.h"
#include "Worker.h"
#include "Client.h"
#include "Manicure.h"
#include "Staff.h"
using namespace std;
int main()
{

	string name1("Anastasia");
	string email("@email.ru");
	string type("French");
	string type1("Plain color");
	string type2("Stamping");
	string name2("Ulyana");
	string day("Friday");
	string name3("Maria");
	string post("Director");
	string name4("Alexandr");
	string post1("Security");
	string name5("Olga");
	string post2("Administrator");
	string name6("Vlada");
	string post3("Сleaning lady");

	cout << "Barankina nails <3" << endl;

	cout << "_________Price list___________" << endl;

	Manicure manicure(type, 1000);
	cout << manicure << endl;

	Manicure manicure1(type1, 900);
	cout << manicure1 << endl;

	Manicure manicure2(type2, 1500);
	cout << manicure2;

	cout << "______________________________" << endl;

	Staff Maria(name3, 666, 22, email, 40000, 10, post);
	cout << Maria << endl;

	Staff Alexandr(name4, 107, 35, email, 18000, 5, post1);
	cout << Alexandr << endl;

	Staff Olga(name5, 109, 20, email, 15000, 3, post2);
	cout << Olga << endl;

	Staff Vlada(name6, 111, 18, email, 10000, 1, post3);
	cout << Vlada << endl;

	cout << "Master:" << endl;
	Master Anastasia(name1, 999, 19, email, 20000, 4, type, 1500, 3);
	cout << Anastasia << endl;
	
	cout << "Client:" << endl;
	Client Ulyana(name2, 555, 18, email, type2, 1500, day, 17);
	cout << Ulyana << endl;

	
}
