import yt_dlp
import certifi
import ssl

def download_video(link):
    ydl_opts = {
        'format': 'bestvideo+bestaudio[ext=m4a]',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'ssl_context': ssl.create_default_context(cafile=certifi.where())
         }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Descarga Completa")
    except Exception as e:
        print(f"Hubo un problema al descargar el video: {e}")


link= str(input("Pega la URL del video a descargar: ")).strip()
download_video(link)