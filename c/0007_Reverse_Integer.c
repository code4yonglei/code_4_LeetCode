/*

0007_Reverse_Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

*/


int reverse(int x){
    long rev = 0, rem;
    while(x) {
        rem = x%10;
        rev = rev*10+rem;
        x = x/10;
    }
    if(rev < INT_MIN || rev> INT_MAX) {
        return 0;
    }
    return rev;
}