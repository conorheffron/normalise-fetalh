import pandas as pd
import sys
import evaluation
import normalise
from warnings import simplefilter


def assignment_1(decimals, include_hist, display_plots, save_plots, img_dir, csv_file):
    # Read fetal health data
    df = pd.read_csv(csv_file)

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
    print("The run-time arguments are: %s" % sys.argv)
    decimals = int(sys.argv[1])
    include_histogram_features = eval(sys.argv[2])
    display_plots = eval(sys.argv[3])
    save_plots = eval(sys.argv[4])
    img_dir = str(sys.argv[5])
    csv_file = str(sys.argv[6])

    simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

    assignment_1(decimals, include_histogram_features, display_plots, save_plots, img_dir, csv_file)