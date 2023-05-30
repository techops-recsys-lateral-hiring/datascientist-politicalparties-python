import pandas as pd
import numpy as np


class DensityEstimator:
    """Class to estimate Density/Distribution of the given data.
    1. Write a function to model the distribution of the political party dataset
    2. Write a function to randomly sample 10 parties from this distribution
    3. Map the randomly sampled 10 parties back to the original higher dimensional
    space as per the previously used dimensionality reduction technique.
    """

    def __init__(self, data: pd.DataFrame, dim_reducer, high_dim_feature_names):
        self.data = data
        self.dim_reducer_model = dim_reducer.model()
        self.feature_names = high_dim_feature_names

    def multivariate_normal_mle_estimator(self):
        """Calculate the MLE estimates of mean and covariance matrix from a sample.
        """
        self.mean = self.data.mean()
        self.cov = np.cov(self.data)

    def multivariate_normal_variable_generator(self, size:int) -> np.array:
        """ Generate random variables from a multivariate normal distribution.
        """
        
        return np.random.multivariate_normal(mean=self.mean, cov=self.cov, size=size)
    
    def map_to_original(self, reduced_data: np.array) -> np.array:
        """Convert reduced data back to its initial dimensions.
        """
        
        high_dimension_data = self.dim_reducer_model.inverse_transform(reduced_data)
        return high_dimension_data


