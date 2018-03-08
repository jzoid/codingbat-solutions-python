def parrot_trouble(talking, hour):
  if talking and hour not in range(7,21):
    return True
  return False
