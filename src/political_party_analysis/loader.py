from pathlib import Path
from urllib.request import urlretrieve

import pandas as pd


class DataLoader:
    """Class to load the political parties dataset"""

    data_url: str = "https://www.chesdata.eu/s/CHES2019V3.dta"

    def __init__(self) -> None:
        """Initialize the data loader."""
        self.party_data = self._download_data()
        self.non_features = []
        self.index = ["party_id", "party", "country"]

    def _download_data(self) -> pd.DataFrame:
        """Download the dataset."""
        data_path, _headers = urlretrieve(
            self.data_url,
            filename=Path(__file__).parents[2] / "data" / "CHES2019V3.dta",
        )
        return pd.read_stata(data_path)

    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        """Remove duplicates in DataFrame."""
        ##### YOUR CODE GOES HERE #####

    def remove_nonfeature_cols(
        self, df: pd.DataFrame, non_features: list[str], index: list[str]
    ) -> pd.DataFrame:
        """Remove non-feature cols and set certain cols as indices in the DataFrame."""
        ##### YOUR CODE GOES HERE #####

    def handle_NaN_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Handle NaN values in the DataFrame."""
        ##### YOUR CODE GOES HERE #####

    def scale_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Normalise values in the DataFrame using StandardScaler."""
        ##### YOUR CODE GOES HERE #####

    def preprocess_data(self) -> None:
        """Combine all pre-processing steps for the dataset."""
        ##### YOUR CODE GOES HERE #####
