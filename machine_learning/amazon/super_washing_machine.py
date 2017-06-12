class Flatten(object):
    def __init__(self):
        pass

    def argmin_avg(self, array):
        pass

    def max_entropy(self, array):
        # find the equilibrium dresses/num_machines, if == 0, equilibrium is 0
        # next step is to maximize the
        pass

    def eval(self, array):
        return all(x == array[0] for x in array)

    def tree_search(self, array):
        '''
        Depth first search, check termination conditions and traverse all neighbours,
        :param array:
        :return:
        '''
        pass

    def get_neighbours(self, array):
        ret = []
        for i in range(len(array)):
            if i > 0:
                array[i-1] = array[i-1]

    def dp(self, array):
        pass

    def heuristic(self, array):
        pass

    def appsoximation(self, array):
        pass