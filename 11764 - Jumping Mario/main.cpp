#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;
ll arr[12345];

int main() {
	ll a;
	while(scanf("%lld",&a) == 1){
		for(ll cas = 0; cas < a; cas++){
			ll h = 0, l = 0;
			ll n;
			scanf("%lld",&n);
			for(ll i = 0; i < n; i++){
				scanf("%lld",&arr[i]);
			}
			for(ll i = 1; i  < n; i++){
				if(arr[i] > arr[i - 1]){
					h += 1;
				}
				if(arr[i - 1] > arr[i]){
					l += 1;
				}
			}
			printf("Case %lld: %lld %lld\n",cas+1, h, l);
		}
	}

	return 0;
}
