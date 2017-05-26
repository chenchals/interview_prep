from collections import OrderedDict

# RETURN AN EMPTY LIST IF NO ITEM ASSOCIATION IS GIVEN
def largestItemAssociation(itemAssociation):
    '''
    Idea:
    Use graph traversal to traverse entire graph, count the size of each path while traversing.
    Iterate all nodes and return the longest (or tied) path.
    Have a set to store visited nodes, track the best-value-so-far
    :param itemAssociation: list of edges (node, node) tuples
    :return: the longest path
    '''
    g = _build_graph(itemAssociation)
    # Both BFS and DFS works, here I use BFS
    best_so_far = {
        'path': [],
        'len': 0
    }
    visited = set()
    for node in g:
        # traverse every node in the graph, ignore already visited
        if node in visited:
            continue
        stack = list()
        stack.append(node)
        current_path = {
            'path': [],
            'len': 0
        }
        while len(stack) != 0:
            current = stack.pop(0)
            for neighbour in g[current]:
                if neighbour not in visited:
                    stack.append(neighbour)
            visited.add(current)
            current_path['path'].insert(0,current)
            current_path['len'] += 1
        if current_path['len'] == best_so_far['len']:
            best_so_far = current_path if current_path['path'][0] > best_so_far['path'][0] else best_so_far
        if current_path['len'] > best_so_far['len']:
            best_so_far = current_path
    return best_so_far['path']


def _build_graph(g):
    # iterate edge list and build graph.
    # the way I use to represent a graph is to use a adjacency list
    # build adj_list
    # undirect graph, create symmetric adj list
    # adj_list = {}
    adj_list = OrderedDict()
    for edge in g:
        if len(edge) == 0:
            continue
        if len(edge) != 2:
            raise Exception('Edge requires two nodes, current edge', str(edge))
        u,v = edge
        # undirect graph, add symmetric edges
        for _u, _v in [(u, v), (v, u)]:
            if _u in adj_list:
                adj_list[_u].append(_v)
            else:
                # I wanna use set, but set doesn't preserve the order, so I use list here
                # adj_list[_u] = set()
                # adj_list[_u].add(_v)
                adj_list[_u] = list()
                adj_list[_u].append(_v)
    adj_list = OrderedDict(reversed(adj_list.items()))
    return adj_list

# path = [['item1','item2'], ['item3', 'item4']]
path = [['item1','item2'], ['item3', 'item4'], ['item4', 'item5']]
ret = largestItemAssociation(path)
print(ret)