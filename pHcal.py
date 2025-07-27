import streamlit as st
import math

# Konfigurasi halaman
st.set_page_config(page_title="Smart Kalkulator pH", layout="centered")

# Fungsi untuk menghitung pH asam kuat

def perhitungan_pH_asam_kuat(konsentrasi, a):
    H_plus = konsentrasi * a
    pH = -math.log10(H_plus)
    return H_plus, pH

# Fungsi untuk menghitung pH basa kuat

def perhitungan_pH_basa_kuat(konsentrasi, a):
    OH_minus = konsentrasi * a
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH

# Fungsi untuk menghitung pH asam lemah

def perhitungan_pH_asam_lemah(konstanta_asam, konsentrasi):
    H_plus = math.sqrt(konstanta_asam * konsentrasi)
    pH = -math.log10(H_plus)
    return H_plus, pH
    
# Fungsi untuk menghitung pH basa lemah

def perhitungan_pH_basa_lemah(konstanta_basa, konsentrasi):
    OH_minus = math.sqrt(konstanta_basa * konsentrasi)
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH

# Tema warna biru dengan font putih dan navigasi hitam
st.markdown("""
    <style>
    /* Ubah warna latar belakang utama */
    body, .stApp {
        background-color: #537895;
        color: white;
    }

    /* Ubah semua teks termasuk heading dan input */
    h1, h2, h3, h4, h5, h6, p, label, .stTextInput, .stSelectbox, .stNumberInput, .stMarkdown, .stButton, .stRadio > div {
        color: white !important;
    }

    /* Styling tombol */
    .stButton > button {
        background-color: #1e3a8a;
        color: white;
        border-radius: 8px;
    }

    /* Styling khusus sidebar */
    .stSidebar {
        background-color: black !important;
    }

    /* Warna font pada radio (navigasi sidebar) */
    section[data-testid="stSidebar"] .stRadio label {
        color: black !important;
    }

    /* Optional: Ubah warna teks judul sidebar jika ada */
    section[data-testid="stSidebar"] .css-1cypcdb {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)


# Sidebar Navigasi
menu = st.sidebar.radio("Navigasi", ["Beranda", "Hitung pH", "Tentang Aplikasi"])

if menu == "Beranda":
    st.title("Selamat Datang di Smart Kalkulator pH")

    # Menampilkan gambar dengan ukuran custom (HTML)
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://cdn.pixabay.com/photo/2013/07/13/13/48/chemistry-161575_640.png" 
                 alt="Ilustrasi Kimia" 
                 width="250">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Informasi pembuat
    st.markdown("""
    ### Dibuat Oleh:
    - Amar Evan Gading (2460321)
    - Diandra Namira Zahfa (2460360)
    - Lutfhia Salwani Fatonah (2460410)
    - Nevi Sahara (2460471)
    - Taufan Aliafi (2460525)
    """)
    
    st.markdown("""
    ### Teori Asam Basa
    📖 Teori Arrhenius
    - Asam adalah zat yang dapat melepaskan ion H+ dalam larutan air.
    - Basa adalah zat yang dapat melepaskan ion OH- dalam larutan air.

    📖Teori Bronsted-Lowry
    - Asam adalah zat yang dapat melepaskan proton (H+).
    - Basa adalah zat yang dapat menerima proton (H+).

    📖 Teori Lewis
    - Asam adalah zat yang dapat menerima pasangan elektron.
    - Basa adalah zat yang dapat memberikan pasangan elektron.
    """)


elif menu == "Hitung pH":
     st.title(":blue[Kalkulator pH Larutan]")
     st.subheader("Menghitung [H+] dan pH dari Konsentrasi Asam Kuat dan Asam Lemah")
    
     selected2 = option_menu(None, ["Asam Kuat", "Asam Lemah", "Custom"], 
    menu_icon = "cast", default_index=0, orientation="horizontal",
    styles ={
        "nav-link": {"font-size": "15px", "text-align": "center"},
        "nav-link-selected": {"background-color": "blue"},})

     if selected2 == "Asam Kuat":
        # Pilih senyawa asam kuat
        asam_kuat = {
            "Asam Klorida (HCl)": 1,
            "Asam Nitrat (HNO3)": 1,
            "Asam Sulfat (H2SO4)": 2,            
            "Asam Bromida (HBr)": 1,
            "Asam Bromit (HBrO3)": 1,
            "Asam Perbromat (HBrO4)": 1,
            "Asam Klorat (HClO3)": 1,             
            "Asam Perklorat (HClO4)": 1,
            "Asam Iodida (HI)": 1,
            "Asam Iodit (HIO3)": 1,
            "Asam Periodat (HIO4)": 1,
        }
            
        selected_asam_kuat = st.selectbox("Pilih senyawa asam kuat", list(asam_kuat.keys()))
        a = asam_kuat[selected_asam_kuat]
        st.write("a = ", a)
            
        # Masukkan konsentrasi
        konsentrasi = st.number_input("Masukkan konsentrasi (M)", format = "%.4f", step=0.0001, key = "H1")
        st.write("Konsentrasi = ", konsentrasi)
            
        # Tombol hitung
        if st.button("Hitung pH", key = "T1"):
            H_plus, pH = perhitungan_pH_asam_kuat(konsentrasi, a)
            st.write("[H+] =", round(H_plus, 4))
            st.write("pH =", round(pH, 2))            
            st.success(f'pH asam adalah {pH:.2f}')

        
     elif selected2 == "Asam Lemah":
        # Masukkan Ka
        konstanta_asam = st.number_input("Masukkan Ka", key = "K2")
        st.write("Ka = ", konstanta_asam)

        # Masukkan konsentrasi
        konsentrasi = st.number_input("Masukkan konsentrasi (M)", format = "%.4f", step=0.0001, key = "H2")
        st.write("Konsentrasi = ", konsentrasi )
            
        # Tombol hitung
        if st.button ("Hitung pH", key = "T2"):
            H_plus, pH = perhitungan_pH_asam_lemah(konsentrasi, konstanta_asam)
            st.write("[H+] =", round(H_plus, 4))
            st.write("pH =", round(pH, 2))
            st.success(f'pH asam adalah {pH:.2f}')


     elif selected2 == "Custom":
        st.subheader("Asam Kuat")
        # Masukkan konsentrasi
        konsentrasi = st.number_input("Masukkan konsentrasi (M)", format = "%.4f", step=0.0001, key = "H3")
        st.write("Konsentrasi = ", konsentrasi)

        # Masukkan valensi
        a = st.number_input("Masukkan valensi (a)", format = "%i", step=1, key = "A3")
        st.write("a = ", a)
                
        # Tombol hitung
        if st.button("Hitung pH", key = "B3"):
            H_plus, pH = perhitungan_pH_asam_kuat(konsentrasi, a)
            st.write("[H+] =", round(H_plus, 4))
            st.write("pH =", round(pH, 2))            
            st.success(f'pH asam adalah {pH:.2f}')


     elif selected == "Konsentrasi Basa":
      st.title(":blue[Kalkulator pH Larutan]")
     st.subheader("Menghitung [OH-], pOH, dan pH dari Konsentrasi Basa Kuat dan Basa Lemah")

     selected3 = option_menu(None, ["Basa Kuat", "Basa Lemah", "Custom"], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "nav-link": {"font-size": "15px", "text-align": "center"},
        "nav-link-selected": {"background-color": "blue"}})

if selected3 == "Basa Kuat":
        # Pilih senyawa basa kuat
        basa_kuat = {
            "Natrium Hidroksida (NaOH)": 1,
            "Litium Hidroksida (LiOH)": 1,
            "Kalium Hidroksida (KOH)": 1,
            "Rubidium Hidroksida (RbOH)": 1,
            "Cesium Hidroksida (CsOH)": 1,
            "Kalsium Hidroksida (Ca(OH)2)": 2,
            "Barium Hidroksida (Ba(OH)2)": 2,
            "Stronsium Hidroksida (Sr(OH)2)": 2,
            "Magnesium Hidroksida (Mg(OH)2)": 2
        }
    
        selected_basa_kuat = st.selectbox(
            "Pilih senyawa basa kuat", list(basa_kuat.keys()))
        a = basa_kuat[selected_basa_kuat]
        st.write("a = ", a)
    
        # Masukkan konsentrasi
        konsentrasi = st.number_input(
            "Masukkan konsentrasi (M)", format= "%.4f", step=0.0001, key = "H5")
        st.write("Konsentrasi = ", konsentrasi)
    
        # Tombol hitung
        if st.button("Hitung pH", key = "T5"):
            OH_minus, pOH, pH = perhitungan_pH_basa_kuat(konsentrasi, a)
            st.write("[OH-] =", round(OH_minus, 4))
            st.write("pOH =", round(pOH, 2))
            st.write("pH =", round(pH, 2))
            st.success(f'pH basa adalah {pH:.2f}')

        elif selected3 == "Basa Lemah":
        # Masukkan Kb
         konstanta_basa = st.number_input("Masukkan Kb", key = "K6")
        st.write("Kb = ", konstanta_basa)
    
        # Masukkan konsentrasi
        konsentrasi = st.number_input("Masukkan konsentrasi (M)", format = "%.4f", step=0.0001, key = "H6")
        st.write("Konsentrasi = ", konsentrasi)
        
        # Tombol hitung
        if st.button("Hitung pH", key = "T6"):
            OH_minus, pOH, pH = perhitungan_pH_basa_lemah(konsentrasi, konstanta_basa)
            st.write("[OH-] =", round(OH_minus, 4))
            st.write("pOH =", round(pOH, 2))
            st.write("pH =", round(pH, 2))
            st.success(f'pH basa adalah {pH:.2f}')
            
        elif selected3 == "Custom":
         st.subheader("Basa Kuat")
        
        # Masukkan konsentrasi
        konsentrasi = st.number_input("Masukkan konsentrasi (M)", format = "%.4f", step=0.0001, key = "H7")
        st.write("Konsentrasi = ", konsentrasi)
    
        # Masukkan valensi
        a = st.number_input("Masukkan valensi (a)", format = "%i", step=1, key = "A7")
        st.write("a = ", a)
                
        # Tombol hitung
        if st.button("Hitung pH", key = "B7"):
            OH_minus, pOH, pH = perhitungan_pH_basa_kuat(konsentrasi, a)
            st.write("[OH-] =", round(OH_minus, 4))
            st.write("pOH =", round(pOH, 2))
            st.write("pH =", round(pH, 2))
            st.success(f'pH basa adalah {pH:.2f}')

        elif menu == "Tentang Aplikasi":
         st.header("📘 Tentang Aplikasi")

         st.markdown("""
    ### 1. Apa itu pH?
    pH adalah ukuran konsentrasi ion hidrogen (H⁺) dalam larutan. 
    Skala pH berkisar dari 0 sampai 14:
    - pH < 7 : larutan bersifat asam
    - pH = 7 : larutan netral
    - pH > 7 : larutan bersifat basa
    """)

        st.markdown("""            
    ### 2. Rumus pH yang Digunakan:
    - Asam Kuat : pH = -log[H⁺]
    - Basa Kuat : pH = 14 - (-log[OH⁻])
    - Asam Lemah: pH = -log(√(Ka * [HA]))
    - Basa Lemah: pH = 14 - log(√(Kb * [B]))
    """)

        st.markdown("""            
    ### 3. Contoh Soal:
    Hitung pH dari larutan HCl 0.01 M (Asam Kuat)
    - Rumus: pH = -log [H⁺] = -log(0.01) = 2.00
    Hitung pH dari NH₃ 0.1 M, Kb = 1.8 * 10⁻⁵ (Basa Lemah)
    - [OH⁻] = √(Kb * [B]) = √(1.8e-5 * 0.1) ≈ 1.34*10⁻³
    - pOH = -log(1.34e-3) ≈ 2.87
    - pH = 14 - 2.87 = 11.13
    """)








