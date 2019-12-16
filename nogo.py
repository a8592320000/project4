import MCTS
import board as bo
quit = False
com = ['boardsize','clear_board','genmove','play','quit']
pos_dic = {}
repos_dic = {}
for i in range(81):
    string = chr(i // 9 + 65) + str(i % 9 +1)
    if string[0] == 'i':
        string = 'j' + string[1]
    pos_dic[string] = i
    repos_dic[i] = string
while not quit:
    command = input()
    command = command.split(' ')
    if command[0] in com:
        if command[0] == 'genmove':
            pos = mc.predict()
            print('=' + repos_dic[pos] + '\n')
        if command[0] == 'play':
            mc.opponent(pos_dic[command[2]])
            print('=\n')
        if command[0] == 'boardsize':
            b = bo.Board(int(command[1]),int(command[1]))
            mc = MCTS(b,10)
    else:
        print('=\n')
