import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st

#import data
all_df = pd.read_csv("all_data.csv")
groupByStation_df = pd.read_csv("groupbystation.csv")
groupByYear_df = pd.read_csv("groupbyyear.csv")

#title
st.title("Data Kualitas Udara 2013-2017 di Kota Beijing")
st.link_button(label="Link Air Quality Dataset", url="https://drive.google.com/file/d/1RhU3gJlkteaAQfyn9XOVAz7a5o1-etgr/view?usp=share_link")

#visualisasi tahun ke tahun
st.header("Visualisasi Rata-rata Kadar Polutan pada 2013-2017 ")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["PM 2.5", "PM 10", "SO2", "NO2", "CO", "O3"])
with tab1:
    st.subheader("PM 2.5")
    st.caption("Particulate Matter (PM2.5) adalah partikel udara yang berukuran lebih kecil dari atau sama dengan 2.5 µm (mikrometer).")
    st.line_chart(data=groupByYear_df, x="year", y="PM25")
with tab2:
    st.subheader("PM 10")
    st.caption("Partikulat (PM10) adalah Partikel udara yang berukuran lebih kecil dari 10 mikron (mikrometer).")
    st.line_chart(data=groupByYear_df, x="year", y="PM10")
with tab3:
    st.subheader("SO2")
    st.caption("Belerang dioksida merupakan gas beracun dengan bau menyengat yang dilepaskan oleh gunung berapi dan beberapa pemrosesan industri.")
    st.line_chart(data=groupByYear_df, x="year", y="SO2")
with tab4:
    st.subheader("NO2")
    st.caption("Nitrogen dioksida (NO 2 ) adalah kontributor utama pembentukan kabut asap dan prekursor banyak polutan sekunder berbahaya.")
    st.line_chart(data=groupByYear_df, x="year", y="NO2")
with tab5:
    st.subheader("CO")
    st.caption("CO atau karbon monoksida adalah gas beracun yang tidak berwarna, tidak berbau dan tidak berasa.")
    st.line_chart(data=groupByYear_df, x="year", y="CO")
with tab6:
    st.subheader("O3")
    st.caption("Ozon (O3) adalah gas tidak berwarna hingga kebiruan yang terbentuk oleh radiasi ultraviolet matahari (sinar matahari) dan molekul oksigen.")
    st.line_chart(data=groupByYear_df, x="year", y="O3")

#visualisasi rata-rata tiap polutan perstasiun
st.header("Visualisasi Rata-rata Kadar Polutan Berdasarkan Stasiun")
col1, col2 = st.columns(2)

with col1:
    st.subheader("PM 2.5")
    fig, ax = plt.subplots(figsize=(20, 10))
    sb.barplot(
        x="PM25", 
        y="station",
        data=groupByStation_df.sort_values(by="PM25", ascending=False),
        color="blue",
        ax=ax
    )
    ax.set_title("Rata-rata PM 2.5 Berdasarkan Stasiun", loc="center", fontsize=25)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    st.pyplot(fig)
with col2:
    st.subheader("PM 10")
    fig, ax = plt.subplots(figsize=(20, 10))
    sb.barplot(
        x="PM10", 
        y="station",
        data=groupByStation_df.sort_values(by="PM10", ascending=False),
        color="orange",
        ax=ax
    )
    ax.set_title("Rata-rata PM 10 Berdasarkan Stasiun", loc="center", fontsize=25)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    st.pyplot(fig)
with col1:
    st.subheader("SO2")
    fig, ax = plt.subplots(figsize=(20, 10))
    sb.barplot(
        x="SO2", 
        y="station",
        data=groupByStation_df.sort_values(by="SO2", ascending=False),
        color="green",
        ax=ax
    )
    ax.set_title("Rata-rata SO2 Berdasarkan Stasiun", loc="center", fontsize=25)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    st.pyplot(fig)
with col2:
    st.subheader("NO2")
    fig, ax = plt.subplots(figsize=(20, 10))
    sb.barplot(
        x="NO2", 
        y="station",
        data=groupByStation_df.sort_values(by="NO2", ascending=False),
        color="red",
        ax=ax
    )
    ax.set_title("Rata-rata NO2 Berdasarkan Stasiun", loc="center", fontsize=25)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    st.pyplot(fig)
with col1:
    st.subheader("CO")
    fig, ax = plt.subplots(figsize=(20, 10))
    sb.barplot(
        x="CO", 
        y="station",
        data=groupByStation_df.sort_values(by="CO", ascending=False),
        color="violet",
        ax=ax
    )
    ax.set_title("Rata-rata CO Berdasarkan Stasiun", loc="center", fontsize=25)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    st.pyplot(fig)
with col2:
    st.subheader("O3")
    fig, ax = plt.subplots(figsize=(20, 10))
    sb.barplot(
        x="O3", 
        y="station",
        data=groupByStation_df.sort_values(by="O3", ascending=False),
        color="brown",
        ax=ax
    )
    ax.set_title("Rata-rata O3 Berdasarkan Stasiun", loc="center", fontsize=25)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    st.pyplot(fig)
    
#copyright
st.caption("Copyright (c) Marizka Maulidina 2023")