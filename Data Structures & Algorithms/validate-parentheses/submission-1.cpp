#include <stack>
#include <unordered_map>
#include <string>



class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> pair = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        for (char c : s) {

            if (c == '(' || c == '[' || c == '{') {
                st.push(c);
            }
            else if (c== ')' || c == ']' || c == '}') {
                if (st.empty()) {
                    return false;
                }
                char top = st.top();
                st.pop();
                if (top != pair[c]){
                    return false;
                }
            }
        }
        return st.empty();

    }
};
