# ASCII Artify

ASCII Artify is a Streamlit app that utilizes the LangChain library to generate ASCII art from an article provided by the user. The app uses the GPT-3.5 Turbo language model from OpenAI to generate creative and artistic ASCII representations of the input article.

## Installation

To run the ASCII Artify app locally, follow these steps:
1. Clone the repository containing the code:
```bash
git clone https://github.com/ebiwonjumit/textToASCII.git
cd textToASCII/
```
2. Install the required dependencies. You can use the following command to install them:
```bash
pip install streamlit langchain
```

3. Run the Streamlit app:
```bash
streamlit run your_app_name.py
```
Replace your_app_name.py with the name of the Python file containing the provided code.

## How to Use

Once you have the app running, a web page will open in your browser showing the title "ASCII Artify."

You will see a text area labeled "Enter the article." In this area, you can type or paste the text of the article from which you want to generate ASCII art.

After entering the article, click the "Generate ASCII Art" button.

The app will process the input article using the GPT-3.5 Turbo model and generate an ASCII art representation based on the content of the article.

The generated ASCII art will be displayed below the button.

<img width="870" alt="Captura de pantalla 2023-08-23 a la(s) 11 23 29 a m" src="https://github.com/ebiwonjumit/textToASCII/assets/31973148/db604855-a661-47b9-ac41-c9581e73bb7a">


## Notes

* Make sure to provide a meaningful and descriptive article to get creative ASCII art outputs.
* The quality and creativity of the generated ASCII art may vary based on the input article and the language model's interpretation.

Please note that this app requires an internet connection to communicate with the GPT-3.5 Turbo model hosted by OpenAI.

## About

This app was developed using Streamlit and the LangChain library, which facilitates interaction with language models for various text generation tasks. LangChain simplifies the process of working with language models by providing templates and utilities for creating conversational chains, prompts, and more.

Feel free to explore and modify the code to customize the app according to your preferences and requirements. If you have any questions, suggestions, or improvements, please don't hesitate to get in touch!

Disclaimer: This app utilizes the capabilities of the GPT-3.5 Turbo model to generate content. The accuracy, appropriateness, and quality of the generated content are determined by the language model's algorithms and training data.
