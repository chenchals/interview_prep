def check_valid(i_str):
    counter = 0
    # print(list(i_str))
    if len(i_str) == 0:
        return True
    if list(i_str)[0] == ')':
        return False
    for c in i_str:
        if c == '(':
            counter += 1
        if c == ')':
            if counter == 0:
                return False
            counter -= 1
    return counter == 0

def get_neighbors(i_str):
    n = list()
    i_str = list(i_str)
    for i in range(len(i_str)):
        neighbor = ''.join([i_str[x] for x in range(len(i_str)) if ((i_str[i] !='(' and i_str[i] != ')') or x != i)])
        n.append(neighbor)
    # print(n)
    return n

def BFS(i_str):
    if len(i_str) == 0:
        return [""]
    if check_valid(i_str):
        return [i_str]
    neighbors = get_neighbors(i_str)
    queue = neighbors
    ret = set()
    visited = set()
    found = False
    while len(queue) != 0:
        c = queue.pop(0)
        visited.add(c)
        if check_valid(c):
            found = True
            ret.add(c)
        if not found:
            for neighbor in get_neighbors(c):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
    return  list(ret)


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return BFS(s)


if __name__ == "__main__":
    test_case = "n"
    test_case = ")"
    # test_case = "()()n)()"
    # test_case = "(()((()d)o"
    test = Solution()
    print(test.removeInvalidParentheses(test_case))
