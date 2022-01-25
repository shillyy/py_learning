#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;

int main() {
	int obl=0,a,b,w;
	cout << "Jakie obliczenia chcesz wykonac?" << endl;
	cout << "(1) Dodawanie" << endl;
	cout << "(2) Odejmowanie" << endl;
	cout << "(3) Mnozenie" << endl;
	cout << "(4) Dzielenie" << endl;
	cout << "(5) Potegowanie" << endl;
	cout << "(6) Pierwiastkowanie" << endl;
	cout << "Zeby wyjsc, wpisz dowonly, inny znak" << endl;
	cin >> obl;
	if (obl==1){
		cout << "Podaj pierwsza liczbe" << endl;
		cin >> a;
		cout << "Podaj druga liczbe" << endl;
		cin >> b;
		w=a+b;
		cout << "Wynik to: " << w << endl;
	} else if (obl==2){
		cout << "Podaj pierwsza liczbe" << endl;
		cin >> a;
		cout << "Podaj druga liczbe" << endl;
		cin >> b;
		w=a-b;
		cout << "Wynik to: " << w << endl;	
	} else if (obl==3){
		cout << "Podaj pierwsza liczbe" << endl;
		cin >> a;
		cout << "Podaj druga liczbe" << endl;
		cin >> b;
		w=a*b;
		cout << "Wynik to: " << w << endl;	
	} else if (obl==4){
		cout << "Podaj pierwsza liczbe" << endl;
		cin >> a;
		cout << "Podaj druga liczbe" << endl;
		cin >> b;
		w=a/b;
		cout << "Wynik to: " << w << endl;	
	} else if (obl==5){
		
	} else if (obl==6){
	
	}else {
		cout << "Oki to pa" << endl;
	}
	return 0;
}
