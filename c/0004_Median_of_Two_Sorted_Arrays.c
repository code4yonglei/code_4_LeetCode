/*

0004_Median_of_Two_Sorted_Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

*/


int comp (const void * a, const void * b) { return ( *(int*)a - *(int*)b ); }

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){

    int lgth = nums1Size + nums2Size;
    int nums3[lgth];
    
    for(int i=0; i< nums1Size; i++)
        nums3[i]=nums1[i];
    for(int i=nums1Size; i< lgth; i++)
        nums3[i]=nums2[i-nums1Size];
    
    qsort(nums3, lgth, sizeof(int), comp);
    
    if(lgth%2)
        return nums3[lgth/2];
    else
        return (nums3[lgth/2]+nums3[lgth/2-1])/2.0;
    
}
