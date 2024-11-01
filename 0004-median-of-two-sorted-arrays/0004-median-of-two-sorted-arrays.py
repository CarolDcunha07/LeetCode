class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst=nums1+nums2
        lst=sorted(lst)
        
        if len(lst)%2!=0:
            idx=(len(lst)-1)//2
            res=lst[idx]
            
        else:
            idx1=((len(lst)-1)//2)
            idx2=((len(lst))//2)
            res=(lst[idx1]+lst[idx2])/2
        return res
        