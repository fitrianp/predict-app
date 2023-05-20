import streamlit as st
import pandas as pd
import plotly_express as px

st.set_page_config(
    page_title="Visualization MIUDR",
    page_icon="📈"
)

# Membuat container
dataset = st.container()
filter = st.container()
visualisasi = st.container()

with dataset:
    # Title
    st.markdown("<h1 style='text-align: center;'> <b> Summary MIUDR <b></h1>",
                unsafe_allow_html=True)

    # Menampilkan Dataset .csv/.xlsx
    miudr_dataset = pd.read_csv(
        "data/MIUDR 2020-2022 (Original).csv")
    # miudr_dataset = pd.read_excel(io='data/MIUDR 2020-2022 (Original).xlsx',
    #                               engine='openpyxl',
    #                               sheet_name='MIUDR 2020-2022',
    #                               usecols='A:V',
    #                               nrows=50000)

    # Mengganti nama kolom Lokasi Kegiatan
    miudr_dataset = miudr_dataset.rename(
        columns={"Lokasi Kegiatan": "Lokasi_kegiatan"})
    miudr_dataset = miudr_dataset.rename(
        columns={"Tempat Kegiatan": "Tempat_kegiatan"})

with filter:
    # Membuat Sidebar untuk Filter
    st.sidebar.header("Please Filter Here:")
    tahun = st.sidebar.multiselect("Pilih tahun dataset",
                                   options=miudr_dataset["Tahun"].unique(),
                                   default=miudr_dataset["Tahun"].unique()
                                   )
    bulan = st.sidebar.multiselect("Pilih bulan dataset",
                                   options=miudr_dataset["Bulan"].unique(),
                                   default=miudr_dataset["Bulan"].unique()
                                   )
    area = st.sidebar.multiselect("Pilih area (TTA) lokasi kerja instruktur",
                                  options=miudr_dataset["TTA"].unique(),
                                  default=miudr_dataset["TTA"].unique())
    kategori = st.sidebar.multiselect("Pilih kategori materi pembelajaran",
                                      options=miudr_dataset["Kategori"].unique(
                                      ),
                                      default=miudr_dataset["Kategori"].unique())
    lokasi = st.sidebar.multiselect("Pilih lokasi kerja",
                                    options=miudr_dataset["Lokasi_kegiatan"].unique(
                                    ),
                                    default=miudr_dataset["Lokasi_kegiatan"].unique(
                                    )
                                    )

    # tk = st.sidebar.multiselect("Pilih tempat kegiatan",
    #                             options=miudr_dataset["Tempat_kegiatan"].unique(
    #                             ),
    #                             default=miudr_dataset["Tempat_kegiatan"].unique(
    #                             ))

    # Memberikan fungsi kerja pada filter sidebar
    df_selection = miudr_dataset.query(
        "Tahun == @tahun & Bulan == @bulan & TTA == @area & Kategori == @kategori & Lokasi_kegiatan == @lokasi"
    )
    df_selection_user_area = miudr_dataset.query(
        "Tahun == @tahun & TTA == @area"
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
    col1, col2, col3, col4 = st.columns(4)
    row = df_selection.shape[0]
    col1.metric("**Total Data Input**", row)
    column = df_selection.shape[1]
    col2.metric("**Total Kolom Data**", column)
    user_by_tahun = df_selection['NRP'].nunique()
    col3.metric("**Total User**", user_by_tahun)
    area = df_selection['TTA'].nunique()
    col4.metric("**Total Area**", area)

    # Membagi columns u/ chart
    left_column, right_column = st.columns(2)

    # 1. Visualisasi persebaran jumlah instruktur di masing-masing area [Bar Chart]
    user_area = df_selection.groupby(
        'TTA')['NRP'].nunique().sort_values(ascending=False)
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
    left_column.plotly_chart(fig_user_area, use_container_width=True)

    # 2. Visualisasi Banyaknya Pertemuan Instruktur By Tahun [Pie hart]
    pertemuan_kategori1 = df_selection.groupby('Kategori')['NRP'].count()
    pertemuan_kategori1 = pertemuan_kategori1.sort_values(ascending=False)
    pertemuan_kategori1 = pd.DataFrame({'Kategori': pertemuan_kategori1.index,
                                        'Banyaknya Pertemuan': pertemuan_kategori1.values})
    value = pertemuan_kategori1['Banyaknya Pertemuan']
    name = pertemuan_kategori1['Kategori']
    fig_pertemuan_kategori1 = px.pie(pertemuan_kategori1, values=value, names=name,
                                     title="Banyaknya Pertemuan Instruktur per Kategori",
                                     width=200, height=300,
                                     color_discrete_sequence=px.colors.sequential.Emrld)
    right_column.plotly_chart(fig_pertemuan_kategori1,
                              use_container_width=True)

    # 3. Visualisasi persebaran instruktur berdasarkan lokasi kegiatan
    freq_loc = df_selection['Lokasi_kegiatan'].value_counts()
    freq_loc = freq_loc.sort_values(ascending=False)
    freq_loc = pd.DataFrame(
        {'Lokasi': freq_loc.index, 'Banyaknya Pelaksanaan': freq_loc.values})
    fig_freq_loc = px.bar(freq_loc,
                          title="Banyaknya Pertemuan Instruktur per Lokasi",
                          width=200, height=300,
                          x='Lokasi',
                          y='Banyaknya Pelaksanaan',
                          color='Lokasi',
                          color_discrete_sequence=px.colors.sequential.Emrld)
    left_column.plotly_chart(fig_freq_loc, use_container_width=True)

    # 4. Visualisasi 10 Tempat Kegiatan favorite
    most_freq_loc = df_selection['Tempat_kegiatan'].value_counts()
    most_freq_loc = most_freq_loc.sort_values(ascending=False)
    most_freq_loc = most_freq_loc.iloc[0:10]
    most_freq_loc = pd.DataFrame(
        {'Lokasi': most_freq_loc.index, 'Banyaknya Pelaksanaan': most_freq_loc.values})
    fig_most_freq_loc = px.bar(
        most_freq_loc,
        title="<b>10 Tempat Kegiatan favorite</b>",
        x='Banyaknya Pelaksanaan',
        y='Lokasi',
        orientation="h",
        color_discrete_sequence=px.colors.sequential.Emrld,
        width=200, height=300,)
    right_column.plotly_chart(fig_most_freq_loc, use_container_width=True)

    # 5. Visualisasi pembagian Job Assignment
    # Menghitung jumlah jam
    freq_jam = df_selection.groupby(['Tahun', 'TTA', 'NRP']).sum()[
        ['Jumlah Jam']]
    # st.write(freq_jam.head())
    # st.write(freq_jam.shape)
    # freq_jam.insert(loc=2, column="JA", value='')
    Class = []
    for index, row in freq_jam.iterrows():
        if row["Jumlah Jam"] > 1872:
            Class.append('Overload')
        elif row["Jumlah Jam"] > 936 and row["Jumlah Jam"] <= 1872:
            Class.append('Normal')
        elif row["Jumlah Jam"] <= 936:
            Class.append('Underload')

    freq_jam["JA"] = Class
    # st.write(freq_jam.head())
    freq_jam = freq_jam['JA'].value_counts()
    # st.write(freq_jam)

    freq_jam = pd.DataFrame(
        {'Class': freq_jam.index, 'Jumlah Instruktur': freq_jam.values})
    fig_freq_ja = px.bar(freq_jam,
                         title="Pembagian Job Assignment",
                         width=200, height=370,
                         x='Class',
                         y='Jumlah Instruktur',
                         color="Class",
                         color_discrete_sequence=px.colors.sequential.Emrld)
    left_column.plotly_chart(fig_freq_ja, use_container_width=True)

    # 6. Visualisasi Trend Pelaksanaan Instruktu By Tahun dan Bulan [Line Chart]
    tab1, tab2 = right_column.tabs(
        ["Tahun & Bulan", "Tahun & Area"])

    with tab1:
        # st.markdown("### **Trend Pelaksanaan Instruktur By Tahun dan Bulan**")
        df_selection['Bulan'] = df_selection['Bulan'].replace(
            ['Januari'], '01')
        df_selection['Bulan'] = df_selection['Bulan'].replace(
            ['Februari'], '02')
        df_selection['Bulan'] = df_selection['Bulan'].replace(['Maret'], '03')
        df_selection['Bulan'] = df_selection['Bulan'].replace(['April'], '04')
        df_selection['Bulan'] = df_selection['Bulan'].replace(['Mei'], '05')
        df_selection['Bulan'] = df_selection['Bulan'].replace(['Juni'], '06')
        df_selection['Bulan'] = df_selection['Bulan'].replace(['Juli'], '07')
        df_selection['Bulan'] = df_selection['Bulan'].replace(
            ['Agustus'], '08')
        df_selection['Bulan'] = df_selection['Bulan'].replace(
            ['September'], '09')
        df_selection['Bulan'] = df_selection['Bulan'].replace(
            ['Oktober'], '10')
        df_selection['Bulan'] = df_selection['Bulan'].replace(
            ['Nopember'], '11')
        df_selection['Bulan'] = df_selection['Bulan'].replace(
            ['Desember'], '12')

        pelaksanaan = df_selection.groupby('Bulan')['NRP'].count()
        pelaksanaan = pelaksanaan.to_frame(name='Jumlah')
        fig_pelaksanaan = px.line(
            pelaksanaan,
            title="<b>Trend Pelaksanaan Instruktur By Tahun dan Bulan</b>",
            width=200, height=300,
            color_discrete_sequence=px.colors.sequential.Emrld,
        )
        st.plotly_chart(fig_pelaksanaan, use_container_width=True)
        # st.write(fig)

        # fig1 = plt.figure(figsize=(7, 2))
        # plt.plot(pelaksanaan)
        # st.write(fig1)

    with tab2:
        # st.markdown("### **Trend Pelaksanaan Instruktur By Tahun dan Area**")
        pelaksanaan_area = df_selection.groupby('TTA')['NRP'].count()
        pelaksanaan_area = pelaksanaan_area.sort_values(ascending=False)
        pelaksanaan_area = pelaksanaan_area.to_frame(
            name='Jumlah')

        fig_pelaksanaan_area = px.line(
            pelaksanaan_area,
            title="<b>Trend Pelaksanaan Instruktur By Tahun dan Area</b>",
            width=200, height=300,
            color_discrete_sequence=px.colors.sequential.Emrld)
        st.plotly_chart(
            fig_pelaksanaan_area, use_container_width=True)

# Menghapus Hamburger dan Footer Bawaan Streamlit
st.markdown("""
<style>
.css-1h3hwqk{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)
