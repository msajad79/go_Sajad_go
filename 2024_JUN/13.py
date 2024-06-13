"""
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
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float("inf")
        s_ans = 0
        nums.sort()
        k = len(nums) - 1
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j != k:
                sum_ = nums[i] + nums[j] + nums[k]
                diff = sum_ - target
                if diff == 0:
                    return target
                elif diff < 0:
                    j += 1
                    k = len(nums) - 1
                else:
                    k -= 1
                if abs(diff) < ans:
                    ans = abs(diff)
                    s_ans = sum_
        return s_ans