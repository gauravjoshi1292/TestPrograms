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
	int n,p,q,i,j,ans=0;
	cin>>n;
	for(i=0;i<n;i++){
		cin>>p>>q;
		if(q-p > 1){
			ans++;
		}
	}
	cout<<ans<<endl;
	return 0;
}