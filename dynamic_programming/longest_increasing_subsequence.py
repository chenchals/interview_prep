def longest_increasing_subsequence(seq):
    dp = [1 for _ in seq]
    for i in range(1, len(seq)):
        for j in range(1, i-1):
            if seq[j] > seq[j-1] and dp[j] > dp[j-1]:
                dp[i] = dp[j] + 1
    return