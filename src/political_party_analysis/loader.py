from pathlib import Path
from typing import List
from urllib.request import urlretrieve

import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler


class DataLoader:
    """Class to load the political parties dataset"""

    data_url: str = "https://www.chesdata.eu/s/CHES2019V3.dta"

    def __init__(self):
        self.party_data = self._download_data()
        self.non_features = []
        self.index = ["party_id", "party", "country"]

    def _download_data(self) -> pd.DataFrame:
        data_path, _ = urlretrieve(
            self.data_url,
            Path(__file__).parents[2].joinpath(*["data", "CHES2019V3.dta"]),
        )
        return pd.read_stata(data_path)

    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to remove duplicates in a dataframe"""

        df = df.drop_duplicates() 
        return df
        

    def remove_nonfeature_cols(
        self, df: pd.DataFrame, non_features: List[str], index: List[str]
    ) -> pd.DataFrame:
        """Write a function to remove certain features cols and set certain cols as indices
        in a dataframe"""
        
        df.drop(non_features, axis=1, inplace=True)
        df.set_index(index, inplace=True) #eastwest - exception iceland(would make it 1)
        return df
       

    def handle_NaN_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to handle NaN values in a dataframe"""
    
        threshold = int(len(df) / 2) # may need to be adjusted
        df.dropna(axis=1, thresh=threshold, inplace=True) #turkey
        
        imputer = KNNImputer(n_neighbors=3, weights="distance")
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns, index=df.index)
        
        return df_imputed
    
    def scale_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to normalise values in a dataframe. Use StandardScaler."""

        scaler = StandardScaler()
        normalized_values = scaler.fit_transform(df.values)
        normalized_df = pd.DataFrame(normalized_values, columns=df.columns, index=df.index)

        return normalized_df


    def preprocess_data(self):
        """Write a function to combine all pre-processing steps for the dataset"""
        
        self.party_data = self.remove_duplicates(self.party_data)
        self.party_data = self.remove_nonfeature_cols(self.party_data, self.non_features, self.index)
        self.party_data = self.handle_NaN_values(self.party_data)
        self.party_data = self.scale_features(self.party_data)