#include <bits/stdc++.h>
using namespace std;
typedef long long int ll ;

ll price[1005];
ll weight[1005];
ll dp[1005][1005];
ll CAP, people, N;

ll knapshack(ll i, ll w){
	if( i == N){
		return 0;
	}
	if(dp[i][w] != -1 ){
		return dp[i][w];
	}
	ll res1 = 0, res2 = 0;
	if(w + weight[i] <= CAP){
		res1 = price[i] + knapshack(i + 1, w + weight[i]);
	}
	else{
		res1 = 0;
	}
	res2 = knapshack(i + 1, w);
	dp[i][w] = max(res1, res2);

	return dp[i][w];
}

int main() {
	ll T;
	scanf("%lld",&T);
	while(T--){
		scanf("%lld",&N);
		for(ll i = 0; i < N; i++){
			scanf("%lld %lld",&price[i], &weight[i]);
		}
		ll ans = 0;
		scanf("%lld",&people);
		while(people -- ){
			memset(dp, -1, sizeof dp);
			scanf("%lld",&CAP);
			ans += knapshack(0,0);
		}
		printf("%lld\n",ans);
	}

	return 0;
}
