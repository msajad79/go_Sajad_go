/*
   ______                        _           __     ______    
  / ____/___       _________ _  (_)___ _____/ /    / ____/___ 
 / / __/ __ \     / ___/ __ `/ / / __ `/ __  /    / / __/ __ \ 
/ /_/ / /_/ /    (__  ) /_/ / / / /_/ / /_/ /    / /_/ / /_/ /
\____/\____/    /____/\__,_/_/ /\__,_/\__,_/     \____/\____/ 
                          /___/                               

Daily coding problem (Algorithm, DB and etc)

Date: 2024-JUN-13

app: leetcode
problem: https://leetcode.com/problems/3sum-closest/description/
*/

#include <bits/stdc++.h>
#include <vector>
using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int ans = 400000000, sum, diff, j ,k;
        int s_ans = 0;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for (int i=0; i<n-2; i++) {
            j = i + 1;
            k = n - 1;
            while (j != k) {
                sum = nums[i] + nums[j] + nums[k];
                diff = sum - target;
                if (diff == 0)
                    return target;
                else if (diff < 0){
                    j ++;
                    k = n - 1;
                }else
                    k--;
                if (abs(diff) < ans) {
                    ans = abs(diff);
                    s_ans = sum;
                }
            }
        }
        return s_ans;
    }
};