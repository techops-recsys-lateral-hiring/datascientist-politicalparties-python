import pandas as pd
from sklearn.decomposition import PCA


class DimensionalityReducer:
    """Class to model a dimensionality reduction method for the given dataset.
    1. Write a function to convert the high dimensional data to 2 dimensional.
    """

    def __init__(self, data: pd.DataFrame, n_components: int = 2):
        self.n_components = n_components
        self.data = data
        self.feature_columns = data.columns

    def pca(self) -> pd.DataFrame:
        """Convert high-dimensional data to 2-dimensional using PCA."""

        pca = PCA(n_components=self.n_components)
        reduced_data = pca.fit_transform(self.data[self.feature_columns])
        reduced_df = pd.DataFrame(reduced_data, columns=["pc1", "pc2"])
        reduced_df.index = self.data.index
        return reduced_df
