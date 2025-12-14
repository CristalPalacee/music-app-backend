from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000",
  "https://music-app-frontend.vercel.app",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve file musik & cover secara langsung
app.mount("/musik", StaticFiles(directory="musik"), name="musik")
app.mount("/cover", StaticFiles(directory="cover"), name="cover")

# Data lagu manual
songs = [
    {
        "id": 1,
        "title": "Menyimpan rasa",
        "artist": "Devano dahendra",
        "url": "/musik/Menyimpan Rasa.mp3",
        "cover": "/cover/menyimpan rasa.jpg",
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
        "url": "/musik/Pacar Rahasia.mp3",
        "cover": "/cover/pacarrahasia.jpg",
    },
    {
        "id": 4,
        "title": "Siapkah Tuk Jatuh cinta lagi",
        "artist": "Hivi",
        "url": "/musik/HIVI! - Siapkah Kau 'Tuk Jatuh Cinta Lagi (Official Lyric Video).mp3",
        "cover": "/cover/hivi.jpg",
    },
    {
        "id": 5,
        "title": "Tanpa tergesa",
        "artist": "Juicy luicy",
        "url": "/musik/Tanpa Tergesa.mp3",
        "cover": "/cover/juicy.jpg",
    },
    {
        "id": 6,
        "title": "Lebih Indah ( Demo )",
        "artist": "Adera",
        "url": "/musik/Lebih Indah (Demo Version).mp3",
        "cover": "/cover/R-11302993-1760885529-7284.jpg",
    },
]






lyrics_data = {
    1: """
Kau diam diam aku jatuh cinta kepadamu
Ku bosan sudah ku menyimpan rasa kepadamu
Tapi tak mampu ku berkata di depanmu
Aku tak mudah mencintai
Tak mudah bilang cinta
Tapi mengapa kini denganmu
Aku jatuh cinta
Tuhan tolong dengarkanku
Beri aku dia
Tapi jika belum jodoh
Aku bisa apa
Ku bosan sudah ku menyimpan rasa kepadamu
Tapi tak mampu ku berkata didepanmu
Aku tak mudah mencintai
Tak mudah bilang cinta
Tapi mengapa kini denganmu
Aku jatuh cinta
Tuhan tolong dengarkanku
Beri aku dia
Tapi jika belum jodoh
Aku bisa apa
Tak bisa ku paksakan dirimu
Tuk jadi kekasihku bila tak jodohku
Aku tak mudah mencintai
Tapi mengapa denganmu aku jatuh cinta (aku tak mudah mencintai tak mudah bilang cinta)
Tapi mengapa kini denganmu aku jatuh cinta
Tuhan tolong dengarkanku
Beri aku dia
Tapi jika belum jodoh
Aku bisa apa
Aku bisa apa
""",
    2: """
Sama saja, beberapa kali dalam tahun ini
Kau mengulang salah yang sama
Belum berubah, pernah berjanji tak akan mengulangi
Namun kau tetap sama saja

Ternyata ku bukanlah satu-satunya
Saat ku ingin dapat perhatianmu
Apa yang kau lakukan di belakangku
Ada satu hati yang selama ini
Kau sembunyikan dari mulut manismu

Dan bodohnya diriku terlambat menyadari
Sepercaya itu ku pada dirimu
Biarkan waktu yang membalas di hati yang lain

Sudah tak bisa kau kembali untuk merayuku lagi
Tak lagi percaya janji yang sama
Selama ini ku bukanlah satu-satunya
Saat ku ingin dapat perhatianmu
Apa yang kau lakukan di belakangku
Ada satu hati yang selama ini
Kau sembunyikan dari mulut manismu

Dan bodohnya diriku terlambat menyadari
Sepercaya itu ku pada dirimu
Biarkan waktu yang membalas di hati yang lain

Saat ku ingin dapat perhatianmu
Apa yang kau lakukan di belakangku
Ada satu hati yang selama ini
Kau sembunyikan dari mulut manismu

Dan bodohnya diriku terlambat menyadari
Sepercaya itu ku pada dirimu
Biarkan waktu yang membalas di hati yang lain
Ternyata ku bukanlah satu-satunya
""",
    3: """
C                 A/C#     Dm   G           Em
Kau yang tlah berdua Ternyata masih inginkanku
           Am       Dm           G
Walau ku tahu ini salah apa daya ku tlah cinta
 
  C             A/C#    Dm    G                     Em
kamu datang padaku bertanya Maukah ku jadi yang kedua
          Am        Dm         G
Menjadi pacar rahasia Lalu aku pun terima
 
 
F                 G
Meski harus terbagi
           Em           Am
Percayalah aku tak perduli
              Dm    G
Kelak kau pun mengerti
            C    C7
Akulah yang terbaik
 
   F             G
Tinggalkan saja dia
         Em              Am
Biarlah aku menjadi yang pertama
Dm     Em    F          D/F#   G
Bersamaku pastikan lebih bahagia
 
  C                A/C#    Dm
tapi jangan sampai dia curiga
   G                       Em
Gantilah namaku dihandphonemu
        Am          Dm          G
Buat seolah ku tak ada diantara kau dan dia
 
 
[Interlude]
F G Em Am Dm G C C7
F G Em Am Dm G C
 
 
F                 G
Meski harus terbagi
           Em           Am
Percayalah aku tak perduli
              Dm    G
Kelak kau pun mengerti
            C    C7
Akulah yang terbaik
 
   F             G
Tinggalkan saja dia
         Em              Am
Biarlah aku menjadi yang pertama
Dm     Em    F          D/F#   G
Bersamaku pastikan lebih bahagia
 
F                 G
Meski harus terbagi
           Em           Am
Percayalah aku tak perduli
              Dm    G
Kelak kau pun mengerti
            C    C7
Akulah yang terbaik
 
   F             G
Tinggalkan saja dia
         Em              Am
Biarlah aku menjadi yang pertama
Dm     Em    F          D/F#   G
Bersamaku pastikan lebih bahagia
 
[Outro]
D C CMaj7
X

""",
4: """ketika ku mendengar bahwa
kini kau tak lagi dengannya
dalam benakku timbul tanya

masihkah ada dia di hatimu bertahta
atau ini saat bagiku
untuk singgah di hatimu

namun siapkah kau tuk jatuh cinta lagi

meski bibir ini tak berkata
bukan berarti ku tak merasa
ada yang berbeda di antara kita

dan tak mungkin ku melewatkanmu
hanya karena diriku tak mampu untuk bicara
bahwa aku inginkan kau ada di hidupku

kini ku tak lagi dengannya
sudah tak ada lagi rasa antara aku dengan dia (dengan dia)
siapkah kau bertahta di hatiku, adinda
karena ini saat yang tepat untuk singgah di hatiku
namun siapkah kau tuk jatuh cinta lagi oooh

meski bibir ini tak berkata
bukan berarti ku tak merasa ada yang berbeda di antara kita
dan tak mungkin ku melewatkanmu hanya karena
diriku tak mampu untuk bicara bahwa aku inginkan kau ada di hidupku

pikirlah saja dulu hingga tiada ragu
agar mulus jalanku melangkah menuju ke hatimu
pikirlah saja dulu hingga tiada ragu
agar mulus jalanku melangkah menuju ke hatimu
oooh siapkah kau tuk jatuh cinta lagi

meski bibir ini tak berkata
bukan berarti ku tak merasa ada yang berbeda di antara kita
dan tak mungkin ku melewatkanmu hanya karena
diriku tak mampu untuk bicara bahwa aku inginkan kau ada di hidupku

meski bibir ini tak berkata
bukan berarti ku tak merasa ada yang berbeda di antara kita
dan tak mungkin ku melewatkanmu hanya karena
diriku tak mampu untuk bicara bahwa aku inginkan kau ada di hidupku

bila kau jatuh cinta, katakanlah, jangan buang sia-sia
bila kau jatuh cinta, katakanlah, jangan buang sia-sia
bila kau jatuh cinta, katakanlah, jangan buang sia-sia
siapkah kau tuk jatuh cinta lagi
?""",
5:"""
Jaga dulu jarak kita
Jika tak ingin akhirnya
Kau menangis lagi

Jangan terlalu kau dekat
Jangan buat terikat
Coba kau rasakan lagi

Mungkin kau dapat perannya
Tapi hanya sebagai bayang-bayangnya saja
Jangan minta jatuh cinta
Luka lama ku juga belum reda
Beri dulu aku waktu untuk sembuh sendirinya

Jangan minta jatuh cinta
Sakit sebelumnya masih kurasa
Beri waktu hingga aku mampu lupakan semua

Jangan terlalu kau dekat
Jangan buat terikat
Coba kau rasakan lagi

Mungkin kau dapat perannya
Tapi hanya sebagai bayang-bayangnya saja
Jangan minta jatuh cinta
Luka lama ku juga belum reda
Beri dulu aku waktu untuk sembuh sendirinya

Jangan minta jatuh cinta
Sakit sebelumnya masih kurasa
Beri waktu hingga aku mampu lupakan semua

Jangan minta jatuh cinta
Luka lama ku juga belum reda
Beri dulu aku waktu untuk sembuh sendirinya

Bukan ku tak jatuh cinta
Lelah ulang kesalahan yang sama
Ku ingin kita jalani cinta
Ku ingin kita jalani cinta
Tanpa tergesa
""",
6: """
saat ku tenggelam dalam sendu
Waktupun enggan untuk berlalu
Ku berjanji tuk menutup pintu hatiku
Entah untuk siapapun itu

Semakin ku lihat masa lalu
semakin hatiku tak menentu
Tetapi satu sinar terangi jiwaku
Saat ku melihat senyummu

Reff:
Dan kau hadir merubah segalanya
Menjadi lebih indah
Kau bawa cintaku setinggi angkasa
Membuatku merasa sempurna
Dan membuatku utuh tuk menjalani hidup
Berdua denganmu selama-lamanya
Kaulah yang terbaik untukku

Kini ku ingin hentikan waktu
Bila kau berada di dekatku
Bunga cinta bermekaran dalam jiwaku
Kan ku petik satu untukmu

Repeat Reff

Kaulah yang terbaik untukku

Ku percayakan seluruh hatiku padamu
Kasihku satu janjiku kaulah yang terakhir bagiku

""",
7: """

""",
8: """

""",
9: """

""",
}




@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/api/songs")
def get_songs():
    return songs


@app.get("/api/songs/{song_id}")
def get_song(song_id: int):
    for song in songs:
        if song["id"] == song_id:
            return song
    return {"error": "Song not found"}

@app.get("/api/songs/{song_id}/lyrics")
def get_lyrics(song_id: int):
    lyrics = lyrics_data.get(song_id)
    if not lyrics:
        return {"lyrics": "Lirik belum tersedia"}
    return {"lyrics": lyrics}
