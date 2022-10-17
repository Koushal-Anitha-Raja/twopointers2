#time complexity:o(n)
#space complexity:o(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first=0
        zeroth=0
        #third pointer at the end of the nums array
        second=len(nums)-1
        #iterate through the loop until first crosses second
        while(first<=second):
            #if the nums value of first is one then increment first by one
            if nums[first]==1:
                first+=1
                #if the first pointer points to zero 
            elif nums[first]==0:
                #then swap first and zeroth positions
                nums[first],nums[zeroth]=nums[zeroth],nums[first]
                #inc both first and zeroth
                zeroth+=1
                first+=1
            else:
                #or else sswap the first and second position
                nums[first],nums[second]=nums[second],nums[first]
                #dec second pointer
                second-=1
                
        
        