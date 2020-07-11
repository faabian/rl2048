import numpy as np
import gym

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam, SGD

from sklearn.model_selection import train_test_split

import game

n_samples = 50000

shape = (4, 4)

x = np.random.randint(5, size=(n_samples,) + shape)
actions = np.zeros((n_samples,), dtype='int')    # np.random.randint(4, size=(n_samples,))
y = np.copy(x)
for i in range(len(x)):
    y[i], _ = game.move_num(x[i], actions[i])
x = x.reshape(n_samples, -1)
actions = actions.reshape(n_samples, 1)
x_a = np.concatenate((x, actions), axis=1)
print(x_a.shape)
y = y.reshape(n_samples, -1)

x_train, x_val, y_train, y_val = train_test_split(x_a, y, test_size=0.2)

size = np.prod(shape)

model = Sequential()
# model.add(Flatten(input_shape=(size + 1,)))
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dense(size))
# model.add(Activation('linear'))
# print(model.summary())

# Finally, we configure and compile our agent. You can use every
# built-in Keras optimizer and even the metrics!
# model.compile(SGD(lr=1e-3), metrics=['mae'])
model.compile(optimizer='adam', loss='mae', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=100, batch_size=32,
        validation_data=(x_val, y_val))

for i in range(10):
    print("Before:")
    game.render(x_val[i][:-1].reshape(shape))
    print("After:")
    game.render(y_val[i].reshape(shape))
    print("Prediction:")
    game.render(np.round(
        model.predict(x_val[i].reshape(1, 17))).reshape(shape))

# Okay, now it's time to learn something! We visualize the training
# here for show, but this slows down training quite a lot. You can
# always safely abort the training prematurely using Ctrl + C.
# model.fit(env, nb_steps=50000, verbose=2)

# test:
# dqn.test(env, nb_episodes=5, visualize=True)
