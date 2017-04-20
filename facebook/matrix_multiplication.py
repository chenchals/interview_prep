def mul(m1, m2):
    ret = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    # print(ret, m1)
    m1 = sparse_matrix(m1)
    m2 = sparse_matrix(m2, col_index=True)
    # print(m1)
    # print(m2)
    for i in range(len(ret)):
        for j in range(len(ret[i])):
            sum = 0
            if i in m1 and j in m2:
                # print(i, j)  # <- correct
                # print(m1[i], i , j)
                for k in m1[i]:
                    v1 = m1[i][k]
                    # common entry, the intersection of two non zero entries
                    v2 = m2.get(j, {}).get(k, 0)
                    # print(i, k, v1, v2)
                    sum +=  v1 * v2
            ret[i][j]=sum
    return ret

def sparse_matrix(m, col_index=False):
    s_mat = {}
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] != 0:
                if col_index:
                    if j in s_mat:
                        s_mat[j][i] = m[i][j]
                    else:
                        s_mat[j] = {i:m[i][j]}
                else:
                    if i in s_mat:
                        s_mat[i][j] = m[i][j]
                    else:
                        s_mat[i] = {j:m[i][j]}
    return s_mat

def mul_v(v1, v2):
    return sum([v1[i]*v2[i] for i in range(len(v1))])

import random
import cProfile
def test(tid):
    l, u = 100, 200
    if l > u:
        return 'l must smaller than u'
    m,n,k = random.randint(l, u), random.randint(l, u), random.randint(l, u)
    mat1 = [[random.randint(0,1) for _ in range(n)] for _ in range(m)]
    mat2 = [[random.randint(0,1) for _ in range(m)] for _ in range(k)]
    ret = mul(mat1, mat2)

cProfile.run('test(9)')
