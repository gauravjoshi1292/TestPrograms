#include <iostream>
#include <cstdio>
#include <string.h>

using namespace std;

int main(){
	char name1[25];
	char name2[25];

	//Take user input
	cout<<"Please input the first name"<<endl;
	cin.getline(name1, 25);
	cout<<"Please input the second name"<<endl;
	cin.getline(name2, 25);
	
	//Compare the strings and display them in alphabetical order
	cout<<endl<<"The names are as follows"<<endl;
	if(strcmp(name1, name2) <= 0){
		cout<<name1<<endl;
		cout<<name2<<endl;
	}
	else{
		cout<<name2<<endl;
		cout<<name1<<endl;
	}

	return 0;
}