# ------------------------------
# LIBRARIES
# ------------------------------

import streamlit as st


# ------------------------------
# CONSTANTS
# ------------------------------

CONTEXT_ENRICHMENT_PLACEHOLDER = "sample context enrichment text"
SAMPLE_SELECTION_PLACEHOLDER = "sample active prompt sample text"


# ------------------------------
# HELPERS
# ------------------------------

def format_choices(choices: list[str]):
        """
        Accepts a list of choices and formats them for the language model
        with a letter for each choice and one choice per line.

        Args:
            choices (list): A list of choices.
        """
        formatted_choices = "\n\n".join(
            [f"{chr(65 + idx)} - {choice}" for idx, choice in enumerate(choices)]
        )
        return formatted_choices


# ------------------------------
# PIPELINE
# ------------------------------

def show_system_instructions(meta_prompt):
    st.markdown(
        '<h4 style="color:rgb(255, 189, 69)">System Instructions:</h4>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:rgb(255, 189, 69)">{}</div>'.format(
            meta_prompt
        ),
        unsafe_allow_html=True
    )

def show_optimized_example(example_prompt, example):
    example_question = example["example_question"]
    example_choices = example["example_choices"]
    example_answer = example["example_answer"]

    st.markdown(
        '<h4 style="color:rgb(225, 77, 238)">Optimized Example:</h4>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="color:rgb(225, 77, 238)">{}</div>'.format(
            example_prompt % (
                example_question,
                format_choices(example_choices),
                example_answer
            )
        ),
        unsafe_allow_html=True
    )

def show_user_prompt(user_prompt, question, choices):
    st.markdown(
        '<h4 style="color:rgb(96, 180, 255)">User Prompt:</h4>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="color:rgb(96, 180, 255)">{}</div>'.format(
            user_prompt % (
                question,
                format_choices(choices)
            )
        ),
        unsafe_allow_html=True
    )

def show_context(context):
    st.markdown(
        '<h4 style="color:rgb(13, 183, 151)">Context Enrichment:</h4>',
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div style="color:rgb(13, 183, 151)">
            <p>Background Research:</p>
            <p>{context}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def show_inference(inference_result = "{inference result}"):
    st.markdown(
        """<hr style="height:10px;border:none;color:yellow;background-color:gray;" /> """, 
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div style="color:yellow;padding: 0 0 20px 0">Answer: {inference_result}</div>',
        unsafe_allow_html=True
    )

def show_current_stage(stage_num: int):
    if stage_num == 0:
        stage = "no prompt"
    elif stage_num == 1:
        stage = "system instructions"
    elif stage_num == 2:
        stage = "system instructions + optimized example"
    elif stage_num == 3:
        stage = "system instructions + optimized example + user prompt"
    elif stage_num == 4:
        stage = "system instructions + optimized example + user prompt + context"
    else: # stage_num >= 5:
        stage = "system instructions + optimized example + user prompt + context + inference"

    st.markdown(
        f"**Current stage:** {stage}"
    )

def run_pipeline(df, question, prompt_dict, stage_num):
    row = df[df["question"] == question].iloc[0]
    question = row["question"]
    choices = row["choices"]
    example = row["best_example"]
    context = row["context"]
    
    if stage_num == 0:
        st.markdown(
            "Click the **next stage** button to begin prompt construction..."
        )

    if stage_num == 1:
        show_current_stage(stage_num)
        st.markdown("### Prompt:")
        
        show_system_instructions(prompt_dict["meta"])
        
    if stage_num == 2:
        show_current_stage(stage_num)
        st.markdown("### Prompt:")

        show_system_instructions(prompt_dict["meta"])
        show_optimized_example(prompt_dict["example"], example)
    
    if stage_num == 3:
        show_current_stage(stage_num)
        st.markdown("### Prompt:")

        show_system_instructions(prompt_dict["meta"])
        show_optimized_example(prompt_dict["example"], example)
        show_user_prompt(prompt_dict["human"], question, choices)

    if stage_num == 4:
        show_current_stage(stage_num)
        st.markdown("### Prompt:")

        show_system_instructions(prompt_dict["meta"])
        show_optimized_example(prompt_dict["example"], example)
        show_user_prompt(prompt_dict["human"], question, choices)
        show_context(context)

    if stage_num >= 5:
        show_current_stage(stage_num)
        st.markdown("### Prompt:")

        show_system_instructions(prompt_dict["meta"])
        show_optimized_example(prompt_dict["example"], example)
        show_user_prompt(prompt_dict["human"], question, choices)
        show_context(context)
        show_inference()

