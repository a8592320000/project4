import copy
import board as bo
import random
from 測試 import tc
class MCTS_obj():
    def __init__(self,row,column,time_limit):
        self.board = bo.Board(row,column)
        self.tree = {}
        self.time_limit = time_limit
        color = self.board.available_color
        self.expend(self.tree,copy.deepcopy(self.board))
        for i in self.tree['leagle_pos'][self.board.color_index[color]]:
            test_b = copy.deepcopy(self.board)
            test_b.add(i)
            self.expend(self.tree[i],test_b)


    def expend(self,leaf,board):
        leaf['leagle_pos'] = board.leagle_pos
        leaf['board'] = board
        leaf['played'] = 0
        leaf['win'] = 0
        for i in board.leagle_pos[board.color_index[board.available_color]]:
            leaf[i] = {}

    def play_forward(self):
        self.tree['played'] += 1


    def random_play(self,board,pos):
        color = board.available_color
        i = pos
        while not board.add(i):
            try:
                i = random.choice(board.leagle_pos[board.color_index[board.available_color]])
            except:
                i = 0
        if color == board.add(i):
            return 0
        else:
            return 1


    def __str__(self):
        return self.tree.__str__()


if __name__ == '__main__':
    mc = MCTS_obj(9, 9, 1)
    tc()
    for i in range(4600):
        mc.random_play(copy.deepcopy(mc.board),0)
    tc()


