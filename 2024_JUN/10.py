"""
   ______                        _           __     ______    
  / ____/___       _________ _  (_)___ _____/ /    / ____/___ 
 / / __/ __ \     / ___/ __ `/ / / __ `/ __  /    / / __/ __ \ 
/ /_/ / /_/ /    (__  ) /_/ / / / /_/ / /_/ /    / /_/ / /_/ /
\____/\____/    /____/\__,_/_/ /\__,_/\__,_/     \____/\____/ 
                          /___/                               

Daily coding problem (Algorithm, DB and etc)

Date: 2024-JUN-9

app: leetcode
problem: https://leetcode.com/problems/roman-to-integer/description/
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        info = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        info_e = {
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900,
        }
        i = 0
        data = 0
        while len(s) != i:
            if i != len(s)-1 and s[i:i+2] in info_e.keys():
                data+= info_e[s[i:i+2]]
                i+=2
            else:
                data += info[s[i]]
                i+=1
        return data

