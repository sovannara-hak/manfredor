import scipy.cluster.vq

class ManfObject(object):
    def __init__(self):
        self.url = ""
        self.tags = []
        self.rules = {}

    def computeScore(self):
        score = 0
        if len(self.rules) != 0:
            for t in self.tags:
                score += self.rules[t]
        return score

