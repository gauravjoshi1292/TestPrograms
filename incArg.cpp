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
	int n,i,ans=0;
	char k;
	vector<char>v;
	cin>>n;
	for(i=0;i<n;i++){
		cin>>k;
		v.push_back(k);
	}

	for(i=0;i<v.size();i++){
		if(v[i]=='0'){
			ans+=1;
			break;
		}
		else{
			ans+=1;
		}
	}
	cout<<ans<<endl;
	return 0;
}