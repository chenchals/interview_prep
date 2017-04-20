def add_bin(a, b):
    if a == '0' and b == '0':
        return '0'
    # reverse string before pass the recursion
    # a = a[::-1]
    # b = b[::-1]
    a = [int(s) for s in a]
    b = [int(s) for s in b]
    # a.reverse()
    # b.reverse()
    return _add_bin(a, b, 0)

def _add_bin(a, b, buf):
    '''
    2 scenarios:
     <= 1
     > 1
     for each buf = 0 or 1
     check current
     to next with buf
     return current char
    '''
    if len(a) == 0 and len(b) == 0:
        return str(buf) if buf ==1 else ''
    if len(a) == 0:
        a = [0]
    if len(b) == 0:
        b = [0]
    inc = 1 if buf + a[-1] + b[-1] > 1 else 0
    ret = (a[-1] + b[-1] + buf) % 2
    return _add_bin(a[:-1], b[:-1], inc)+str(ret)

s = add_bin('1','101')
print(s)