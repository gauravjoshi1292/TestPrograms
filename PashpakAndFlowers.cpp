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
    long long int n,i,k,ans;
    vector<long long int>v;
    cin>>n;
    for(i=0;i<n;i++){
        cin>>k;
        v.push_back(k);
    }

    long long int x=0,y=0;

    long long int max=*max_element(v.begin(), v.end());
    long long int min=*min_element(v.begin(), v.end());

    if(max==min){
        ans=n*(n-1)/2;
        cout<<0<<" "<<ans;
        return 0;
    }

    x += count(v.begin(), v.end(), min);
    y += count(v.begin(), v.end(), max);
    ans=x*y;
    cout<<(max-min)<<" "<<ans;
    return 0;
}