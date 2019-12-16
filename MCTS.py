import copy
import board as bo
import random
import math
import time
from 測試 import tc
class MCTS_obj():
    def __init__(self,board,time_limit):
        self.board = board
        self.tree = {}
        self.time_limit = time_limit
        color = self.board.available_color
        self.expend(self.tree,copy.deepcopy(self.board))
        for i in self.tree['legal_pos'][self.board.color_index[color]]:
            test_b = copy.deepcopy(self.board)
            test_b.add(i)
            self.expend(self.tree[i],test_b)
        self.leaf_first_play()


    def expend(self,leaf,board):
        leaf['legal_pos'] = board.legal_pos
        leaf['board'] = board
        leaf['played'] = 0
        leaf['win'] = 0
        leaf['root_2log_played'] = 0
        leaf['root_played'] = 0
        leaf['win_rate'] = 0
        for i in board.legal_pos[board.color_index[board.available_color]]:
            leaf[i] = {}
    def leaf_first_play(self):
        self.tree['played'] += len(self.tree['legal_pos'])
        self.tree['root_2log_played'] = (2 * math.log(self.tree['played'])) ** 0.5
        t_board = self.tree['board']
        for l in self.tree['legal_pos'][t_board.color_index[t_board.available_color]]:
            child = self.tree[l]
            child['played'] += 1
            child['root_played'] = 1
            child['win'] += self.random_play(copy.deepcopy(child['board']))
            child['win_rate'] = child['win']
    def UCB(self):
        pos = self.UCB_pos_choice()
        result = self.random_play(copy.deepcopy(self.tree[pos]['board']))
        self.UCB_update(pos,result)

    def UCB_pos_choice(self):
        max_score = 0
        pos = 0
        for p in self.tree['board'].legal_pos[self.tree['board'].color_index[self.tree['board'].available_color]]:
            if self.tree[p]['root_played'] == 0:
                print(self.tree)
            score = self.tree[p]['win_rate'] + self.tree['root_2log_played'] / self.tree[p]['root_played']
            if score > max_score:
                max_score = score
                pos = p
        return pos
    def UCB_update(self,pos,result):
        t = self.tree
        targ = self.tree[pos]
        t['played'] += 1
        targ['played'] += 1
        if result:
            t['win'] += result
            targ['win'] += result
        t['win_rate'] = t['win'] / t['played']
        targ['win_rate'] = targ['win'] / targ['played']
        t['root_2log_played'] = (2 * math.log(self.tree['played'])) ** 0.5
        targ['root_played'] = targ['played'] ** 0.5

    def random_play(self,board):
        color = board.available_color
        try:
            i = random.choice(board.legal_pos[board.color_index[board.available_color]])
        except:
            return 0
        while not board.add(i):
            try:
                i = random.choice(board.legal_pos[board.color_index[board.available_color]])
            except:
                i = 0
        if color == board.add(i):
            return 0
        else:
            return 1
    def predict(self):
        t = time.time()
        while time.time() - t < self.time_limit - 0.5:
            for i in range(100):
                self.UCB()
        return self.UCB_pos_choice()
    def update(self,pos):
        self.tree = self.tree[pos]
        self.board = self.tree['board']
        for i in self.tree['legal_pos'][self.tree['board'].color_index[self.tree['board'].available_color]]:
            test_b = copy.deepcopy(self.board)
            test_b.add(i)
            self.expend(self.tree[i],test_b)

    def opponent(self,pos):
        self.update(pos)
        self.leaf_first_play()
    def resign(self):
        if len(self.board.legal_pos[self.board.color_index[self.board.available_color]]) == 0:
            return True
        else:
            return False

    def __str__(self):
        return self.tree.__str__()


if __name__ == '__main__':
    b = bo.Board(4,4)
    R = False
    mc = MCTS_obj(b, 0.6)
    mc.opponent(0)
    while not R:
        tc()
        po = mc.predict()
        mc.update(po)
        mc.opponent(mc.tree['legal_pos'][0][0])
        R = mc.resign()
        tc()


