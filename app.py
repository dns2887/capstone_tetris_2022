import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu

koperasi = pd.read_csv('https://raw.githubusercontent.com/dns2887/capstone_tetris_2022/main/combined_2016_2019.csv')

hasil_korelasi = {'Pengamatan': ['Koperasi & Tingkat Lulus SMA', 'Koperasi & Tingkat Keterampilan TIK', 'Koperasi & Indeks Literasi Keuangan'], 'Tahun 2016': [-0.144, 0.070, 0.407], 'Tahun 2019': [-0.034, 0.160, 0.338]}
tabel = pd.DataFrame(hasil_korelasi).set_index('Pengamatan')

st.set_page_config(layout='wide',
                   initial_sidebar_state='expanded',
                   page_title='Koperasi & Literasi (Studi Data Tahun 2016 & 2019)')

st.markdown("<body style='background-color:#3d85c6;'></body>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: orange;'>Hubungan Antara Koperasi & Literasi Pada Tiap Provinsi Di Indonesia</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>(Studi Data Tahun 2016 & 2019)</h3>", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=['Latar Belakang', 'Analisa', 'Kesimpulan', 'Sumber Data', 'Lainnya']
    )

if selected == 'Latar Belakang':
    st.markdown("<h4 style='text-align: justify; color: orange;'>Apa itu koperasi?</h4>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify; color: white;'>Berdasarkan UU 17 Tahun 2012, Koperasi adalah badan hukum yang didirikan oleh orang perseorangan atau badan hukum Koperasi, dengan pemisahan kekayaan para anggotanya sebagai modal untuk menjalankan usaha, yang memenuhi aspirasi dan kebutuhan bersama di bidang ekonomi, sosial, dan budaya sesuai dengan nilai dan prinsip Koperasi.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify; color: white;'>Koperasi bertujuan meningkatkan kesejahteraan anggota pada khususnya dan masyarakat pada umumnya, sekaligus sebagai bagian yang tidak terpisahkan dari tatanan perekonomian nasional yang demokratis dan berkeadilan.</h5>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: justify; color: orange;'>Apa itu literasi?</h4>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify; color: white;'>Literasi adalah pengetahuan atau keterampilan dalam bidang atau aktivitas tertentu. Literasi juga dapat diartikan sebagai kemampuan individu dalam mengolah informasi dan pengetahuan untuk kecakapan hidup.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify; color: white;'>Menurut Kementrian Pendidikan, Kebudayaan, Riset, dan Teknologi (Kemendikbud) ada 6 jenis literasi, yaitu:</h5>", unsafe_allow_html=True)
    st.markdown("<ol><li><h5 style='text-align: justify; color: white;'>Literasi Baca Tulis</h5></li><li><h5 style='text-align: justify; color: white;'>Literasi Numerasi</h5></li><li><h5 style='text-align: justify; color: white;'>Literasi Sains</h5></li><li><h5 style='text-align: justify; color: white;'>Literasi Digital</h5></li><li><h5 style='text-align: justify; color: white;'>Literasi Finansial</h5></li><li><h5 style='text-align: justify; color: white;'>Literasi Budaya & Kewargaan</h5></li></ol>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: justify; color: orange;'>Hipotesis</h4>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify; color: white;'>Literasi merupakan salah satu faktor pendukung bagi tingkat kesejahteraan seseorang. Sedangkan tujuan koperasi adalah kesejahteraan baik bagi anggotanya dan juga masyarakat sekitar. Apabila suatu daerah memiliki jumlah unit koperasi aktif yang besar, apakah populasi di daerah tersebut juga memiliki tingkat literasi yang tinggi?</h5>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: justify; color: orange;'>Metode Studi</h4>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify; color: white;'>Seluruh variabel didapat dari sumber resmi yaitu berbagai instansi milik pemerintah Republik Indonesia. Lalu variabel-variable tersebut dikelompokkan berdasarkan tahun, kemudian dilakukan standarisasi agar perbandingan antar nilai variabel lebih setara.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify; color: white;'>Dalam studi ini, untuk literasi baca tulis, numerasi, dan sains akan digunakan tingkat kelulusan SMA di tiap provinsi sebagai indikatornya. Sedangkan untuk literasi digital akan digunakan tingkat kemampuan teknologi informasi & komputer (TIK). Dan yang terakhir, untuk literasi finansial akan digunakan indeks literasi keuangan dari Otoritas Jasa Keuangan (OJK). Untuk literasi budaya & kewargaan tidak termasuk dalam studi ini.</h5>", unsafe_allow_html=True)    
if selected == 'Analisa':
    jml_koperasi = px.bar(koperasi, x='Kode Provinsi', y='Koperasi_unit', color='Kode Provinsi', animation_frame='Tahun', animation_group="Kode Provinsi", hover_name='Provinsi', range_y=[0,30000], labels={'Koperasi_unit': 'Koperasi Aktif (unit)'})
    sma = px.bar(koperasi, x='Kode Provinsi', y='SMA_persen', color='Kode Provinsi', animation_frame='Tahun', animation_group='Kode Provinsi', hover_name='Provinsi', range_y=[0,100], labels={'SMA_persen': 'Tingkat Lulus SMA (%)'})
    tik = px.bar(koperasi, x='Kode Provinsi', y='TIK_persen', color='Kode Provinsi', animation_frame='Tahun', animation_group='Kode Provinsi', hover_name='Provinsi', range_y=[0,100], labels={'TIK_persen': 'Tingkat Keterampilan TIK (%)'})
    ilk = px.bar(koperasi, x='Kode Provinsi', y='ILK_persen', color='Kode Provinsi', animation_frame='Tahun', animation_group='Kode Provinsi', hover_name='Provinsi', range_y=[0,100], labels={'ILK_persen': 'Indeks Literasi Keuangan (%)'})
    kop_sma = px.scatter(koperasi,x='SMA_standard', y='Koperasi_standard',animation_frame='Tahun', animation_group='Kode Provinsi',size='Koperasi_unit', color='Kode Provinsi', hover_name='Provinsi', opacity=0.5, range_x=[-3,4], range_y=[-3,5], text='Kode Provinsi', labels={'SMA_standard': 'Tingkat Lulus SMA', 'Koperasi_standard': 'Koperasi Aktif'})
    kop_sma['layout']['yaxis'].update(autorange = True)
    kop_tik = px.scatter(koperasi,x='TIK_standard', y='Koperasi_standard',animation_frame='Tahun', animation_group='Kode Provinsi',size='Koperasi_unit', color='Kode Provinsi', hover_name='Provinsi', opacity=0.5, range_x=[-3,4], range_y=[-3,5], text='Kode Provinsi', labels={'TIK_standard': 'Tingkat Keterampilan TIK', 'Koperasi_standard': 'Koperasi Aktif'})
    kop_tik['layout']['yaxis'].update(autorange = True)
    kop_ilk = px.scatter(koperasi,x='ILK_standard', y='Koperasi_standard',animation_frame='Tahun', animation_group='Kode Provinsi',size='Koperasi_unit', color='Kode Provinsi', hover_name='Provinsi', opacity=0.5, range_x=[-3,4], range_y=[-3,5], text='Kode Provinsi', labels={'ILK_standard': 'Indeks Literasi Keuangan', 'Koperasi_standard': 'Koperasi Aktif'})
    kop_ilk['layout']['yaxis'].update(autorange = True)
    st.markdown("<h4 style='text-align: justify; color: orange;'>Berapa Jumlah Koperasi Aktif Tiap Provinsi Di Indonesia Pada Tahun 2016 & 2019?</h4>", unsafe_allow_html=True)
    st.plotly_chart(jml_koperasi)
    st.markdown("<ul><li><h5 style='text-align: justify; color: white;'>Jumlah unit koperasi aktif dari tahun 2016 hingga tahun 2019 cenderung menurun di tiap provinsi.</h5></li><li><h5 style='text-align: justify; color: white;'>Kenaikan terbesar ada di provinsi Papua (<font color=#ff0066><b>PA</b></font>) dari 777 unit pada tahun 2016, menjadi 2.131 unit di tahun 2019.</h5></li><li><h5 style='text-align: justify; color: white;'>Penurunan terbesar ada di provinsi Jawa tengah (<font color=#ff0066><b>JT</b></font>), dari 21.667 unit pada tahun 2016, menjadi 13.164 unit di tahun 2019.</h5></li></ul>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: justify; color: orange;'>Berapa Tingkat Lulus SMA Tiap Provinsi Di Indonesia Pada Tahun 2016 & 2019?</h4>", unsafe_allow_html=True)
    st.plotly_chart(sma)
    st.markdown("<ul><li><h5 style='text-align: justify; color: white;'>Rata-rata tingkat lulus SMA di Indonesia dari tahun 2016 hingga 2019 cenderung menurun dari 59,93% menjadi 59,07%.</h5></li><li><h5 style='text-align: justify; color: white;'>Kenaikan terbesar ada di provinsi Kalimantan Barat (<font color=#ff0066><b>KB</b></font>) dari 35,69% menjadi 49,29%, naik sebesar 13,6%.</h5></li><li><h5 style='text-align: justify; color: white;'>Penurunan terbesar ada di provinsi Sulawesi Tengah (<font color=#ff0066><b>ST</b></font>) dari 61,79% menjadi 52%, turun sebesar 9,79%.</h5></li></ul>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: justify; color: orange;'>Berapa Tingkat Keterampilan TIK Tiap Provinsi Di Indonesia Pada Tahun 2016 & 2019?</h4>", unsafe_allow_html=True)
    st.plotly_chart(tik)
    st.markdown("<ul><li><h5 style='text-align: justify; color: white;'>Rata-rata tingkat keterampilan TIK di Indonesia dari tahun 2016 hingga 2019 terus meningkat dari 30,65% menjadi 54,35%.</h5></li><li><h5 style='text-align: justify; color: white;'>Kenaikan terbesar ada di provinsi Jawa Barat (<font color=#ff0066><b>JB</b></font>) dari 34,84% menjadi 65,37%, naik sebesar 30,53%.</h5></li></ul>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: justify; color: orange;'>Berapa Indeks Literasi Keuangan Tiap Provinsi Di Indonesia Pada Tahun 2016 & 2019?</h4>", unsafe_allow_html=True)
    st.plotly_chart(ilk)
    st.markdown("<ul><li><h5 style='text-align: justify; color: white;'>Rata-rata indeks literasi keuangan di Indonesia cenderung meningkat dari 29,24% menjadi 38,34% pada tahun 2019.</h5></li><li><h5 style='text-align: justify; color: white;'>Kenaikan terbesar ada di provinsi DI Yogyakarta (<font color=#ff0066><b>YO</b></font>) dari 38,5% menjadi 58,53%, naik sebesar 20,03%.</h5></li><li><h5 style='text-align: justify; color: white;'>Penurunan terbesar ada di provinsi Nusa Tenggara Timur (<font color=#ff0066><b>NT</b></font>) dari 28% menjadi 27,2%, turun sebesar 0,18%.</h5></li></ul>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: justify; color: orange;'>Bagaimana Hubungan Jumlah Koperasi Aktif Dengan Tingkat Pendidikan Tiap Provinsi Di Indonesia Pada Tahun 2016 & 2019?</h4>", unsafe_allow_html=True)
    st.plotly_chart(kop_sma)
    st.markdown("<ul><li><h5 style='text-align: justify; color: white;'><font color=#ff0066><b>YO</b></font> & DKI Jakarta (<font color=#ff0066><b>JK</b></font>) masih memiliki tingkat lulus sma yang tinggi dari tahun 2016 hingga 2019, meskipun jumlah koperasi aktif <font color=#ff0066><b>JK</b></font> menurun selama periode tersebut.</h5></li><li><h5 style='text-align: justify; color: white;'><font color=#ff0066><b>PA</b></font> memiliki performa terburuk selama periode tersebut, sementara <font color=#ff0066><b>KB</b></font> yang tadinya di tahun 2016 sempat 1 posisi dengan <font color=#ff0066><b>PA</b></font> merangkak naik di tahun 2019 mendekati rata-rata nasional.</h5></li><li><h5 style='text-align: justify; color: white;'>Sedangkan Jawa Timur (<font color=#ff0066><b>JI</b></font>), meskipun jumlah koperasi aktifnya terbanyak, namun tingkat lulus SMA masih berada di bawah rata-rata nasional selama periode tersebut.</h5></li></ul>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: justify; color: orange;'>Bagaimana Hubungan Jumlah Koperasi Aktif Dengan Tingkat Keterampilan TIK Tiap Provinsi Di Indonesia Pada Tahun 2016 & 2019?</h4>", unsafe_allow_html=True)
    st.plotly_chart(kop_tik)
    st.markdown("<ul><li><h5 style='text-align: justify; color: white;'><font color=#ff0066><b>JK</b></font> pada tahun 2016 memiliki performa keterampilan TIK tertinggi, namun di 2019, tersusul oleh performa Gorontalo (<font color=#ff0066><b>GO<b></font>) meskipun jumlah unit koperasi <font color=#ff0066><b>GO</b></font> di bawah rata-rata nasional.</h5></li><li><h5 style='text-align: justify; color: white;'><font color=#ff0066><b>JI</b></font> dan <font color=#ff0066><b>JT</b></font> yang tadinya memiliki performa TIK di bawah rata-rata, akhirnya berhasil naik di atas rata-rata pada tahun 2019.</h5></li><li><h5 style='text-align: justify; color: white;'>Sebaliknya untuk <font color=#ff0066><b>JB</b></font> yang tadinya di atas rata-rata, pada tahun 2019 performa nilainya menjadi di bawah rata-rata.</h5></li></ul>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: justify; color: orange;'>Bagaimana Hubungan Jumlah Koperasi Aktif Dengan Indeks Literasi Keuangan Tiap Provinsi Di Indonesia Pada Tahun 2016 & 2019?</h4>", unsafe_allow_html=True)
    st.plotly_chart(kop_ilk)
    st.markdown("<ul><li><h5 style='text-align: justify; color: white;'>Performa indeks literasi keuangan Provinsi Kepulauan Riau (<font color=#ff0066><b>KR</b></font>), Banten (<font color=#ff0066><b>BT<b></font>), dan Bali (<font color=#ff0066><b>BA</b></font>) pada tahun 2016 hampir setara dengan <font color=#ff0066><b>YO</b></font> dan <font color=#ff0066><b>JK</b></font>, namun di tahun 2019 menurun kembali ke nilai dekat rata-rata nasional.</h5></li><li><h5 style='text-align: justify; color: white;'>Lagi-lagi untuk <font color=#ff0066><b>JB</b></font> yang tadinya di atas rata-rata di tahun 2016, performa nilainya menjadi di bawah rata-rata pada tahun 2019.</h5></li></ul>", unsafe_allow_html=True)
if selected == 'Kesimpulan':
    st.markdown("<h4 style='text-align: justify; color: orange;'>Tabel Korelasi Antara Koperasi Aktif & Berbagai Indikator Literasi</h4>", unsafe_allow_html=True)
    st.table(tabel)
    st.markdown("<h5 style='text-align: justify; color: white;'>Tidak ada korelasi antara jumlah unit koperasi aktif dengan berbagai indikator literasi pada tiap provinsi di Indonesia.</h5>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: justify; color: orange;'>Apa Yang Bisa Kita Lakukan Berikutnya?</h4>", unsafe_allow_html=True)
    st.markdown("<ul><li><h5 style='text-align: justify; color: white;'>Mengadakan studi lebih lanjut dengan data yang terbaru. Misalnya, OJK baru saja mengeluarkan data indeks literasi keuangan tahun 2022.</h5></li><li><h5 style='text-align: justify; color: white;'>Perlunya penelitian lebih lanjut dengan survey khusus bagi para anggota, pengurus, dan pengawas koperasi tiap daerah dalam hal literasi dan kegiatan apa yang telah koperasi tersebut lakukan untuk menunjang indikator-indikator literasi terkait pemenuhan tugasnya untuk mensejahterakan anggota dan masyarakat sekitarnya.</h5></li></ul>", unsafe_allow_html=True)
if selected == 'Sumber Data':
    st.markdown("<h4 style='text-align: justify; color: orange;'>Badan Pusat Statistik Republik Indonesia</h4>", unsafe_allow_html=True)
    st.markdown("<ul><li><h5 style='text-align: justify; color: white;'><a href='https://www.bps.go.id/indicator/28/1447/1/proporsi-remaja-dan-dewasa-usia-15-59-tahun-dengan-keterampilan-teknologi-informasi-dan-komputer-tik-menurut-provinsi.html'>Proporsi Remaja Dan Dewasa Usia 15-59 Tahun Dengan Keterampilan Teknologi Informasi Dan Komputer (TIK) Menurut Provinsi (Persen)</a></h5></li><li><h5 style='text-align: justify; color: white;'><a href='https://www.bps.go.id/indicator/28/1980/1/tingkat-penyelesaian-pendidikan-menurut-jenjang-pendidikan-dan-provinsi.html'>Tingkat Penyelesaian Pendidikan Menurut Jenjang Pendidikan dan Provinsi</a></h5></li></ul>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: justify; color: orange;'>Otoritas Jasa Keuangan Republik Indonesia</h4>", unsafe_allow_html=True)
    st.markdown("<ul><li><h5 style='text-align: justify; color: white;'><a href='https://www.ojk.go.id/id/berita-dan-kegiatan/siaran-pers/Documents/Pages/Siaran-Pers-OJK-Indeks-Literasi-dan-Inklusi-Keuangan-Meningkat/17.01.23%20Tayangan%20%20Presscon%20%20nett.compressed.pdf'>Survey Nasional Literasi dan Inklusi Keuangan Tahun 2016</a></h5></li><li><h5 style='text-align: justify; color: white;'><a href='https://www.ojk.go.id/id/berita-dan-kegiatan/publikasi/Documents/Pages/Survei-Nasional-Literasi-dan-Inklusi-Keuangan-2019/BOOKLET%20Survei%20Nasional%20Literasi%20dan%20Inklusi%20Keuangan%202019.pdf'>Survey Nasional Literasi dan Inklusi Keuangan Tahun 2019</a></h5></li></ul>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: justify; color: orange;'>Kementrian Koperasi dan UKM Republik Indonesia</h4>", unsafe_allow_html=True)
    st.markdown("<ul><li><h5 style='text-align: justify; color: white;'><a href='https://kemenkopukm.go.id/uploads/laporan/1566783223_Data%20Koperasi%20Tahun%202016.pdf'>Data Koperasi Tahun 2016</a></h5></li><li><h5 style='text-align: justify; color: white;'><a href='https://kemenkopukm.go.id/uploads/laporan/1580298872_Data%20Koperasi%2031%20Desember%202019-1.pdf'>Data Koperasi Tahun 2019</a></h5></li></ul>", unsafe_allow_html=True)
if selected == 'Lainnya':
    st.markdown("<h4 style='text-align: justify; color: orange;'>Tentang Situs Web Ini</h4>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify; color: white;'>Dibuat sebagai salah satu prasyarat kelulusan dari program beasiswa Digitalent Kominfo Data Analyst yang difasilitasi oleh DQLab.</h5>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: justify; color: orange;'>Tentang Saya</h4>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify; color: white;'>Halo! Saya Denis Setiawan, dan sudah berkarir lebih dari 8 tahun di berbagai bidang IT. Mari terhubung via <a href='https://www.linkedin.com/in/denissetiawan/'>LinkedIn</a>. Salam dan terima kasih sudah berkunjung! :)</h5>", unsafe_allow_html=True)
