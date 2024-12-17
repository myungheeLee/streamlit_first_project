import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Plot the population structure
def plot_population_structure(region, data):
    region_data = data[data['Region'] == region]
    if region_data.empty:
        st.warning("선택한 지역에 대한 데이터가 없습니다.")
        return

    # Assuming the columns contain age groups and population
    age_groups = region_data.columns[1:]  # Exclude 'Region' column
    population = region_data.iloc[0, 1:].values  # Population values for the region
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(age_groups, population, color='skyblue')
    ax.set_title(f"{region}의 인구 구조", fontsize=16)
    ax.set_xlabel("연령대", fontsize=14)
    ax.set_ylabel("인구 수", fontsize=14)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Streamlit app
st.title("지역별 인구 구조 시각화")
st.markdown("### 원하는 지역을 선택하고 인구 구조를 확인하세요!")

# Load data
file_path = "/mnt/data/age2411.csv"
data = load_data(file_path)

# Region selection
if 'Region' in data.columns:
    region = st.selectbox("지역을 선택하세요:", options=data['Region'].unique())
    if region:
        plot_population_structure(region, data)
else:
    st.error("파일에 'Region' 열이 없습니다. 데이터를 확인해주세요.")
