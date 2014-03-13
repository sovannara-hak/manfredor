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

def manfredor(list_obj, num_cluster=10):
    score_list = []
    for obj in list_obj:
        score_list.append(obj.computeScore())

    whitened = scipy.cluster.vq.whiten(score_list) 

    centroids, _ = scipy.cluster.vq.kmeans(whitened, num_cluster)
    idx,_ = scipy.cluster.vq.vq(whitened, centroids)

    clustered = {}
    i = 0
    for obj in list_obj:
        clustered[obj.url] = idx[i]
        i += 1

    return clustered


