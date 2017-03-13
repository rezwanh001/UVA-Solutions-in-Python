#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

ll dp[105][105];

ll nCr(ll n, ll r){
	if( r == 1 ) return n;
	if( r == n ) return 1;
	if(dp[n][r] != -1 ) return dp[n][r];
	dp[n][r] = nCr(n - 1, r) + nCr(n-1, r - 1);
	return dp[n][r];
}
int main() {
	ll n, r;
	while(cin >> n >> r){
		if (n == 0 && r == 0){
			break;
		}
		memset(dp, -1, sizeof dp);
		printf("%lld things taken %lld at a time is %lld exactly.\n",n,r, nCr(n, r));
	}
	return 0;
}
