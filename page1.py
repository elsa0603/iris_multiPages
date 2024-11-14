import streamlit as st
import pandas as pd
import joblib

# st.title("new page 1")

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
df = pd.read_csv("iris.csv")
se1 = st.slider('花萼長度(cm)', 
                                 float(df['sepal.length'].min()), 
                                 float(df['sepal.length'].max()), 
                                 float(df['sepal.length'].mean()))
se2 = st.slider('花萼寬度(cm)', 
                                 float(df['sepal.width'].min()), 
                                 float(df['sepal.width'].max()), 
                                 float(df['sepal.width'].mean()))
se3 = st.slider('花瓣長度(cm)', 
                                 float(df['petal.length'].min()), 
                                 float(df['petal.length'].max()), 
                                 float(df['petal.length'].mean()))
se4 = st.slider('花瓣寬度(cm)', 
                                 float(df['petal.length'].min()), 
                                 float(df['petal.length'].max()), 
                                 float(df['petal.length'].mean()))
# # se1 = st.slider("花萼長度:", 3.0, 8.0, 5.8)
# se2 = st.slider("花萼寬度:", 1.8, 5.0, 3.8)
# se3 = st.slider("花瓣長度:", 0.7, 7.2, 5.0)
# se4 = st.slider("花瓣寬度:", 0.0, 3.5, 1.8)

st.image("iris.png")
# 進行預測
labels = ['Setosa', 'Versicolor', 'Virginica']

if st.button("進行預測"):
    X = [[se1, se2, se3, se4]]
    y = model.predict(X)
    st.write(y[0])
    st.write("### 預測結果,品種名稱應是: ", labels[y[0]])

# 跳頁
# st.switch_page("pages/my_page.py")


