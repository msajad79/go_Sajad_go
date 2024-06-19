"""
   ______                        _           __     ______    
  / ____/___       _________ _  (_)___ _____/ /    / ____/___ 
 / / __/ __ \     / ___/ __ `/ / / __ `/ __  /    / / __/ __ \ 
/ /_/ / /_/ /    (__  ) /_/ / / / /_/ / /_/ /    / /_/ / /_/ /
\____/\____/    /____/\__,_/_/ /\__,_/\__,_/     \____/\____/ 
                          /___/                               

Daily coding problem (Algorithm, DB and etc)

Date: 2024-JUN-19

app: leetcode
problem: https://leetcode.com/problems/second-highest-salary/description
"""

SELECT COALESCE(
    (SELECT DISTINCT salary AS SecondHighestSalary
     FROM Employee
     ORDER BY salary DESC
     LIMIT 1 OFFSET 1),
    NULL
) AS SecondHighestSalary;