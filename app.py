import streamlit as st

st.title("Aksara Jawa OCR")
st.write("Selamat datang di aplikasi OCR Aksara Jawa!")

uploaded_file = st.file_uploader("Upload gambar berisi aksara Jawa", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Gambar yang diunggah", use_column_width=True)
    st.write("OCR processing akan segera hadir!")
