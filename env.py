import os
import gym
from gym import spaces
import numpy as np
import game

class GameEnv(gym.Env):
    """Gym environment for 2048 game."""
    metadata = {'render.modes': ['human']}

    def __init__(self, shape=(4, 4)):
        super(GameEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        self.shape = shape
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(
            low=0, high=15, shape=shape, dtype=np.uint8)
        self.arr = np.zeros(shape, dtype='uint8')


    def step(self, action):
        # Execute one time step within the environment
        (self.arr, alive) = game.spawn(self.arr)
        (dim, dir) = (action // 2, action % 2)
        # print("Taking action {}.".format((dim, dir)))
        (self.arr, succ) = game.move(self.arr, dim, dir)
        # reward = 1 if succ else 0 #-np.sum(self.arr)
        # reward = 100 - np.sum(self.arr) + 5 * np.max(self.arr) if succ else 0
        reward = (float(self.arr.size - np.count_nonzero(self.arr))
                  / self.arr.size)
        return self.arr, reward, not alive, {}


    def reset(self):
        # Reset the state of the environment to an initial state
        self.arr = np.zeros(self.shape, dtype='uint8')
        return self.arr


    def render(self, mode='human', close=False):
        # Render the environment to the screen
        game.render(self.arr)
        raw_input("Enter to continue.")
        os.system('clear')
    
