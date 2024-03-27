# normalise-fetalh

## Min-Max Normalisation of Fetal Health Data

### See report in pdf format at: [report](https://conorheffron.github.io/normalise-fetalh/assignment-1.pdf)

### Command Line (CLI) syntax: 
`python main.py <rounding_decimals> <include_histogram_features?> <display_plots?> <save_plots?> <dir_for_plots_write/save> <csv_file_path_for_analysis>`

```shell
> python main.py 3 True False False "plots/" "/path/fetal_health.csv"
The run-time arguments are: ['main.py', '3', 'True', 'False', 'False', 'plots/', '/path/fetal_health.csv']
------------------------------------------------
Min of baseline_value is: 106
Max of baseline_value is: 160
Mean of baseline_value is: 133.30070921985816
Median of baseline_value is: 133.0
Standard Deviation of baseline_value is: 9.83714960081248
Z score value baseline_value is: 1069.301
------------------------------------------------
Min of accelerations is: 0.0
Max of accelerations is: 0.019
Mean of accelerations is: 0.0031787234042553194
Median of accelerations is: 0.002
Standard Deviation of accelerations is: 0.00386396168242526
Z score value accelerations is: 353.89599999999996
------------------------------------------------
Min of fetal_movement is: 0.0
Max of fetal_movement is: 0.481
Mean of fetal_movement is: 0.009526713947990545
Median of fetal_movement is: 0.0
Standard Deviation of fetal_movement is: 0.04678268182928352
Z score value fetal_movement is: 41.832
------------------------------------------------
Min of uterine_contractions is: 0.0
Max of uterine_contractions is: 0.015
Mean of uterine_contractions is: 0.004373049645390071
Median of uterine_contractions is: 0.004
Standard Deviation of uterine_contractions is: 0.002947399462280176
Z score value uterine_contractions is: 616.602
------------------------------------------------
Min of light_decelerations is: 0.0
Max of light_decelerations is: 0.015
Mean of light_decelerations is: 0.001888888888888889
Median of light_decelerations is: 0.0
Standard Deviation of light_decelerations is: 0.002963582883045093
Z score value light_decelerations is: 266.35200000000003
------------------------------------------------
Min of prolongued_decelerations is: 0.0
Max of prolongued_decelerations is: 0.005
Mean of prolongued_decelerations is: 0.00015933806146572102
Median of prolongued_decelerations is: 0.0
Standard Deviation of prolongued_decelerations is: 0.0005913692853366469
Z score value prolongued_decelerations is: 67.4
------------------------------------------------
Min of abnormal_short_term_variability is: 12
Max of abnormal_short_term_variability is: 87
Mean of abnormal_short_term_variability is: 46.95035460992908
Median of abnormal_short_term_variability is: 49.0
Standard Deviation of abnormal_short_term_variability is: 17.16258426336172
Z score value abnormal_short_term_variability is: 985.59
------------------------------------------------
Min of mean_value_of_short_term_variability is: 0.2
Max of mean_value_of_short_term_variability is: 7.0
Mean of mean_value_of_short_term_variability is: 1.3339952718676122
Median of mean_value_of_short_term_variability is: 1.2
Standard Deviation of mean_value_of_short_term_variability is: 0.8837077165359872
Z score value mean_value_of_short_term_variability is: 352.705
------------------------------------------------
Min of percentage_of_time_with_abnormal_long_term_variability is: 0
Max of percentage_of_time_with_abnormal_long_term_variability is: 91
Mean of percentage_of_time_with_abnormal_long_term_variability is: 9.823167848699764
Median of percentage_of_time_with_abnormal_long_term_variability is: 0.0
Standard Deviation of percentage_of_time_with_abnormal_long_term_variability is: 18.391154458995597
Z score value percentage_of_time_with_abnormal_long_term_variability is: 228.381
------------------------------------------------
Min of mean_value_of_long_term_variability is: 0.0
Max of mean_value_of_long_term_variability is: 50.7
Mean of mean_value_of_long_term_variability is: 8.19886524822695
Median of mean_value_of_long_term_variability is: 7.4
Standard Deviation of mean_value_of_long_term_variability is: 5.636014802636036
Z score value mean_value_of_long_term_variability is: 342.053
------------------------------------------------
Min of histogram_width is: 3
Max of histogram_width is: 180
Mean of histogram_width is: 70.49267139479906
Median of histogram_width is: 68.0
Standard Deviation of histogram_width is: 38.95078910381834
Z score value histogram_width is: 806.44
------------------------------------------------
Min of histogram_min is: 50
Max of histogram_min is: 159
Mean of histogram_min is: 93.54704491725768
Median of histogram_min is: 93.0
Standard Deviation of histogram_min is: 29.580143601297486
Z score value histogram_min is: 844.961
------------------------------------------------
Min of histogram_max is: 122
Max of histogram_max is: 238
Mean of histogram_max is: 164.03971631205673
Median of histogram_max is: 162.0
Standard Deviation of histogram_max is: 17.94418266456923
Z score value histogram_max is: 766.471
------------------------------------------------
Min of histogram_number_of_peaks is: 0
Max of histogram_number_of_peaks is: 18
Mean of histogram_number_of_peaks is: 4.069976359338061
Median of histogram_number_of_peaks is: 3.0
Standard Deviation of histogram_number_of_peaks is: 2.9476385605500326
Z score value histogram_number_of_peaks is: 478.36300000000006
------------------------------------------------
Min of histogram_number_of_zeroes is: 0
Max of histogram_number_of_zeroes is: 10
Mean of histogram_number_of_zeroes is: 0.3224586288416076
Median of histogram_number_of_zeroes is: 0.0
Standard Deviation of histogram_number_of_zeroes is: 0.7041179104063187
Z score value histogram_number_of_zeroes is: 68.20000000000002
------------------------------------------------
Min of histogram_mode is: 60
Max of histogram_mode is: 187
Mean of histogram_mode is: 137.44586288416076
Median of histogram_mode is: 139.0
Standard Deviation of histogram_mode is: 16.403044334341082
Z score value histogram_mode is: 1289.778
------------------------------------------------
Min of histogram_mean is: 73
Max of histogram_mean is: 182
Mean of histogram_mean is: 134.60614657210402
Median of histogram_mean is: 136.0
Standard Deviation of histogram_mean is: 15.617939011476764
Z score value histogram_mean is: 1195.417
------------------------------------------------
Min of histogram_median is: 77
Max of histogram_median is: 186
Mean of histogram_median is: 138.09078014184396
Median of histogram_median is: 139.0
Standard Deviation of histogram_median is: 14.484268212258401
Z score value histogram_median is: 1185.414
------------------------------------------------
Min of histogram_variance is: 0
Max of histogram_variance is: 269
Mean of histogram_variance is: 18.846808510638297
Median of histogram_variance is: 7.0
Standard Deviation of histogram_variance is: 29.03532873969983
Z score value histogram_variance is: 148.18900000000002
------------------------------------------------
Min of histogram_tendency is: -1
Max of histogram_tendency is: 1
Mean of histogram_tendency is: 0.32056737588652484
Median of histogram_tendency is: 0.0
Standard Deviation of histogram_tendency is: 0.6107888873223887
Z score value histogram_tendency is: 1396.5
------------------------------------------------
z_i_fetal_health                                              1426.000
z_i_histogram_tendency                                        1396.500
z_i_histogram_mode                                            1289.778
z_i_histogram_mean                                            1195.417
z_i_histogram_median                                          1185.414
z_i_baseline_value                                            1069.301
z_i_abnormal_short_term_variability                            985.590
z_i_histogram_min                                              844.961
z_i_histogram_width                                            806.440
z_i_histogram_max                                              766.471
z_i_uterine_contractions                                       616.602
z_i_histogram_number_of_peaks                                  478.363
z_i_accelerations                                              353.896
z_i_mean_value_of_short_term_variability                       352.705
z_i_mean_value_of_long_term_variability                        342.053
z_i_light_decelerations                                        266.352
z_i_percentage_of_time_with_abnormal_long_term_variability     228.381
z_i_histogram_variance                                         148.189
z_i_histogram_number_of_zeroes                                  68.200
z_i_prolongued_decelerations                                    67.400
z_i_fetal_movement                                              41.832
dtype: float64
```

