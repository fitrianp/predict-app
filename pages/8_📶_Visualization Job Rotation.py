import streamlit as st
import pandas as pd
import plotly_express as px

st.set_page_config(
    page_title="Visualization 2",
    page_icon="📈"
)

# Membuat container
dataset = st.container()
filter = st.container()
visualisasi = st.container()

with dataset:
    # Title
    st.markdown("<h1 style='text-align: center;'> <b> Visualization Job Rotation <b></h1>",
                unsafe_allow_html=True)

    # Menampilkan Dataset .csv/.xlsx
    miudr_dataset = pd.read_csv(
        "data/MIUDR 2020-2022 (Bersih-Target) (3).csv")
    miudr_dataset = miudr_dataset.drop(columns=['Unnamed: 0'], axis=1)
    # st.write(miudr_dataset.head())

with filter:
    # Membuat Sidebar untuk Filter
    st.sidebar.header("Please Filter Here:")
    area = st.sidebar.multiselect("Pilih area (TTA) lokasi kerja instruktur",
                                  options=miudr_dataset["TTA"].unique(),
                                  default=miudr_dataset["TTA"].unique())
    umur = st.sidebar.multiselect("Pilih kategori Umur",
                                  options=miudr_dataset["Umur"].unique(
                                  ),
                                  default=miudr_dataset["Umur"].unique(
                                  )
                                  )
    level = st.sidebar.multiselect("Pilih kategori Level",
                                   options=miudr_dataset["Level"].unique(
                                   ),
                                   default=miudr_dataset["Level"].unique(
                                   )
                                   )
    dev = st.sidebar.multiselect("Pilih kategori Dev",
                                 options=miudr_dataset["Dev"].unique(
                                 ),
                                 default=miudr_dataset["Dev"].unique(
                                 )
                                 )

    ji = st.sidebar.multiselect("Pilih kategori JI",
                                options=miudr_dataset["JI"].unique(
                                ),
                                default=miudr_dataset["JI"].unique(
                                )
                                )

    jni = st.sidebar.multiselect("Pilih kategori JNI",
                                 options=miudr_dataset["JNI"].unique(
                                 ),
                                 default=miudr_dataset["JNI"].unique(
                                 )
                                 )

    jr = st.sidebar.multiselect("Pilih kategori Job Rotation",
                                options=miudr_dataset["JobRotation"].unique(
                                ),
                                default=miudr_dataset["JobRotation"].unique(
                                )
                                )

    # tk = st.sidebar.multiselect("Pilih tempat kegiatan",
    #                             options=miudr_dataset["Tempat_kegiatan"].unique(
    #                             ),
    #                             default=miudr_dataset["Tempat_kegiatan"].unique(
    #                             ))

    # Memberikan fungsi kerja pada filter sidebar
    df_selection = miudr_dataset.query(
        "TTA == @area & Umur == @umur & Level == @level & Dev == @dev & JI == @ji & JNI == @jni & JobRotation == @jr"
    )

    # Filter data pada dataframe
    # st.markdown("#### **Show Data**")
    # st.markdown(
    #     ">Data yang diupload merupakan data MIUDR 2020-2022. Berikut potongan dataset MIUDR 2020-2022")
    # st.write(df_selection.head(3))


with visualisasi:
    # Folder CSS
    with open('assets/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Membuat card
    col1, col2 = st.columns(2)
    row = df_selection.shape[0]
    col1.metric("**Total Data Input**", row)
    column = df_selection.shape[1]
    col2.metric("**Total Kolom Data**", column)

    # 1. Visualisasi persebaran jumlah instruktur di masing-masing area [Bar Chart]
    user_area = df_selection['TTA'].value_counts().sort_values(ascending=True)
    user_area = pd.DataFrame({'Area': user_area .index,
                              'Jumlah Instruktur': user_area .values})
    fig_user_area = px.bar(user_area,
                           x='Jumlah Instruktur',
                           y='Area',
                           orientation="h",
                           title="<b> Jumlah Instruktur di Masing-Masing Area</b>",
                           color='Area',
                           color_discrete_sequence=px.colors.sequential.Emrld,
                           width=200, height=300,
                           )
    st.plotly_chart(fig_user_area, use_container_width=True)

    # 2. Visualisasi Dev
    fig_dev = df_selection['Dev'].value_counts().sort_values(ascending=True)
    fig_dev = pd.DataFrame(
        {'Dev': fig_dev.index, 'Jumlah Instruktur': fig_dev.values})
    fig_freq_dev = px.bar(fig_dev,
                          title="Jumlah Instruktur Dev",
                          width=200, height=370,
                          x='Dev',
                          y='Jumlah Instruktur',
                          color="Dev",
                          color_discrete_sequence=px.colors.sequential.Emrld)
    # Membagi columns u/ chart
    left_column, right_column = st.columns(2)
    left_column.plotly_chart(fig_freq_dev, use_container_width=True)

    # 2. Visualisasi JI
    fig_ji = df_selection['JI'].value_counts().sort_values(ascending=True)
    fig_ji = pd.DataFrame(
        {'JI': fig_ji.index, 'Jumlah Instruktur': fig_ji.values})
    fig_freq_ji = px.bar(fig_ji,
                         title="Jumlah Instruktur JI",
                         width=200, height=370,
                         x='JI',
                         y='Jumlah Instruktur',
                         color="JI",
                         color_discrete_sequence=px.colors.sequential.Emrld)
    # Membagi columns u/ chart
    right_column.plotly_chart(fig_freq_ji, use_container_width=True)

    # 2. Visualisasi JNI
    fig_jni = df_selection['JNI'].value_counts().sort_values(ascending=True)
    fig_jni = pd.DataFrame(
        {'JNI': fig_jni.index, 'Jumlah Instruktur': fig_jni.values})
    fig_freq_jni = px.bar(fig_jni,
                          title="Jumlah Instruktur JNI",
                          width=200, height=370,
                          x='JNI',
                          y='Jumlah Instruktur',
                          color="JNI",
                          color_discrete_sequence=px.colors.sequential.Emrld)
    # Membagi columns u/ chart
    left_column.plotly_chart(fig_freq_jni, use_container_width=True)


# Menghapus Hamburger dan Footer Bawaan Streamlit
st.markdown("""
<style>
.css-1h3hwqk{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)
