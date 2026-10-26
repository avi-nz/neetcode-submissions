class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> previous_numbers = {};
        for (int index = 0; index < nums.size(); index++) {

            int number = nums[index];
            int difference = target - number;

            if (previous_numbers.find(difference) != previous_numbers.end()) {
                return {previous_numbers[difference], index};
            }

            previous_numbers[number] = index;
    }
    return {};
}
};