st.session_state.code: import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.document_loaders import *
from langchain.chains.summarize import load_summarize_chain
import tempfile
from langchain.docstore.document import Document

st.title("ASCII Artify")

# Initialize user input variables
article = ""

# Get the article from the user
article = st.text_area("Enter the article")

# Generate ASCII art from the article
def asciiArtGenerator(article):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0
    )
    system_template = """You are an assistant tasked with generating ASCII art from the given article."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = """Please generate ASCII art based on the following article:

{article}"""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(article=article)
    return result # returns string   

# Initialize output variable
ascii_art = ""

# Create a button to trigger the functionality of the app
if st.button("Generate ASCII Art"):
    # Check if article is provided
    if article:
        # Generate ASCII art
        ascii_art = asciiArtGenerator(article)
    else:
        # Set empty string if article is not provided
        ascii_art = ""
    
    # Display the generated ASCII art to the user
    st.markdown(ascii_art)

