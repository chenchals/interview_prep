def RepresentsInt(s):
    try:
        return int(s)
    except ValueError:
        return 0

def totalScore(blocks, n):
    if len(blocks) == 0:
        return 0
    # This is like the calculator question, use a LIFO stack to store the operators and numbers
    results = []
    for cur in blocks:
        if cur in ['Z', 'X', '+']:
            if cur == '+':
                if len(results) == 0:  # empty
                    continue
                elif len(results) == 1:  # only one value
                    results.append(results[-1])
                else:
                    results.append(results[-1] + results[-2])
            elif cur == 'Z':
                if len(results) > 0:
                    results.pop()
                else:  # empty list
                    # do nothing
                    continue
            elif cur == 'X':
                if len(results) > 0:
                    results.append(results[-1] * 2)
                else:  # empty list
                    continue
        elif RepresentsInt(cur):
            results.append(int(cur))
        else:
            raise Exception('unknown type', str(type(cur)), str(cur))
    return sum(results)

# ret = totalScore([1,2,'+','Z'], 8)
# print(ret)

ret = totalScore(['1', '-2','+','Z' ,'"'], '8')
print(ret)