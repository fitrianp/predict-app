import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="About Dataset",
    page_icon="💬"
)

# 2. Navbar Menu
tab1, tab2, tab3 = st.tabs(
    ["Dataset Utama (MIUDR)", "Dataset Tambahan (Manpower SVC)", "Integrasi Data (MIUDR + Manpower SVC)"])

with tab1:
    st.title("MIUDR Dataset")
    st.markdown("""
    >- MIUDR (Monthly Instructor Utilization Development Report) merupakan laporan atau logbook instruktur untuk mengetahui kegiatan yang dilakukannya baik itu kegiatan mengajar, non mengajar ataupun pengembangan.
    >- Dalam penelitian ini, data yang didapatkan dalam 3 tahun terakhir, yakni MIUDR 2020, MIUDR 2021, dan MIUDR 2023. 
    >- MIUDR biasanya diolah untuk mentracking kegiatan instruktur apakah kegiatan yang dilakukannya memenuhi target atau tidak atau bahkan melebihinya.
    >- Biasanya juga sebagai evaluasi, evaluasi dilakukan biasanya pada tiap akhir tahun. Hasil dari evaluasi akan diterapkan pada awal tahun berikutnya.
    """)

    st.header("Preview Dataset")
    st.markdown(
        """
        >Dataset yang didapatkan berupa dataset MIUDR yang terpisah yaitu MIUDR 2020, MIUDR 2021, MIUDR 2022. Masing-masing jumlah baris dan kolom, sebagai berikut:
        >- MIUDR 2020: 13.722 baris dan 22 kolom
        >- MIUDR 2021: 18.692 baris dan 22 kolom
        >- MIUDR 2022: 16.018 baris dan 22 kolom
        """)
    col1, col2, col3 = st.columns(3)
    col1.image("assets/preview MIUDR 2020.jpg", caption="MIUDR 2020")
    col2.image("assets/preview MIUDR 2021.jpg", caption="MIUDR 2021")
    col3.image("assets/preview MIUDR 2022.jpg", caption="MIUDR 2022")

    st.header("Penggabungan Data")
    st.markdown(
        """
        >Dari dataset MIUDR yang terpisah tersebut, maka dilakukan penggabungan data (secara manual). Dan didapatkan jumlah baris dan kolom masing-masing sebanyak 48.432 baris dan 22 kolom.
        """)
    st.image("assets/preview MIUDR 2020-2022.jpg",
             caption="MIUDR 2020-2022")

    st.header("Informasi Data")
    st.markdown(
        ">Untuk lebih mengetahui informasi dari masing-masing kolom pada dataset, berikut informasinya:")
    st.image("assets/info MIUDR.jpg", caption="Informasi Data MIUDR")


with tab2:
    st.title("Man Power SVC")
    st.markdown("""
    >- Terdapat dataset lain yang dijadikan sebagai sumber untuk proses integrasi data (penggabungan data), yaitu data Manpower SVC 2023.
    >- Manpower SVC 2023 merupakan data seluruh karyawan yang bekerja pada bagian divisi Service di PT United Tractors Tbk.
    >- Dalam penelitian ini, data yang digunakan untuk penambahannya yaitu kolom Cabang/Site, Umur, dan Lama Kerja. Kolom-kolom tersebut digunakan karena memiliki relasi dengan penelitian ini.
    """)

    st.header("Preview Dataset")
    st.markdown(
        ">Data ini memiliki jumlah baris dan kolom masing-masing sebanyak 1.217 baris dan 19 kolom.")
    st.image("assets/preview Manpower SVC 2023.jpg", caption="Manpower SVC")

    st.header("Informasi Data")
    st.markdown(
        ">Untuk lebih mengetahui informasi dari masing-masing kolom pada dataset, berikut informasinya:")
    st.image("assets/info Manpower SVC.jpg",
             caption="Informasi Data Manpower SVC 2023")

with tab3:
    st.title("Integrasi Data")
    st.markdown("""
    >- Data penggabungan MIUDR + Manpower SVC dilakukan pada tahapan proses KDD, yakni integrasi data.
    >- Data ini digabungkan secara manual dimana dalam proses penggabungan menyesuaikan dengan NRP masing-masing instruktur.
    >- Sehingga, jumlah baris dan kolom menjadi sebanyak 48.432 baris dengan 25 kolom.
    """)

    st.header("Preview & Informasi Data")
    left, right = st.columns(2)
    left.image("assets/preview Integrasi Data.jpg",
               caption="Preview Integrasi Data")
    right.image("assets/info Integrasi Data.jpg",
                caption="Informasi Integrasi Data")


# Menghapus Hamburger dan Footer Bawaan Streamlit
st.markdown("""
<style>
.css-1h3hwqk{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)
