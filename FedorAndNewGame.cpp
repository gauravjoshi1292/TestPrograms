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

int countBits(int num){
	int i,j,k,retVal=0;
	while(num){
		retVal += num & 1;
		num >>= 1;
	}
	return retVal;
}

int main(){
	int n,m,f,k,i,j,ans=0;
	cin>>n>>m>>k;
	vector<int>v;

	for(i=0;i<m;i++){
		cin>>j;
		v.push_back(j);
		
	}
	cin>>f;
	

	for(i=0;i<v.size();i++){
		j = v[i]^f;
		j = countBits(j);
		if(j<=k){
			ans++;
		}
	}
	cout<<ans<<endl;
	return 0;
}