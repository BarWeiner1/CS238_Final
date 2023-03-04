import numpy as np
import random

class TradingAgent(object):
  """ A simple Deep Q agent """
  def __init__(self, state_size, action_size):
    self.state_size = state_size
    self.action_size = action_size
    self.gamma = 0.95  # discount rate
    self.epsilon = 1.0  # exploration rate
    self.epsilon_min = 0.01
    self.epsilon_decay = 0.95
    # TODO use multilayer perceptron to get next states
    #self.model = mlp(state_size, action_size)


def perform_update(self, batch_size=32):
    for i in range(batch_size):
        states =
        actions =
        rewards =
        next_states =
        done =

        # Use Bellman Equation to optimize Q lerning Q(s', a)
        target = rewards + self.gamma * np.amax(self.model.predict(next_states), axis=1)
        target[done] = rewards[done]

        # Q(s, a)
        target_f = self.model.predict(states)
        # make the agent to approximately map the current state to future discounted reward
        target_f[range(batch_size), actions] = target

        self.model.fit(states, target_f, epochs=1, verbose=0)

        if self.epsilon > self.epsilon_min:
          self.epsilon *= self.epsilon_decay