"""
   ______                        _           __     ______    
  / ____/___       _________ _  (_)___ _____/ /    / ____/___ 
 / / __/ __ \     / ___/ __ `/ / / __ `/ __  /    / / __/ __ \ 
/ /_/ / /_/ /    (__  ) /_/ / / / /_/ / /_/ /    / /_/ / /_/ /
\____/\____/    /____/\__,_/_/ /\__,_/\__,_/     \____/\____/ 
                          /___/                               

Daily coding problem (Algorithm, DB and etc)

Date: 2024-JUN-25

app: leetcode
problem: https://leetcode.com/problems/rank-scores/description/
"""

import pandas as pd
rank = 1
prev_val = None
def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    global rank, prev_val
    def ranking(val):
        global rank, prev_val
        if prev_val == val:
            return rank
        rank += 1
        prev_val = val
        return rank
    scores_ser = scores.score.sort_values(ascending=False)
    rank = 1
    if len(scores_ser.index) != 0:
        prev_val = scores_ser.iloc[0]
    rank_ser = scores_ser.apply(ranking)
    return pd.concat([scores_ser, rank_ser.rename("rank")], axis=1)