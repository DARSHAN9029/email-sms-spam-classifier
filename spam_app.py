import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import sys

ps = PorterStemmer()

# Ensure NLTK data path is correctly set
nltk.data.path.append(r"C:\Users\PINKY\OneDrive\Desktop\spam classifier\analysis_env\Lib\site-packages\nltk\tokenizers\punkt")

# Function to process text
def transform_text(text):
    try:
        text = text.lower()  # Convert to lowercase
        text = nltk.word_tokenize(text)  # Tokenize words

        y = []  # Remove special characters
        for i in text:
            if i.isalnum():
                y.append(i)

        text = y[:]
        y.clear()

        for i in text:  # Remove stopwords and punctuation
            if i not in stopwords.words('english') and i not in string.punctuation:
                y.append(i)

        text = y[:]
        y.clear()
        for i in text:
            y.append(ps.stem(i))

        return " ".join(y)
    except Exception as e:
        print("Error in transform_text:", e, file=sys.stderr)
        return ""  # Return empty string in case of error

try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except Exception as e:
    print("Error loading model or vectorizer:", e, file=sys.stderr)
    st.error("Error loading model or vectorizer. Check the terminal for details.")

st.title("EMAIL/SMS-Spam Classifier")

input_sms = st.text_area("Enter the message:")

if st.button('Predict'):
    try:
        # 1. vectorize the input message
        vector_input = tfidf.transform([input_sms])
        # 2. Predict
        result = model.predict(vector_input)[0]
        # 3. Display
        if result == 1:
            st.header("Spam!!!!!!")
        else:
            st.header("Not Spam!!!!!")
    except Exception as e:
        print("Error during prediction:", e, file=sys.stderr)
        st.error("An error occurred during prediction. Check the terminal for details.")