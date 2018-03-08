"""
Given a string, return a new string where the first and last chars have been exchanged.
"""
def front_back(str):
  # update to use str[-1] for last
  if len(str) < 2 :
    return str
  elif len(str) == 2:
    return str[1] + str[0]
  
  last = str[len(str) -1]
  mid = str[1:len(str) -1]
  first = str[0]
  
  return last + mid + first
