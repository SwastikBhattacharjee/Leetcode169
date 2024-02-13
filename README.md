# Majority Element Problem (LeetCode  169)

Find all the elements in an array that appear more than `n/2` times.

## Problem Statement

Given an integer array `nums`, the majority element is the element that appears more than `n/2` times where `n` is the length of the array. Your task is to find all such elements.

## Solution

Here is the Python solution for the Majority Element problem:


```python
class Solution(object): 
    def majorityElement(self, nums):
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
```

## Test Cases

To ensure the solution works correctly, here are some test cases:

- **Test Case  1:**
```
Input: nums = [1,2,3,4,5,6,7,8,9,10]; Output: [1,2,3,4,5,6,7,8,9,10]
```
- **Test Case  2:**
```
Input: nums = [3,2,3]; Output: 3
```
- **Test Case  3:**
```
Input: nums = [2]; Output: 2
```


## Usage

To run the solution locally, follow these steps:

1. Save the above Python code in a file named `majority_element.py`.
2. Open a terminal and navigate to the directory containing the `majority_element.py` file.
3. Execute the Python file using the command `python majority_element.py`.

## License

This project is licensed under the terms of the MIT license.

---

For any feedback or improvements, feel free to contribute to this repository.
