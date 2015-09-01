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

void nextPerm(string s, int start, int end, int p){
	string retVal;
	int i,j,k;
	for(i=end-1;i>=start;i++){
		s[i] = s[i] + 1;
		if(s[i]-'a' == p-1){
			s[i] = 'a';
			nextPerm(s, start-1, end);
		}
	}
}

int main(){
	int n,p,i,j,k;
	string s;
	cin>>n>>p;
	cin>>s;
	for(i=s.size()-1;i>=0;i++){
		s = nextPerm(s, s.size()-1, s.size(), p);
	}
	return 0;
}