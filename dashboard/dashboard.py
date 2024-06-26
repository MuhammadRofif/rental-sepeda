import pandas as pd                #Mengimport modul
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

                                                    #MENYIAPKAN DATA FRAME
# helper function adalah fungsi yang dibuat untuk membantu atau menyelesaikan tugas tertentu dalam sebuah program atau aplikasi yang lebih besar.
def weekday_df(df): #Mengelompokkan data
    avg_weekday = df.groupby('weekday')['cnt'].mean().reset_index()
    return avg_weekday

def holiday_df(df):#Mengelompokkan data
    avg_holiday = df.groupby('holiday')['cnt'].mean().reset_index().sort_values("cnt")
    return avg_holiday

all_df = pd.read_csv("https://raw.githubusercontent.com/MuhammadRofif/rental-sepeda/main/dashboard/all_data.csv") #Memuat berkas yang csv

with st.sidebar:
    # Menambahkan logo perusahaan
    
    st.write("""# Proyek Analisis Data: [Bike Sharing Dataset]
- **Nama:** [Muhammad Rofiif Taqiyyuddin Nabiil]
- **Email:** [muhammad.rofif369@gmail.com]
- **ID Dicoding:** [rofifdk]""")
    st.write("Penyewaan Sepeda")
    st.image("https://media.istockphoto.com/id/1152337759/id/vektor/logo-untuk-penyewaan-sepeda-ilustrasi-vektor-pada-latar-belakang-putih.jpg?s=170667a&w=0&k=20&c=EDH6cNhLFbE0EvRDaX5KqCzYvNifMt71zdPF9X6crgk=")

#memanggi beberapa fungsi atau helper function
avg_weekday = weekday_df(all_df)
avg_holiday = holiday_df(all_df)

                    #MELENGKAPI DASHBOARD DENGAN BERBAGAI VISUALISASI DATA
st.title('Rental Sepeda Semoga Berkah :sparkles:')
st.write("- Berapa Rata-rata Jumlah Penyewaan Sepeda per Hari Kerja dalam Seminggu?")
st.write("- Bagaimana Penggunaan Penyewaan Sepeda Berdasarkan Hari Kerja dan Hari Libur?")

st.subheader('Weekday')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(avg_weekday['weekday'], avg_weekday['cnt'], linestyle='-', marker='o', color='b')
ax.set_title('Rata-rata Jumlah Penyewaan Sepeda per Hari Kerja dalam Seminggu')
ax.set_xlabel('Hari dalam Seminggu')
ax.set_ylabel('Rata-rata Jumlah Penyewaan Sepeda (cnt)')
ax.grid(True)
ax.set_xticks(avg_weekday['weekday'])
ax.set_xticklabels(['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'])
st.pyplot(fig)
with st.expander("Kesimpulan"):
    st.write("Penyewaan sepeda dalam seminggu lebih tinggi pada hari Kamis dan Jumat, sedangkan penyewaan terendah pada hari minggu. Berdasarkan data ini maka pemilik bisa untuk mengatur strategi pemasaran dan penawaran layanan rental sepeda lebih efektif, seperti memberikan promosi khusus atau paket-paket yang menarik pada hari-hari dengan jumlah penyewaan sepeda tinggi")


st.subheader('Holiday')
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='holiday', y='cnt', data=avg_holiday, palette='Set1', ax=ax)
ax.set_title('Penyewaan Sepeda pada Hari Libur')
ax.set_xlabel('Hari Libur atau tidak')
ax.set_ylabel('Jumlah Rata-Rata Penyewaan')
ax.set_xticklabels(['Not Holiday', 'Holiday'])
st.pyplot(fig)
with st.expander("Kesimpulan"):
    st.write("Penyewaan sepeda lebih tinggi pada hari kerja dibandingkan hari libur. Berdasarkan data maka pemilik bisa untuk meningkatkan omset seperti menyediakan fasilitas tambahan seperti paket sewa dengan sarapan untuk mendorong pelanggan untuk berlangganan secara teratur.")
# Tampilkan plot di Streamlit

st.caption('Copyright (c) rofifdk 2024')
