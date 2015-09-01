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
	long long int n,i,j,k,l,ans;
	long long int max = 1000000000 + 7;
	
	vector<string>v;
	vector<long long int>a;
	string s,tmp,rep,sub;
	cin>>s;
	cin>>n;

	for(i=0;i<10;i++){
		tmp = "";
		tmp.push_back('0'+i);
		v.push_back(tmp);
	}
	
	for(i=0;i<n;i++){
		char t;
		string s1;
		cin>>s1;
		j = s1[0]-'0';
		tmp = "";
		for(k=3;k<s1.size();k++){
			tmp.push_back(s1[k]);
		}
		t = '0'+j;
		for(j=0;j<10;j++){
			rep = "";
			for(k=0;k<v[j].size();k++){
				if(v[j][k]==t){
					for(l=0;l<tmp.size();l++){
						rep.push_back(tmp[l]);
					}
				}
				else{
					rep.push_back(v[j][k]);
				}
			}
			v[j] = rep;
		}
	}

	for(i=0;i<10;i++){
		k=1;
		ans=0;
		if(v[i].size()>0){
			for(j=v[i].size()-1;j>=0;j--){
				ans += (((v[i][j]-'0')%max)*(k%max))%max;
				ans %= max;
				k = (k*10)%max;
			}
		}
		a.push_back(ans);
	}
	
	ans=0;
	k=1;
	int indx;
	for(i=s.size()-1;i>=0;i--){
		indx = s[i]-'0';
		ans += ((a[indx]%max) * (k%max)) % max;
		ans %= max;
		for(j=0;j<v[indx].size();j++){
			k *= 10;
			k %= max;
		}
	}

	cout<<ans<<endl;
	return 0;
}