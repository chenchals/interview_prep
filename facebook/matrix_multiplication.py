def mul(m1, m2):
    return 0




def mul_v(v1, v2):
    return sum([v1[i]*v2[i] for i in range(len(v1))])






v1 = [1,5,6]
v2 = [2,6,8]
print(mul_v(v1, v2))