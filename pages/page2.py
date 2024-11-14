import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("IRIS 相關資訊")
st.write("依'花萼長寬'繪製散點圖：")
df = pd.read_csv("iris.csv")

fig, ax = plt.subplots()
# species_map = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
species_map = {'Setosa':0 , 'Versicolor':1 , 'Virginica':2 }
colors = ['red', 'green', 'blue']

#分Tab顯示不同欄位的圖
tab1, tab2 = st.tabs(["依花萼長寬", "依花瓣長寬"])

tab1.write("依花萼長寬顯示樣本分佈情形")
with tab1:
    for i, species in species_map.items():
        subset = df[df['variety'] == i]  
        ax.scatter(subset['sepal.length'], subset['sepal.width'],label=i)#, color=colors[i]

    ax.set_xlabel('Sepal Length (cm)')
    ax.set_ylabel('Sepal Width (cm)')
    ax.legend()
    st.pyplot(fig)

fig2, ax2 = plt.subplots()
tab2.write("依花瓣長寬顯示樣本分佈情形")
with tab2:
    for i, species in species_map.items():
        subset = df[df['variety'] == i]  
        ax2.scatter(subset['petal.length'], subset['petal.width'],label=i)#, color=colors[i]

    ax2.set_xlabel('Petal Length (cm)')
    ax2.set_ylabel('Petal Width (cm)')
    ax2.legend()
    st.pyplot(fig2)

# df['variety'] = df['variety'].map({0: "Setosa", 1: "Versicolor", 2: 'Virginica'})
# st.write(df['variety'])



st.write("繪製線條圖：")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']) 
st.line_chart(chart_data)

st.write("繪製地圖：")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [22.7, 120.3],
    columns=['lat', 'lon'])
st.map(map_data)

st.write("可收合側邊欄位：")
expander = st.expander("點擊來展開...")#原st.beta_expander("點擊來展開...")
expander.write("如果你要顯示很多文字，但又不想佔大半空間，可以使用這種方式。")