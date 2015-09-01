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
	int n,i,j,ans=0;
	vector<int>v;
	cin>>n;
	for(i=0;i<n;i++){
		cin>>j;
		v.push_back(j);
	}
	
	j=0;
	for(i=0;i<v.size();i++){
		if(v[i] == 1 && j == 0){
			if(ans > 0){
				ans++;
			}
			ans++;
			j=1;
		}
		else if(v[i] == 1 && j == 1){
			ans++;
		}
		else if(v[i] == 0){
			j=0;
		}
	}
	cout<<ans<<endl;
	return 0;
}