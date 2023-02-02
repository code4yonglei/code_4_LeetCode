/*

*/

class Solution {
public:
    string categorizeBox(int l, int w, int h, int m) {
        long long v=(long long)l*(long long)w*(long long)h;
        if(l>=10000||w>=10000||h>=10000||v>=pow(10,9)){
            if (m>=100) return "Both";
            else return "Bulky";
        }
        else if (m>=100) return "Heavy";
        else return "Neither";
    }
};
