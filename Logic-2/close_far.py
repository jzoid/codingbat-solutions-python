"""
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
"""

def close_far(a, b, c):
  ab_diff = abs(a - b)
  ac_diff = abs(a - c)
  bc_diff = abs(b - c)
  if ab_diff < 2 and ac_diff > 1 and bc_diff > 1:
    return True
  elif ac_diff < 2 and ab_diff > 1 and bc_diff > 1:
    return True
  else:
    return False

