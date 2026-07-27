#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, B;
    cin >> n >> B;
    vector<int> w(n + 1), v(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> w[i] >> v[i];
    }
    vector<int> dp(B + 1, 0);

    for (int i = 1; i <= n; ++i) {
        for (int j = B; j >= w[i]; --j) {
            dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
        }
    }

    cout << dp[B] << endl;
    
    return 0;
}
