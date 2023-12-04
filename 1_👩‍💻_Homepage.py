import streamlit as st

st.set_page_config(
    page_title="HomePage",
    page_icon="👩‍💻",
)

# Title
st.markdown("<h1 style='text-align: center;'> <b>This is My Data Science Project</b></h1>",
            unsafe_allow_html=True)

st.markdown("""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
  </head>
  <body>
    <div class="card" style="margin-top: 2rem; border-radius: 20px; box-shadow: 10px 7px #0083B8;">
        <div class="card-body">
            <p class="card-text" style='text-align: justify;'>
                Project ini merupakan hasil luaran dari penelitian yang diajukan sebagai salah satu
                syarat untuk memperoleh gelar Sarjana Strata 1 (S1) Program Studi Teknik Informatika 
                Universitas Trisakti oleh Fitria Nabilah Putri (2019) dengan judul <b>OPTIMASI ALGORITMA C4.5 
                UNTUK PENENTUAN JOB ROTATION MENGGUNAKAN PARTICLE SWARM OPTIMIZATION.</b>
            </p>
            <p class="card-text" style='text-align: justify;'> 
                Dimana, lokasi penelitian ini di PT United Tractors Tbk dengan menganalisis permasalahan terkait pemerataan beban kerja instruktur.
                Serta, data yang didapatkan yaitu data MIUDR (Monthly Instructor Utilization Development Report) atau logbook kegiatan instruktur yang didapatkan 3 tahun terakhir, yaitu tahun 2020,2021 dan 2022. 
            </p>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
  </body>
</html>
""", unsafe_allow_html=True)


# Menghapus Hamburger dan Footer Bawaan Streamlit
st.markdown("""
<style>
.css-1h3hwqk{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)
