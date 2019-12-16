import time as t
import random as r

def tc():
    count = globals().get('time_counter',False)
    if count:
        print(t.time()-timecounter)
        globals()['time_counter'] = False
    else:
        globals()['timecounter'] = t.time()
        globals()['time_counter'] = True

def x(i):
    for i in range(2):
        i+i
    return i
if __name__ == '__main__':
    p = []
    N = 100000
    tc()

    for i in range(N):
        a = x(1)
        b = x(1)
        p.append(a+b)

    tc(1)

    tc()

    for i in range(N):
        a = x(1)
        p.append(x(1) + a)

    tc(1)


