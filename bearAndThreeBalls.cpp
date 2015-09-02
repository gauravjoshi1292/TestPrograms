#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>

using namespace std;

int main(){
	// cout<<"Start"<<endl;
	int n,i,j;
	std::vector<int> v;
	std::vector<int>::iterator end;

	// cout<<"input n"<<endl;
	cin>>n;

	// cout<<n<<endl;

	for(i=0;i<n;i++){
		cin>>j;
		// cout<<"j:"<<j<<endl;
		v.push_back(j);
	}
	
	// cout<<"Input done";

	sort(v.begin(), v.end());
	end = unique(v.begin(), v.end());
	
	int f = 0;
	for(i=0;i<v.size()-2;i++){
		if(v[i+1] - v[i] == 1 and v[i+2] - v[i+1] == 1){
        	cout<<"YES"<<endl;
        	f = 1;
        	break;
        }
	}

	if(f==0){
		cout<<"NO"<<endl;
	}

	return 0;
}