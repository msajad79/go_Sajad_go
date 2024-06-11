"""
   ______                        _           __     ______    
  / ____/___       _________ _  (_)___ _____/ /    / ____/___ 
 / / __/ __ \     / ___/ __ `/ / / __ `/ __  /    / / __/ __ \ 
/ /_/ / /_/ /    (__  ) /_/ / / / /_/ / /_/ /    / /_/ / /_/ /
\____/\____/    /____/\__,_/_/ /\__,_/\__,_/     \____/\____/ 
                          /___/                               

Daily coding problem (Algorithm, DB and etc)

Date: 2024-JUN-11

app: leetcode
problem: https://leetcode.com/problems/longest-common-prefix/description/
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        num = 0
        ans = ""
        while True:
            try:
                ev = strs[0][num]
                for word in strs[1:]:
                    if word[num] != strs[0][num]:
                        return ans
                num += 1
                ans += strs[0][num]
            except IndexError as e:
                return ans