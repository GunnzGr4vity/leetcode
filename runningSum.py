# https://leetcode.com/problems/running-sum-of-1d-array/
# did with family
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        newList = []
        for i in nums:
            total = total + i
            newList.append(total)
            print(total)
        return newList
    def printName(self):
        print("my name is gunner m8")

s = Solution()
totalList = []
totalList = s.runningSum([1,2,3,4])
s.printName()

for i in totalList:
    print(i)
    