# Demo

This folder contains a demonstration interface to show how the pipeline produces enriched prompts for input questions. The demo does not currently use real-time inference with the pipeline (due to resource constraints for hosting a demo and making large language model API calls). Instead, the demo draws on pre-computed context and active prompt examples, as saved in `test_df_latest.json` in the [data](../data) folder.


## Requirements

To run the demo, you will need to install `streamlit` and `pandas` using Conda, pip, Poetry, or any other Python package manager.


## Running the Demo

In the terminal, navigate to the `/demo` directory and run the `streamlit run demo.py` command to start the demo. Use a web browser to navigate to the appropriate URL (by default it should be [http://localhost:8501](http://localhost:8501) but it could be a different port depending on your settings). Select a sample question in the main window and hit the `run` button to show the enriched prompt, including: system instructions; optimized examples; the user prompt; and, context enrichment.

