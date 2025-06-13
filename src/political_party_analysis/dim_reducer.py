import pandas as pd


class DimensionalityReducer:
    """Class to model a dimensionality reduction method for the given dataset.
    1. Write a function to convert the high dimensional data to 2 dimensional.
    """

    def __init__(self, data: pd.DataFrame, n_components: int = 2) -> None:
        self.n_components = n_components
        self.data = data

    def transform(self) -> pd.DataFrame:
        """Transform this instance's data to lower number of dimensions."""
        ##### YOUR CODE GOES HERE #####
