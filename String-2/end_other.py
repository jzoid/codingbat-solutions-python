"""
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
"""

def end_other(a, b):
  # lower case and find shortest string
  a = a.lower()
  b = b.lower()
  if len(a) > len(b):
    shortest = b
    longest = a
  else:
    shortest = a
    longest = b

  # True if shortest str is equal to the same lenght last indexes of longest 
  if shortest == longest[- len(shortest):]:
    return True
  else:
    return False

# change to use str.endswith(str)

