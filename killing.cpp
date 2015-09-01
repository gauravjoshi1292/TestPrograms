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
#include <ctime>

using namespace std;

int main(){
	int i,j,s;
	vector<int>v;
	for(i=0;i<100;i++){
		v.push_back(i+1);
	}
	
	i = 0;
	while(v.size()>1){
		cout<<"knife = "<<v[i];
		cout<<" dead = "<<v[(i+1)%v.size()]<<endl;
		s = v.size();
		v.erase(v.begin()+(i+1)%v.size());
		i++;
		i%=s;
	}
	cout<<"ans = "<<v[0]<<"size = "<<v.size()<<endl;
	return 0;
}