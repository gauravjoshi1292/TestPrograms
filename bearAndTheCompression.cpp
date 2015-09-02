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

std::map<string, string> dp;

string compression(string s){
	if(s.size() == 1){
		return s;
	}

	// cout<<"s: "<<s<<" dp[s]: "<<dp[s]<<endl;
	if(dp[s].size()>=1){
		return dp[s];
	}
	return s;
}

string collapse(string s){
	if(s.size() == 1){
		return s;
	}

	if(s.size() == 2){
		return compression(s);
	}

	// cout<<s.substr(0, 2);

	string cs = compression(s.substr(0, 2)) + s.substr(2, s.size());
	if(cs.size() < s.size()){
		return collapse(cs);
	}
	else{
		return s;
	}
}


int main(){
	int i, k, n, m, q, count;
	set <string> y, ycp;
	set <string> :: iterator j;
	std::vector<string> st;
	std::map<string, string> :: iterator it;
	st.push_back("a");
	st.push_back("b");
	st.push_back("c");
	st.push_back("d");
	st.push_back("e");
	st.push_back("f");

	y.insert("a");y.insert("b");y.insert("c");y.insert("d");y.insert("e");y.insert("f");


	cin>>n>>q;

	// cout<<n<<" "<<q<<endl;

	for(i=0;i<q;i++){
		string a, b;
		cin>>a>>b;
		// cout<<a<<" "<<b<<endl;
		dp[a] = b;
	}

	for(i=1;i<n;i++){
		// cout<<"i:"<<i<<endl;
		ycp.insert(y.begin(), y.end());
		for(j=ycp.begin();j!=ycp.end();j++){
			string key = *j;
			
			// cout<<"key:"<<key<<endl;

			for(k=0;k<st.size();k++){
				string c = st[k];
				
				// cout<<"key:"<<key<<"c:"<<c<<endl;

				for(m=0;m<key.size();m++){
					string new_key = key.substr(0, m) + c + key.substr(m, key.size());
					string val = collapse(new_key);

					// cout<<new_key<<val<<endl;
					dp[new_key] = val;
			
					y.insert(new_key);
				}
			}
		}
		
	}

	for(it=dp.begin(); it!=dp.end(); it++){
		string key = it->first;
		string val = it->second;
		if(key.size() == n and val == "a"){
			// cout<<key<<" "<<val<<endl;
        	count++;
		}
	}
    

	cout<<count<<endl;

	return 0;
}