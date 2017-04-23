dc = {
    '0':" ",
    '1':"",
    '2':"abc",
    '3':"def",
    '4':"ghi",
    '5':"jkl",
    '6':"mno",
    '7':"pqrs",
    '8':"tuv",
    '9':"wxyz"
}

def letter_combination(num):
    num = list(num)
    results = []
    com = ['' for _ in range(len(num))]
    ind = 0
    _impl(num, com, ind, results)
    return results

def _impl(num, com, ind, buffer):
    # print(num, len(num), ind, com)
    if ind == (len(num)):
        s = ''.join(com)
        if s != '':
            buffer.append(s)
        return
    n = dc[num[ind]]
    # print(dc[num[ind]])
    if dc[num[ind]] == '':
        n = ['']
    for char in n:
        com[ind] = char
        next_ind = ind+1
        _impl(num, com, next_ind, buffer)
    return

input = ''
print(letter_combination(input))