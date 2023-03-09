"""
    This file contains the class creation of a KNN algorithm from scratch and was
    not implemented with scikit-learn but rather with numpy
"""

import numpy as np

class KMeans:
    """Class implementing the core logic of KMeans algorithm"""

    def __init__(self, n_clusters, max_iters=1000, tol=1e-5):
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.tol = tol
        self.centroids = None
        self.labels = None

    def _calc_distance(self, X):
        """Function to calculate the distance between points to assign into cluster"""
        distances = np.zeros((X.shape[0], self.n_clusters))
        print(distances.shape)
        for i, centroid in enumerate(self.centroids):
            distances[:, i] = np.linalg.norm(X - centroid, axis=1)
        return distances

    def fit(self, X):
        """Function to fit onto the training dataset"""

        n_samples, n_features = X.shape

        #Initialise centroids randomly
        idx = np.random.choice(n_samples, self.n_clusters, replace=False) 
        self.centroids = X[idx]

        for i in range(self.max_iters):
            #assign each data point to the nearest centroid
            distances =self._calc_distance(X)           #Here we are calculating the distance btw each point and the relative centroid
            self.labels = np.argmin(distances, axis=1)  #Choosing the value closest to the centroid row-wise

            #update the centroids
            new_centroids = np.zeros((self.n_clusters, n_features))
            for j in range(self.n_clusters):
                new_centroids[j] = np.mean(X[self.labels==j], axis=0)

            #Check for convergence
            if np.sum(np.abs(new_centroids - self.centroids)) < self.tol:
                break

            self.centroids = new_centroids

    def predict(self, X):
        distances = self._calc_distance(X)
        return np.argmin(distances, axis=1)