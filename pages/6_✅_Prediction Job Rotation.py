import streamlit as st
import pickle
from sklearn.tree import DecisionTreeClassifier

st.set_page_config(
    page_title="Predict App",
    page_icon=":bar_chart:"
)

# Model C4.5
with open('C45.pickle', 'rb') as f:
    clf = pickle.load(f)


def main():
    # Set Form
    st.markdown("<h2 style='text-align: center;'> Predict Yes Or No to Implement Job Rotation </h2>",
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    # Umur Instruktur
    age_options = {
        0: "Produktif 1 (20 - 29 tahun)",
        1: "Produktif 2 (30 - 39 tahun)",
        2: "Produktif 3 (40 - 49 tahun)",
        3: "Produktif 4 (50 - 59 tahun)",
    }
    select_age = col1.selectbox(
        label="Umur Instruktur?",
        options=(0, 1, 2, 3),
        format_func=lambda x: age_options.get(x),
    )
    # st.write(f'You have chosen {age_options.get(select_age)}'
    #          f' with the value {select_age}.')
    # st.write(select_age)

    # Cabang/Site
    cab_site_options = {
        0: "Cabang",
        1: "Site",
    }
    select_cabang = col2.selectbox(
        label="Lokasi Kerja di Cabang/Site?",
        options=(0, 1),
        format_func=lambda x: cab_site_options.get(x),
    )
    # st.write(f'You have chosen {cab_site_options.get(select_cabang)}'
    #          f' with the value {select_cabang}.')
    # st.write(select_cabang)

    # Berapa Lama kerja Di Cabang/Site
    level_options = {
        0: "Junior (0 - 5 tahun)",
        1: "Senior (6 - 11 tahun)",
    }
    select_level = col2.selectbox(
        label="Level Instruktur (Lama Kerja di Cabang/Site)?",
        options=(0, 1),
        format_func=lambda x: level_options.get(x),
    )
    # st.write(f'You have chosen {level_options.get(select_level)}'
    #          f' with the value {select_level}.')
    # st.write(select_level)

    # Pemisalan untuk kondisi tertentu
    if select_cabang == 0:
        # Area
        area_options = {
            1: "Banjarmasin (BJM)",
            3: "Balik Papan (BLP)",
            5: "Jakarta (JKT)",
            7: "Pekanbaru (PKB)",
            9: "Samarinda (SMD)",
            12: "Ujung Pandang (UPG)",
        }
        select_area = col1.selectbox(
            label="Lokasi Area Cabang/Site Kerja Instruktur?",
            options=(1, 3, 5, 7, 9),
            format_func=lambda x: area_options.get(x),
        )
        # st.write(f'You have chosen {area_options.get(select_area)}'
        #          f' with the value {select_area}.')
        # st.write(select_area)

        # Dev
        dev_options = {
            0: "Normal (141 - 281 jam)",
            1: "Overload (> 281 jam) ",
            2: "Underload (< 241 jam)",
        }
        select_dev = col1.selectbox(
            label="Interval jumlah jam yang dihabiskan untuk mengajar kategori Development selama satu tahun?",
            options=(0, 1, 2),
            format_func=lambda x: dev_options.get(x),
        )
        # st.write(f'You have chosen {dev_options.get(select_dev)}'
        #          f' with the value {select_dev}.')
        # st.write(select_dev)

        # JI
        ji_options = {
            0: "Normal (659 - 1310 jam)",
            1: "Overload (> 1310 jam) ",
            2: "Underload (< 659 jam)",
        }
        select_ji = col2.selectbox(
            label="Interval jumlah jam yang dihabiskan untuk mengajar kategori Job Institusional (JI) selama satu tahun?",
            options=(0, 1, 2),
            format_func=lambda x: ji_options.get(x),
        )
        # st.write(f'You have chosen {ji_options.get(select_ji)}'
        #          f' with the value {select_ji}.')
        # st.write(select_ji)

        # JNI
        jni_options = {
            0: "Normal (141 - 281 jam)",
            1: "Overload (> 281 jam) ",
            2: "Underload (< 241 jam)",
        }
        select_jni = st.selectbox(
            label="Interval jumlah jam yang dihabiskan untuk mengajar kategori Job Noninstitusional (JNI) selama satu tahun?",
            options=(0, 1, 2),
            format_func=lambda x: jni_options.get(x),
        )
        # st.write(f'You have chosen {jni_options.get(select_jni)}'
        #          f' with the value {select_jni}.')
        # st.write(select_jni)
    else:
        # Area
        area_options = {
            0: "Adaro (ADR)",
            2: "Batu Kajang (BKJ)",
            4: "Bontang (BNT)",
            6: "Malawai (MLW)",
            8: "Sanggata (SGT)",
            10: "Tanjung Enim (TJE)",
            11: "Tanjung Redeb (TJR)",
        }
        select_area = col1.selectbox(
            label="Lokasi Area Cabang/Site Kerja Instruktur?",
            options=(0, 2, 4, 6, 8, 10, 11),
            format_func=lambda x: area_options.get(x),
        )
        # st.write(f'You have chosen {area_options.get(select_area)}'
        #          f' with the value {select_area}.')
        # st.write(select_area)

        # Dev
        dev_options = {
            0: "Normal (126 - 252 jam)",
            1: "Overload (> 252 jam) ",
            2: "Underload (< 126 jam)",
        }
        select_dev = col1.selectbox(
            label="Interval jumlah jam yang dihabiskan untuk mengajar kategori Development selama satu tahun?",
            options=(0, 1, 2),
            format_func=lambda x: dev_options.get(x),
        )
        # st.write(f'You have chosen {dev_options.get(select_dev)}'
        #          f' with the value {select_dev}.')
        # st.write(select_dev)

        # JI
        ji_options = {
            0: "Normal (588 - 1176 jam)",
            1: "Overload (> 1176 jam) ",
            2: "Underload (< 588 jam)",
        }
        select_ji = col2.selectbox(
            label="Interval jumlah jam yang dihabiskan untuk mengajar kategori Job Institusional (JI) selama satu tahun?",
            options=(0, 1, 2),
            format_func=lambda x: ji_options.get(x),
        )
        # st.write(f'You have chosen {ji_options.get(select_ji)}'
        #          f' with the value {select_ji}.')
        # st.write(select_ji)

        # JNI
        jni_options = {
            0: "Normal (126 - 252 jam)",
            1: "Overload (> 252 jam) ",
            2: "Underload (< 126 jam)",
        }
        select_jni = st.selectbox(
            label="Interval jumlah jam yang dihabiskan untuk mengajar kategori Job Noninstitusional (JNI) selama satu tahun?",
            options=(0, 1, 2),
            format_func=lambda x: jni_options.get(x),
        )
        # st.write(f'You have chosen {jni_options.get(select_jni)}'
        #          f' with the value {select_jni}.')
        # st.write(select_jni)

    if st.button('Predict'):
        result = clf.predict([[select_age, select_cabang, select_area,
                             select_level, select_dev, select_ji, select_jni]])
        if result == 0:
            st.success(
                'No (Instruktur tersebut tidak perlu dilakukan job rotation)')
        else:
            st.success('Yes (Instruktur tersebut perlu dilakukan job rotation)')


if __name__ == '__main__':
    main()


# Menghapus Hamburger dan Footer Bawaan Streamlit
st.markdown("""
<style>
.css-h5rgaw {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)
