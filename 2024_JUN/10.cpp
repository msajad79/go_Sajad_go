/*
   ______                        _           __     ______    
  / ____/___       _________ _  (_)___ _____/ /    / ____/___ 
 / / __/ __ \     / ___/ __ `/ / / __ `/ __  /    / / __/ __ \ 
/ /_/ / /_/ /    (__  ) /_/ / / / /_/ / /_/ /    / /_/ / /_/ /
\____/\____/    /____/\__,_/_/ /\__,_/\__,_/     \____/\____/ 
                          /___/                               

Daily coding problem (Algorithm, DB and etc)

Date: 2024-JUN-10

app: leetcode
problem: https://leetcode.com/problems/roman-to-integer/description/
*/

#include <map>

class Solution {
public:
    int romanToInt(string s) {
        string rom_info[] = {"I","V","X","L","C","D","M"};
        map<string, int> info;
        
        info["I"] = 1;
        info["V"] = 5;
        info["X"] = 10;
        info["L"] = 50;
        info["C"] = 100;
        info["D"] = 500;
        info["M"] = 1000;
        info["IV"] = 4;
        info["IX"] = 9;
        info["XL"] = 40;
        info["XC"] = 90;
        info["CD"] = 400;
        info["CM"] = 900;
        
        int i = 0;
        int ans = 0;
        while (i != s.length()){ 
            if ((i != s.length()-1) && (info.find(s.substr(i,2)) != info.end())){
                ans += info.find(s.substr(i,2))->second;
                i+=2;
            }else{
                ans += (info.find(s.substr(i,1))->second);
                i += 1;
            }
        }
        return ans;
    }
};