#include <iostream>
#include<bits/stdc++.h>
using namespace std;
void fast()
{
    cin.tie(0);
    cout.sync_with_stdio(NULL);
}
int main()
{
    fast();
    int n;
    cin>>n;
    int arr[n];
    int m=INT_MAX;
    for(int i=0; i<n; i++)
    {
        cin>>arr[i];
        int c=0;
        while(arr[i]%2==0&&arr[i]>0)
        {
            c++;
            arr[i]/=2;

        }
        m=min(m,c);

    }
   cout<<m;

    return 0;
}