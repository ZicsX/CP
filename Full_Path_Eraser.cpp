#include<bits/stdc++.h>
#define ll long long
#define vl vector < ll >
#define ml map < ll, vector < ll >>
using namespace std;

ll compute(ll idx, ll parentV, ml & adjList,
  vl & values, vl & intermediate, vl & final) {
  ll curr = values[idx];
  ll sum = 0;
  for (auto & i: adjList[idx]) {
    if (i != parentV) {
      ll child = compute(i, idx, adjList, values, intermediate, final);
      sum += child;
      curr = __gcd(curr, child);
    }
  }
  intermediate[idx] = curr;
  final[idx] = sum;
  return curr;
}

void fidxMax(ll idx, ll parentV, ll sb, ml & adjList,
  vl & values, vl & intermediate, vl & final,
  ll & maxgcd) {
  maxgcd = max(maxgcd, sb);
  for (auto & i: adjList[idx]) {
    if (i != parentV)
      fidxMax(i, idx, sb - intermediate[i] + final[i], adjList, values, intermediate, final, maxgcd);
  }
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    ll n;
    cin >> n;
    vl values(n);
    vl intermediate(n);
    vl final(n);
    ll maxgcd = 0;
    ml adjList;
    for (ll i = 0; i < n; ++i)
      cin >> values[i];
    for (ll i = 0; i < n - 1; i++) {
      ll x, y;
      cin >> x >> y;
      x--;
      y--;
      adjList[x].push_back(y);
      adjList[y].push_back(x);
    }
    ll total = compute(0, -1, adjList, values, intermediate, final);
    fidxMax(0, -1, final[0], adjList, values, intermediate, final, maxgcd);
    cout << maxgcd << endl;
  }
  return 0;
}