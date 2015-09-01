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
#include <cstring>

using namespace std;

vector<long long int> convertBase(long long int n, long long int b, long long int d){
	vector<long long int> v;
	
	while(n>0){
		long long int q,r;
		r = n % b + 1;
		v.insert(v.begin(),r);
		n /= b;
	}
	
	while(v.size() < d){
		v.insert(v.begin(), 1);
	}
	
	return v;
}

int main(){
    long long int n,k,d,i,j;
    vector<long long int> v;
    vector< vector<long long int> > a;
    cin>>n>>k>>d;

    if(n-pow(k,d)>0.1){
        cout<<-1<<endl;
        return 0;
    }
    else{
    	for(i=0;i<d;i++){
    		a.push_back(vector<long long int>());
    	}
        long long int num = 0;
        
        for(i=0;i<n;i++){
        	v = convertBase(num, k, d);
        	num ++;
        	for(j=0;j<v.size();j++){
	   			a[j].push_back(v[j]);
		   	}
        }
        
        for(i=0;i<a.size();i++){
        	for(j=0;j<a[i].size();j++){
        		cout<<a[i][j]<<" ";
        	}
        	cout<<endl;
        }
    }
    return 0;
}