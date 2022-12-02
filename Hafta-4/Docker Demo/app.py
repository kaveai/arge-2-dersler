import streamlit as st
from sumapi.api import SumAPI

api = SumAPI(username='kaveai', password='kaveai')

st.title('Summarify Sentiment Analysis Demo')
text = st.text_input("Metni Giriniz", value="Bu filmi çok beğendim.")
check_button = st.button("Duygusunu bul!")

if check_button:
    result = api.sentiment_analysis(text)
    if result["evaluation"]["label"] == 'Pozitif':
        st.markdown(f'<h3>%{round(result["evaluation"]["score"]*100, 2)} olasılıkla </h3><h1 style="color:#33ff33;font-size:24px;">Pozitif</h1>', unsafe_allow_html=True)
    else:
        st.markdown(f'<h3>%{round(result["evaluation"]["score"]*100, 2)} olasılıkla </h3><h1 style="color:#FF0000;font-size:24px;">Negatif</h1>', unsafe_allow_html=True)