import re
import board
text = '''B[ii];W[ia];B[aa];W[ai];B[hh];W[ih];B[hg];W[gi];B[if];W[bh];B[ah];W[bg];B[ci];W[af];B[he];W[be];B[bf];W[hf];B[ae];W[ie];B[ac];W[ab];B[bc];W[bb];B[ic];W[cc];B[cd];W[da];B[df];W[gd];B[ff];W[fa];B[ea];W[gb];B[gc];W[ec];B[ga];W[ef];B[dg];W[cg];B[fi]'''#;W[ce];B[ba];W[de];B[dh];W[di];B[eh];W[fh];B[gg];W[dc];B[ge];W[ee];B[ed];W[bd];B[dd];W[fe];B[hd]'''
text = text.split(';')
print(text)
print(ord('A'))
B = board.Board(9,9)
import numpy as np
A = np.zeros((9,9),dtype=int)
for s in text:
    i,j = ord(s[2]) - ord('a'),ord(s[3]) - ord('a')
    if s[0] == 'B':
        A[i,j] = 1
        B.add(i*9+j,1)
    else:
        A[i, j] = -1
        B.add(i*9+j, -1)
print(B.add(80,-1))
print(np.sum(A))
import matplotlib.pyplot as plt
plt.imshow(A)
plt.colorbar()
plt.savefig('HAHANOGO')
plt.show()

