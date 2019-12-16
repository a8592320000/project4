import numpy as np
class Board():
    def __init__(self,row,colum):
        self.value = [0 for i in range(row * colum)]
        self.shape = row,colum
        self.shape_max = row * colum
        self.group = {}
        self.neighbor = [self.__neighbor(i) for i in range(self.shape_max)]
        self.color_index = {1:1,-1:0}
        self.ban_white = [0 for i in range(row * colum)]
        self.ban_black = [0 for i in range(row * colum)]
        self.ban_board = [self.ban_white,self.ban_black]
        self.legal_pos_white = [i for i in range(row * colum)]
        self.legal_pos_black = [i for i in range(row * colum)]
        self.legal_pos = [self.legal_pos_white,self.legal_pos_black]
        self.available_color = 1

    def add(self,pos):
        color = self.available_color
        passed = self.check(pos,color)
        if passed[0]:
            self.value[pos] = color
            air = passed[2]
            new_group = []
            for f in passed[1]:
                if f[-1] == color:
                    new_group.append(f[:-1])
                    air += self.group[f] - 1
                    del self.group[f]
                else:
                    self.group[f] -= 1
            new_family = (pos,)
            for i in new_group:
                new_family += i
            self.group[new_family + (color,)] = air
            self.available_color *= -1
            if pos in self.legal_pos_black:
                self.legal_pos_black.remove(pos)
            if pos in self.legal_pos_white:
                self.legal_pos_white.remove(pos)
        elif pos in self.legal_pos[self.color_index[color]]:
            self.legal_pos[self.color_index[color]].remove(pos)
        else:
            return color

    def check(self,pos,color):
        if self.value[pos] == 1:
            return (False,)
        color_index = self.color_index[color]
        if self.ban_board[color_index][pos] == 1:
            return (False,)
        family = self.__family_detect(pos,color)
        zeros = self.__zero_neighbor_number(pos)
        if zeros > 0:
            for f in family:
                if self.group[f] <= 1:
                    if f[-1] != color:
                        self.ban_board[color_index][pos] = 1
                        return (False,)
        else:
            for f in family:
                if self.group[f] <= 1:
                    self.ban_board[color_index][pos] = 1
                    return (False,)
            if sum([color * f[-1] for f in family]) == -len(family) and len(family) != 0:
                self.ban_board[color_index][pos] = 1
                return (False,)
        return (True,family,zeros)


    def __family_detect(self,pos,color):
        nb = self.neighbor[pos]
        families = self.group.keys()
        targ = []
        for n in nb:
            for f in families:
                if (n in f[:-1]):
                    targ.append(f)
        return list(set(targ))


    def __neighbor(self,i):
        nei = []
        u = i - self.shape[1]
        r = i + 1
        d = i + self.shape[1]
        l = i -1
        if u >= 0 :
            nei.append(u)
        if (r < self.shape_max) and (i % self.shape[1] != (self.shape[1]-1)):
            nei.append(r)
        if d < self.shape_max:
            nei.append(d)
        if l >= 0 and (i % self.shape[1] != 0):
            nei.append(l)
        return tuple(nei)
    def __zero_neighbor_number(self,pos):
        return sum([1-abs(self.value[i]) for i in self.neighbor[pos]])
    def show(self):
        print(np.array(self.value).reshape(self.shape))
    def legal(self,color):
        lea = []
        for i in self.legal_pos[self.color_index[color]]:
            if self.check(i,color):
                lea.append(i)
        self.legal_pos[self.color_index[color]] = lea
        return lea
if __name__ == '__main__':
    b = Board(4,4)
    for i in [10,1,8,4]:
        b.add(i)
    b.check(0,b.available_color)
    b.show()
