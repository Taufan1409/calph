import streamlit as st
from streamlit_option_menu import option_menu
import math

# Coba hapus menu_icon dulu
selected2 = option_menu(None, ["Asam", "Basa"], 
                        default_index=0, orientation="horizontal",
                        styles={
                            "nav-link": {"font-size": "15px", "text-align": "center"},
                            "nav-link-selected": {"background-color": "blue"},
                        })

# Cek apakah streamlit_option_menu terinstall
try:
    from streamlit_option_menu import option_menu
except ImportError:
    st.error("Package 'streamlit-option-menu' belum terinstall.\n"
             "Silakan jalankan perintah ini di terminal:\n"
             "`pip install streamlit-option-menu`")
    st.stop()

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

# Sidebar Navigasi utama
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
    st.title("Kalkulator pH Larutan")
    st.subheader("Menghitung pH Larutan Asam dan Basa")

    # Submenu utama untuk tipe larutan asam atau basa
    selected2 = option_menu(None, ["Asam", "Basa"], 
                            menu_icon="cast", default_index=0, orientation="horizontal",
                            styles={
                                "nav-link": {"font-size": "15px", "text-align": "center"},
                                "nav-link-selected": {"background-color": "blue"},
                            })

    if selected2 == "Asam":
        # Submenu jenis asam
        selected_asam = option_menu(None, ["Asam Kuat", "Asam Lemah", "Custom"], 
                                menu_icon="cast", default_index=0, orientation="horizontal",
                                styles={
                                    "nav-link": {"font-size": "15px", "text-align": "center"},
                                    "nav-link-selected": {"background-color": "blue"},
                                })

        if selected_asam == "Asam Kuat":
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
            st.write("Valensi (a) =", a)

            konsentrasi = st.number_input("Masukkan konsentrasi (M)", format="%.4f", step=0.0001)
            st.write("Konsentrasi =", konsentrasi)

            if st.button("Hitung pH asam kuat (Asam Kuat)"):
                if konsentrasi > 0:
                    H_plus, pH = perhitungan_pH_asam_kuat(konsentrasi, a)
                    st.write("[H+] =", round(H_plus, 4))
                    st.write("pH =", round(pH, 2))
                    st.success(f'pH asam adalah {pH:.2f}')
                else:
                    st.error("Konsentrasi harus lebih besar dari 0!")

        elif selected_asam == "Asam Lemah":
            konstanta_asam = st.number_input("Masukkan Ka (konstanta asam)", format="%.6e", step=0.0001)
            st.write("Ka =", konstanta_asam)

            konsentrasi = st.number_input("Masukkan konsentrasi (M)", format="%.4f", step=0.0001)
            st.write("Konsentrasi =", konsentrasi)

            if st.button("Hitung pH asam lemah"):
                if konstanta_asam > 0 and konsentrasi > 0:
                    H_plus, pH = perhitungan_pH_asam_lemah(konstanta_asam, konsentrasi)
                    st.write("[H+] =", round(H_plus, 4))
                    st.write("pH =", round(pH, 2))
                    st.success(f'pH asam adalah {pH:.2f}')
                else:
                    st.error("Ka dan konsentrasi harus lebih besar dari 0!")

        elif selected_asam == "Custom":
            konsentrasi = st.number_input("Masukkan konsentrasi asam (M)", format="%.4f", step=0.0001)
            a = st.number_input("Masukkan valensi (a)", min_value=1, step=1)
            st.write("Valensi (a) =", a)

            if st.button("Hitung pH custom asam kuat"):
                if konsentrasi > 0 and a > 0:
                    H_plus, pH = perhitungan_pH_asam_kuat(konsentrasi, a)
                    st.write("[H+] =", round(H_plus, 4))
                    st.write("pH =", round(pH, 2))
                    st.success(f'pH asam adalah {pH:.2f}')
                else:
                    st.error("Konsentrasi dan valensi harus lebih besar dari 0!")

    elif selected2 == "Basa":
        selected_basa = option_menu(None, ["Basa Kuat", "Basa Lemah", "Custom"], 
                                menu_icon="cast", default_index=0, orientation="horizontal",
                                styles={
                                    "nav-link": {"font-size": "15px", "text-align": "center"},
                                    "nav-link-selected": {"background-color": "blue"},
                                })

        if selected_basa == "Basa Kuat":
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
            selected_basa_kuat = st.selectbox("Pilih senyawa basa kuat", list(basa_kuat.keys()))
            a = basa_kuat[selected_basa_kuat]
            st.write("Valensi (a) =", a)

            konsentrasi = st.number_input("Masukkan konsentrasi (M)", format="%.4f", step=0.0001)
            st.write("Konsentrasi =", konsentrasi)

            if st.button("Hitung pH basa kuat (Basa Kuat)"):
                if konsentrasi > 0:
                    OH_minus, pOH, pH = perhitungan_pH_basa_kuat(konsentrasi, a)
                    st.write("[OH-] =", round(OH_minus, 4))
                    st.write("pOH =", round(pOH, 2))
                    st.write("pH =", round(pH, 2))
                    st.success(f'pH basa adalah {pH:.2f}')
                else:
                    st.error("Konsentrasi harus lebih besar dari 0!")

        elif selected_basa == "Basa Lemah":
            konstanta_basa = st.number_input("Masukkan Kb (konstanta basa)", format="%.6e", step=0.0001)
            st.write("Kb =", konstanta_basa)

            konsentrasi = st.number_input("Masukkan konsentrasi (M)", format="%.4f", step=0.0001)
            st.write("Konsentrasi =", konsentrasi)

            if st.button("Hitung pH basa lemah"):
                if konstanta_basa > 0 and konsentrasi > 0:
                    OH_minus, pOH, pH = perhitungan_pH_basa_lemah(konstanta_basa, konsentrasi)
                    st.write("[OH-] =", round(OH_minus, 4))
                    st.write("pOH =", round(pOH, 2))
                    st.write("pH =", round(pH, 2))
                    st.success(f'pH basa adalah {pH:.2f}')
                else:
                    st.error("Kb dan konsentrasi harus lebih besar dari 0!")

        elif selected_basa == "Custom":
            konsentrasi = st.number_input("Masukkan konsentrasi basa (M)", format="%.4f", step=0.0001)
            a = st.number_input("Masukkan valensi (a)", min_value=1, step=1)
            st.write("Valensi (a) =", a)

            if st.button("Hitung pH custom basa kuat"):
                if konsentrasi > 0 and a > 0:
                    OH_minus, pOH, pH = perhitungan_pH_basa_kuat(konsentrasi, a)
                    st.write("[OH-] =", round(OH_minus, 4))
                    st.write("pOH =", round(pOH, 2))
                    st.write("pH =", round(pH, 2))
                    st.success(f'pH basa adalah {pH:.2f}')
                else:
                    st.error("Konsentrasi dan valensi harus lebih besar dari 0!")

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
