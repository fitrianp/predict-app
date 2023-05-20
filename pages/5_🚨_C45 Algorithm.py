import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
import graphviz
from sklearn import tree

st.set_page_config(
    page_title="Predict App",
    page_icon=":bar_chart:"
)

# Membuat container
header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()

with header:
    # st.markdown("<h1 style='text-align: center;'> This is My Data Science Project</h1>",
    #             unsafe_allow_html=True)
    # st.markdown("---")
    st.header(
        "Step by Step In Using C4.5 Algorithm As A Classification to Determine Job Rotation")
    st.markdown(
        ">Dalam project ini saya melihat Logbook kegiatan mengajar Instruktur di PT United Tractors Tbk. Dan dari hasil eksplor dataset ternyata dalam **tiga tahun terakhir terjadi ketidakseimbangan dalam penerapan beban kerja instruktur**, dimana beberapa instruktur memiliki beban kerja mengajar yang lebih besar dari yang telah ditetapkan oleh perusahaan. **Oleh karena itu, sangat penting untuk menilai kualifikasi masing-masing instruktur dalam memutuskan apakah Job Rotation harus diterapkan atau tidak** demi menjaga keseimbangan beban kerja para instruktur.")
    # st.markdown("---")

with dataset:
    st.header("MIUDR Dataset")
    st.markdown(
        ">MIUDR(Monthly Instructor Utilization Development Report) merupakan laporan atau logbook instruktur untuk mengetahui kegiatan yang dilakukannya baik itu kegiatan mengajar, non mengajar ataupun pengembangan. Dalam penelitian ini, data yang didapatkan dalam 3 tahun terakhir, yakni MIUDR 2020, MIUDR 2021, dan MIUDR 2023. :orange[Untuk lebih jelasnya tertera pada halaman About Dataset.]")
    st.warning(
        "Pada tahapan ini data yang digunakan merupakan data yang sudah dilakukan pre-processing")

    # Menampilkan dataset
    st.markdown("##### Load Dataset")
    miudr_dataset = pd.read_csv(
        "data/MIUDR 2020-2022 (Bersih-Target) (3).csv")
    st.write(miudr_dataset.head())

    # Seleksi dataset
    st.markdown("##### Seleksi Dataset")
    st.text("Menghapus kolom unnamed: 0")
    miudr_dataset = miudr_dataset.drop(columns=['Unnamed: 0'], axis=1)
    st.write(miudr_dataset.head())

    # Menampilkan Jumlah Baris dan Kolom
    st.markdown("##### Menampilkan Jumlah Baris dan Kolom")
    st.write(miudr_dataset.shape)

with features:
    st.header("Feature Engineering")

    # Label Encoding
    st.markdown("##### Label Encoding")
    le = LabelEncoder()
    miudr_dataset['TTA'] = le.fit_transform(miudr_dataset['TTA'].values)
    miudr_dataset['Cabang/Site'] = le.fit_transform(
        miudr_dataset['Cabang/Site'].values)
    miudr_dataset['Umur'] = le.fit_transform(miudr_dataset['Umur'].values)
    miudr_dataset['Level'] = le.fit_transform(miudr_dataset['Level'].values)
    miudr_dataset['Dev'] = le.fit_transform(miudr_dataset['Dev'].values)
    miudr_dataset['JI'] = le.fit_transform(miudr_dataset['JI'].values)
    miudr_dataset['JNI'] = le.fit_transform(miudr_dataset['JNI'].values)
    miudr_dataset['JobRotation'] = le.fit_transform(
        miudr_dataset['JobRotation'].values)
    st.write(miudr_dataset.head())

    # Informasi dari perubahan Label Encoding
    st.markdown("##### Informasi data dari hasil Label Encoding")
    data_le = pd.DataFrame(
        {"TTA": ["ADR", "BJM", "BKJ", "BLP", "BNT", "JKT", "MLW", "PKB", "SGT", "SMD", "TJE", "TJR", "UPG"], "Cabang/Site": ["Cabang", "Site", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], "Umur": ["Produktif1", "Produktif2", "Produktif3", "Produktif4", "-", "", "-", "-", "-", "-", "-", "-", "-"], "Level": ["Junior", "Senior", "-", "-", "-", "", "-", "-", "-", "-", "-", "-", "-"], "Dev": ["Normal", "Overload", "Underload", "-", "-", "", "-", "-", "-", "-", "-", "-", "-"], "JI": ["Normal", "Overload", "Underload", "-", "-", "", "-", "-", "-", "-", "-", "-", "-"], "JNI": ["Normal", "Overload", "Underload", "-", "-", "", "-", "-", "-", "-", "-", "-", "-"]})
    # st.dataframe(data_le)
    st.table(data_le)

with modelTraining:
    st.header("Modelling with C4.5 Algorithm")

    # Memisahkan Target Variable
    X = miudr_dataset.drop(['JobRotation'], axis=1)
    y = miudr_dataset['JobRotation']

    # Split data into separate training and test set
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1)

    col_1, col_2 = st.columns(2)
    max_depth = col_1.slider('What should be the max_depth of the model?',
                             min_value=1, max_value=100, value=5, step=2)

    # Modelling Decision Tree dengan Algoritma C4.5
    dct = DecisionTreeClassifier(max_depth=max_depth, random_state=1)

    # fit the model
    dct.fit(X_train, y_train)

    # Akurasi
    pred = dct.predict(X_test)
    st.write("Tingkat Akurasi Algoritma C4.5")
    asc = accuracy_score(y_test, pred)
    st.success("Tingkat Akurasi: %d persen" % (asc*100))

    st.header("Modelling with C4.5 & PSO Algorithm")
    st.markdown("> Karena luaran penelitian ini memiliki batasan, bahwa penggabungan algoritma C4.5 dan PSO hanya digunakan untuk memastikan bahwa ada peningkatan di dalam akurasi dan tidak mempengaruhi pada prediksi data. Oleh sebab itu, PSO tidak ditambahkan pada web app ini.")

    st.markdown(
        "[C45 PSO algorithm. Click This Link!](https://colab.research.google.com/drive/1oECTC1xGvqpG3echVyKxrCS8YylitLvw?usp=sharing)")

    # Menampilkan hasil tree yang terbentuk
    st.markdown("##### Hasil Pohon Keputusan yang terbentuk")
    tree = export_graphviz(dct, class_names=["yes", "no"])
    st.graphviz_chart(tree)

# Menghapus Hamburger dan Footer Bawaan Streamlit
st.markdown("""
<style>
.css-1h3hwqk{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)
