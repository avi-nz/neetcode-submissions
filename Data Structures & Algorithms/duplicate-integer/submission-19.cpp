class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> hasAppeared;

        for (auto num: nums) {
            if (hasAppeared.contains(num)) {
                return true;
            }
            hasAppeared.insert(num);
        }
        return false;
    }
};