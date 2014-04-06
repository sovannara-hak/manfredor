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

class Manfredor(object):
    def __init__(self):
        self.rules = Rules()
        self.centroids = None
        self.list_obj = None
        self.clustered_obj = None

    def loadRules(self, rules_file_path):
        self.rules.loadRules(rules_file_path)

    def whitened(self):
        score_list = []
        for obj in self.list_obj:
            score_list.append(obj.computeScore(self.rules))

        #Normalize observations
        whitened = scv.whiten(score_list) 
        return whitened

    def cluster(self):
        whitened = self.whitened()
        self.centroids, _ = scv.kmeans(whitened, self.centroids)
        idx,_ = scv.vq(whitened, self.centroids)

        self.sortCluster(idx)

    def sortCluster(self, idx):
        #Get index that will sort centroids
        rank = np.argsort(self.centroids)

        #Map a centroid to a rank
        rank_mapping = dict(zip([c for c in self.centroids], rank))

        clustered = {}
        i = 0
        for obj in self.list_obj:
            cluster_of_obs = idx[i]
            centroid = self.centroids[cluster_of_obs]
            #map url to rank
            clustered[obj.url] = rank_mapping[centroid]
            i += 1

        self.clustered_obj = sorted(clustered.iteritems(), key=operator.itemgetter(1))

    def cluster_init(self, num_cluster=10):

        whitened = self.whitened()

        #Compute Kmeans on the set of observations
        #centroids contains the center of each cluster
        self.centroids, _ = scv.kmeans(whitened, num_cluster)

        #Assign each sample to a cluster
        idx,_ = scv.vq(whitened, self.centroids)

        self.sortCluster(idx)

