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

