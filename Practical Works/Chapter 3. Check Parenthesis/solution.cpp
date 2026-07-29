#include <bits/stdc++.h>
using namespace std;

bool isValid(const string& s) {
    string st;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            st.push_back(c);
        } else {
            if (st.empty()) return false;
            char top = st.back();
            if ((c == ')' && top == '(') || 
                (c == ']' && top == '[') || 
                (c == '}' && top == '{')) {
                st.pop_back();
            } else {
                return false;
            }
        }
    }
    return st.empty();
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        cout << (isValid(s) ? 1 : 0) << "\n";
    }
    
    return 0;
}
