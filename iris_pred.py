import streamlit as st
import joblib

# streamlit: https://docs.streamlit.io/develop/api-reference/status
# 圖示: https://tw.piliapp.com/emoji/list/
pg = st.navigation([
    st.Page("pages/page1.py", title="IRIS 品種預測", icon="🌹"),
    st.Page("pages/page2.py", title="IRIS 相關資訊", icon=":material/favorite:"),
])
pg.run()

