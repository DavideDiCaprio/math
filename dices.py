import random


def throw_dice(n_faces=6):
  outcome = random.randint(1,n_faces)
  return outcome


def throw_n_dices(n_dices,n_faces=6):
  list_of_outcomes = []
  while len(list_of_outcomes) != n_dices:
    list_of_outcomes.append(throw_dice(n_faces=6))

  return list_of_outcomes
