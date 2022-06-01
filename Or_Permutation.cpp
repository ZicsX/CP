#include <bits/stdc++.h>
#define ll long long
using namespace std;
void solve(){
  ll n; cin>>n;
  vector<ll> a(n),b(n);
  for (int i = 0; i < n; i++)
  {
    cin>>a[i];
  }
  for (int i = 0; i < n; i++)
  {
    cin>>b[i];
  }
  int ans = 0;
  for (int i = 0; i < 32; i++)
  {
    int val = (1<<i);
    int c=0;
    for (int j = 0; j < n; j++)
    {
      int x = val&b[j];
      if(x)
      c++;
    }
    if(c == n){
      ans += val;
    }
  }
  for(int i=0;i<n;i++) a[i] |= ans;
  sort(a.begin(),a.end());
  sort(b.begin(),b.end());
  if(a != b) ans=-1;
  cout<<ans<<"\n";
}
int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int tt=1; cin>>tt;
  while (tt--)
  {
    solve();
  }
}