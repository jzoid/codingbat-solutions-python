"""
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
"""

def lone_sum(a, b, c):
  new_l = []
  for n in [a,b,c]:
    if [a,b,c].count(n) < 2:
      new_l.append(n)
  return sum(new_l)

