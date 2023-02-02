"""
Intuition & Approach
Q: we need to minimize the number of arrows.
A: we can only minimize this if we somehow can manage to merge the intervals lying on the number line this reduces the search space.
In order to merge the interval we need to keep in mind that interval can only merge if the start of given interval is less than end of previous interval now after merging the interval suppose we get new interval coordinates as nx and ny so nx=min(prev_start,curr_start) and ny=min(prev_end,curr_end) here nx needs to be start of interval so it has to be minimum among the prev_start and curr_start but as we know maximum range to shoot ballon is between start<=x<=end so if we make ny=curr_end we can miss previous ballon that we had taken into consideration thus at step k we need to consider minimum ending interval first in order to burst i,i+1,...,i+k-1 ballons

Complexity
Time complexity:  O(nlogn)
Space complexity: O(1)
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        start, end = points[0][0], points[0][1]
        cnt = 0
        for s, e in points:
            if s <= end:
                end = min(e, end)
            else:
                cnt += 1
                start, end= s, e
        return cnt + 1

