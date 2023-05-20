import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Preprocessing Data",
    page_icon="🧹"
)

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["KDD", "Pembersihan", "Integrasi", "Seleksi", "Transformasi"])
# Membuat container

with tab1:
    st.markdown("<h1 style='text-align: center;'> Proses KDD </h1>",
                unsafe_allow_html=True)
    st.markdown(
        """
    >**Langkah-langkah pre-processing dataset dengan konsep KDD:**
    >1. Pembersihan Data
    >2. Integrasi Data
    >3. Seleksi Data
    >4. Transformasi Data
    >5. Proses Mining
    >6. Evaluasi Pola
    """
    )
    # st.markdown("[Untuk proses Pre-Processing dapat melalui Google Colab. Click This Link!](https://colab.research.google.com/drive/1jCApdEu6kFoLJ9PNxVM___o5g_IDZiNC?usp=sharing)")

with tab2:
    st.subheader("1. Pembersihan Data")
    st.markdown("""
    > Luaran yang diharapkan pada tahapan ini bahwa data telah bersih, yaitu tidak adanya missing values.
    """)

    # Menampilkan Dataset .csv/.xlsx
    st.markdown("#### Load Dataset")
    miudr_dataset = pd.read_csv("data/MIUDR 2020-2022 (Original).csv")
    st.warning("Note: Data yang digunakan merupakan data gabungan MIUDR 2020-2022")
    st.write(miudr_dataset.head(2))

    # Memeriksa jumlah baris dan kolom
    st.markdown("#### Memeriksa jumlah baris dan kolom")
    st.write(miudr_dataset.shape)

    # Memeriksa banyaknya nilai atribut yang kosong
    st.markdown("#### Memeriksa Missing Values")
    st.write(miudr_dataset.isnull().sum().to_frame("Banyaknya Nilai Kosong"))
    st.success("*Karena pada atribut/kolom yang akan digunakan sudah bersih seperti NRP & Nama (Sebagai Sample), Kategori, Jumlah Jam, dan TTA (Sebagai Atribut) sudah bersih")

with tab3:
    st.subheader("2. Integrasi Data")
    st.markdown("""
    >Pada tahap ini menerapkan integrasi data yang berasal dari 2 sumber:
    > 1. Dari dataset luar (Manpower SVC), dan
    > 2. Dari hasil analisa pada dataset yang sama.
    > Setelah itu, dilakukan penggabungan dari semuanya
    """)

    # Dari sumber dataset luar
    st.markdown("### 1. Sumber dari dataset luar(Manpower SVC)")
    st.markdown(
        """
        > Data yang diambil dari Manpower SVC yaitu kolom Cabang/Site, Umur, dan Lama Kerja.
        > Penggabungan data dilakukan secara manual dengan acuan NRP pada masing-masing instruktur.
        > Untuk informasi tentang data Manpower, dapat melihat pada halaman about dataset -> Manpower SVC 2023.
        """)

    # Menampilkan Dataset .csv/.xlsx
    st.markdown("##### Load Dataset")
    miudr_dataset1 = pd.read_csv("data/MIUDR 2020-2022 (Modif) 1.csv")
    st.write(miudr_dataset1.head(2))

    # Memeriksa jumlah baris dan kolom
    st.markdown("##### Memeriksa jumlah baris dan kolom")
    st.write(miudr_dataset1.shape)

    # Memeriksa banyaknya nilai atribut yang kosong
    st.markdown("##### Memeriksa Missing Values")
    st.write(miudr_dataset1.isnull().sum().to_frame("Banyaknya Nilai Kosong"))
    st.success("*Karena pada atribut/kolom yang akan digunakan sudah bersih seperti NRP & Nama (Sebagai Sample), Kategori, Jumlah Jam, TTA, Cabang/Site, umur, Lama Kerja (Sebagai Atribut) sudah bersih")

    # Sumber pada dataset yang sama
    st.markdown("### 2. Sumber dari hasil analisa pada dataset yang sama")
    st.markdown(
        "> Didapatkan dari hasil akumulasi jumlah jam yang ada.")

    # Perhitungan JA per Instruktur
    st.markdown("##### Menghitung Total Jam secara keseluruhan (JA)")
    st.markdown(
        "> Tahapan ini untuk mengetahui total jam yang dihabiskan instruktur untuk mengajar selama 1 tahun.")
    freq_jam = miudr_dataset1.groupby(['Tahun', 'NRP', 'TTA'])[
        'Jumlah Jam'].sum()
    freq_jam.to_frame(name='Freq Jam')
    st.write(freq_jam)

    # Perhitungan Jumlah Jam Per Kategori
    st.markdown("##### Menghitung Total Jam per Kategori")
    st.markdown(
        "> Tahapan ini untuk mengetahui total jam yang dihabiskan instruktur untuk mengajar pada masing-masing kategori pembelajaran selama 1 tahun.")
    jumlah_jam = miudr_dataset1.groupby(['Tahun', 'Kategori', 'NRP', 'TTA'])[
        'Jumlah Jam'].sum()
    jumlah_jam.to_frame(name='Jam Kategori')
    st.write(jumlah_jam)

    # Penggabungan Integrasi 1&2
    st.markdown("### 3. Penggabungan dari dataset diatas")
    st.markdown(
        """
        > - Ini merupakan tahapan terakhir pada integrasi data, yaitu menggabungkan semua dari 2 langkah integrasi diatas.
        > - Penggabungan dilakukan secara manual dengan menjadikan atribut baru seperti umur, lama kerja, cabang/site, dev, ji, jni, dan total jam.
        > - Penggabungan ini dilakukan berdasarkan acuan NRP pada masing-masing instruktur.
        """)

    # Menampilkan Dataset .csv/.xlsx
    st.markdown("##### Load Dataset")
    miudr_dataset1 = pd.read_csv("data/MIUDR 2020-2022 (Vers 1)_totaljam2.csv")
    st.write(miudr_dataset1.head(2))

    # Informasi data
    st.markdown("##### Informasi Dataset")
    st.image("assets/info Integrasi Data2.jpg",
             caption="Informasi Data")

    # Memeriksa jumlah baris dan kolom
    st.markdown("##### Memeriksa Jumlah Baris dan Kolom")
    st.write(miudr_dataset1.shape)

    # Memeriksa jumlah baris dan kolom
    st.markdown("##### Memeriksa Missing Values")
    st.write(miudr_dataset1.isnull().sum())

    # Mengatasi Missing Values
    st.markdown("##### Mengatasi Missing Values")
    st.markdown("> Dengan mengisi kolom Dev dan JNI yang kosong dengan nilai 0. Artinya, instruktur tersebut tidak mengajar di kategori tersebut")
    miudr_dataset1['Dev'] = miudr_dataset1['Dev'].fillna(0)
    miudr_dataset1['JNI'] = miudr_dataset1['JNI'].fillna(0)
    miudr_dataset1.isnull().sum()
    st.write(miudr_dataset1.isnull().sum())

    # Note
    st.success("Tahap Integrasi sudah selesai")

with tab4:
    st.subheader("3. Seleksi Data")
    st.markdown("""
    > Luaran yang diharapkan pada tahap ini, yakni bahwa dataset hanya menyisakan atribut-atribut yang akan digunakan selanjutnya (Proses Mining).
    > Yang dilakukan yaitu menghapus kolom No, Tahun, dan NRP. Karena, sudang tidak akan digunakan lagi.
    """)

    # Seleksi Data
    st.markdown("##### Load Data")
    selection_data = miudr_dataset1.drop(
        columns=['No', 'Tahun', 'NRP'], axis=1)
    st.write(selection_data.head(2))

    st.markdown("##### Memeriksa Jumlah Baris dan Kolom")
    st.write(selection_data.shape)

    # Informasi data
    st.markdown("##### Informasi Dataset")
    st.image("assets/info Integrasi Data3.jpg",
             caption="Informasi Data")
    # Note
    st.success("Tahap Seleksi sudah selesai")

with tab5:
    st.subheader("4. Transformasi Data")
    st.markdown("""
    > Pada tahap ini untuk memudahkan proses mining dilakukan perubahan nilai atribut menjadi kategorikal, dengan syarat berikut:
    """)

    # Mengubah Kolom Umur
    st.markdown("##### Mengubah Kolom Umur")
    st.markdown(""" Perubahan Kolom Umur dengan syarat:
    > - **Produktif1** [20-29 tahun],
    > - **Produktif2** [30-39 tahun],
    > - **Produktif3** [40-49 tahun],
    > - **Produktif4** [50-59 tahun]""")
    Umur = []
    for index, row in selection_data.iterrows():
        if row["Umur"] >= 20 and row["Umur"] <= 29:
            Umur.append('Produktif1')
        elif row["Umur"] >= 30 and row["Umur"] <= 39:
            Umur.append('Produktif2')
        elif row["Umur"] >= 40 and row["Umur"] <= 49:
            Umur.append('Produktif3')
        elif row["Umur"] >= 50 and row["Umur"] <= 59:
            Umur.append('Produktif4')
    selection_data["Umur"] = Umur

    st.write(selection_data.head(2))
    st.write(selection_data["Umur"].value_counts())

    # Mengubah Kolom Lama Kerja
    st.markdown("##### Mengubah Kolom Lama Kerja")
    st.markdown(""" Pada kolom ini mengalami perubahan nama kolom, yakni Lama Kerja menjadi Level. Serta perubahan nilai atribut dengan mengikuti syarat berikut :
    > - **Junior** (0-5 tahun),
    > - **Senior** (6-11 tahun)""")
    Level = []
    for index, row in selection_data.iterrows():
        if row["Lama Kerja"] >= 0 and row["Lama Kerja"] <= 5:
            Level.append('Junior')
        elif row["Lama Kerja"] >= 6 and row["Lama Kerja"] <= 11:
            Level.append('Senior')
    selection_data["Lama Kerja"] = Level
    # mengubah nama kolom Lama Kerja menjadi Level
    selection_data.rename(columns={"Lama Kerja": "Level"}, inplace=True)

    st.write(selection_data.head(2))
    st.write(selection_data["Level"].value_counts())

    # Mengubah Kolom Dev
    st.markdown("##### Mengubah Kolom Dev")
    st.markdown(""" Perubahan nilai atribut dengan mengikuti syarat berikut :
    > 1. **Dev & Cabang :**
    >> -  Overload (> 281 jam)
    >> -  Normal (141 - 281 jam)
    >> -  Underloaad (< 141 jam)
    > 2. **Dev & Site :**
    >> - Overload (> 252 jam),
    >> - Normal (126 - 252 jam),
    >> - Underload (< 126 jam)
    """)
    Dev = []
    for index, row in selection_data.iterrows():
        # Cabang
        if row["Dev"] > 281 and row["Cabang/Site"] == 'Cabang':
            Dev.append('Overload')
        elif row["Dev"] >= 141 and row["Dev"] <= 281 and row["Cabang/Site"] == 'Cabang':
            Dev.append('Normal')
        elif row["Dev"] < 141 and row["Cabang/Site"] == 'Cabang':
            Dev.append('Underload')

        # Site
        elif row["Dev"] > 252 and row["Cabang/Site"] == 'Site':
            Dev.append('Overload')
        elif row["Dev"] >= 126 and row["Dev"] <= 252 and row["Cabang/Site"] == 'Site':
            Dev.append('Normal')
        elif row["Dev"] < 126 and row["Cabang/Site"] == 'Site':
            Dev.append('Underload')
    selection_data["Dev"] = Dev

    st.write(selection_data.head(2))
    st.write(selection_data["Dev"].value_counts())

    # Mengubah Kolom JI
    st.markdown("##### Mengubah Kolom JI")
    st.markdown(""" Perubahan nilai atribut dengan mengikuti syarat berikut :
    > 1. **JI & Cabang :**
    >> -  Overload (> 1310 jam)
    >> -  Normal (659 - 1310 jam)
    >> -  Underloaad (< 659 jam)
    > 2. **JI & Site :**
    >> - Overload (> 1176 jam),
    >> - Normal (588 - 1176 jam),
    >> - Underload (< 588 jam)
    """)
    # Mengubah Kolom JI
    JI = []
    for index, row in selection_data.iterrows():
        # Cabang
        if row["JI"] > 1310 and row["Cabang/Site"] == 'Cabang':
            JI.append('Overload')
        elif row["JI"] >= 659 and row["JI"] <= 1310 and row["Cabang/Site"] == 'Cabang':
            JI.append('Normal')
        elif row["JI"] < 659 and row["Cabang/Site"] == 'Cabang':
            JI.append('Underload')

    # Site
        elif row["JI"] > 1176 and row["Cabang/Site"] == 'Site':
            JI.append('Overload')
        elif row["JI"] >= 588 and row["JI"] <= 1176 and row["Cabang/Site"] == 'Site':
            JI.append('Normal')
        elif row["JI"] < 588 and row["Cabang/Site"] == 'Site':
            JI.append('Underload')
    selection_data["JI"] = JI

    st.write(selection_data.head(2))
    st.write(selection_data["JI"].value_counts())

    # Mengubah Kolom JNI
    st.markdown("##### Mengubah Kolom JNI")
    st.markdown(""" Perubahan nilai atribut dengan mengikuti syarat berikut :
    > 1. **JNI & Cabang :**
    >> -  Overload (> 281 jam)
    >> -  Normal (141 - 281 jam)
    >> -  Underloaad (< 141 jam)
    > 2. **JNI & Site :**
    >> - Overload (> 252 jam),
    >> - Normal (126 - 252 jam),
    >> - Underload (< 126 jam)
    """)
    JNI = []
    for index, row in selection_data.iterrows():
        # Cabang
        if row["JNI"] > 281 and row["Cabang/Site"] == 'Cabang':
            JNI.append('Overload')
        elif row["JNI"] >= 141 and row["JNI"] <= 281 and row["Cabang/Site"] == 'Cabang':
            JNI.append('Normal')
        elif row["JNI"] < 659 and row["Cabang/Site"] == 'Cabang':
            JNI.append('Underload')

        # Site
        elif row["JNI"] > 252 and row["Cabang/Site"] == 'Site':
            JNI.append('Overload')
        elif row["JNI"] >= 126 and row["JNI"] <= 252 and row["Cabang/Site"] == 'Site':
            JNI.append('Normal')
        elif row["JNI"] < 126 and row["Cabang/Site"] == 'Site':
            JNI.append('Underload')
    selection_data["JNI"] = JNI

    st.write(selection_data.head(2))
    st.write(selection_data["JNI"].value_counts())

    # Mengubah Kolom Total Jam > JA
    st.markdown("##### Mengubah Kolom Total Jam -> JA ")
    st.markdown(""" Pada kolom ini mengalami perubahan nama kolom, yakni Total Jam menjadi JA. Dimana JA merupakan akumulasi total jam seluruh kategori (JA = Dev+JI+JNI). Serta perubahan nilai atribut dengan mengikuti syarat berikut :
    > 1. **JA & Cabang :**
    >> -  Overload (> 1872 jam), 
    >> -  Normal (936 - 1872 jam),
    >> -  Underload (< 936 jam),
    > 2. **JA & Site :**
    >> - Overload (> 1680 jam), 
    >> - Normal (840 - 1680 jam),
    >> - Underload (< 840 jam)
    """)
    JA = []
    for index, row in selection_data.iterrows():
        # Cabang
        if row["Total Jam"] > 1872 and row["Cabang/Site"] == 'Cabang':
            JA.append('Overload')
        elif row["Total Jam"] > 936 and row["Total Jam"] <= 1872 and row["Cabang/Site"] == 'Cabang':
            JA.append('Normal')
        elif row["Total Jam"] < 936 and row["Cabang/Site"] == 'Cabang':
            JA.append('Underload')

        # Site
        elif row["Total Jam"] > 1680 and row["Cabang/Site"] == 'Site':
            JA.append('Overload')
        elif row["Total Jam"] > 840 and row["Total Jam"] <= 1680 and row["Cabang/Site"] == 'Site':
            JA.append('Normal')
        elif row["Total Jam"] < 840 and row["Cabang/Site"] == 'Site':
            JA.append('Underload')
    selection_data["Total Jam"] = JA
    # mengubah nama kolom Total Jam menjadi JA
    selection_data.rename(columns={"Total Jam": "JA"}, inplace=True)

    st.write(selection_data.head())
    st.write(selection_data["JA"].value_counts())

    # Membuat Class Target
    st.markdown("##### Membuat Class Target ")
    selection_data.insert(loc=8, column="JobRotation", value='')
    st.write(selection_data.head())

    # Mengisi data Class Target
    st.markdown("##### Mengisi Nilai Atribut Job Rotation ")
    st.markdown("""
    > Dalam mengisi JobRotation menggunakan acuan dari hasil kolom JA, dengan syarat:
    > - Jika, JA Overload dan Underload, maka yes
    > - Jika, JA Normal, maka no 
    """)
    Rotation = []
    for index, row in selection_data.iterrows():
        if row["JA"] == 'Overload':
            Rotation.append('yes')
        elif row["JA"] == 'Underload':
            Rotation.append('yes')
        else:
            Rotation.append('no')
    selection_data["JobRotation"] = Rotation

    st.write(selection_data.head(2))

    # Menghapus kolom JA
    st.markdown("##### Menghapus Kolom JA ")
    st.markdown(
        "> Kolom JA dihapus, karena sudah digantikan dengan kolom JobRotation")
    selection_data1 = selection_data.drop(columns=['JA'], axis=1)
    st.write(selection_data1.head(10))

    # Note
    st.success(
        "Tahap Transformasi sudah selesai, artinya data sudah siap untuk dilakukan proses mining.")

# Menghapus Hamburger dan Footer Bawaan Streamlit
st.markdown("""
<style>
.css-1h3hwqk{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)
