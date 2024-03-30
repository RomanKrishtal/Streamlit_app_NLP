import streamlit as st

def main():
    # Set page title and icon
    st.set_page_config(page_title="NLP App Introduction", page_icon=":memo:")

    # Define the content for the introduction page
    introduction_text = """
    # Welcome to the NLP App!
    Brought to you by Roman Krishtal, Zied Mehouachi, Ping Ju (Paula) Chen.
    
    This app showcases the power of Natural Language Processing (NLP) techniques.

    ## What is NLP?
    NLP stands for Natural Language Processing. It is a branch of artificial intelligence (AI) 
    that focuses on enabling computers to understand, interpret, and generate human language in a 
    way that is both natural and meaningful.

    ## What can you do with NLP?
    With NLP, you can perform a wide range of tasks, including:
    - Text analysis
    - Sentiment analysis
    - Language translation
    - Named entity recognition
    - Speech recognition
    - And much more!

    ## How does this app work?
    This app demonstrates various NLP techniques using the Streamlit framework. 
    You can interact with different features and explore the capabilities of NLP in real-time.

    Feel free to explore and enjoy the app!
    """

    # Display the introduction page content
    st.markdown(introduction_text, unsafe_allow_html=True)

if __name__ == "__main__":
    main()