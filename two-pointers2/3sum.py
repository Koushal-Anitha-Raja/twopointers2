#using hashset: TC--> o(n^2),Sc:o(n)
#using binary search :TC-->o(n^2)(logn) Sc:o(c)
#using two pointers
#Time complexity:o(n^2)
#spacde complexity:o(C)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        triplets=[]#resultant array
        
        #sorting the array
        nums.sort()
        #i is the fixed pointer so the first pointer should goes until n-2
        for i in range(n-2):
            #if my number and before element are equal iterate until the last number
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            #pointer 1 should be in second pos of array
            p1=i+1
            #pointer 2 is at last position
            p2=n-1
            #target is calculated by
            target=0-nums[i]
            #stop until p1 is less than p2
            while p1<p2:
                #ifthe value is equal to target
                if (nums[p1]+nums[p2])==target:
                    #our nums result
                    res=[nums[i],nums[p1],nums[p2]]
                    #if the value equals to target then add it to the triplet array
                    triplets.append(res)
                    #until the p1 value is same move p1 
                    while p1<p2 and nums[p1]==nums[p1+1]:
                        p1+1
                    #until the p2 value is same move the p2 pointer    
                    while p1<p2 and nums[p2]==nums[p2-1]:
                        p2-=1
                    #no matter what just increment the pointers    
                    p1+=1
                    p2-=1
                else:
                    #target<
                    if target<(nums[p1]+nums[p2]):
                        p2-=1
                   #target>    
                    else:
                        p1+=1
                        
        return triplets     
                