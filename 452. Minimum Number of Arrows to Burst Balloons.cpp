class Solution {
public:
    static bool cmp(vector<int>& a , vector<int>& b){
        return a[1] < b[1];
    }
    int findMinArrowShots(vector<vector<int>>& nums) {
        sort(nums.begin(), nums.end(), cmp);
        int cnt = 0;
        for(int i = 0; i < nums.size(); i++){
            int temp = nums[i][1];
            while (i+1 < nums.size() && temp >= nums[i+1][0])
                i++;
            cnt++;
        }
        return cnt;
    }
};


/*
Intuition
Sort on the basis of end point and check how many baloons can you burst with it.
Why sort on the basis of end point and not the start point ?
Eg : [ [6,7] , [1,10] , [5,8] , [9,12] ]

if you sort on the basis of start point and start taking the end then you'll get ans 1 but the answer is 2 
because 10 wont touch the tip of the 7 and 9 together because [6,7] has the tip till 7 & 9 starts at 9 and ends at 12 so we can burst that only.

Approach
Sort on the basis of end values, iterate over the values and check for how many can you actually burst, keep a cnt for it.

Complexity
Time complexity:  O(N)
Space complexity: O(1)
*/
