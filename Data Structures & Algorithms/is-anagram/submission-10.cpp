class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        set<char> uniqueChars(s.begin(), s.end());

        for (char c : uniqueChars) {
            if (count(s.begin(), s.end(), c) != count(t.begin(), t.end(), c)) {
                return false;
            }
        }

        return true;
    }
};
