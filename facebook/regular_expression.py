def re_match(q, s):
    if q == '' and s =='':
        return True
    len_q = len(q)
    len_s = len(s)
    dp = [[False for _ in range(len_s+1)] for _ in range(len_q+1)]
    dp [0][0] = True if q[0] == s[0] or q[0] == '.' else False
    for i in range(1, len_s):
        if dp[0][i-1] and q[0] == '*':
            dp[0][i] = True

    for j in range(1, len_q):
        for i in range(1, len_s):
            if q[j] == '.' or q[j] == s[i]:
                dp[j][i] = dp[j-1][i-1]
            else: #q[j] == '*'
                pass
    print(dp)
    return dp[len(q)-1][len(s)-1]


q = 'a*bc'
s = 'abc'
ret = re_match(q,s)
print(ret)