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
	long long int i,j,k,n,ans=0;
	double sum,s1;
	cin>>n;
	vector<long long int>v;
	vector<long long int>s;
	vector<long long int>c;

	sum = 0;
	for(i=0;i<n;i++){
		cin>>j;
		sum += j;
		v.push_back(j);
		s.push_back(0);
	}

	if(n<3){
		cout<<0<<endl;
		return 0;
	}

	k=0;s1=0;

	for(i=n-1;i>1;i--){
		k+=v[i];
		if(k==sum/3){
			s1++;
		}
		s[i]=s1;
	}

	s1=0;
	for(i=0;i<n-2;i++){
		s1+=v[i];
		if(s1==sum/3){
			ans+=s[i+2];
		}
	}

	cout<<ans<<endl;
	return 0;
}