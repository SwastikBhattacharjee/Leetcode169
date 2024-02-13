"""
Author: Swastik Bhattacharjee
Date: 13th February, 2023
Github: @SwastikBhattacharjee
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_number = 0
        max_digit = []

        dictionary = {}

        for number in nums:
            dictionary[number] = dictionary.get(number, 0) + 1

        for number in dictionary.keys():
            if dictionary[number] > max_number:
                max_number = dictionary[number]
                max_digit = []
                max_digit.append(number)
            elif dictionary[number] == max_number:
                max_number = dictionary[number]
                max_digit.append(number)

        return max_digit

# Testing the program
print(Solution().majorityElement([1,2,3,4,5,6,7,8,9,10]))
