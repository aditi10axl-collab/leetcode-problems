#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> combinationSum(std::vector<int>& candidates, int target) {
        std::vector<std::vector<std::vector<int>>> dp(target + 1);
        dp[0] = {{}};

        for (int c : candidates) {
            for (int i = c; i <= target; i++) {
                for (auto combo : dp[i - c]) {
                    combo.push_back(c);
                    dp[i].push_back(combo);
                }
            }
        }

        return dp[target];
    }
};
