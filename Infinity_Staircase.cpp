#include <bits/stdc++.h>
using namespace std;
#define ll long long

signed main() {
    int t = 1;
    cin >> t;
    while (t--) {
        ll n;
        cin >> n;
        ll ans = 0;
        ans = (n/5) * 2;
        if (n%5 == 1 || n%5 == 0) {
        }
        else {
            ans ++;
        }
        cout << ans << "\n";
    }
} 
