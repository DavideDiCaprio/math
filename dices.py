import random


def throw_dice(n_faces=6):
  outcome = random.randint(1,n_faces)
  return outcome

def sum_throw_two_dices(n_faces=6):
  '''add sum of two dices thow '''
  outcome = random.randint(1,n_faces) + random.randint(1,n_faces)
  return outcome


def throw_n_dices(n_dices,n_faces=6):
  list_of_outcomes = []
  while len(list_of_outcomes) != n_dices:
    list_of_outcomes.append(throw_dice(n_faces=6))
  return list_of_outcomes


def measure_frequency_of_outcome(outcome, list_of_outcomes):
  count = 0
  for i in range(len(list_of_outcomes)):
    if outcome == list_of_outcomes[i]:
      count+=1
  print(f'The frequency of {outcome} is {count/len(list_of_outcomes):.2%}')


def measure_frequency_of_outcomes(list_of_outcomes):
  observed_outcomes = list(set(list_of_outcomes)) 
  for o in observed_outcomes:
    measure_frequency_of_outcome(outcome=o, list_of_outcomes=list_of_outcomes)
    
    
def estimate_probability_of_dice_faces(n_throws, n_faces=6):
  print()
  print(f'Estimating with {n_throws} throws')
  list_of_outcomes = throw_n_dices(n_dices=n_throws,n_faces=n_faces)
  measure_frequency_of_outcomes(list_of_outcomes)


for n_throws in [20, 50, 100, 500, 1000, 10000, 50000, 100000]:
  estimate_probability_of_dice_faces(n_throws=n_throws, n_faces=6)
  
  
 'An example of output using sum_throw_two_dices:'

'''
Estimating with 100000 throws
The frequency of 2 is 0.02656
The frequency of 3 is 0.05481
The frequency of 4 is 0.08307
The frequency of 5 is 0.11051
The frequency of 6 is 0.14138
The frequency of 7 is 0.16618
The frequency of 8 is 0.13882
The frequency of 9 is 0.11131
The frequency of 10 is 0.08391
The frequency of 11 is 0.05577
The frequency of 12 is 0.02768
'''
