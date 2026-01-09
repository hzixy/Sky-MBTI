import streamlit as st

# --- 1. KONFIGURASI HALAMAN (Wajib Paling Atas) ---
st.set_page_config(
    page_title="SkyPersonality Codex",
    page_icon="🕯️",
    layout="centered"
)

# --- 2. SETUP SESSION STATE ---
# Ini berguna agar aplikasi 'ingat' tombol mana yang ditekan
if 'selected_mbti' not in st.session_state:
    st.session_state.selected_mbti = None

def set_mbti(mbti_key):
    st.session_state.selected_mbti = mbti_key

# --- 3. CUSTOM CSS (BACKGROUND & STYLE) ---
# Saya mengganti URL background dengan sumber yang lebih stabil (WallpaperCave/Official)
st.markdown("""
    <style>
    /* --- Background Image --- */
    [data-testid="stAppViewContainer"] {
        /* Gambar Background: Isle of Dawn / Sky Aesthetic */
        background-image: url("https://images5.alphacoders.com/133/1337449.png");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    }

    /* --- Container Utama (Semi-Transparan) --- */
    .main .block-container {
        background-color: rgba(255, 255, 255, 0.92); /* Putih 92% agar teks jelas */
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
        margin-top: 20px;
    }

    /* --- Style AI Overview Box --- */
    .ai-overview-box {
        background-color: #f8f9fa;
        border-radius: 15px;
        padding: 25px;
        border-left: 6px solid #6366f1;
        margin-bottom: 25px;
        color: #31333F;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    
    .section-header {
        color: #4338ca;
        font-weight: 800;
        margin-top: 20px;
        margin-bottom: 10px;
        font-size: 1.2em;
        border-bottom: 2px solid #e0e7ff;
        padding-bottom: 5px;
    }

    /* --- Style Tombol Grid --- */
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        border: 1px solid #e0e7ff;
        background-color: white;
        color: #4b5563;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        border-color: #6366f1;
        color: #6366f1;
        background-color: #eef2ff;
        transform: translateY(-2px);
    }
    div.stButton > button:focus {
        background-color: #6366f1;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. DATABASE DATA (LENGKAP) ---
sky_data = {
    "ISTJ": {
        "aka": "The Inventor",
        "summary": "Pemain **ISTJ (The Inventor)** adalah teknisi Sky. Mereka fokus pada mekanik, efisiensi, dan rutinitas. Bagi mereka, Sky adalah sistem yang harus dioptimalkan.",
        "playstyle": ["**Mechanic Mastery:** Menguasai *glitch* dan trik terbang.", "**Routine:** Punya jadwal CR yang kaku.", "**Helper:** Membantu lewat solusi teknis."],
        "archetypes": ["**The Glitch Hunter**", "**The Solo Grinder**", "**The Wiki Walker**"],
        "location": ["**Vault/Isle:** Mencari celah dinding (OOB).", "**The Office:** Area rahasia."]
    },
    "INTJ": {
        "aka": "The Mastermind",
        "summary": "Pemain **INTJ (The Mastermind)** adalah ahli strategi. Efisiensi adalah segalanya. Mereka jarang bicara, tapi sangat paham *lore* dan rute tercepat.",
        "playstyle": ["**Strategic:** Rute CR paling optimal.", "**Independent:** Lebih suka main solo.", "**Analyst:** Menganalisis *lore* game."],
        "archetypes": ["**The Efficiency Expert**", "**The Silent Uber**", "**The Observer**"],
        "location": ["**Valley Race:** Jalur balap.", "**Geyser/Grandma:** Tepat waktu event."]
    },
    "ENTJ": {
        "aka": "The Marshall",
        "summary": "Pemain **ENTJ (The Marshall)** adalah pemimpin alami. Mereka tegas memimpin grup melewati bahaya seperti Krill dan mengorganisir komunitas.",
        "playstyle": ["**Leader:** Uber yang tegas pakai emote Point.", "**Fearless:** Tidak takut Krill.", "**Goal Oriented:** Mengejar item mahal."],
        "archetypes": ["**The Veteran Captain**", "**The Krill Bait**", "**The Strict Mentor**"],
        "location": ["**Golden Wasteland:** Graveyard/Battlefield.", "**Eden:** Gerbang depan."]
    },
    "INTP": {
        "aka": "The Architect",
        "summary": "Pemain **INTP (The Architect)** adalah penjelajah yang penasaran. Lebih tertarik pada rahasia dunia dan teori *lore* daripada mengumpulkan lilin.",
        "playstyle": ["**Curious:** Eksperimen fisika game.", "**Lore Focus:** Membaca mural/sejarah.", "**OOB:** Suka tempat sepi."],
        "archetypes": ["**The OOB Explorer**", "**The Wikipedia**", "**The Chill Soloist**"],
        "location": ["**Vault Library:** Lantai 1 & 2.", "**Cave of Prophecy:** Mural elemen."]
    },
    "INFP": {
        "aka": "The Healer",
        "summary": "Pemain **INFP (The Healer)** adalah jiwa puitis Sky. Fokus pada estetika, emosi, dan keindahan visual. Sangat peduli perasaan teman.",
        "playstyle": ["**Aesthetic:** Suka pemandangan.", "**Emotional:** Suka emote Hug/Bow.", "**Roleplay:** Outfit sesuai tema."],
        "archetypes": ["**The Photographer**", "**The Musician**", "**The Emotional Moth**"],
        "location": ["**Hidden Forest:** Bawah hujan.", "**Starlight Desert:** Lihat bulan."]
    },
    "ENFJ": {
        "aka": "The Teacher",
        "summary": "Pemain **ENFJ (The Teacher)** adalah malaikat pelindung. Misi mereka membantu pemain baru (Moth) dan menjaga keharmonisan server.",
        "playstyle": ["**Moth Adopter:** Suka bantu newbie.", "**Harmony:** Penengah konflik.", "**Social:** Aktif di chat bench."],
        "archetypes": ["**The Guide**", "**The Party Host**", "**The Protector**"],
        "location": ["**Isle of Dawn:** Cari moth.", "**8-Player Door:** Menunggu orang."]
    },
    "ENFP": {
        "aka": "The Champion",
        "summary": "Pemain **ENFJ (The Champion)** adalah sumber kekacauan yang seru. Penuh energi, spontan, dan suka spam *honk* untuk menyapa semua orang.",
        "playstyle": ["**Chaotic:** Mudah terdistraksi.", "**Social:** Teman banyak.", "**Creative:** Outfit aneh/unik."],
        "archetypes": ["**The Distracted Uber**", "**The Honk Master**", "**The Friend Collector**"],
        "location": ["**Prairie Lobby:** Kolam sosial.", "**Sanctuary:** Main sama manta."]
    },
    "INFJ": {
        "aka": "The Counselor",
        "summary": "Pemain **INFJ (The Counselor)** adalah penjaga yang tenang. Bermain untuk koneksi mendalam dengan sedikit teman dekat, bukan keramaian.",
        "playstyle": ["**Deep Talk:** Suka ngobrol privat.", "**Intuitive:** Peka kebutuhan teman.", "**Private:** Menghindari kerumunan."],
        "archetypes": ["**The Silent Guardian**", "**The Confidant**", "**The Mystic**"],
        "location": ["**Wind Paths:** Jalur angin.", "**Hermit Valley:** Puncak gunung."]
    },
    "ESFJ": {
        "aka": "The Provider",
        "summary": "Pemain **ESFJ (The Provider)** memastikan logistik aman. Mereka sangat sopan (etika Sky) dan rajin mengirim heart/light ke teman.",
        "playstyle": ["**Logistics:** Pastikan semua dapat lilin.", "**Polite:** Rajin bow.", "**Giver:** Kirim heart rutin."],
        "archetypes": ["**The Heart Trader**", "**The Mom Friend**", "**The Banquet Host**"],
        "location": ["**Grandma's Table:** Bawa obor.", "**Home:** Konstelasi teman."]
    },
    "ISFJ": {
        "aka": "The Protector",
        "summary": "Pemain **ISFJ (The Protector)** adalah support setia. Selalu membawa item berguna (payung/obor) dan menjaga Uber agar tidak kehabisan energi.",
        "playstyle": ["**Support:** Bawa alat bantu.", "**Loyal:** Setia follow teman.", "**Safety:** Pilih rute aman."],
        "archetypes": ["**The Walking Battery**", "**The Umbrella Holder**", "**The Silent Partner**"],
        "location": ["**Trailing:** Di belakang teman.", "**Wasteland:** Menerangi jalan."]
    },
    "ESTJ": {
        "aka": "The Supervisor",
        "summary": "Pemain **ESTJ (The Supervisor)** menganggap CR sebagai pekerjaan. Efisien, disiplin waktu, dan tidak suka basa-basi yang membuang waktu.",
        "playstyle": ["**Efficient:** Cepat dan tepat.", "**Structured:** Ikut jadwal event.", "**Direct:** Tidak suka AFK tanpa izin."],
        "archetypes": ["**The Schedule Master**", "**The No-Nonsense Uber**", "**The Grinder**"],
        "location": ["**Home:** Lari antar portal.", "**Trials:** Mode speedrun."]
    },
    "ISTP": {
        "aka": "The Operator",
        "summary": "Pemain **ISTP (The Operator)** suka tantangan fisik. Hobi mereka adalah terbang solo di Eden tanpa terluka atau melakukan *shortcut* sulit.",
        "playstyle": ["**Skill:** Terbang manual jago.", "**Solo:** Eden sendirian.", "**Action:** Sedikit bicara, banyak aksi."],
        "archetypes": ["**The Solo Ace**", "**The Trial Speedrunner**", "**The Parkour Master**"],
        "location": ["**Trial of Fire:** Shortcut.", "**Citadel:** Akrobatik udara."]
    },
    "ESFP": {
        "aka": "The Performer",
        "summary": "Pemain **ESFP (The Performer)** menjadikan Sky panggung mereka. Suka pusat perhatian, main musik di lobi, dan pakai kosmetik mahal.",
        "playstyle": ["**Showman:** Main lagu hits.", "**Fashion:** Outfit mencolok.", "**Social:** Suka lobi ramai."],
        "archetypes": ["**The Musician**", "**The Fashionista**", "**The Drama**"],
        "location": ["**Harmony Hall:** Toko musik.", "**Village Theater:** Panggung."]
    },
    "ISFP": {
        "aka": "The Composer",
        "summary": "Pemain **ISFP (The Composer)** adalah pengelana artistik. Main sesuai *mood*, menikmati visual, dan mengekspresikan diri lewat fashion unik.",
        "playstyle": ["**Visual:** Outfit estetik.", "**Sensory:** Nikmati suara/visual.", "**Fluid:** Ikuti arus."],
        "archetypes": ["**The Photographer**", "**The Silent Musician**", "**The Vibes Player**"],
        "location": ["**Rainbow Bridge:** OOB.", "**Village of Dreams:** Skating."]
    },
    "ESTP": {
        "aka": "The Promoter",
        "summary": "Pemain **ESTP (The Promoter)** mencari adrenalin. Suka aksi berbahaya, *prank* ringan ke teman, dan balapan liar di Valley.",
        "playstyle": ["**Thrill:** Cari bahaya.", "**Playful:** Suka bercanda.", "**Competitive:** Balapan."],
        "archetypes": ["**The Krill Dodger**", "**The Racer**", "**The Prankster**"],
        "location": ["**Wasteland:** Main sama Krill.", "**Valley:** Balapan ski."]
    },
    "ENTP": {
        "aka": "The Debater",
        "summary": "Pemain **ENTP (The Debater)** suka menguji batas game. Mencari glitch baru, debat teori di chat, dan kadang iseng (chaotic).",
        "playstyle": ["**Limit Test:** Coba hal mustahil.", "**Intellectual:** Debat teori.", "**Chaotic:** Tidak bisa ditebak."],
        "archetypes": ["**The Hacker**", "**The Troll**", "**The Innovator**"],
        "location": ["**Glitch Area:** Tembus tembok.", "**Lobby:** Debat chat."]
    }
}

# --- 5. HEADER & JUDUL ---
st.title("🌌 Sky: Children of the Light")
st.subheader("MBTI Personality Codex")
st.markdown("**Analisis karakter & gaya bermain berdasarkan tipe kepribadian MBTI di dunia Sky.**")

# --- 6. KOLOM PENCARIAN & TOMBOL GRID ---

# A. Pencarian Manual
with st.form(key='search_form'):
    col_input, col_btn = st.columns([4, 1])
    with col_input:
        manual_query = st.text_input("", placeholder="🔍 Ketik manual (contoh: INTJ, The Healer)...", label_visibility="collapsed")
    with col_btn:
        submit_search = st.form_submit_button(label='Cari 🔎')

if submit_search and manual_query:
    st.session_state.selected_mbti = manual_query

# B. Tombol Cepat (Grid 4 Kolom)
st.write("---")
st.caption("👇 **Atau pilih tipe MBTI secara langsung:**")

# Membuat Grid Tombol (4 baris x 4 kolom)
mbti_keys = list(sky_data.keys())
cols = st.columns(4) # Membagi layar jadi 4 kolom
for i, key in enumerate(mbti_keys):
    with cols[i % 4]: # Logika untuk menempatkan tombol di kolom yang benar
        # Tampilkan tombol dengan Nama Tipe + Julukan Singkat
        aka_short = sky_data[key]['aka'].split(" ")[1] # Ambil kata kedua (The [Inventor])
        if st.button(f"**{key}**\n{aka_short}", use_container_width=True):
            set_mbti(key) # Update session state saat diklik

# --- 7. LOGIKA TAMPILAN HASIL ---
# Cek apakah ada MBTI yang dipilih di session state
final_query = st.session_state.selected_mbti

if final_query:
    found_key = None
    
    # Mencari match di key atau value
    for key, data in sky_data.items():
        if final_query.upper() == key or final_query.lower() in data['aka'].lower():
            found_key = key
            break
    
    if found_key:
        d = sky_data[found_key]
        
        # --- TAMPILAN UTAMA (AI OVERVIEW STYLE) ---
        st.markdown("###") # Spacer
        st.markdown(f"""
        <div class="ai-overview-box">
            <h3 style="margin-top:0;">✨ {found_key} - {d['aka']}</h3>
            <p style="font-size:1.05em; line-height:1.6;">{d['summary']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # --- DETAIL 2 KOLOM ---
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown(f"<div class='section-header'>🎮 Playstyle</div>", unsafe_allow_html=True)
            for item in d['playstyle']:
                st.markdown(f"- {item}")
            
            st.markdown(f"<div class='section-header'>🎭 Archetypes</div>", unsafe_allow_html=True)
            for item in d['archetypes']:
                st.markdown(f"- {item}")
                
        with c2:
            st.markdown(f"<div class='section-header'>📍 Where to Find Them</div>", unsafe_allow_html=True)
            for item in d['location']:
                st.info(item.replace("**", "LOCATION: ", 1).replace("LOCATION: ", "")) # Sedikit trik formatting

    else:
        st.warning(f"⚠️ Maaf, data untuk '{final_query}' tidak ditemukan.")

else:
    # Pesan default jika belum ada yang dipilih
    st.info("👈 Silakan pilih salah satu tombol MBTI di atas untuk melihat analisisnya.")
