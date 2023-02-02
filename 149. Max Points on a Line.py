'''

'''

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        points.sort()
        dict1, max_val = collections.defaultdict(int), 0

        for i in range(len(points)):
            dict1.clear()
            for j in range(i+1,len(points)):
                x, y = points[j][0] - points[i][0], points[j][1] - points[i][1]
                m = (x//math.gcd(x,y),y//math.gcd(x,y))
                dict1[m] += 1
                max_val = max(max_val,dict1[m])
        return max_val + 1
