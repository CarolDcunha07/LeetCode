class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)-1
        
        if len(nums1)%2!=0:
            i=n//2
            return nums1[i]
        else:
            i=n//2
            j=i+1
            res=(nums1[i]+nums1[j])/2
            return res

            
        