from pathlib import Path

from matplotlib import pyplot

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
    # pyplot.figure()
    # splot = pyplot.subplot()
    # scatter_plot(
    #     reduced_dim_data,
    #     color="r",
    #     splot=splot,
    #     label="dim reduced data",
    # )
    # pyplot.savefig(plots_path / "dim_reduced_data.png")

    # Density estimation/distribution modelling step
    ##### YOUR CODE GOES HERE #####

    # Plot density estimation results here
    ##### YOUR CODE GOES HERE #####
    pyplot.savefig(plots_path / "density_estimation.png")

    # Plot left and right wing parties here
    pyplot.figure()
    splot = pyplot.subplot()
    ##### YOUR CODE GOES HERE #####
    pyplot.savefig(plots_path / "left_right_parties.png")
    pyplot.title("Lefty/righty parties")

    # Plot finnish parties here
    ##### YOUR CODE GOES HERE #####

    print("Analysis Complete")
