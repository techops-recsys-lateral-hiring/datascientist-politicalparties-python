import pandas as pd
import numpy as np
from sklearn.decomposition import PCA


class DimensionalityReducer:
    """Class to model a dimensionality reduction method for the given dataset.
    1. Write a function to convert the high dimensional data to 2 dimensional.
    """

    def __init__(self, data: pd.DataFrame, n_components: int = 2):
        self.n_components = n_components
        self.data = data
        self.feature_columns = data.columns

    def model(self):
        """Create a PCA model object with 2 principal components"""
       
        pca = PCA(n_components=self.n_components)
        return pca

    def transform_data(self) -> np.array:
        """Convert high-dimensional data to 2-dimensional using the dimension reduction model."""
        
        reduced_data = self.model().fit_transform(self.data[self.feature_columns]) 
        return reduced_data
    
    def map_to_original(self, reduced_data: np.array) -> np.array:
        """Convert reduced data back to its initial dimensions"""
        
        high_dimension_data = self.model().inverse_transform(reduced_data)
        return high_dimension_data

