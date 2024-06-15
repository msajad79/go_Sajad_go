"""
   ______                        _           __     ______    
  / ____/___       _________ _  (_)___ _____/ /    / ____/___ 
 / / __/ __ \     / ___/ __ `/ / / __ `/ __  /    / / __/ __ \ 
/ /_/ / /_/ /    (__  ) /_/ / / / /_/ / /_/ /    / /_/ / /_/ /
\____/\____/    /____/\__,_/_/ /\__,_/\__,_/     \____/\____/ 
                          /___/                               

Daily coding problem (Algorithm, DB and etc)

Date: 2024-JUN-15

app: leetcode
problem: https://leetcode.com/problems/merge-k-sorted-lists/description/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists =[val for val in lists if val is not None]
        if lists == []:
            return ListNode(val="")
        ans = lists[0]
        for i in range(1,len(lists)):
            compaire_chain = lists[i]
            base_chain = ans
            prev = None
            while not compaire_chain is None:
                if compaire_chain.val > base_chain.val:
                    if base_chain.next is None:
                        base_chain.next = compaire_chain
                        break
                    prev = base_chain
                    base_chain = base_chain.next
                elif compaire_chain.val <= base_chain.val:
                    new_compaire_chain = compaire_chain.next
                    compaire_chain.next = base_chain
                    if prev is not None:
                        prev.next = compaire_chain
                    else:
                        ans = compaire_chain
                    prev = compaire_chain
                    compaire_chain = new_compaire_chain
        return ans
            
            