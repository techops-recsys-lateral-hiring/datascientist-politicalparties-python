from pathlib import Path

import matplotlib.pyplot as plt

from political_party_analysis.loader import DataLoader
from political_party_analysis.visualization import scatter_plot


if __name__ == "__main__":
    plots_path = Path(__file__).parent / "plots"
    data_loader = DataLoader()

    # Data pre-processing step
    ##### YOUR CODE GOES HERE #####

    # Dimensionality reduction step
    ##### YOUR CODE GOES HERE #####

    ## Uncomment this snippet to plot dim reduced data
    # plt.figure()
    # splot = plt.subplot()
    # scatter_plot(
    #     reduced_dim_data,
    #     color="r",
    #     splot=splot,
    #     label="dim reduced data",
    # )
    # plt.title("Prepared data reduced to 2 dimensions")
    # plt.savefig(plots_path / "dim_reduced_data.png")

    # Density estimation/distribution modelling step
    ##### YOUR CODE GOES HERE #####

    # Plot density estimation results here
    ##### YOUR CODE GOES HERE #####
    plt.savefig(plots_path / "density_estimation.png")

    # Plot left and right wing parties here
    plt.figure()
    splot = plt.subplot()
    ##### YOUR CODE GOES HERE #####
    plt.title("Lefty/righty parties")
    plt.savefig(plots_path / "left_right_parties.png")

    # Plot finnish parties here
    ##### YOUR CODE GOES HERE #####

    print("Analysis Complete")
