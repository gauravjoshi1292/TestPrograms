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

struct date
{
	/* data */
	int a;
	int b;
};

typedef struct date date;

bool cmp(date d1, date d2){
	if(d1.a != d2.a)
		return d1.a < d2.a;
	else
		return d1.b < d2.b;
}

int main(){
	int i,j,k,n,c,ans=0;
	vector<date> v;

	cin>>n;

	for(i=0;i<n;i++){
		date d;
		cin>>d.a>>d.b;
		v.push_back(d);
	}

	sort(v.begin(), v.end(), cmp);

	int prev_date = 0;
	for(i=0;i<v.size();i++){
		// cout<<v[i].a<<" "<<v[i].b<<endl;
		// cout<<"prev_date = "<<prev_date<<endl;
		if(v[i].b >= prev_date){
			prev_date = v[i].b;
		}
		else{
			prev_date = v[i].a;
		}
	}
	cout<<prev_date<<endl;
	return 0;
}