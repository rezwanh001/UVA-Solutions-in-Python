#include <bits/stdc++.h>
using namespace std;
#define ull unsigned long long
#define ms(a,b) memset(a, b, sizeof a)
#define pb push_back

ull dp[10100];
ull coins[30];

int main(){
	for(ull i = 1 ; i < 22 ; i++){
		coins[i] = (i*i*i);
	}
	//for(ull i = 1 ;i < 22 ;i++)cout<< coins[i] << " ";
	dp[0] = 1;
	for(ull i = 1; i < 22; i++){
		for(ull j = coins[i] ; j < 10100; j++){
      if(dp[j - coins[i]]){
        dp[j] += dp[j - coins[i]];
      }
		}
	}

	ull n;

	while(cin >> n){
    cout<< dp[n] << endl;
	}
	return 0;
}

/**
ull n;
ull dp[25][10100];
vector<ull>v;

ull coin_change(ull indx, ull cur) {
	if(indx>=21) {
		if(cur==0) {
			return (ull)1;
		}
		return 0;
	}
	if(cur<0) return (ull)0;
	if(cur==0) {
		return (ull)1;
	}
	ull &rfr=dp[indx][cur];
	if(rfr!=9999999999999) return rfr;
	ull r1=0, r2=0;
	if(cur-v[indx]>=0) {
		r1=coin_change(indx,cur-v[indx]);
	}
	r2=coin_change(indx+1,cur);
	rfr=r1+r2;
	return rfr;
}

ull cube(int n) {
	return (ull)n*n*n;
}

int main() {
	///freopen("in.txt","r",stdin);
	///freopen("out.txt","w",stdout);
	for(int i=1; i<=21; i++)
		v.pb(cube(i));
	ms(dp,9999999999999);
	//cout<<v[19]<<endl;
	while(cin>>n) {
		// ms(dp,-1);
		// cnt=0;
		cout<<coin_change(0,n)<<endl;
	}
	return 0;
}
*/
