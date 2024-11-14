import streamlit as st
import joblib

def page2():
    st.title("Second page")

# https://docs.streamlit.io/develop/api-reference/status
# https://tw.piliapp.com/emoji/list/
pg = st.navigation([
    st.Page("page1.py", title="IRIS 品種預測", icon="🌹"),
    st.Page("page2.py", title="IRIS 相關資訊", icon=":material/favorite:"),
])
pg.run()

