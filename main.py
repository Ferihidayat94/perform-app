import streamlit as st
import pandas as pd
from datetime import datetime

# Page Config
st.set_page_config(page_title="First Line Maintenance", layout="wide")

# Responsive Styling
st.markdown(
    """
    <style>
    @media screen and (max-width: 768px) {
        .block-container {
            padding: 1rem;
        }
        h1 {
            font-size: 1.5rem;
        }
        .stDataFrame {
            overflow-x: auto;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo and Title

st.image("logo.png", width=200)

st.markdown(
    """
    <h1 style='text-align: center; font-family: "Orbitron", sans-serif; color: #4CAF50;'>
    First Line Maintenance Produksi A
    </h1>
    <hr style='border: 1px solid #4CAF50;'>
    """,
    unsafe_allow_html=True
)

# Input Form
st.markdown("### Input Data Maintenance")

col1, col2 = st.columns(2)

with st.form("monitoring_form"):
    with col1:
        tanggal = st.date_input("Tanggal", datetime.today())
        area = st.selectbox("Area", ["Boiler", "Turbine", "CHCB", "WTP"])
        nomor_sr = st.text_input("Nomor SR")
    
    with col2:
        nama_pelaksana = st.selectbox("Nama Pelaksana", [
            "Winner PT Daspin Sitanggang", "Devri Candra Kardios", "Rendy Eka Priansyah", "Selamat", 
            "M Yanuardi", "Hendra", "Gilang", "Kamil", "M Soleh Alqodri", "M Soleh", "Debby", 
            "Dandi", "Aminudin", "Hasan", "Budi", "Sarmidun", "Reno", "Rafi", "Akbar", 
            "Sunir", "Eka", "Hanafi", "Diki"
        ])
        evidance = st.file_uploader("Upload Evidance")
    
    keterangan = st.text_area("Keterangan")
    submit_button = st.form_submit_button("Submit", help="Klik untuk menyimpan data")

# Data Storage
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Tanggal", "Area", "Keterangan", "Nomor SR", "Evidance", "Nama Pelaksana"])

# Add new data
if submit_button:
    new_data = pd.DataFrame({
        "Tanggal": [tanggal],
        "Area": [area],
        "Keterangan": [keterangan],
        "Nomor SR": [nomor_sr],
        "Evidance": [evidance.name if evidance else ""],
        "Nama Pelaksana": [nama_pelaksana]
    })
    st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
    st.success("Data berhasil disimpan!")

# Show data
st.markdown("### Data Monitoring")
st.dataframe(st.session_state.data, height=400)

# Export to CSV
st.markdown("### Export Data")
csv = st.session_state.data.to_csv(index=False)
st.download_button("Download Data CSV", data=csv, file_name="monitoring_kinerja.csv", mime="text/csv")

st.info("untuk visualisasi real-time.")

# Footer
st.markdown(
    """
    <hr>
    <p style='text-align: center;'>
    Dibuat oleh Tim Operasi - PLTU Bangka 🛠️
    </p>
    """,
    unsafe_allow_html=True
)
