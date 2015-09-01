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
    long long int i,j,k,n,m,r,l,sum,ans=0;
    vector<long long int>v;
    vector<long long int>s;
    cin>>n>>m>>k;
    for(i=0;i<n;i++){
        cin>>j;
        v.push_back(j);
    }

    sum=0;
    for(i=0;i<v.size();i++){
        sum += v[i];
        s.push_back(sum);
    }

    vector< vector<long long int> >a;
    for(i=0;i<2;i++){
        a.push_back(vector<long long int>());
        for(j=0;j<n;j++){
            a[i].push_back(0);
        }
    }

    a[1][m-1] = s[m-1];

    // cout<<"all clear"<<endl;
    for(i=1;i<=k;i++){
        for(j=m;j<n;j++){
            a[1][j] = max(a[1][j-1], a[1-1][j-m] + s[j]-s[j-m]);
        }
        for(j=0;j<n;j++){
            a[0][j] = a[1][j];
        }
    }

    // cout<<"all clear end"<<endl;
    ans = a[1][n-1];
    cout<<ans<<endl;
    return 0;
}