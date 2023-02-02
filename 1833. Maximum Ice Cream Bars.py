'''

'''

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        num = 0
        for i in range(len(costs)):
            if coins > 0 and coins >= costs[i]:
                coins -= costs[i] 
                num += 1
        return num
