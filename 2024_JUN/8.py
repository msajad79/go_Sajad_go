"""
   ______                        _           __     ______    
  / ____/___       _________ _  (_)___ _____/ /    / ____/___ 
 / / __/ __ \     / ___/ __ `/ / / __ `/ __  /    / / __/ __ \ 
/ /_/ / /_/ /    (__  ) /_/ / / / /_/ / /_/ /    / /_/ / /_/ /
\____/\____/    /____/\__,_/_/ /\__,_/\__,_/     \____/\____/ 
                          /___/                               

Daily coding problem (Algorithm, DB and etc)

Date: 2024-JUN-8

app: leetcode
problem: https://leetcode.com/problems/container-with-most-water/description/
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ind1 = 0
        ind2 = len(height)-1
        ans = 0
        while ind1 != ind2:
            h = min([height[ind1],height[ind2]])
            w = ind2 - ind1
            ans = max([h*w, ans])
            if h == height[ind1]:
                ind1 += 1
            else:
                ind2 -= 1
        return ans
