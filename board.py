import numpy as np
class Board():
    def __init__(self,row,colum):
        self.value = [0 for i in range(row * colum)]
        self.shape = row,colum
        self.shape_max = row * colum
        self.group = {}
        self.neighbor = [self.__neighbor(i) for i in range(self.shape_max)]
        self.ban_white = [0 for i in range(row * colum)]
        self.ban_black = [0 for i in range(row * colum)]
        self.ban_board = [self.ban_white,self.ban_black]

    def add(self,pos,color):
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
        else:
            print('error')


    def check(self,pos,color):
        if self.value[pos] == 1:
            return (False,)
        color_index = int((color + 1) / 2)
        if self.ban_board[color_index][pos] == 1:
            return False
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
        return (True,family,zeros)


    def __family_detect(self,pos,color):
        nb = self.neighbor[pos]
        families = self.group.keys()
        targ = []
        for n in nb:
            for f in families:
                if (n in f[:-1]) and f[-1] == color:
                    targ.append(f)
        return targ


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
        return sum([abs(self.value[i]) for i in self.neighbor[pos]])
    def show(self):
        print(np.array(self.value).reshape(self.shape))
if __name__ == '__main__':
    b = Board(9,9)
    b.add(12,-1)
    b.add(11,1)
    b.add(11,1)
    b.show()