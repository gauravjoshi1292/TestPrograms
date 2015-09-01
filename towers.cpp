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

struct tower
{
	int height;
	int index;
};

typedef struct tower tower;

bool cmp(tower t1, tower t2){
	return t1.height < t2.height;
}

int main(){
	vector<tower> v;
	vector<int> a,b;
	int i,j,k,n,c,diff,ans=0;
	
	cin>>n>>k;

	for(i=0;i<n;i++){
		tower t;
		cin>>t.height;
		t.index = i+1;
		v.push_back(t);
	}

	if(n==1){
		cout<<0<<" "<<0<<endl;
		return 0;
	}

	if(k==0){
		diff = (*max_element(v.begin(), v.end(), cmp)).height - (*min_element(v.begin(), v.end(), cmp)).height;
		cout<<diff<<" "<<0<<endl;
		return 0;
	}
	
	// cout<<"n = "<<n<<" k = "<<k<<endl;
	for(i=0;i<k;i++){
		sort(v.begin(), v.end(), cmp);
		reverse(v.begin(), v.end());

		v[0].height--;
		v[v.size()-1].height++;

		if((v[0].height-v[v.size()-1].height) < 0){
			v[0].height++;
			v[v.size()-1].height--;
			break;
		}

		a.push_back(v[0].index);
		b.push_back(v[v.size()-1].index);
		ans++;

		// for(j=0;j<v.size();j++){
		// 	cout<<v[j].height<<" ";
		// }
		// cout<<endl;
	}
	
	diff = (*max_element(v.begin(), v.end(), cmp)).height - (*min_element(v.begin(), v.end(), cmp)).height;
	cout<<diff<<" "<<ans<<endl;

	for(i=0;i<a.size();i++){
		cout<<a[i]<<" "<<b[i]<<endl;
	}

	return 0;
}