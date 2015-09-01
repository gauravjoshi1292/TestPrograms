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

int main(){
    int n,i,j,k,maxi;
    cin>>n;
    vector<int> v,sl,sr,cl,cr;

    v.push_back(0);
    for(i=1;i<=n;i++){
        cin>>k;
        v.push_back(k);
    }

    maxi = *max_element(v.begin(), v.end());
    for(i=0;i<=maxi;i++){
        cl.push_back(0);
    }

    sl.push_back(0);
    for(i=1;i<v.size();i++){
        // cout<<"i = "<<i<<endl;
        cl[v[i]]++;
        sl.push_back(cl[v[i]]);
    }
    cl.clear();

    // for(i=1;i<sl.size();i++){
    //     cout<<"i = "<<i<<" "<<sl[i]<<endl;
    // }
    // cout<<endl;

    for(i=0;i<=maxi;i++){
        cr.push_back(0);
    }

    for(i=v.size()-1;i>0;i--){
        // cout<<"i = "<<i<<endl;
        cr[v[i]]++;
        sr.insert(sr.begin(), cr[v[i]]);
    }
    sr.insert(sr.begin(), 0);
    cr.clear();

    // for(i=1;i<sr.size();i++){
    //     cout<<"i = "<<i<<" "<<sr[i]<<endl;
    // }

    int ans = 0;
    for(i=1;i<sl.size()-1;i++){
        for(j=i+1;j<sr.size();j++){
            if(sl[i] > sr[j]){
                ans++;
            }
        }
    }
    cout<<ans<<endl;
}