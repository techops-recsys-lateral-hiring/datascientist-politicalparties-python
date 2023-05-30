import pandas as pd
import pytest
import pdb
from political_party_analysis.dim_reducer import DimensionalityReducer

@pytest.fixture
def mock_df() -> pd.DataFrame:
    df = pd.DataFrame(
        data={
            "col1": [-1.225, 0, 1.225],
            "col2": [-1.175, -0.1, 1.257],
            "col3": [-1.019, -0.340, 1.359],
        },
        index=[0, 1, 2],
    )
    df.index.name = "id"
    return df

def test_dim_reducer(mocker, mock_df: pd.DataFrame):
    dim_reducer = DimensionalityReducer(data=mock_df)
    mocker.patch.object(dim_reducer, "data", mock_df)
    reduced_data = dim_reducer.transform_data()
    assert reduced_data.shape == (3, 2)