"""
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
"""

def array123(nums):
  #if "1, 2, 3" in str(nums):
  #  return True
  #return False
  
  return "1, 2, 3" in str(nums)

