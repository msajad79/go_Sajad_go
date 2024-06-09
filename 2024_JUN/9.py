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
problem: https://leetcode.com/problems/integer-to-roman/description/
"""


class Solution:
    def intToRoman(self, num: int) -> str:
 
        int_info = [1,5,10,50,100,500,1000]
        rom_info = ["I","V","X","L","C","D","M"]
        def find_down(HV, c_zero):
            if c_zero >= 3:
                ind = 6
                typ = 0
            elif HV < 5:
                ind = 2*c_zero
                typ = 0
            else:
                ind = 2*c_zero+1
                typ = 1
            return int_info[ind], rom_info[ind], ind, typ

        def get_HV_czero(num):
            c_zero = len(str(num)) - 1
            HV = num // 10**c_zero
            return HV, c_zero

        ans = ""
        for i in range(len(str(num))):
            if str(num)[i] == "0":
                continue
            HV, c_zero = get_HV_czero(int(str(num)[i:]))
            valint, rom, ind, typ = find_down(HV, c_zero)
            if HV == 4:
                ans = f"{ans}{rom}{rom_info[ind+1]}"
            elif HV == 9:
                ans = f"{ans}{rom_info[ind-1]}{rom_info[ind+1]}"
            else:
                if typ == 0:
                    ans = f"{ans}{rom*HV}"
                else:
                    ans = f"{ans}{rom}{rom_info[ind-1]*(HV-5)}"

        return ans

