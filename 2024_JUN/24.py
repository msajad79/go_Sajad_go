"""
   ______                        _           __     ______    
  / ____/___       _________ _  (_)___ _____/ /    / ____/___ 
 / / __/ __ \     / ___/ __ `/ / / __ `/ __  /    / / __/ __ \ 
/ /_/ / /_/ /    (__  ) /_/ / / / /_/ / /_/ /    / /_/ / /_/ /
\____/\____/    /____/\__,_/_/ /\__,_/\__,_/     \____/\____/ 
                          /___/                               

Daily coding problem (Algorithm, DB and etc)

Date: 2024-JUN-24

app: leetcode
problem: https://leetcode.com/problems/nth-highest-salary/description/
"""
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    data = sorted(employee.salary.unique(), reverse=True)
    if len(data) >= N and N > 0:
        data = [data[N-1]]
    else:
        data = [None]
    return pd.DataFrame(data=data, columns=[f"getNthHighestSalary({N})"])