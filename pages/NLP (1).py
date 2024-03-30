import pandas as pd
import spacy
import streamlit as st
from bertopic import BERTopic

st.title('Natural Language Processing')
st.header('With this app, we aim to analyze the different topics n\
        in terms of their semantic differences, likelyhood of word n\
        appearance, and similarity between linguistic units')

st.write('The DataFrame is presented below.')

df = pd.read_csv("/Users/roman/Desktop/webapp_streamlit-2/pages/data/emotion_sentimen_dataset.csv", index_col=False)

df = df[:10000]

# Drop the 'Unnamed: 0' column
df.drop(columns=['Unnamed: 0'], inplace=True)

# Display the head of the DataFrame
st.write(df.head())

code1 = """nlp = spacy.load('en_core_web_md', 
                exclude=['tagger', 'parser', 'ner', 'attribute_ruler', 'lemmatizer'])
model = BERTopic(embedding_model=nlp,verbose=True)
docs = df.text.to_list()
topics, probabilities = model.fit_transform(docs)
text_column = df['text']
topic_model = BERTopic()
topics, _ = topic_model.fit_transform(text_column)
fig = topic_model.visualize_topics()
fig.show()"""

st.write("""The code below presents that in order to initiate spacy, firsly an english core must be loaded, 
        later we use BERTopic to initialise a model that would be used for data lavelling.
        Initialization: It initializes a BERTopic model object without specifying any parameters. This creates a BERTopic model with default settings.

Fitting the Model: It fits the BERTopic model to the text data stored in the variable text_column. The fit_transform() method is used to fit the model to the data and transform the text data into topics. It returns two variables: topics and an underscore _. topics contains the topic labels assigned to each document, while _ contains the probabilities associated with each topic-document pair.

Visualization: It generates a visualization of the topics using the visualize_topics() method of the BERTopic model. This visualization typically displays the top words associated with each topic and their relevance scores.

Display: The visualization (stored in the variable fig) is shown using the .show() method. However, it's important to note that Streamlit does not support the .show() method for displaying figures. Instead, you would need to use Streamlit's built-in functions like st.pyplot(fig) to display the visualization in a Streamlit app.""")

st.code(code1, language='python')

st.image("/Users/roman/Desktop/NLP/newplot.png", caption='Your Image Caption', use_column_width=True)

st.write('Overall, the dataset have 144 topics. These topics are divided by 2 dimensions. The biggest clasters n\
        are Topic 0, 1, and 2. The model managed to accurately identify the words that should be clustered. For example n\
        Topic 13 that clustered words such as "weird", "strange", "different" ')

code2 = "topic_model.visualize_barchart()"
st.write('This line of code displays the Topic Word Score visualisation.')
st.code(code2, language='python')

st.image("/Users/roman/Desktop/NLP/newplot1.png", caption='Your Image Caption', use_column_width=True)

st.write('Spacy also has a functionality that allows the analysis of the word scores. Topic word scores represent the importance or relevance of each word within a specific topic. These scores indicate how likely a word is to appear in a given topic, with higher scores indicating greater relevance. Analyzing these scores helps identify key terms that characterize each topic, aiding in the interpretation and labeling of topics generated by the topic modeling algorithm.')

code3 = 'model.visualize_heatmap()'
st.write('This line of code is used to visualise the similarity matrix')
st.code(code3, language='python')

st.image("/Users/roman/Desktop/NLP/newplot2.png", caption='Your Image Caption', use_column_width=True)

st.write('In the context of spaCy, a similarity matrix typically shows the pairwise similarity scores between documents, tokens, or other linguistic units. These similarity scores quantify the degree of similarity or dissimilarity between pairs of items based on their semantic content or features.')

st.subheader('To see the whole code, consult NLP.ipynb notebook.')