import numpy as np
import gym

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam, SGD

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

from env import GameEnv


# Get the environment and extract the number of actions.
env = GameEnv(shape=(5, 5))
nb_actions = env.action_space.n

memory_window = 1

# Next, we build a very simple model.
model = Sequential()
model.add(Flatten(input_shape=(memory_window,) + env.observation_space.shape))
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dense(128))
model.add(Activation('relu'))
#model.add(Dense(256))
#model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))
print(model.summary())

# Finally, we configure and compile our agent. You can use every
# built-in Keras optimizer and even the metrics!
memory = SequentialMemory(limit=50000, window_length=memory_window)
policy = BoltzmannQPolicy()
dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory,
               nb_steps_warmup=100, target_model_update=1e-2,
               policy=policy)
dqn.compile(SGD(lr=1e-3), metrics=['mae'])

# Okay, now it's time to learn something! We visualize the training
# here for show, but this slows down training quite a lot. You can
# always safely abort the training prematurely using Ctrl + C.
dqn.fit(env, nb_steps=50000, visualize=False, verbose=2)

# test:
dqn.test(env, nb_episodes=5, visualize=True)
