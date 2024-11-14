import streamlit as st
import joblib

st.title("IRIS 品種預測")
#載入模型
svm = joblib.load("svm_model.joblib")
knn = joblib.load("KNN_model.joblib")
lr = joblib.load("LR_model.joblib")
rf = joblib.load("RF_model.joblib")

#左側
s1 = st.sidebar.selectbox("### 請選擇模型:", ("SVM", "KNN", "LogisticRegression", "RandomForest"))
if s1 == "SVM":
    model = svm
elif s1 == "KNN":
    model = knn
elif s1 == "LogisticRegression":
    model = lr
elif s1 == "RandomForest":
    model = rf
#st.info(s1)

# 使用者輸入資料:slider
se1 = st.slider("花萼長度:", 3.0, 8.0, 5.8)
se2 = st.slider("花萼寬度:", 1.8, 5.0, 3.8)
se3 = st.slider("花瓣長度:", 0.7, 7.2, 5.0)
se4 = st.slider("花瓣寬度:", 0.0, 3.5, 1.8)

st.image("iris.png")
# 進行預測
labels = ['Setosa', 'Versicolor', 'Virginica']

if st.button("進行預測"):
    X = [[se1, se2, se3, se4]]
    y = model.predict(X)
    st.write(y[0])
    st.write("### 預測結果,品種名稱應是: ", labels[y[0]])


# import altair as alt
# import pandas as pd

# data = pd.DataFrame([[65,58,72],[172,168,177]])
# aa = alt.Chart(data=data).mark_point().encode(
#     x="A",
#     y="B"
# )
# st.altair_chart(aa, use_container_width=True)

# 跳頁
# st.switch_page("pages/my_page.py")


# # # Define a navigation widget in your entrypoint file
# pg = st.navigation(
#     st.Page("page1.py", title="Home", url_path="home", default=True)
#     st.Page("page2.py", title="Preferences", url_path="settings")
# )
# pg.run()

