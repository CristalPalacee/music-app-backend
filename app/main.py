from fastapi import FastAPI, HTTPException
import os
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

# Inisialisasi App
app = FastAPI(title="Music API", version="1.0.0")

# 1. KONFIGURASI BASE URL (PENTING!)
# Jika di .env tidak ada BASE_URL, otomatis pakai localhost:8000
# Ini mengatasi masalah gambar tidak muncul saat development
BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000").rstrip("/")

if not BASE_URL:
    print("⚠️ WARNING: BASE_URL is not set")

# 2. CORS (Agar bisa diakses dari Frontend Next.js)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],  
    allow_headers=["*"],
)

# 3. STATIC FILES (Folder tempat file asli disimpan)
# Pastikan folder 'musik', 'cover', dan 'album' ada di folder project
app.mount("/musik", StaticFiles(directory="musik"), name="musik")
app.mount("/cover", StaticFiles(directory="cover"), name="cover")
app.mount("/album", StaticFiles(directory="album"), name="album")

# ==========================================
# DATA SOURCE (DATABASE SEMENTARA)
# ==========================================

# Data Album (Baru)
albums = [
    {
        "id": 1,
        "title": "Daftar Putar",
        "artist": "Kaleb J",
        "cover": "/album/kalebj.jfif",
        "year": 2020,
    },


]

# Data Lagu (Lama - Full)
songs = [
    {
        "id": 1,
        "title": "Menyimpan rasa",
        "artist": "Devano dahendra",
        "url": "/musik/MenyimpanRasa.mp3",
        "cover": "/cover/menyimpanrasa.jpg",
    },
    {
        "id": 2,
        "title": "Sama saja",
        "artist": "Vadel Nasir",
        "url": "/musik/samasaja.mp3",
        "cover": "/cover/vadelnasircover.jpg",
    },
    {
        "id": 3,
        "title": "Pacar rahasia",
        "artist": "cappucino",
        "url": "/musik/PacarRahasia.mp3",
        "cover": "/cover/pacarrahasia.jpg",
    },
    {
        "id": 4,
        "title": "Siapkah Tuk Jatuh cinta lagi",
        "artist": "Hivi",
        "url": "/musik/hivi.mp3",
        "cover": "/cover/hivi.jpg",
    },
    {
        "id": 5,
        "title": "Tanpa tergesa",
        "artist": "Juicy luicy",
        "url": "/musik/TanpaTergesa.mp3",
        "cover": "/cover/juicy.jpg",
    },
    {
        "id": 6,
        "title": "Lebih Indah ( Demo )",
        "artist": "Adera",
        "url": "/musik/LebihIndah.mp3",
        "cover": "/cover/R-11302993-1760885529-7284.jpg",
    },
    {
        "id": 7,
        "title": "Siapa Menyangka",
        "artist": "Glenn samuel",
        "url": "/musik/SiapaMenyangka.mp3",
        "cover": "/cover/600x600bf-60.jpg",
    },
    {
        "id": 8,
        "title": "Melepaskanmu",
        "artist": "Kaleb j",
        "url": "/musik/Melepaskanmu.mp3",
        "cover": "/cover/test.jfif",
    },
    {
        "id": 9,
        "title": "Somebody pleasure Extended",
        "artist": "Aziz hedra",
        "url": "/musik/Somebody.mp3",
        "cover": "/cover/gambar.jfif",
    },
    {
        "id": 10,
        "title": "Kacamata",
        "artist": "Afgann",
        "url": "/musik/Kacamata.mp3",
        "cover": "/cover/kacamata.jpg",
    },
    {
        "id": 11,
        "title": "Somebody pleasure Inst",
        "artist": "Aziz hedra",
        "url": "/musik/somebodyinst.mp3",
        "cover": "/cover/gambar.jfif",
    },
    {
        "id": 12,
        "title": "Utopia ( Hujan )",
        "artist": "Utopia",
        "url": "/musik/Utopia_Hujan.mp3",
        "cover": "/cover/utopia.jpg",
    },
    {
        "id": 13,
        "title": "Adinda",
        "artist": "Kaleb J",
        "url": "/musik/Kaleb J - Adinda.mp3",
        "cover": "/cover/test.jfif",
    },
    {
        "id": 14,
        "title": "Now I Know",
        "artist": "Kaleb J",
        "url": "/musik/Kalebj_nowiknow.mp3",
        "cover": "/cover/test.jfif",
    },
    {
        "id": 15,
        "title": "Bahagia Bersamamu",
        "artist": "Adera",
        "url": "/musik/Bahagia Bersamamu.mp3",
        "cover": "/cover/adera.jpg",
    },
    {
        "id": 16,
        "title": "Terlambat",
        "artist": "Adera",
        "url": "/musik/Terlambat.mp3",
        "cover": "/cover/R-11302993-1760885529-7284.jpg",
    },
    {
        "id": 17,
        "title": "Menjadi Miliku",
        "artist": "Adera",
        "url": "/musik/Menjadi_miliku.mp3",
        "cover": "/cover/menjadi.jfif",
    },
    {
        "id": 18,
        "title": "Putri iklan",
        "artist": "keljo",
        "url": "/musik/Putri Iklan.mp3",
        "cover": "/cover/putriiklan.jpg",
    },
    {
        "id": 19,
        "title": "Will U",
        "artist": "Glenn samuel",
        "url": "/musik/Will U_.mp3",
        "cover": "/cover/willu.jpg",
    },
    {
        "id": 20,
        "title": "JKT48 Rapsodi",
        "artist": "Jkt48",
        "url": "/musik/Rapsodi.mp3",
        "cover": "/cover/jkt48.jpg",
    },
    {
        "id": 21,
        "title": "Sesaat Kau Hadir",
        "artist": "Gery Gany",
        "url": "/musik/Sesaat Kau Hadir.mp3",
        "cover": "/cover/unnamed.jpg",
    },
]

# Data Lirik (Disingkat sebagian, tambahkan sisanya sesuai data Anda)
lyrics_data = {
    1: """Kau diam diam aku jatuh cinta kepadamu...""", 
    2: """Sama saja, beberapa kali dalam tahun ini...""",
    3: """Kau yang tlah berdua Ternyata masih inginkanku...""",
    4: """ketika ku mendengar bahwa kini kau tak lagi dengannya...""",
    5: """Jaga dulu jarak kita...""",
    6: """saat ku tenggelam dalam sendu...""",
    # ... (Anda bisa paste sisa lirik lengkap di sini)
}

# ==========================================
# HELPER FUNCTIONS (LOGIKA URL)
# ==========================================

def process_song_url(song: dict) -> dict:
    """Khusus memproses data LAGU (ada url mp3 & cover)"""
    return {
        **song,
        "url": f"{BASE_URL}{song['url']}",
        "cover": f"{BASE_URL}{song['cover']}",
    }

def process_album_url(album: dict) -> dict:
    """Khusus memproses data ALBUM (hanya cover)"""
    return {
        **album,
        "cover": f"{BASE_URL}{album['cover']}"
    }

# ==========================================
# API ENDPOINTS
# ==========================================

@app.get("/")   
def root():
    return {"status": "ok", "message": "Music API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

# --- ENDPOINTS SONGS ---

@app.get("/api/songs", tags=["Songs"])
def get_songs():
    return [process_song_url(song) for song in songs]

@app.get("/api/songs/{song_id}", tags=["Songs"])
def get_song(song_id: int):
    for song in songs:
        if song["id"] == song_id:
            return process_song_url(song)
    raise HTTPException(status_code=404, detail="Song not found")

@app.get("/api/songs/{song_id}/lyrics", tags=["Songs"])
def get_lyrics(song_id: int):
    lyrics = lyrics_data.get(song_id)
    if not lyrics:
        return {"lyrics": "Lirik belum tersedia"}
    return {"lyrics": lyrics}

# --- ENDPOINTS ALBUMS (BARU) ---

@app.get("/api/albums", tags=["Albums"])
def get_all_albums():
    return [process_album_url(album) for album in albums]

@app.get("/api/albums/{album_id}", tags=["Albums"])
def get_one_album(album_id: int):
    for album in albums:
        if album["id"] == album_id:
            return process_album_url(album)
    raise HTTPException(status_code=404, detail="Album not found")