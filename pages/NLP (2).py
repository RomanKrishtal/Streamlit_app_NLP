import streamlit as st
import pandas as pd
from transformers import pipeline
import re
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/roman/Desktop/webapp_streamlit-2/pages/data/emotion_sentimen_dataset.csv")
df = df[:10000]

st.set_page_config(
    page_title="NLP",
    layout="wide"
)

# Load a model with a function

def load_model():
    model = pipeline("text-classification", model="bert-base-uncased")
    return model

# assign a function to a variable

model = load_model()

st.title("Write a word to see what cluster it belongs to as well as what sentiment it implies at DataFrame's sentences.")

st.write("The code and the comments that explain how the model was setup")

code="""# Create a checkbox that enables the sotring of substring from the output compared to the substrings of the df text column
if st.checkbox('Show matching string from DataFrame'):
    # Check if the variable 'sentence' is not empty (assuming 'sentence' is defined elsewhere)
    if sentence:
        # Define a regular expression pattern to match the substring as a separate word
        regex_pattern = r'\b' + re.escape(sentence) + r'\b'
        
        # Filter the DataFrame to select rows where the 'text' column contains the substring
        matching_df = df[df['text'].str.contains(regex_pattern, case=False, na=False)]
        
        # Check if any matching rows were found in the DataFrame
        if not matching_df.empty:
            # Display the matching strings from the DataFrame, grouped by emotion
            st.write("Matching strings from DataFrame grouped by emotion:")
            
            # Group the matching strings by emotion and convert them to a list
            grouped_by_emotion = matching_df.groupby('Emotion')['text'].apply(list)
            
            # Iterate over each emotion and its corresponding list of matching strings
            for emotion, strings in grouped_by_emotion.items():
                # Display the emotion label
                st.write(f"Emotion: {emotion}")
                
                # Iterate over each matching string and display it
                for string in strings:
                    st.write(f"- {string}")
        # If no matching rows were found in the DataFrame, display a message
        else:
            st.write("No matching string found in DataFrame")


# Check if the 'Submit' button is pressed
if st.button('Submit'):
    # Perform emotion analysis on the input sentence using the model and return all scores
    result = model(sentence, return_all_scores=True)
    
    # Convert the result into a DataFrame and sort it by score in descending order
    df_result = pd.DataFrame(result[0]).sort_values(by='score', ascending=False)
    
    # Rename the 'label' column to 'Feeling' for clarity
    df_result.rename(columns={'label': 'Feeling'}, inplace=True)

    # Plot the analysis result as a pie chart for better visibility
    labels = df_result['Feeling']  # Extract emotion labels
    scores = df_result['score']    # Extract scores
    fig, ax = plt.subplots()       # Create a new figure and axis
    ax.pie(scores, labels=labels, autopct='%1.1f%%', startangle=90)  # Plot pie chart
    ax.axis('equal')               # Ensure pie chart is drawn as a circle
    st.write('Emotional analysis result distribution:')  # Display title for the chart
    st.pyplot(fig)                 # Display the pie chart in the Streamlit app"""

st.code(code, language='python')

st.write('Now for the analysis')

sentence = st.text_area('Write a word here')


# Create a checkbox that enables the sotring of substring from the output compared to the substrings of the df text column
if st.checkbox('Show matching string from DataFrame'):
    # Check if the variable 'sentence' is not empty (assuming 'sentence' is defined elsewhere)
    if sentence:
        # Define a regular expression pattern to match the substring as a separate word
        regex_pattern = r'\b' + re.escape(sentence) + r'\b'
        
        # Filter the DataFrame to select rows where the 'text' column contains the substring
        matching_df = df[df['text'].str.contains(regex_pattern, case=False, na=False)]
        
        # Check if any matching rows were found in the DataFrame
        if not matching_df.empty:
            # Display the matching strings from the DataFrame, grouped by emotion
            st.write("Matching strings from DataFrame grouped by emotion:")
            
            # Group the matching strings by emotion and convert them to a list
            grouped_by_emotion = matching_df.groupby('Emotion')['text'].apply(list)
            
            # Iterate over each emotion and its corresponding list of matching strings
            for emotion, strings in grouped_by_emotion.items():
                # Display the emotion label
                st.write(f"Emotion: {emotion}")
                
                # Iterate over each matching string and display it
                for string in strings:
                    st.write(f"- {string}")
        # If no matching rows were found in the DataFrame, display a message
        else:
            st.write("No matching string found in DataFrame")


# Check if the 'Submit' button is pressed
if st.button('Submit'):
    # Perform emotion analysis on the input sentence using the model and return all scores
    result = model(sentence, return_all_scores=True)
    
    # Convert the result into a DataFrame and sort it by score in descending order
    df_result = pd.DataFrame(result[0]).sort_values(by='score', ascending=False)
    
    # Rename the 'label' column to 'Feeling' for clarity
    df_result.rename(columns={'label': 'Feeling'}, inplace=True)

    # Plot the analysis result as a pie chart for better visibility
    labels = df_result['Feeling']  # Extract emotion labels
    scores = df_result['score']    # Extract scores
    fig, ax = plt.subplots()       # Create a new figure and axis
    ax.pie(scores, labels=labels, autopct='%1.1f%%', startangle=90)  # Plot pie chart
    ax.axis('equal')               # Ensure pie chart is drawn as a circle
    st.write('Emotional analysis result distribution:')  # Display title for the chart
    st.pyplot(fig)                 # Display the pie chart in the Streamlit app