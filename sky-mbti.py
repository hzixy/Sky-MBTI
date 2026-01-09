import streamlit as st
from PIL import Image
import io
import os
import tempfile
import requests
from moviepy.editor import VideoFileClip

# --- Konfigurasi Halaman ---
st.set_page_config(page_title="MediaToolbox Pro", layout="centered", page_icon="🛠️")

st.title("🛠️ MediaToolbox Pro")
st.markdown("Aplikasi All-in-One untuk Konversi, Kompresi, dan Upload Media.")

# --- Sidebar Navigasi ---
menu = ["Konverter Gambar", "Kompresor Media", "Buat Link (Upload)"]
choice = st.sidebar.selectbox("Pilih Fitur", menu)

# --- FUNGSI BANTUAN ---

def get_size_format(b, factor=1024, suffix="B"):
    """Mengubah byte menjadi format yang mudah dibaca"""
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"

# --- FITUR 1: KONVERTER GAMBAR ---
if choice == "Konverter Gambar":
    st.header("🖼️ Konverter Format Gambar")
    st.info("Mendukung JPG, PNG, WEBP, GIF (Statis)")

    uploaded_file = st.file_uploader("Upload Gambar", type=["jpg", "jpeg", "png", "webp"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gambar Asli", use_column_width=True)
        
        # Pilihan Format Output
        format_type = st.selectbox("Pilih Format Tujuan", ["PNG", "JPEG", "WEBP", "GIF"])
        
        if st.button("Konversi Sekarang"):
            try:
                buf = io.BytesIO()
                # Konversi mode warna jika perlu (JPEG tidak mendukung transparansi/RGBA)
                if format_type == "JPEG" and image.mode in ("RGBA", "P"):
                    image = image.convert("RGB")
                
                image.save(buf, format=format_type)
                byte_im = buf.getvalue()

                st.success(f"Berhasil dikonversi ke {format_type}!")
                
                st.download_button(
                    label="⬇️ Download Gambar",
                    data=byte_im,
                    file_name=f"converted_image.{format_type.lower()}",
                    mime=f"image/{format_type.lower()}"
                )
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")

# --- FITUR 2: KOMPRESOR MEDIA ---
elif choice == "Kompresor Media":
    st.header("🗜️ Kompresor Gambar & Video")
    
    media_type = st.radio("Tipe Media", ["Gambar", "Video/GIF"])

    if media_type == "Gambar":
        uploaded_file = st.file_uploader("Upload Gambar untuk Dikompres", type=["jpg", "png", "jpeg"])
        if uploaded_file:
            image = Image.open(uploaded_file)
            original_size = len(uploaded_file.getvalue())
            st.text(f"Ukuran Asli: {get_size_format(original_size)}")

            quality_val = st.slider("Kualitas Kompresi (1-100)", 10, 95, 60)
            
            if st.button("Kompres Gambar"):
                buf = io.BytesIO()
                # Pastikan mode RGB untuk JPEG
                if image.mode in ("RGBA", "P"):
                    image = image.convert("RGB")
                
                image.save(buf, format="JPEG", quality=quality_val, optimize=True)
                byte_im = buf.getvalue()
                
                compressed_size = len(byte_im)
                st.write(f"Ukuran Setelah Kompresi: **{get_size_format(compressed_size)}**")
                st.write(f"Penghematan: {((original_size-compressed_size)/original_size)*100:.1f}%")
                
                st.download_button(
                    label="⬇️ Download Hasil Kompresi",
                    data=byte_im,
                    file_name="compressed_image.jpg",
                    mime="image/jpeg"
                )

    elif media_type == "Video/GIF":
        st.warning("Pemrosesan video memerlukan waktu dan resource CPU.")
        uploaded_video = st.file_uploader("Upload Video/GIF", type=["mp4", "mov", "gif"])
        
        if uploaded_video:
            tfile = tempfile.NamedTemporaryFile(delete=False) 
            tfile.write(uploaded_video.read())
            
            clip = VideoFileClip(tfile.name)
            st.text(f"Durasi: {clip.duration} detik")
            
            resize_factor = st.slider("Ubah Ukuran (Resolusi)", 0.1, 1.0, 0.5)
            
            if st.button("Kompres Video"):
                with st.spinner('Sedang memproses video... Harap tunggu...'):
                    output_path = tempfile.mktemp(suffix=".mp4")
                    # Resize dan tulis file baru dengan bitrate rendah
                    new_clip = clip.resize(resize_factor)
                    new_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", bitrate="500k")
                    
                    with open(output_path, "rb") as file:
                        btn = st.download_button(
                            label="⬇️ Download Video Kompres",
                            data=file,
                            file_name="compressed_video.mp4",
                            mime="video/mp4"
                        )
                    # Cleanup
                    os.remove(output_path)
            
            # Cleanup input temp file
            # os.remove(tfile.name) # Note: Removing temp file in usage can cause errors depending on OS lock

# --- FITUR 3: BUAT LINK (UPLOAD KE CLOUD) ---
elif choice == "Buat Link (Upload)":
    st.header("🔗 Ubah File Menjadi Link")
    st.markdown("""
    Fitur ini akan mengupload file Anda ke layanan hosting sementara (**file.io**) 
    dan memberikan link yang bisa dibagikan. Link akan kadaluarsa setelah **1 kali download** atau **14 hari**.
    """)
    
    file_to_link = st.file_uploader("Upload File Apa Saja (Gambar/GIF/Video)", type=["jpg", "png", "gif", "mp4", "webp"])
    
    if file_to_link:
        if st.button("Generate Link"):
            with st.spinner("Mengupload ke server..."):
                try:
                    # Menggunakan API file.io (Gratis, tanpa auth untuk tes dasar)
                    files = {'file': file_to_link.getvalue()}
                    response = requests.post('https://file.io', files=files)
                    
                    if response.status_code == 200:
                        data = response.json()
                        if data["success"]:
                            link = data["link"]
                            st.success("File berhasil diupload!")
                            st.text_input("Salin Link Anda:", value=link)
                            st.warning("⚠️ Catatan: Link ini hanya berlaku untuk 1 kali download (default file.io).")
                        else:
                            st.error("Gagal mendapatkan link dari server.")
                    else:
                        st.error(f"Error server: {response.status_code}")
                except Exception as e:
                    st.error(f"Terjadi kesalahan koneksi: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Dibuat dengan Python & Streamlit")