import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="SkyPersonality Codex",
    page_icon="🕯️",
    layout="centered"
)

# --- CUSTOM CSS UNTUK TAMPILAN MIRIP AI OVERVIEW ---
st.markdown("""
    <style>
    .ai-overview-box {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        border-left: 5px solid #6366f1;
        margin-bottom: 20px;
        color: #31333F;
    }
    .highlight {
        background-color: #e0e7ff;
        padding: 2px 5px;
        border-radius: 4px;
        font-weight: 600;
        color: #3730a3;
    }
    .section-header {
        color: #1f2937;
        font-weight: 700;
        margin-top: 15px;
        margin-bottom: 5px;
        font-size: 1.1em;
    }
    .stTextInput > div > div > input {
        border-radius: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- DATABASE MBTI SKY ---
sky_data = {
    "ISTJ": {
        "aka": "The Inventor",
        "summary": "Pemain **ISTJ (The Inventor)** mewujudkan pola pikir **'Technical Analyst'**. Mereka berfokus pada pemahaman mendalam tentang mekanik game, eksperimen dengan *bug/glitch* secara sistematis, dan efisiensi. Pikiran mereka sibuk menghitung detik atau sudut terbang terbaik.",
        "playstyle": [
            "**Mechanic Mastery:** Membongkar cara kerja game, menghitung *wax* per area, menguasai *rocket jump*.",
            "**Routine & Reliability:** Rute *farming* spesifik. Selalu tepat waktu jika janjian.",
            "**Fact-Based Helper:** Membantu dengan solusi teknis (glitch pintu, lokasi WL) daripada basa-basi.",
            "**Inventory Management:** Teliti menabung *Candles* dan *Hearts* untuk Traveling Spirit."
        ],
        "archetypes": [
            "**The Glitch Hunter:** Mencari celah OOB untuk melihat struktur game.",
            "**The Solo Grinder:** CR 20 lilin tanpa bicara sepatah kata pun.",
            "**The Wiki Walker:** Menghafal harga item dan lokasi Spirit."
        ],
        "location": [
            "**Glitch Spots:** Menabrak dinding di **Vault** atau **Isle** mencari OOB.",
            "**The Office:** Menganalisis konten di area rahasia TGC."
        ]
    },
    "INTJ": {
        "aka": "The Mastermind",
        "summary": "Pemain **INTJ (The Mastermind)** adalah **'Strategic Visionary'**. Fokus pada optimalisasi rute, kemandirian mutlak, dan observasi. *Sky* adalah sistem yang harus dipecahkan. Mereka efisien namun sangat mengapresiasi *lore*.",
        "playstyle": [
            "**Strategic Exploration:** Peta mental sempurna, rute terpendek tanpa buang energi.",
            "**System Analysis:** *Candle Run* adalah teka-teki efisiensi waktu.",
            "**Introverted Independence:** Nyaman solo, menolak teman jika memperlambat.",
            "**Lore Theorist:** Merenungkan sejarah Elders dan teori peradaban Sky."
        ],
        "archetypes": [
            "**The Efficiency Expert:** Full CR 3 realm < 45 menit.",
            "**The Silent Uber:** Memimpin di *Trial of Fire* dengan cepat tanpa bicara.",
            "**The Observer:** Mengamati pemain lain dari tempat tinggi."
        ],
        "location": [
            "**Efficient Routes:** Jalur balap **Valley of Triumph**.",
            "**Scheduled Events:** Tiba tepat waktu di **Geyser** (:05) atau **Grandma** (:35)."
        ]
    },
    "ENTJ": {
        "aka": "The Marshall",
        "summary": "Pemain **ENTJ (The Marshall)** adalah **'Leader of the Pack'**. Fokus pada pengorganisasian grup, keberanian menghadapi Krill, dan struktur tegas. Mereka memastikan *moth* mendapat panduan jelas.",
        "playstyle": [
            "**Commanding Leadership:** Uber alami, menggunakan emote *Point* untuk instruksi.",
            "**Objective Driven:** Main dengan tujuan (Elder Hair, konstelasi penuh).",
            "**Fearless Approach:** Tidak takut Krill, melihatnya sebagai tantangan.",
            "**Community Builder:** Sering jadi admin grup atau inisiator event."
        ],
        "archetypes": [
            "**The Veteran Captain:** Menarik 3-7 pemain menembus badai.",
            "**The Krill Bait:** Mengalihkan Krill agar teman aman.",
            "**The Strict Mentor:** Mengajar *moth* dengan tegas."
        ],
        "location": [
            "**Golden Wasteland:** Memimpin di **Graveyard** atau **Battlefield**.",
            "**Eden Entrance:** Melakukan *Deep Call* mengumpulkan pasukan."
        ]
    },
    "INTP": {
        "aka": "The Architect",
        "summary": "Pemain **INTP (The Architect)** adalah **'Curious Explorer'**. Didorong rasa ingin tahu intelektual. Lebih tertarik pada *kenapa* dunia Sky seperti ini daripada sekadar cari lilin. Gudang rahasia game.",
        "playstyle": [
            "**Unconventional Methods:** Mencoba hal aneh/eksperimen fisika game.",
            "**Deep Lore Focus:** Membaca mural, memahami narasi tersirat.",
            "**Detached Observation:** Suka OOB sunyi daripada tempat sosial.",
            "**Sporadic Activity:** Pola main tidak teratur (burst energy)."
        ],
        "archetypes": [
            "**The OOB Explorer:** Lebih sering di luar peta (*Rainbow Bridge*) daripada di dalam.",
            "**The Wikipedia:** Tahu segala detail sejarah Season.",
            "**The Chill Soloist:** Duduk diam di gua sepi."
        ],
        "location": [
            "**Lore Locations:** **Library (Vault)** membaca arsip.",
            "**Cave of Prophecy:** Mengamati mural elemen di **Isle**."
        ]
    },
    "INFP": {
        "aka": "The Healer",
        "summary": "Pemain **INFP (The Healer)** adalah **'Soul of Sky'**. Fokus pada estetika, koneksi emosional, dan ekspresi. Sky adalah pelarian puitis. Sangat peduli mood teman.",
        "playstyle": [
            "**Aesthetic Appreciation:** Berhenti demi pemandangan/cahaya bagus.",
            "**Emotional Support:** Siap dengan emote *Hug*, *Bow*, *Cry*.",
            "**Imaginative Roleplay:** Ganti outfit sesuai tema area.",
            "**Non-Competitive:** Terbang lambat menikmati musik."
        ],
        "archetypes": [
            "**The Photographer:** Galeri penuh screenshot pemandangan.",
            "**The Musician:** Main musik di tempat sepi untuk diri sendiri.",
            "**The Emotional Moth:** Veteran yang tetap polos sifatnya."
        ],
        "location": [
            "**Atmospheric Spots:** Bangku **Hidden Forest** (hujan) atau **Starlight Desert**.",
            "**Social Spaces:** Sendirian di **Treehouse**."
        ]
    },
    "ENFJ": {
        "aka": "The Teacher",
        "summary": "Pemain **ENFJ (The Teacher)** adalah **'Guardian Angel'**. Misi utama: keharmonisan sosial dan membantu yang kesulitan. Rela habiskan waktu demi bantu orang asing.",
        "playstyle": [
            "**Moth Adopter:** Radar pendeteksi pemain baru yang bingung.",
            "**Harmony Keeper:** Penengah konflik, pelindung dari troll.",
            "**Group Coordinator:** 'No one left behind' mentalitas.",
            "**Verbal/Social:** Aktif di Chat Bench, pendengar baik."
        ],
        "archetypes": [
            "**The Guide:** Selalu bawa *Table* untuk bantu orang.",
            "**The Party Host:** Mengumpulkan orang menari di lobi.",
            "**The Protector:** Pasang badan depan Krill demi Moth."
        ],
        "location": [
            "**Moth Spawn Points:** **Isle of Dawn** atau Lobi **Prairie**.",
            "**8-Player Door:** Menunggu sabar di puzzle 8 orang."
        ]
    },
    "ENFP": {
        "aka": "The Champion",
        "summary": "Pemain **ENFP (The Champion)** membawa energi **'Chaotic Good'**. Penuh semangat, spontan, mudah teralihkan. Pusat kegembiraan server yang suka spam honk.",
        "playstyle": [
            "**Spontaneous Adventure:** Rute berantakan karena distraksi seru.",
            "**Social Butterfly:** Berteman dengan siapa saja, honk sapaan.",
            "**Creative Expression:** Kombinasi kosmetik unik/aneh.",
            "**Emote Spammer:** Komunikasi lewat emote cepat & spin."
        ],
        "archetypes": [
            "**The Distracted Uber:** Berhenti tiba-tiba karena lihat kupu-kupu.",
            "**The Honk Master:** *Deep call* terus-menerus cari perhatian.",
            "**The Friend Collector:** Teman dari seluruh dunia."
        ],
        "location": [
            "**Social Hubs:** Kolam Lobi **Prairie** atau **Sanctuary**.",
            "**Event Areas:** Tengah keramaian event Days of Color/Bloom."
        ]
    },
    "INFJ": {
        "aka": "The Counselor",
        "summary": "Pemain **INFJ (The Counselor)** adalah **'Silent Guardian'**. Tenang, misterius, protektif pada *inner circle*. Bermain untuk koneksi dalam, bukan kuantitas.",
        "playstyle": [
            "**Deep Connection:** Lebih suka ngobrol deep berdua di bench.",
            "**Intuitive Support:** Tahu kapan teman butuh recharge tanpa diminta.",
            "**Private:** Jarang muncul di chat publik yang ramai.",
            "**Purposeful:** Main untuk relaksasi mental."
        ],
        "archetypes": [
            "**The Silent Guardian:** Jarang bicara tapi selalu ada.",
            "**The Confidant:** Tempat curhat aman di Sky.",
            "**The Mystic:** Outfit bertema gelap/misterius (Anubis mask)."
        ],
        "location": [
            "**Quiet Heights:** Puncak **Hermit Valley** atau **Wind Paths**.",
            "**Chat Benches:** Sudut sepi untuk bicara privat."
        ]
    },
    "ESFJ": {
        "aka": "The Provider",
        "summary": "Pemain **ESFJ (The Provider)** adalah **'The Heart Trader'**. Memastikan logistik grup aman. Sangat taat etika Sky (selalu bow, light, kirim heart).",
        "playstyle": [
            "**Logistics:** Memastikan semua dapat lilin & heart.",
            "**Sky Etiquette:** Sangat sopan, bow berkali-kali.",
            "**Community Glue:** Mengingat ulang tahun teman Sky.",
            "**Routine Giver:** Rajin kirim light fragment."
        ],
        "archetypes": [
            "**The Heart Trader:** Kirim heart tiap hari tanpa absen.",
            "**The Mom Friend:** 'Sudah ambil WL di sana belum?'",
            "**The Banquet Host:** Menyiapkan meja makan di Grandma."
        ],
        "location": [
            "**Grandma's Feast:** Menaruh *Torch*/*Brazier* untuk orang lain.",
            "**Home:** Berdiri di konstelasi kirim light."
        ]
    },
    "ISFJ": {
        "aka": "The Protector",
        "summary": "Pemain **ISFJ (The Protector)** adalah **'Loyal Support'**. Tipe support sejati. Membawa properti berguna, tidak menonjol tapi krusial bagi tim.",
        "playstyle": [
            "**Support Role:** Membawa payung di Forest, Torch di Wasteland.",
            "**Loyal Follower:** Setia mengikuti Uber kemanapun.",
            "**Detail Oriented:** Mengingat preferensi teman.",
            "**Safety First:** Menghindari rute berbahaya."
        ],
        "archetypes": [
            "**The Walking Battery:** Tugas utama: recharge Uber.",
            "**The Umbrella Holder:** Melindungi teman dari hujan.",
            "**The Silent Partner:** Teman CR paling nyaman."
        ],
        "location": [
            "**Trailing Leaders:** Mode follow di belakang teman.",
            "**Dark Water Areas:** **Wasteland**, menerangi jalan."
        ]
    },
    "ESTJ": {
        "aka": "The Supervisor",
        "summary": "Pemain **ESTJ (The Supervisor)** adalah **'Task Master'**. CR adalah pekerjaan. Efisien, tegas, tidak suka basa-basi atau AFK tanpa izin.",
        "playstyle": [
            "**Efficiency:** 'Ayo cepat, geyser 2 menit lagi'.",
            "**Structure:** Patuh jadwal event (Geyser-Grandma-Turtle).",
            "**Direct:** Menegur jika ada yang main-main saat CR.",
            "**Goal Oriented:** Mengejar 20 lilin/hari wajib."
        ],
        "archetypes": [
            "**The Schedule Master:** Hafal mati jadwal event.",
            "**The No-Nonsense Uber:** 'Duduk atau ditinggal'.",
            "**The Grinder:** Fokus murni pada currency."
        ],
        "location": [
            "**Clock-Watching:** Lari antar portal di **Home**.",
            "**Trials:** Menyelesaikan **Trial Earth/Air** dengan kaku."
        ]
    },
    "ISTP": {
        "aka": "The Operator",
        "summary": "Pemain **ISTP (The Operator)** adalah **'Skill Master'**. Praktis, berani, suka tantangan fisik. Terbang solo di Eden tanpa terluka adalah hobi.",
        "playstyle": [
            "**Technical Skill:** Terbang manual sempurna.",
            "**Solo Challenges:** Eden solo, Trials shortcut.",
            "**Adaptive:** Bisa selamat di situasi apapun.",
            "**Action Oriented:** Lebih suka bergerak daripada chat."
        ],
        "archetypes": [
            "**The Solo Ace:** Terbang sendiri lebih cepat daripada di-uber.",
            "**The Trial Speedrunner:** Shortcut trial api/air.",
            "**The Parkour Master:** Lompat di aset map sulit."
        ],
        "location": [
            "**Skill Challenges:** Shortcut **Trial of Fire**.",
            "**Flying Race:** Akrobatik di **Citadel (Valley)**."
        ]
    },
    "ESFP": {
        "aka": "The Performer",
        "summary": "Pemain **ESFP (The Performer)** menjadikan langit sebagai **'Panggung'**. Koleksi instrumen & kosmetik mencolok. Suka jadi pusat perhatian.",
        "playstyle": [
            "**Showmanship:** Main musik lagu populer di tempat ramai.",
            "**Fashion:** Pakai Ultimate Gift terbaru/termahal.",
            "**Entertainer:** Emote lucu, kembang api.",
            "**Social Energy:** Suka keramaian lobi."
        ],
        "archetypes": [
            "**The Musician:** Konser tunggal di Harmony Hall.",
            "**The Fashionista:** Outfit paling bersinar.",
            "**The Drama:** Reaksi emote yang heboh."
        ],
        "location": [
            "**Harmony Hall:** Panggung utama toko musik.",
            "**Crowded Lobbies:** Pakai celana Rhythm/Sayap Aurora."
        ]
    },
    "ISFP": {
        "aka": "The Composer",
        "summary": "Pemain **ISFP (The Composer)** adalah **'Artistic Wanderer'**. Bermain mengandalkan *mood*, visual, dan audio. Mengekspresikan diri lewat outfit unik.",
        "playstyle": [
            "**Visual Flair:** Mix-and-match outfit estetik.",
            "**Sensory:** Menikmati suara langkah/seluncur es.",
            "**Solo Artist:** Main musik bukan untuk pamer, tapi rasa.",
            "**Fluid:** Bergerak mengikuti arus/mood."
        ],
        "archetypes": [
            "**The Photographer:** Screenshot artistik OOB.",
            "**The Silent Musician:** Lagu sedih di hujan.",
            "**The Vibes Player:** Login cuma buat jalan-jalan."
        ],
        "location": [
            "**Scenic OOB:** **Rainbow Bridge** atau atas awan.",
            "**Village of Dreams:** Seluncur santai."
        ]
    },
    "ESTP": {
        "aka": "The Promoter",
        "summary": "Pemain **ESTP (The Promoter)** mencari **'Adrenaline'**. Suka aksi, *trolling* ringan, balapan, dan tantangan berbahaya.",
        "playstyle": [
            "**Thrill Seeker:** Sengaja cari bahaya.",
            "**Playful Troll:** Kembang api di muka teman, unfriend prank.",
            "**Competitve:** Ajak balapan di Valley.",
            "**Fast Paced:** Gak betah diam lama."
        ],
        "archetypes": [
            "**The Krill Dodger:** Prank naga Wasteland.",
            "**The Racer:** Selalu ingin duluan sampai.",
            "**The Prankster:** Lucu tapi kadang nyebelin."
        ],
        "location": [
            "**Danger Zones:** Main petak umpet sama Krill **Wasteland**.",
            "**Racing:** Lereng salju **Valley**."
        ]
    },
    "ENTP": {
        "aka": "The Debater", # Menambahkan ENTP agar lengkap 16
        "summary": "Pemain **ENTP (The Debater)** adalah **'Chaos Theorist'**. Inovatif, suka mengetes batas game, dan debat tentang lore atau mekanik di chat.",
        "playstyle": [
            "**Boundary Pushing:** 'Bisa gak ya kita ke sana tanpa sayap?'.",
            "**Intellectual Chat:** Debat teori di bench berjam-jam.",
            "**Unpredictable:** Kadang Uber, kadang kabur.",
            "**Experimenter:** Mencoba glitch baru."
        ],
        "archetypes": [
            "**The Hacker:** (Bukan cheat) Tapi tahu segala trik aneh.",
            "**The Troll:** Menjatuhkan teman ke air (bercanda).",
            "**The Innovator:** Menemukan cara farming baru."
        ],
        "location": [
            "**Glitch Areas:** Mencoba menembus tembok yang mustahil.",
            "**Wasteland Social:** Ngobrol debat di lobi."
        ]
    }
}

# --- HEADER APLIKASI ---
st.title("🌌 Sky: Children of the Light")
st.subheader("MBTI Personality Codex")
st.write("Masukkan tipe MBTI atau julukan (contoh: *INTJ*, *The Healer*) untuk melihat analisis karakter mereka di dunia Sky.")

# --- SEARCH BAR ---
query = st.text_input("", placeholder="🔍 Search MBTI (e.g., ISTJ, The Protector)...").strip()

# --- LOGIKA PENCARIAN & TAMPILAN ---
if query:
    found_key = None
    
    # Mencari match di key (ISTJ) atau value aka (The Inventor)
    for key, data in sky_data.items():
        if query.upper() == key or query.lower() in data['aka'].lower():
            found_key = key
            break
    
    if found_key:
        d = sky_data[found_key]
        
        # TAMPILAN CARD AI OVERVIEW
        st.markdown(f"""
        <div class="ai-overview-box">
            <h3>✨ {found_key} - {d['aka']}</h3>
            <p>{d['summary']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # DETAIL SECTIONS
        c1, c2 = st.columns([1.5, 1])
        
        with c1:
            st.markdown(f"<div class='section-header'>How {found_key} Plays Sky</div>", unsafe_allow_html=True)
            for item in d['playstyle']:
                st.markdown(f"- {item}")
                
        with c2:
            st.markdown(f"<div class='section-header'>Common Archetypes</div>", unsafe_allow_html=True)
            for item in d['archetypes']:
                st.markdown(f"- {item}")

        st.markdown("---")
        st.markdown(f"<div class='section-header'>📍 Where to Find Them</div>", unsafe_allow_html=True)
        col_loc1, col_loc2 = st.columns(2)
        for i, loc in enumerate(d['location']):
            if i % 2 == 0:
                with col_loc1: st.info(loc)
            else:
                with col_loc2: st.info(loc)

    else:
        st.warning(f"Maaf, tidak menemukan data untuk '{query}'. Coba masukkan tipe MBTI (contoh: INFP) atau Julukan (contoh: The Healer).")

else:
    # Tampilan awal jika belum mencari
    st.info("👆 Ketik sesuatu di kolom pencarian di atas untuk memulai AI Overview.")
    with st.expander("Lihat Daftar Kata Kunci"):
        st.write(", ".join([f"{k} ({v['aka']})" for k, v in sky_data.items()]))
