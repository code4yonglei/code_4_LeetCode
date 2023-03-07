/*

1539_Kth_Missing_Positive_Number

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

*/

class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int sz = arr.size();
        int l = 0;
        int h = sz; 
        while(h > l) {
            int mid = (h+l)/2;
            int miss = arr[mid]-1 - mid; 
            if(k <= miss) {
                h = mid;
            } else {
                l = mid+1;
            }
        }
        return h + k;
    }
};
