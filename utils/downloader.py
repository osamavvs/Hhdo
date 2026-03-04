from yt_dlp import YoutubeDL

def download_song(query):
    ydl_opts = {
        "format": "bestaudio",
        "outtmpl": "downloads/%(title)s.%(ext)s",
        "quiet": True
    }

    with YoutubeDL(ydl_opts) as ydl
