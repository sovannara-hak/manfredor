import scipy.cluster.vq as scv
import numpy as np
import operator

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

def manfredor(list_obj, num_cluster=10):
    score_list = []
    for obj in list_obj:
        score_list.append(obj.computeScore())

    whitened = scv.whiten(score_list) 

    centroids, _ = scv.kmeans(whitened, num_cluster)
    idx,_ = scv.vq(whitened, centroids)

    rank = np.argsort(centroids)

    rank_mapping = dict(zip([c for c in centroids], rank))

    clustered = {}
    i = 0
    for obj in list_obj:
        clustered[obj.url] = rank_mapping[centroids[idx[i]]]
        i += 1

    sorted_cluster = sorted(clustered.iteritems(), key=operator.itemgetter(1))

    return sorted_cluster


