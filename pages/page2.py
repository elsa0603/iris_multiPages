import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("IRIS 相關資訊")

st.write("依'花萼長寬'繪製散點圖：")
df = pd.read_csv("iris.csv")
# df['variety'] = df['variety'].map({0: "Setosa", 1: "Versicolor", 2: 'Virginica'})
# st.write(df['variety'])


# Create the scatter plot using matplotlib.
fig, ax = plt.subplots()

# Create a dictionary that maps the target numbers (0, 1, 2) to the species names.
# species_map = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
species_map = {'Setosa':0 , 'Versicolor':1 , 'Virginica':2 }

# Define colors for each species.
colors = ['red', 'green', 'blue']

# Plot each species with its own color.
for i, species in species_map.items():
    subset = df[df['variety'] == i]  # Get the subset of data for species i
    ax.scatter(subset['sepal.length'], subset['sepal.width'],label=i)#, color=colors[i]

# Set the axis labels and show the legend.
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Sepal Width (cm)')
ax.legend()

# Display the plot in the Streamlit app.
st.pyplot(fig)


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