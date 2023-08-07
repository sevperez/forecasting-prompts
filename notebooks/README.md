# Notebooks

This folder contains the core project notebooks associated with context enrichment, active prompt example selection, and pipeline evaluation. The notebooks are organized as follows:

* `0.1-coco-eda.ipynb` is an exploratory data analysis notebook that describes the original Autocast dataset and the data cleaning process, as well as filtering of the dataset to use only those questions in categories where the crowd forecasts were at least 70% accurate.
* `0.2-coco-sample_selection.ipynb` is a notebook that describes the active prompt example selection methodology used to generate examples for the pipeline evaluation experiments.
* `0.3-coco-active_prompt_regression.ipynb` is a notebook that reviews turning the active prompt data into a regression model in order to reduce the need to make API calls to the LLM.
* `GR_0.{1-3}_serpapi_context_engineering.ipynb` is a set of notebooks that explore using SerpAPI to provide external context to the pipeline.
* `GR_Prompt_engineer_MVP.ipynb` is a notebook that explores an MVP to engineer prompts.
* `LR_0.1_Autocast.ipynb` is a notebook that reviews the Autocast dataset.
* `LR_0.2_Analysis_and_Evaluation.ipynb` is a notebook that explores several different LLMs as well as data leakage issues with GPT 3.5.
* `LR_0.2_Analysis_On_Langchain_Baseline.ipynb` is a notebook that explores using Wikipedia to provide external context to the pipeline.
* `2.0-sjp-context-enrichment.ipynb` is a notebook that describes the context enrichment methodology used to generate examples for the pipeline evaluation experiments.
* `2.1-sjp-evaluation.ipynb` is a notebook that describes the evaluation methodology used to evaluate the pipeline predictions.

