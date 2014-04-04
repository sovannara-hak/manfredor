import scipy.cluster.vq as scv
import numpy as np
import operator
from rules import Rules

class ManfObject(object):
    def __init__(self):
        self.url = ""
        self.tags = []

    def computeScore(self, rules):
        score = 0
        if rules != {}:
            for t in self.tags:
                score += rules.rules[t]
        else:
            print "Unrecognized tag, score: 0"
        return score

def manfredor(list_obj, rules, num_cluster=10):
    score_list = []
    for obj in list_obj:
        score_list.append(obj.computeScore(rules))

    #Normalize observations
    whitened = scv.whiten(score_list) 

    #Compute Kmeans on the set of observations
    #centroids contains the center of each cluster
    centroids, _ = scv.kmeans(whitened, num_cluster)

    #Assign each sample to a cluster
    idx,_ = scv.vq(whitened, centroids)

    #Get index that will sort centroids
    rank = np.argsort(centroids)

    #Map a centroid to a rank
    rank_mapping = dict(zip([c for c in centroids], rank))

    clustered = {}
    i = 0
    for obj in list_obj:
        cluster_of_obs = idx[i]
        centroid = centroids[cluster_of_obs]
        #map url to rank
        clustered[obj.url] = rank_mapping[centroid]
        i += 1

    sorted_cluster = sorted(clustered.iteritems(), key=operator.itemgetter(1))

    return sorted_cluster

