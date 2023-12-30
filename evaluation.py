from matplotlib import pyplot as plt


def plot_features(df, save_plots, display_plots, img_dir):
    if display_plots or save_plots:
        # set x axis values
        fetal_health_label = 'fetal_health'
        x = df[fetal_health_label]

        for col in df.columns:
            # set y axis values
            y = df[col]

            # set plot type
            plt.scatter(x, y, c=df['baseline_value'])

            # set axis labels
            plt.xlabel(fetal_health_label)
            plt.ylabel(col)
            plot_name = "Fetal Health against " + col
            plt.title(plot_name)

            if save_plots:
                plt.savefig(img_dir + plot_name + '.png')
            if display_plots:
                plt.show()
            plt.close()


def evaluation_output(df):
    # Write data frame to CSV
    df.to_csv("out.csv")

    # Use columns that start with 'z_i_'
    filter_col = [col for col in df if col.startswith("z_i_") or col == "fetal_health"]
    # Write fetal health and z values to CSV
    df[filter_col].to_csv("z_values.csv")

    # Exclude categorical columns and only select z values or numeric data
    filter_col_sums = [col for col in df if col.startswith("z_i_")]
    # Sort by aggregation of z values (summation)
    ordered_z_sums = df[filter_col_sums].sum().sort_values(ascending=False)

    # Print ordered z sums
    ordered_z_sums.to_csv("z_sums.csv")

    # Print top 7 features from max-min normalisation process
    print("------------------------------------------------")
    print(ordered_z_sums)  # [0:7])
