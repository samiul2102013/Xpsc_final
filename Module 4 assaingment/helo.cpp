#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
typedef long long ll;
typedef long double ld;
#ifdef LOKAL
#include "DEBUG_TEMPLATE.h"
#else
#define HERE
#define debug(args...)
#endif
const int N = 2e5 +5;
typedef pair<int,int> pii;
template <typename T>
using pbds = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;



void TEST_CASES()
{
    pbds<int> p;
    int n;cin>>n;
    vector<int>v(n);
    for(auto &i:v)cin>>i;
    sort(v.begin(),v.end());
    vector<int>pfs(n);
    pfs[0]=v[0];
    for(int i=1;i<v.size();i++){
        int k = pfs[i-1]+v[i];
        pfs[i]=k;
    }
    debug(pfs)
    for(int i=0;i<pfs.size();i++){
        p.insert(pfs[i]);
    }
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