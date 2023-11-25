#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#ifdef LOKAL
#include "DEBUG_TEMPLATE.h"
#else
#define HERE
#define debug(args...)
#endif
typedef pair<int,int> pii;



void TEST_CASES()
{
         int n;cin>>n;
         int c=0;
         map<int,int>mp;
         for(int i=0;i<n;i++){
            int k;cin>>k;
            mp[k]++;
         }
         int cnt=0;
         for(auto i:mp){
            int f = i.first;
            int s = i.second;
            if(f<=s){
                cnt+=f;
            }
         }
         cout<<n-cnt<<endl;
}

int32_t main()
{
#ifndef LOKAL
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
#endif
    int t=1;
    //cin>>t;
    while(t--)
    {
        TEST_CASES();
    }
    return 0;
}