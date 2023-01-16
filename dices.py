import random

def throw_dice(n_faces=6):
  
  outcome = random.randint(1,n_faces)
  return outcome

throw_dice()
