"""
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
"""

def sum13(nums):
  # while 13 is still in nums, loop
  while 13 in nums:

    # Remove the index after 13 first.
    # Only if there is one i.e if 13 is not the last index
    if nums.index(13) < len(nums) -1:
      nums.pop(nums.index(13) +1)

    # now remove the 13's
    nums.pop(nums.index(13))

  # return list summed
  return sum(nums)
  
