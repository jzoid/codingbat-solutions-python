"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
"""
def front_times(str, n):
  # first go
  #
  #if len(str) < 3:
  #  return str * n
  #return str[:3] * n

  return str * n if len(str) < 3 else str[:3] * n

  # this also works not sure how
  # return str[:3] * n

