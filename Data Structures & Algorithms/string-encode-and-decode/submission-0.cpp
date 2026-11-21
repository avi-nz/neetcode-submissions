class Solution {
public:

    string encode(vector<string>& strs) {
        string result;

        for (const string& str : strs) {
            result += static_cast<char>(str.size());
            result += str;
        }

        return result;

    }

    vector<string> decode(string s) {
        vector<string> result;

        int i = 0;

        while (i < s.size()) {
            int len = static_cast<unsigned char>(s[i]);
            i++;

            result.push_back(s.substr(i, len));
            i += len;
        }

        return result;

    }
};
