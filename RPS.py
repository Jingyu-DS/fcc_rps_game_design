# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random
step = {}
def player(prev_opponent_play, opponent_history=[]):
  if prev_opponent_play:
    opponent_history.append(prev_opponent_play)

  if len(opponent_history) > 4:
    last_four = "".join(opponent_history[-4:])
    if last_four in step:
      step[last_four] += 1
    else:
      step[last_four] = 1
    guess = make_guess(opponent_history)

  elif len(opponent_history) == 4:
    last_four = "".join(opponent_history[:])
    if last_four in step:
      step[last_four] += 1
    else:
      step[last_four] = 1
    guess = make_guess(opponent_history)

  elif len(opponent_history) == 3:
    pattern = "".join(opponent_history[:])
    potential_plays = [pattern + "R", pattern + "P", pattern + "S"]
    for i in potential_plays:
      if i not in step:
        step[i] = 0
    predict = max(potential_plays, key=lambda key: step[key])
    prediction = predict[-1:]
    ideal_response = {"P": "S", "R": "P", "S": "R"}
    guess = ideal_response[prediction]
  
  else:
    guess = random.choice(["R", "P", "S"])
  
  return guess

def make_guess(opponent_history):
  pattern = "".join(opponent_history[-3:])
  potential_plays = [pattern + "R", pattern + "P", pattern + "S"]

  for i in potential_plays:
    if i not in step:
      step[i] = 0

  predict = max(potential_plays, key=lambda key: step[key])
  prediction = predict[-1:]

  ideal_response = {"P": "S", "R": "P", "S": "R"}
  
  return ideal_response[prediction]
