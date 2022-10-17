'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''


from typing import List


class solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i #hashmap{2:0, 7:1, 11:2, 15:3}
        for i in range(len(nums)):
            complement = target - nums[i]  #complement = 9-2=7
            if complement in hashmap and hashmap[complement] != i: #while 7 in hashmap and key value of 7 1!=0
                return [i, hashmap[complement]] #[0,1]

#testcases
test=solution()
print(test.twosum([2,7,11,15],9))

