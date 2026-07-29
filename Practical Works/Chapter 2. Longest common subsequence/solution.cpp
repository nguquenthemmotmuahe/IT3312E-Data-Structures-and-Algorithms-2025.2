#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, m; 
    cin >> n >> m;
    
    vector<int> x(n);
    vector<int> y(m);
    vector<vector<int>> dp(n+1, vector<int>(m+1, 0));
    
    for(int i = 0; i < n; i++){
        cin >> x[i];
    }
    
    for(int i = 0; i < m; i++){
        cin >> y[i];
    }
    
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= m; j++) {
            if(x[i-1] == y[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]); 
            }
        }
    }
    
    cout << dp[n][m] << endl;
    
    return 0;
}
