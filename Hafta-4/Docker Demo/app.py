import streamlit as st
from sumapi.api import SumAPI

api = SumAPI(username='kaveai', password='kaveai')

st.title('Summarify Sentiment Analysis Demo')
text = st.text_input("Metni Giriniz", value="Bu filmi çok beğendim.")
check_button = st.button("Duygusunu bul!")

if check_button:
    result = api.sentiment_analysis(text)
    st.write(f'Sonuç: %{round(result["evaluation"]["score"]*100, 2)} olasılıkla {result["evaluation"]["label"]}')


