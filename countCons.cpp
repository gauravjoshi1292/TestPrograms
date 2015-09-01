#include <iostream>
#include <cstdio>
#include <string.h>

using namespace std;

int main(){
	char input[50];
	int i = 0;
	int n = 0;

	//Take user input
	cout<<"Please enter an input string of no more than 50 characters"<<endl;
	cin.getline(input, 50);
	
	//Iterate over the string and count consonents
	while(input[i]!='\0'){
		if(input[i] >= 'a' && input[i] <= 'z' || input[i] >= 'A' && input[i] <= 'Z'){
			if(input[i] == 'a' || input[i] == 'e' || input[i] == 'i' || input[i] == 'o' || input[i] == 'u'){

			}
			else if(input[i] == 'A' || input[i] == 'E' || input[i] == 'I' || input[i] == 'O' || input[i] == 'U'){

			}
			else{
				n++;
			}
		}
		i++;
	}

	//Display output
	cout<<endl<<"The input string is:"<<endl;
	cout<<input<<endl;
	cout<<endl<<"The number of consonants is "<<n<<endl;

	return 0;
}