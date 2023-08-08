# Data

This folder contains project project datasets, including the original Autocast dataset by Zou et. al (2022), as well as custom versions of the dataset used in evaluation experiments. The data is provided in the `data.zip` archive. It is important to **unzip this archive** before running any notebooks. After unzipping, the below datasets will be available.

* `autocast_questions.json` is the original [Autocast dataset](https://github.com/andyzoujm/autocast), as described by Zou et al. in *Forecasting Future World Events with Neural Networks* (2022).

* `autocast_filtered.json` is a filtered version of the Autocast dataset, which the project team used for pipeline evaluation experiments. The filtered version contains a subset of the original Autocast dataset consisting of active questions with tags where the majority vote of crowd forecasts on resolved questions was above 70% accuracy.

* `test_df_latest.json` is a cleaned and enriched version of `autocast_filtered.json`. It includes additional columns related to crowd prediction averages, internal and external context enrichment, and examples generated using active prompt methodology.
