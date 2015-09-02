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

bool is_bad_spot(long long int i, vector<long long int> s){
	// cout<<i<<" "<<s[i]<<" "<<s[i+1]<<endl;
	if(i%2 == 0){
		if(s[i] >= s[i+1]){
			// cout<<"trye odd"<<endl;
			return true;
		}
	}
	else{
		if(s[i] <= s[i+1]){
			// cout<<"true even"<<endl;
			return true;
		}
	}
	// cout<<"s"<<endl;
	// i++;
	return false;
}

bool has_bad_spots(long long int idx_a, long long int idx_b, vector<long long int> v, vector<long long int>bad_spots){
	long long int i,j,p;
	vector<long long int> points;

	points.push_back(idx_a-1);
	points.push_back(idx_a);
	points.push_back(idx_a+1);
	points.push_back(idx_b-1);
	points.push_back(idx_b);
	points.push_back(idx_b+1);

	for(i=0;i<bad_spots.size();i++){
		if(find(points.begin(), points.end(), bad_spots[i])==points.end()){
			return true;
		}
	}

	for(i=0;i<points.size();i++){
		p = points[i];
		if(p == v.size()-1){
			p--;
		}

		if(p >= 0 && p < v.size()-1){
			if(is_bad_spot(p, v)){
				return true;
			}
		}
	}

	return false;
}

vector<long long int> find_bad_spots(vector<long long int>v){
	long long int i,j,k;
	vector<long long int> bad_spots;

	for(i=0;i<=v.size()-2;i++){
		// cout<<"i:"<<i<<" "<<v[i]<<" "<<v[i+1]<<endl;
		if(is_bad_spot(i, v)){
			// cout<<"pushing"<<endl;
			bad_spots.push_back(i);
		}
		// cout<<"pushed "<<v.size()<<endl;
	}
	// cout<<"return";
	return bad_spots;

}

set<long long int> create_swap_spots(vector<long long int> bad_spots, long long int sz){
	long long int i, idx;
	set<long long int> swap_spots;

	for(i=0;i<bad_spots.size();i++){
		idx = bad_spots[i];
		if(idx==0){
			swap_spots.insert(idx);
			swap_spots.insert(idx+1);
		}

		else if(idx==sz){
			swap_spots.insert(idx-1);
			swap_spots.insert(idx);
		}

		else{
			swap_spots.insert(idx-1);
			swap_spots.insert(idx);
			swap_spots.insert(idx+1);
		}
	}

	return swap_spots;
}

typedef struct
{
	long long int x;
	long long int y;
}point;

bool contains(vector<point> v, point a){
	long long int i;
	point b;
	for(i=0;i<v.size();i++){
		b = v[i];
		if(a.x == b.x and a.y == b.y){
			return true;
		}
	}
	return false;
}

int main(){
	long long int i,j,k,n,count=0,idx_a, idx_b, tmp;
	vector<long long int>v, bad_spots;
	vector<point> swaps;
	set<long long int> swap_spots;
	set<long long int>::iterator it_a, it_b;
	cin>>n;

	for(i=0;i<n;i++){
		cin>>j;
		v.push_back(j);
	}

	bad_spots = find_bad_spots(v);

	// for(i=0;i<bad_spots.size();i++){
	// 	cout<<bad_spots[i]<<" ";
	// }
	// cout<<endl;

	// cout<<bad_spots.size()<<endl;

	if(bad_spots.size() > 4){
		cout<<0<<endl;
		return 0;
	}

	else if(bad_spots.size() == 4){
		// cout<<"else if"<<endl;
		swap_spots = create_swap_spots(bad_spots, v.size()-1);
		// cout<<"created swap spots"<<endl;
		for(it_a=swap_spots.begin();it_a!=--swap_spots.end();it_a++){
			for(it_b=++it_a;it_b!=swap_spots.end();it_b++){
				idx_a = *it_a;
				idx_b = *it_b;

				tmp = v[idx_a];
                v[idx_a] = v[idx_b];
                v[idx_b] = tmp;

                if(!has_bad_spots(idx_a, idx_b, v, bad_spots)){
                	count++;
                }

                tmp = v[idx_a];
                v[idx_a] = v[idx_b];
                v[idx_b] = tmp;
			}
		}
	}

	else{
		swap_spots = create_swap_spots(bad_spots, v.size()-1);
		for(it_a=swap_spots.begin();it_a!=swap_spots.end();it_a++){
			for(i=0;i<v.size();i++){
				idx_a = *it_a;
				idx_b = i;

				if(idx_a>idx_b){
					tmp = idx_a;
					idx_a = idx_b;
					idx_b = tmp;
				}

				if(idx_a == idx_b)
					continue;

				tmp = v[idx_a];
                v[idx_a] = v[idx_b];
                v[idx_b] = tmp;

                if(!has_bad_spots(idx_a, idx_b, v, bad_spots)){
                	point sp;
                	sp.x = idx_a;
                	sp.y = idx_b;
                	if(!contains(swaps, sp)){
                		count++;
                		swaps.push_back(sp);	
                	}
                }

                tmp = v[idx_a];
                v[idx_a] = v[idx_b];
                v[idx_b] = tmp;
			}
		}
	}

	// for(it_a=swap_spots.begin();it_a!=swap_spots.end();it_a++){
	// 	cout<<*it_a<<" ";
	// }
	// cout<<endl;

	cout<<count<<endl;
	return 0;
}