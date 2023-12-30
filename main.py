import pandas as pd

import evaluation
import normalise


def assignment_1(decimals, include_hist, display_plots, save_plots, img_dir):
    # Read fetal health data
    df = pd.read_csv('../fetal_health_datasets/fetal_health.csv')

    # Clean / pre-process data
    # Drop severe_decelerations column after analysis of z sums
    df = df.drop('severe_decelerations', axis=1)

    normalise_fetal_health(df, include_hist, decimals)

    evaluation.evaluation_output(df)

    evaluation.plot_features(df, save_plots, display_plots, img_dir)


def normalise_fetal_health(df, include_hist, decimals):
    # Loop through columns in data frame & normalise numeric features where relevant
    for c in df.columns:
        if (c == "fetal_health") or (c.startswith("histogram") and not include_hist):
            if c == "fetal_health":
                normalise.fetal_health(df, decimals)
            continue
        else:
            # Normalise all other numeric features (continuous...)
            normalise.numerical_features(c, df, decimals)


if __name__ == '__main__':
    # Main run configurations
    decimals = 3
    include_histogram_features = True
    display_plots = False
    save_plots = False
    img_dir = 'plots/'

    # Run assignment 1 code
    assignment_1(include_histogram_features, decimals, display_plots, save_plots, img_dir)