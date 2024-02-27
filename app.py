import streamlit as st
import pickle , sys , nltk
sys.path.append("./src")
from src import textPreprocessor as tp

with open("./src/classifier.pkl","rb") as f:
    classifier = pickle.load(f)

with open("./src/vectorizer.pkl","rb") as f:
    vecotrizer = pickle.load(f)

nltk.download("punkt")
nltk.download("stopwords")

st.set_page_config(
        page_title="SMS Spam Classifier",
        page_icon="./src/icon.png"
    )

st.title("SMS Spam Classifier")

message = st.text_area("Message",placeholder="Enter message here",key="input")

col1 , col2 = st.columns(2)

def clear_text():
    st.session_state["input"] = ""

with col1:
    if st.button("Predict",use_container_width=True):
        if message == "":
            pass
        else:
            message = tp.textPreprocessor(message)
            message = vecotrizer.transform([message]).toarray()
            result = classifier.predict(message)[0]
            if result == 0:
                st.header("Not spam")
            else:
                st.header("Spam")

with col2:
    if st.button("Clear",use_container_width=True,type="primary",on_click=clear_text):
        pass