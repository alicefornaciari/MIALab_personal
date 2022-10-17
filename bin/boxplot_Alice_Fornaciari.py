import matplotlib.pyplot as plt
import numpy as np

#import pandas as pd


def main():
    # todo: load the "results.csv" file from the mia-results directory
    # todo: read the data into a list
    import csv
    with open('results.csv') as res:
        csv_reader = csv.reader(res)
        results_list = list(csv_reader)

    print(results_list)

    #alternative
    #data = pd.read_csv("results.csv")
    #data

    # todo: plot the Dice coefficients per label (i.e. white matter, gray matter, hippocampus, amygdala, thalamus)
    #  in a boxplot

    # Multiple box plots on one Axes
    fig, ax = plt.subplots()
    ax.boxplot(results_list)

    ax[0, 0].plot(results_list[0])
    ax[0, 0].set_title('White matter')

    ax[0, 1].plot(results_list[1])
    ax[0, 1].set_title('Gray matter')

    ax[0, 2].plot(results_list[2])
    ax[0, 2].set_title('Hippocampus')

    ax[0, 3].plot(results_list[3])
    ax[0, 3].set_title('Amygdala')

    ax[0, 4].plot(results_list[4])
    ax[0, 4].set_title('Thalamus')

    plt.title('Dice coefficients Boxplot')
    plt.show()

    # alternative: instead of manually loading/reading the csv file you could also use the pandas package
    # but you will need to install it first ('pip install pandas') and import it to this file ('import pandas as pd')
    pass  # pass is just a placeholder if there is no other code


if __name__ == '__main__':
    main()
