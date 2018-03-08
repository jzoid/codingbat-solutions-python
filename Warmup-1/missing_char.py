def missing_char(str, n):
  if n > len(str):
    return False
  new_str = ""
  for c in str:
    if c != str[n]:
      new_str += c
  return new_str
