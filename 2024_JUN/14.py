"""
   ______                        _           __     ______    
  / ____/___       _________ _  (_)___ _____/ /    / ____/___ 
 / / __/ __ \     / ___/ __ `/ / / __ `/ __  /    / / __/ __ \ 
/ /_/ / /_/ /    (__  ) /_/ / / / /_/ / /_/ /    / /_/ / /_/ /
\____/\____/    /____/\__,_/_/ /\__,_/\__,_/     \____/\____/ 
                          /___/                               

Daily coding problem (Algorithm, DB and etc)

Date: 2024-JUN-14

app: leetcode
problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        info = {
            2: ["a","b","c"],
            3: ["d","e","f"],
            4: ["g","h","i"],
            5: ["j","k","l"],
            6: ["m","n","o"],
            7: ["p","q","r","s"],
            8: ["t","u","v"],
            9: ["w","x","y","z"],
        }
        pointers = [0]*len(digits)
        ans = []
        digits[0]
        while pointers[0] != len(info[int(digits[0])]):
            word = ""
            for i in range(len(digits)):
                word += info[int(digits[i])][pointers[i]]
            ans.append(word)
            for i_p in range(len(pointers)-1,-1,-1):
                if pointers[i_p] != len(info[int(digits[i_p])]) -1 or i_p == 0:
                    pointers[i_p] += 1
                    break
                else:
                    pointers[i_p] = 0
        return ans
            

