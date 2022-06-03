#include <bits/stdc++.h>
#define ll long long
#define vi  vector<ll>
using namespace std;
int main()
{ 
    int n,ct=0; 
    cin>>n; 
    vi v; 

    for(int i=0;i<n;i++){
        int x;
        cin>>x;
        v.push_back(x);
    } 

    for(int i=0;i<n;i++){ 
        if(v[i]%2==1){ 
            ct++; 
        } 
    } 
    if(ct>0){ 
        cout<<n-ct<<endl; 
    } 
    else{ 
        int ans=INT_MAX; 
        for(int i=0;i<n;i++){ 
            int ct1=0; 
            while(v[i]%2==0){ 
                v[i]=v[i]/2; 
                ct1++; 
            } 
            ans=min(ans,ct1); 
        } 
        cout<<(ans+n-1)<<endl; 
    }
}