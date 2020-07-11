# Implementation of 2048 game.
# 2020 Fabian Gloeckle

import numpy as np
from termcolor import colored

# TODO: mehrdimensional erlauben?!

def move_aux(arr):
    res = np.copy(arr)
    for i in range(arr.shape[0]):
        row = arr[i]
        elems = list(filter(lambda x: x != 0, row))
        try:
            index = list(map(lambda xy: xy[0] == xy[1], zip(elems, elems[1:]))).index(True)
            elems = elems[:index] + [(elems[index] + 1)] + elems[index+2:]
        except ValueError:
            pass
                        
        res[i] = elems + [0] * (arr.shape[1] - len(elems))
    return res

def move(arr, dim, dir):
    arr0 = np.moveaxis(arr, dim, 0)
    if dir == 1:
        arr0 = np.fliplr(arr0)
    res = move_aux(arr0)
    if dir == 1:
        res = np.fliplr(res)
    res = np.moveaxis(res, 0, dim)
    succ = not np.array_equal(arr, res)
    return (res, succ)


def move_num(arr, action):
    (dim, dir) = (action // 2, action % 2)
    return move(arr, dim, dir)
    

def rand_pos(shape):
    pos = []
    for l in shape:
        pos.append(np.random.randint(l))
    return tuple(pos)

def spawn(arr):
    new = np.random.randint(1, 2 + 1)
    if np.count_nonzero(arr) == arr.size:
        return (arr, False)
    while True:
        pos = rand_pos(arr.shape)
        if arr[pos] == 0:
            break
    res = np.copy(arr)
    res[pos] = new
    return (res, True)

# arr = np.array([[1, 3, 3, 0], [0, 0, 1, 1], [0, 1, 2, 3], [1, 1, 1, 1]])
# print(arr)
# print(move(arr, 0, 0))
# print(move(arr, 0, 1))
# print(move(arr, 1, 0))
# print(move(arr, 1, 1))
# print(spawn(arr))


def dim_dir(c):
    if c == 'a':
        return (0, 0)
    elif c == 'd':
        return (0, 1)
    elif c == 'w':
        return (1, 0)
    else:  # or only if c == 's'?
        return (1, 1)


def render(arr):
    colors = {1 : 'on_white', 2 : 'on_grey', 3 : 'on_blue', 4 : 'on_cyan',
              5 : 'on_green', 6 : 'on_yellow', 7 : 'on_red', 8 : 'on_magenta'}
    for row in arr:
        for e in row:
            e = int(e)
            if e == 0:
                print " ",
            elif 1 <= e <= 8:
                print colored(str(e), 'white', colors[e]),
            else:
                print e,
        print
        
def main():
    arr = np.zeros((4, 4), dtype='uint8')
    alive = True
    while alive:
        (arr, alive) = spawn(arr)
        print(arr)
        succ = False
        while not succ:
            c = input("Direction (w/a/s/d)? ")
            (dim, dir) = dim_dir(c)
            (new, succ) = move(arr, dim, dir)
        arr = new

# main()
