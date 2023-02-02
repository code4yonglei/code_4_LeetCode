/*

*/

class Solution {
public:
    int countOdds(int low, int high) {
        int num = high - low;
        if (low%2 == 1 || high%2 == 1)
            return num/2 + 1; 
        else
            return num/2;
    }
};

