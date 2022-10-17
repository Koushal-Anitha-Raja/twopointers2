class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=2
        slow=1
        #initialize the count var to 1
        count=1
        #iterate through the nums array till end
        for fast in range (1,len(nums)):
            #before element is same as next increment count 
            if nums[fast]==nums[fast-1]:
                count+=1
           #or else leave the count to one
            else:
                count=1
            #if the count value is lesser than given k in question inc slow and continue
            if count<=k:
                nums[slow]=nums[fast]
                slow+=1
                
        return slow
        