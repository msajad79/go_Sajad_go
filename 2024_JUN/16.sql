"""
   ______                        _           __     ______    
  / ____/___       _________ _  (_)___ _____/ /    / ____/___ 
 / / __/ __ \     / ___/ __ `/ / / __ `/ __  /    / / __/ __ \ 
/ /_/ / /_/ /    (__  ) /_/ / / / /_/ / /_/ /    / /_/ / /_/ /
\____/\____/    /____/\__,_/_/ /\__,_/\__,_/     \____/\____/ 
                          /___/                               

Daily coding problem (Algorithm, DB and etc)

Date: 2024-JUN-16

app: leetcode
problem: https://leetcode.com/problems/employees-earning-more-than-their-managers/description/
"""

SELECT E.name as Employee
FROM Employee M
JOIN Employee E ON M.id = E.managerId 
WHERE M.salary < E.salary;

