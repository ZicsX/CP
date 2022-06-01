#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fl for(int i=0;i<n;i++)
#define vll vector<ll>

signed main() {
    int t = 1;
    cin >> t;
    while (t--) {
        ll n;
        cin >> n;
        vll a(n), b(n);
        fl cin >> a[i];
        fl cin >> b[i];
        map <ll,ll> mp;
        ll ans = 0;
        fl {
            ll u = a[i] ^ b[i];
            ans += mp[u];
            mp[u]++;
        }
        cout << ans <<endl;
    }
}