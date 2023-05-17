import youtube_dl

def descargar_audio(url):
    """
    Descarga el audio de un video de YouTube en formato MP3.

    Esta función utiliza la biblioteca youtube-dl para descargar el audio
    de un video de YouTube en formato MP3 y lo guarda en la carpeta "output".
    La calidad del audio descargado es 192 kbps a través de la opción "preferredquality".

    Args:
        url (str): URL del video de YouTube que se desea descargar.
    """
    opciones = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'output/%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(opciones) as ydl:
        ydl.download([url])

if __name__ == "__main__":

    url_video = "URL_DEL_VIDEO"
    descargar_audio(url_video)