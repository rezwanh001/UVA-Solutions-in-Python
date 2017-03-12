#include <iostream>
#include <bits/stdc++.h>

using namespace std;

vector < vector< int > > vvi;
string c, q;

int main() {
    freopen ("10567.txt","r",stdin);
    vvi.resize(256);
    cin>> c;
    int Q;
    for(int i = 0; i < c.size(); i++) {
        vvi[c[i]].push_back(i);
    }
    scanf("%d",&Q);
    for(int i = 0; i < Q; i++) {
        cin >> q;
        int idx = -1, a = 0;
        bool fin = true;
        for(int j = 0; j < q.size(); j++) {
            vector<int> :: iterator low = upper_bound(vvi[q[j]].begin(), vvi[q[j]].end(), idx);
            idx = low - vvi[q[i]].begin();

            if(low == vvi[q[j]].end()) {
                fin = false;

            }
            idx = vvi[q[j]][idx];
            if(j == 0) {
                a = idx;
            }
        }
        if(fin) {
            printf("Matched %d %d\n",a,idx);
        } else {
            printf("Not matched\n");
        }
    }
    return 0;
}
