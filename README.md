# rl2048
Reinforcement learning for the 2048 game.

## Game
See for example https://2048game.com/.

## Frameworks
We use Keras, the keras-rl library for reinforcement learning models and the OpenAI Gym framework for modelling the interface. Note that keras-rl depends on tensorflow-1.x.

## File overview:

game.py : game logic and simple rendering

env.py : OpenAI Gym Env class for reinforcement learning models in keras-rl

dqn.py : attempt at solving with DQN model (adapted keras-rl example file, not working)

cem.py : attempt at solving with DQN model (adapted keras-rl example file, not working)

predict.py : dense MLP model for predicting next states (works for fixed direction with about 0.05 mean absolute error loss)