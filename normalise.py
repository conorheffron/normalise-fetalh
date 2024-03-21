import pandas as pd


def fetal_health(df, decimals):
    # Note: Fetal health is class label (3X) but plan to verify as categorical (nominal) feature
    fetal_health_dict = {'Pathological': 3, 'Suspect': 2, 'Normal': 1, None: 0}

    # Assign int value for fetal health to new column 'fetal_health_categorical'
    df["fetal_health_int"] = df["fetal_health"].apply(lambda x: fetal_health_dict.get(x))

    # absolute difference (after normalisation)
    dict_len = len(fetal_health_dict)
    df["z_i_fetal_health"] = df["fetal_health_int"].apply(lambda x: round(abs((x - dict_len) / dict_len), decimals))


def numerical_features(c, df, decimals):
    # Column labels (max, min, difference, z value etc)
    max_c = "max_" + c
    min_c = "min_" + c
    diff_curr_min_c = "diff_curr_min_" + c
    diff_max_min_c = "diff_max_min_" + c
    z_i = "z_i_" + c
    mean_c = "mean_" + c
    sd_c = "sd_" + c

    # Data manipulation (create max, min, difference and z value columns)
    df[max_c] = pd.to_numeric(max(df[c]))
    df[min_c] = pd.to_numeric(min(df[c]))
    df[diff_curr_min_c] = pd.to_numeric(df[c]) - pd.to_numeric(min(df[c]))
    df[diff_max_min_c] = pd.to_numeric(max(df[c])) - pd.to_numeric(min(df[c]))
    df[mean_c] = pd.to_numeric(df[c]).median()
    df[sd_c] = str(pd.to_numeric(df[c]).std())
    df[z_i] = round(df[diff_curr_min_c] / df[diff_max_min_c], decimals)  # Rounding to specified decimals

    # For numeric or continuous variables
    # The absolute difference after normalisation to range [0, 1] is preferred
    print("------------------------------------------------")
    print("Min of " + c + " is: " + str(pd.to_numeric(df[c]).min()))
    print("Max of " + c + " is: " + str(pd.to_numeric(df[c]).max()))
    print("Mean of " + c + " is: " + str(pd.to_numeric(df[c]).mean()))
    print("Median of " + c + " is: " + str(pd.to_numeric(df[c]).median()))
    print("Standard Deviation of " + c + " is: " + str(pd.to_numeric(df[c]).std()))
    print("Z score value " + c + " is: " + str(pd.to_numeric(df[z_i].sum())))
