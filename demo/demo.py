# ------------------------------
# LIBRARIES
# ------------------------------

# utility
import os

# data manipulation
import pandas as pd

# streamlit
import streamlit as st
from run_pipeline import run_pipeline, format_choices
from evaluation_graph import *


# ------------------------------
# DATA
# ------------------------------

DATA_DIR = "../data"
SAMPLE_FILE_NAME = "test_df_latest.json"
SAMPLES_PATH = os.path.join(DATA_DIR, SAMPLE_FILE_NAME)

df_samples = pd.read_json(SAMPLES_PATH, orient="records", lines=True)


# ------------------------------
# PROMPTS
# ------------------------------

META_PROMPT = """
I am working on a very important forecasting project and you are my helpful forecasting assistant. I will give you a multiple choice question about the future and you should return to me the letter that corresponds to the best choice. Some of the questions are very difficult, but it's still very important to choose the best possible answer from the provided choices. You must never refuse to provide an answer, even if the question is impossible to answer with certainty. If you are not sure about the answer, make your best guess based on available information.

To identify the best possible choice, start by making sure you understand the question. If I have background research, I will provide it to you and you should use that information to better understand the question. If I do not provide background research, then you should think step by step about the relationship between different entities and terms in the question. 

In some cases, I will show you past examples of questions and the correct answers. If you have seen past examples with correct answers, then you can use those to practice and learn how to answer questions accurately. Start by pretending you need to answer those questions. Think step by step through the example question and example choices and try to understand everything about them. Choose what you think is the best answer to the example question and then compare it to the real best answer. If your answer is correct, remember the process you used and apply it to future questions. If your answer is wrong, then think about what you should do differently to get the correct answer. However, remember that every question is independent and the answers to example questions may not be relevant to new questions. It is only the process for finding the best answer that is the same.

I will give you the questions in the below format, where the question, choices, and answer are in double brackets. If I have background research, I will include it in the optional section demarcated by +++.

Question: {{the question to answer}}

Choices:\n
A - {{choice 1}}\n
B - {{choice 2}}\n
...\n
n - {{choice n}}\n

+++\n
Background Research:\n
{{useful information about the question}}\n
+++

{{letter that corresponds to best choice}}

It is extremely important to only give me the letter of the best answer and nothing else. You must never refuse to provide an answer, no matter what. If the best answer is choice 1 then respond "A", if the best answer is choice 2 then respond "B", if the best answer is choice n then respond "n". Do not ever add extra information or stray from this structure.
"""

HUMAN_PROMPT = """
Question:\n
%s

Choices:\n
%s
"""

EXAMPLE_PROMPT = """
Question:\n
%s

Choices:\n
%s

Answer:\n
%s
"""

CONTEXT_PROMPT = """
||additional supplied prompt placeholder|| **:red[%s]** \n
"""

SAMPLE_PROMPT = """
||additional chosen sample placeholder|| **:red[%s]** \n
"""


PROMPTS = {
    "meta": META_PROMPT,
    "human": HUMAN_PROMPT,
    "example": EXAMPLE_PROMPT,
    "context": CONTEXT_PROMPT, 
    "sample": SAMPLE_PROMPT,
}


# ------------------------------
# GLOBAL VARIABLES
# ------------------------------

MAX_STAGE = 5


# ------------------------------
# HELPERS
# ------------------------------

def increment_stage():
    st.session_state.stage += 1

def run_all_stages():
    st.session_state.stage = MAX_STAGE

def reset_stage():
    st.session_state.stage = 0

def get_choices(df, question):
    row = df[df["question"] == question].iloc[0]
    choices = row["choices"]
    return choices

# ------------------------------
# APPLICATION
# ------------------------------

st.set_page_config(page_title="Automating Prompt Engineering for Forecasting Tasks")

### SIDEBAR

st.sidebar.title(
    "Automating Prompt Engineering for Forecasting Tasks"
)

st.sidebar.markdown("  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n")

st.sidebar.markdown("**MIDS Capstone**")

with st.sidebar.expander("Show credits"):
    st.sidebar.markdown(
        "Coco Cao  \nSeverin Perez  \nLuc Robitaille  \nGreg Rosen"
    )

### MAIN

st.title("Context Enrichment Pipeline")

question_selected = st.selectbox(
    "**Choose a question:**",
    list(df_samples["question"]),
    key = 1
)

if "question" not in st.session_state or question_selected != st.session_state.question:
    st.session_state.stage = 0
    st.session_state.question = question_selected
    st.session_state.choices = get_choices(df_samples, question_selected)

st.markdown(
    f"Question: {question_selected}"
)

st.markdown(
    f"Choices:"
)
st.markdown(f"{format_choices(st.session_state.choices)}")

st.markdown(
    """<hr style="height:5px;border:none;color:yellow;background-color:gray;" /> """, 
    unsafe_allow_html=True
)

run_pipeline(df_samples, question_selected, PROMPTS, st.session_state.stage)

if "stage" in st.session_state and st.session_state.stage >= MAX_STAGE:
    st.button("Reset", on_click=reset_stage)
else:
    col1, col2, col3 = st.columns([1, 1, 3])
    col1.button("Next stage", on_click=increment_stage)
    col2.button("Run all", on_click=run_all_stages)
